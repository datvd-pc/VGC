from docx import Document
from pathlib import Path


path = Path(r"D:\CODE\VGC\Long form\The-Art-of-Monetization-Vietnamese-Editable.docx")
doc = Document(path)
old = (
    "Nguyên tắc thực hành rất ngắn: reward nhỏ nhận phản hồi nhỏ nhưng rõ; reward hiếm được phép có khoảnh khắc lớn vì trạng thái game đã thực sự thay đổi; thất bại phải được báo đúng là thất bại; purchase thành công cần xác nhận vật phẩm, quyền lợi và cách dùng mà không giả vờ rằng một gói nhỏ đã giải quyết toàn bộ game. Hãy A/B test intensity của feedback cùng một reward, rồi đọc repeat use, retention, completion, purchase refund và phản hồi định tính, thay vì chỉ đọc tap-through. Nguồn nghiên cứu: Sinha, 2025, Journal of Consumer Research. Part IV sẽ chuyển từ các điều kiện tâm lý sang các sản phẩm monetization cụ thể: rewarded ads, interstitials, booster, IAP và economy."
)
new = (
    "Nguyên tắc thực hành rất ngắn: reward nhỏ nhận phản hồi nhỏ nhưng rõ; reward hiếm được phép có khoảnh khắc lớn vì trạng thái game đã thực sự thay đổi; thất bại phải được báo đúng là thất bại; purchase thành công cần xác nhận vật phẩm, quyền lợi và cách dùng mà không giả vờ rằng một gói nhỏ đã giải quyết toàn bộ game. Hãy A/B test intensity của feedback cùng một reward, rồi đọc repeat use, retention, completion, purchase refund và phản hồi định tính, thay vì chỉ đọc tap-through. Nguồn nghiên cứu: Hampton và Hildebrand, 2025, Journal of Consumer Research. Part IV sẽ chuyển từ các điều kiện tâm lý sang các sản phẩm monetization cụ thể: rewarded ads, interstitials, booster, IAP và economy."
)

matches = [paragraph for paragraph in doc.paragraphs if paragraph.text == old]
if len(matches) != 1:
    raise RuntimeError(f"Expected exactly one unchanged paragraph, found {len(matches)}.")
matches[0].text = new
doc.save(path)
print(f"Updated: {path}")
