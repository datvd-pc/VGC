# Research Backlog trước bản thảo

## Ưu tiên 1 — Evidence còn thiếu

- [ ] Đọc toàn văn S1 và tạo 1 trang notes: định nghĩa, taxonomy, giới hạn áp dụng cho puzzle.
- [ ] Đọc/ghi chú slide S4, đặc biệt các câu hỏi kiểm tra “puzzle contract”.
- [ ] Xem hoặc lấy transcript S5; trích bộ biến số blocker/difficulty mà King công bố.
- [ ] Đọc S6: mô hình, dữ liệu, biến số và điều gì có thể/không thể áp dụng cho production.
- [ ] Tìm nguồn primary về audio, haptic và animation timing cho feedback tương tác.

## Ưu tiên 2 — Case-study matrix

Chọn 3–5 game, không nhằm xếp hạng mà để đối chiếu cơ chế tạo feeling:

| Dạng | Case dự kiến | Điều phải quan sát | Bằng chứng cần lưu |
|---|---|---|---|
| Match-3 | Candy Crush Saga hoặc game nội bộ tương đương | Board readability, blocker, cascade, near-miss, retry | Video màn hình + event log + lời nói người chơi |
| Grid/logic | Baba Is You / Stephen’s Sausage Roll / Sokoban-like | Rule discovery, undo, “aha”, khả năng đọc state | Map giả thuyết của người chơi |
| Physics/spatial | Cut the Rope / Monument Valley-like | Gesture, timing, anticipation, causal feedback | Video + timestamp hesitations |
| Narrative/escape | Case phù hợp | Manh mối, inventory, feedback không spoil | Danh sách false leads/điểm mù |

Không coi tên game ở bảng trên là nguồn trích dẫn. Trước khi xuất bản, cần kiểm tra quyền dùng ảnh/video và dùng nguồn chính thức cho facts về sản phẩm.

## Ưu tiên 3 — Playtest protocol

Mẫu tối thiểu cho mỗi phiên (30–45 phút):

1. Tuyển người chơi mới và có kinh nghiệm; ghi rõ mức quen với thể loại.
2. Yêu cầu think-aloud vừa phải: “Bạn đang nghĩ điều gì sẽ xảy ra nếu làm nước này?”
3. Không hướng dẫn trừ khi protocol quy định; lưu thời điểm tester xin trợ giúp.
4. Sau mỗi level, hỏi ngắn: “Bạn nghĩ mình thắng/thua vì điều gì?” và “Có khoảnh khắc nào game không công bằng/không rõ không?”
5. Mã hoá quan sát theo: hiểu luật, agency, feedback, nhịp, cảm xúc và accessibility.

### Bảng mã quan sát

| Mã | Sự kiện | Dấu hiệu | Hành động tiếp theo |
|---|---|---|---|
| CL-1 | Clarity failure | Không dự đoán được hệ quả | Sửa signifier/preview/cách dạy luật |
| AG-1 | Agency failure | Gọi kết quả là may rủi/định sẵn | Audit RNG và causal feedback |
| FR-1 | Friction tốt | Dừng lại suy nghĩ, tạo giả thuyết | Giữ lại; kiểm tra payoff có đủ rõ |
| FR-2 | Friction xấu | Thử lặp vô hướng, thao tác UI sai | Giảm nhiễu hoặc thiết kế hint theo tầng |
| AM-1 | Amplification mismatch | Phản ứng audiovisual không khớp độ quan trọng | Chỉnh hierarchy, timing, intensity |
| AC-1 | Accessibility barrier | Không đọc màu/flash/đòi hỏi thao tác khó | Bổ sung kênh tín hiệu/tuỳ chỉnh |

## Tiêu chí sẵn sàng viết

Bắt đầu outline chương chỉ khi mỗi luận điểm trọng tâm có: (a) một nguồn đã đọc đầy đủ hoặc dữ liệu test, (b) một ví dụ puzzle cụ thể, (c) một phản ví dụ/rủi ro, và (d) một hành động thực hành cho đội làm game.
