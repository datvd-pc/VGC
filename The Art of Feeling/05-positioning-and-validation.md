# Positioning & Validation — The Art of Feeling

> Cập nhật nghiên cứu: 16-08-2026. Tài liệu này phân biệt rõ **cạnh tranh về tên** với **cạnh tranh về nội dung**. Nó không phải ý kiến pháp lý hay kết luận rằng tên sách có thể đăng ký/được tự do sử dụng ở mọi thị trường.

## Kết luận ngắn

Đã có nhiều tài liệu mạnh ở từng mảng: *Game Feel* (Steve Swink) về cảm giác tương tác, *The Art of Game Design* (Jesse Schell) về phương pháp/lenses, sách/chương về puzzle design, cùng nhiều GDC talk về tutorial, puzzle contract và playtest. Tuy nhiên, chưa tìm thấy một cuốn có đúng tiêu đề **The Art of Feeling** và cùng lời hứa: một phương pháp kiểm chứng được để thiết kế cảm giác *"tôi hiểu, tôi có ý định, và chính tôi đã giải được puzzle"*.

Đây là khoảng trống khả thi. Bản ebook chỉ có giá trị riêng nếu biến lời hứa đó thành bộ công cụ dùng được trên prototype — không chỉ tổng hợp lại “juice, flow, agency”.

## Cạnh tranh về tên: cần đổi cách trình bày

*The Art of Feeling* đã là tên một tiểu thuyết của Laura Tims (HarperCollins, 2017; ISBN 978-0062317353), ngoài ra còn xuất hiện ở các sách về cảm xúc/therapy. Không có bằng chứng từ lần tìm kiếm này rằng có sách game-design trùng tên, nhưng SEO, metadata cửa hàng và nhận diện thương hiệu sẽ bị phân tán.

Khuyến nghị giữ nó là **tên series/nhãn cảm xúc**, nhưng luôn xuất bản với subtitle mô tả rõ ngách. Ba phương án:

1. *The Art of Feeling: Designing Puzzle Games Players Trust*
2. *The Art of Feeling: Clarity, Agency, and the Aha Moment in Puzzle Games*
3. *Designing the Aha: A Field Guide to Puzzle Game Feeling* — mạnh hơn về khả năng tìm kiếm, dùng “The Art of Feeling” làm tagline.

Trước khi chốt thương mại, kiểm tra ISBN, tên miền và nhãn hiệu tại quốc gia/phạm vi bán dự kiến. Đây là bước riêng với việc tìm thấy một tựa sách trùng tên.

## Bản đồ các tác phẩm gần nhất

| Tác phẩm/nguồn | Nó đã làm tốt điều gì | Phần ebook cần vượt qua |
|---|---|---|
| Steve Swink, *Game Feel* (2009) | Cảm giác tương tác, input–response, sound, context, polish, metaphor và rules | Đừng kể lại game feel theo hướng action/physicality. Hãy chỉ ra khi nào feedback trở thành **bằng chứng suy luận** trong puzzle và đo nó thế nào. |
| Pichlmair & Johansen, *Designing Game Feel. A Survey* (2020) | Vocabulary: physicality, amplification, support; đặt juice vào khung nghiên cứu | Nói rõ “intelligibility/clarity” là phần mở rộng biên tập của ebook, chưa phải một dimension đã được survey xác lập độc lập. |
| Jesse Schell, *The Art of Game Design* | Hơn 100 lenses để chẩn đoán design tổng quát | Cung cấp ít lenses hơn nhưng có quyết định rõ ràng: quan sát gì, sửa biến nào, test lại bằng câu hỏi nào. |
| Clara Fernández-Vara, GDC *Puzzle Writing: Best Practices* | “Puzzle contract”: designer cung cấp đủ thông tin nhưng vẫn giữ thách thức | Mở rộng từ narrative/environmental puzzle sang mobile/casual, match-3, sort và physics; đặc biệt xử lý RNG, retry và live balance. |
| GDC *Teaching Puzzle Design*, *Mushroom 11*, *Patrick’s Parabox* | Dạy mechanic, kiến tạo level, phát hiện lỗi qua playtest | Tổng hợp thành một protocol xuyên thể loại và các artefact mẫu có thể in/điền. |
| Sách/chương puzzle design (Gibson Bond; Hiwiller; Browne ed.) | Taxonomy puzzle và nền tảng game design | Không biến ebook thành taxonomy. Giữ trọng tâm ở cảm giác do **quyết định có thể hiểu được** tạo ra. |

## Những điểm cần hiệu chỉnh trước khi viết

1. **Tách ba khái niệm.** Trong bản hiện tại, “feeling” đôi lúc gộp *game feel* (tương tác khoảnh khắc), *player experience* (trải nghiệm chủ quan) và *puzzle insight/learning*. Định nghĩa vận hành nên nêu chúng liên quan nhưng không đồng nghĩa.
2. **Hạ cấp độ chắc chắn của causal claim.** “Juice không thể tạo chiều sâu quyết định” là một luận đề thiết kế hợp lý, nhưng không phải định luật. Viết: “juice có thể tăng clarity/empowerment; nó không thay thế bằng chứng rằng người chơi hiểu nguyên nhân và lựa chọn của mình.”
3. **Không suy từ complexity sang UX.** S13 về độ phức tạp của sort puzzle hỗ trợ mô tả formal/computational; không chứng minh cảm giác player. Cần playtest hoặc nghiên cứu HCI để đỡ phần “feeling cốt lõi”.
4. **Sửa và kiểm chứng metadata nguồn.** Link GDC cho *Puzzle Writing: Best Practices* trong thư viện nguồn cần đối chiếu lại: trang GDC hiện được index là `play/1013851`, không phải `1013781`. Đọc/ghi chú bản đầy đủ trước khi trích dẫn nội dung chi tiết.
5. **Đừng để match-3 áp đảo.** Các phần hiện có rất tốt cho match-3/sort. Physics và narrative/escape cần ít nhất một case study developer + một playtest thật, nếu không phạm vi nên thu hẹp thành “systemic puzzle games”.
6. **Tách fairness thực tế và fairness cảm nhận.** Puzzle có thể hoàn toàn deterministic mà vẫn bị xem là bất công vì signifier/feedback kém; cũng có thể có RNG mà vẫn được chấp nhận nếu player hiểu cách quản trị variance. Mỗi chương nên ghi cả hai loại evidence.
7. **Accessibility là điều kiện nhận thức, không appendix.** Redundancy ngoài màu, timing có thể điều chỉnh và control scheme thay đổi trực tiếp việc người chơi đọc state/dự đoán hệ quả.

## Lời hứa khác biệt nên theo đuổi

**Sau mỗi chương, reader có thể chuyển một nhận xét mơ hồ (“chưa đã”, “khó nhưng không hay”, “board tự chơi”) thành một giả thuyết, một thay đổi prototype và một phép đo playtest.**

Đây là điểm khác biệt tốt hơn “một cuốn về cảm xúc trong game”. Nó cụ thể, kiểm chứng được và phù hợp với designer/producer làm prototype.

### Bộ artefact độc quyền cần có

1. **Feeling Brief (1 trang):** “Player cảm thấy ___ khi họ tự nhận ra/làm ___; game xác nhận bằng ___.”
2. **Causal Feedback Map:** input → state change → signal → prediction for next move; đánh dấu nơi player dễ gán sai nguyên nhân.
3. **Puzzle Trust Audit:** 12–15 câu hỏi kiểm tra state, possibility, prediction, causality, recovery và accessibility.
4. **Playtest coding sheet:** mã CL/AG/FR/AM/AC đã phác thảo, thêm ví dụ quote và quyết định sửa tương ứng.
5. **Before/after micro-case:** cùng một board/level, một biến thay đổi, prediction của player và kết quả đo. Đây nên là “đơn vị chứng minh” chính của sách.

## Cấu trúc ebook đề xuất (ngắn nhưng có chiều sâu)

1. **Feeling nào?** Phân biệt game feel, puzzle trust, agency và insight; nêu mô hình làm việc, giới hạn và evidence standard.
2. **Hợp đồng suy luận.** State/readability, affordance, feedforward, causal feedback; thiết kế failure có thể học.
3. **Cảm giác một nước đi có ý nghĩa.** Choice, trade-off, RNG, cascade, undo/retry và perceived fairness.
4. **Dạy mà không giảng.** Chuỗi see → safe try → understand → purposeful use → twist, với case study grid/logic.
5. **Nhịp, juice và embodied feedback.** Timing/audio/haptic/VFX như tín hiệu phân cấp, không phải lớp trang trí.
6. **Chẩn đoán qua playtest.** Protocol, event log tối thiểu, coding sheet, cách đọc mâu thuẫn giữa metrics và lời nói.
7. **Ba phòng thí nghiệm.** Mỗi lab: sort, match-3, physics; cùng một framework, case/board cụ thể và can thiệp có đối chứng.
8. **Từ hypothesis đến quyết định.** Checklist phát hành và giới hạn của framework.

## Điều kiện để ebook thật sự tốt hơn

- Có **3–5 micro-case gốc** với asset được phép sử dụng và evidence trước/sau; không chỉ bình luận các game nổi tiếng.
- Mỗi luận điểm lớn có một nguồn đã đọc đầy đủ hoặc một quan sát playtest, một phản ví dụ và một thao tác thiết kế.
- Công khai đâu là nghiên cứu, đâu là kinh nghiệm practitioner, đâu là suy luận của tác giả.
- Cho reader tải/copy các template trên và dùng được trong một buổi prototype review 30 phút.
- Có ít nhất một test accessibility trong từng lab, không relegated thành checklist cuối sách.

## Nguồn dùng trong lần định vị này

- Laura Tims, [*The Art of Feeling* — Open Library](https://openlibrary.org/books/OL26930913M/The_art_of_feeling).
- Steve Swink, [*Game Feel: A Game Designer’s Guide to Virtual Sensation* — Routledge](https://www.routledge.com/Game-Feel-A-Game-Designers-Guide-to-Virtual-Sensation/Swink/p/book/9780123743282).
- Pichlmair & Johansen, [*Designing Game Feel. A Survey*](https://arxiv.org/abs/2011.09201).
- Jesse Schell, [*The Art of Game Design*](https://schellgames.com/art-of-game-design).
- Clara Fernández-Vara, [GDC: *Puzzle Writing: Best Practices*](https://www.gdcvault.com/play/1013851/Puzzle-Writing-Best).
- Patrick Traynor, [GDC: *System-Centric Puzzle Design in Patrick’s Parabox*](https://www.gdcvault.com/play/1034415/System-Centric-Puzzle-Design-in).
