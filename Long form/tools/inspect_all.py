import json

files = [f'Draft/sec{i}_part{i}.json' if 1 <= i <= 9 else (f'Draft/sec0_front_matter.json' if i==0 else 'Draft/sec10_closing.json') for i in range(11)]

with open('Draft/all_sections_overview.txt', 'w', encoding='utf-8') as out:
    for fpath in files:
        with open(fpath, 'r', encoding='utf-8') as f:
            items = json.load(f)
        out.write(f"=== {fpath} (items: {len(items)}) ===\n")
        for item in items:
            idx = item['index']
            if item['type'] == 'paragraph' and ('Heading' in item['style'] or 'Title' in item['style'] or 'Subtitle' in item['style']):
                out.write(f"  [{idx}] {item['style']}: {item['text']}\n")
            elif item['type'] == 'table':
                out.write(f"  [{idx}] TABLE: {len(item['rows'])} rows x {len(item['rows'][0])} cols\n")
print("Saved all sections overview to Draft/all_sections_overview.txt")
