import argparse
import os
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    Image,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)

PAGE = A4
MARGIN_X = 18 * mm
MARGIN_Y = 18 * mm
INK = colors.HexColor("#171717")
TEAL = colors.HexColor("#087B86")
PAPER = colors.HexColor("#F7F3EB")
GRID = colors.HexColor("#D6D0C7")


def escape(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", r'<link href="\2" color="#087B86">\1</link>', text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r'<font name="EbookMono">\1</font>', text)
    text = text.replace("&lt;br/&gt;", "<br/>")
    return text


class Cover(Flowable):
    def __init__(self, cover_path):
        super().__init__()
        self.cover_path = cover_path
        self.width, self.height = PAGE

    def wrap(self, avail_width, avail_height):
        return avail_width, avail_height

    def draw(self):
        image = Image(self.cover_path, width=self.width, height=self.height)
        image.drawOn(self.canv, -MARGIN_X, -MARGIN_Y)


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="BodyEbook", parent=styles["BodyText"], fontName="Ebook", fontSize=10.2,
        leading=15.5, textColor=INK, spaceAfter=7, alignment=TA_LEFT,
    ))
    styles.add(ParagraphStyle(
        name="TitleEbook", parent=styles["Title"], fontName="EbookBold", fontSize=25,
        leading=30, textColor=INK, spaceBefore=18, spaceAfter=15,
    ))
    styles.add(ParagraphStyle(
        name="PartEbook", parent=styles["Heading1"], fontName="EbookBold", fontSize=19,
        leading=24, textColor=TEAL, spaceBefore=27, spaceAfter=13, keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="SectionEbook", parent=styles["Heading1"], fontName="EbookBold", fontSize=17,
        leading=21, textColor=INK, spaceBefore=18, spaceAfter=10, keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="ChapterEbook", parent=styles["Heading2"], fontName="EbookBold", fontSize=14,
        leading=18, textColor=INK, spaceBefore=19, spaceAfter=8, keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="SmallEbook", parent=styles["BodyText"], fontName="Ebook", fontSize=8.7,
        leading=12.2, textColor=colors.HexColor("#5E5A55"), spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="BulletEbook", parent=styles["BodyText"], fontName="Ebook", fontSize=10.2,
        leading=15.5, leftIndent=12, firstLineIndent=-8, textColor=INK, spaceAfter=5,
    ))
    return styles


def split_row(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def table_flow(rows, styles):
    data = []
    for i, row in enumerate(rows):
        cells = split_row(row)
        if all(re.fullmatch(r"[-: ]+", c) for c in cells):
            continue
        data.append([Paragraph(escape(c), styles["SmallEbook"]) for c in cells])
    if not data:
        return Spacer(1, 1)
    width = PAGE[0] - 2 * MARGIN_X
    widths = [width / len(data[0])] * len(data[0])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E9F0EF")),
        ("FONTNAME", (0, 0), (-1, 0), "EbookBold"),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, GRID),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def parse_markdown(text, styles):
    lines = text.splitlines()
    story = []
    index = 0
    in_code = False
    code_lines = []
    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            if in_code:
                story.append(Preformatted("\n".join(code_lines), ParagraphStyle(
                    "CodeEbook", fontName="EbookMono", fontSize=8.8, leading=12,
                    backColor=colors.HexColor("#F0EEE9"), borderColor=GRID,
                    borderWidth=0.35, borderPadding=8, spaceBefore=5, spaceAfter=11,
                )))
                code_lines = []
            in_code = not in_code
            index += 1
            continue
        if in_code:
            code_lines.append(line)
            index += 1
            continue
        if line.startswith("|") and index + 1 < len(lines) and lines[index + 1].startswith("|"):
            rows = [line]
            index += 1
            while index < len(lines) and lines[index].startswith("|"):
                rows.append(lines[index])
                index += 1
            story.append(table_flow(rows, styles))
            story.append(Spacer(1, 8))
            continue
        if not line.strip():
            index += 1
            continue
        if line.startswith("# "):
            story.append(Paragraph(escape(line[2:]), styles["TitleEbook"]))
        elif line.startswith("## Part") or line.startswith("## Phan"):
            story.append(Paragraph(escape(line[3:]), styles["PartEbook"]))
        elif line.startswith("## "):
            story.append(Paragraph(escape(line[3:]), styles["SectionEbook"]))
        elif line.startswith("### "):
            story.append(Paragraph(escape(line[4:]), styles["ChapterEbook"]))
        elif re.match(r"^[-*] ", line):
            story.append(Paragraph("- " + escape(line[2:]), styles["BulletEbook"]))
        elif re.match(r"^\d+\. ", line):
            story.append(Paragraph(escape(line), styles["BulletEbook"]))
        else:
            story.append(Paragraph(escape(line), styles["BodyEbook"]))
        index += 1
    return story


def page_decor(canvas, doc, header):
    canvas.saveState()
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.35)
    canvas.line(MARGIN_X, PAGE[1] - 11 * mm, PAGE[0] - MARGIN_X, PAGE[1] - 11 * mm)
    canvas.setFont("Ebook", 8)
    canvas.setFillColor(colors.HexColor("#66615B"))
    canvas.drawString(MARGIN_X, PAGE[1] - 8 * mm, header)
    canvas.drawRightString(PAGE[0] - MARGIN_X, 9 * mm, str(doc.page - 1))
    canvas.restoreState()


def draw_cover(canvas, doc, cover_path):
    canvas.saveState()
    canvas.drawImage(cover_path, 0, 0, width=PAGE[0], height=PAGE[1], preserveAspectRatio=False)
    canvas.restoreState()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--cover", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    pdfmetrics.registerFont(TTFont("Ebook", r"C:\Windows\Fonts\segoeui.ttf"))
    pdfmetrics.registerFont(TTFont("EbookBold", r"C:\Windows\Fonts\segoeuib.ttf"))
    pdfmetrics.registerFont(TTFont("EbookMono", r"C:\Windows\Fonts\consola.ttf"))
    styles = build_styles()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    frame = Frame(MARGIN_X, MARGIN_Y, PAGE[0] - 2 * MARGIN_X, PAGE[1] - 2 * MARGIN_Y, id="body")
    cover_frame = Frame(0, 0, PAGE[0], PAGE[1], id="cover", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc = BaseDocTemplate(str(output), pagesize=PAGE, leftMargin=MARGIN_X, rightMargin=MARGIN_X,
                          topMargin=MARGIN_Y, bottomMargin=MARGIN_Y)
    source_text = Path(args.input).read_text(encoding="utf-8")
    header = "NGHỆ THUẬT KIẾM TIỀN TRONG GAME" if "Nghệ thuật kiếm tiền trong game" in source_text else "THE ART OF MONETIZATION"
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=lambda c, d: draw_cover(c, d, args.cover)),
        PageTemplate(id="ebook", frames=[frame], onPage=lambda c, d: page_decor(c, d, header)),
    ])
    story = [Spacer(1, 1), NextPageTemplate("ebook"), PageBreak()]
    story.extend(parse_markdown(source_text, styles))
    doc.build(story)


if __name__ == "__main__":
    main()
