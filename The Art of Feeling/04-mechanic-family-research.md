# Mechanic Family Research — Sort, Match-3, Physics

## Mục đích và giới hạn

Tài liệu này xác định **lõi feeling cần bảo toàn** khi một game mới muốn sáng tạo trên ba họ mechanic. “Chuẩn” ở đây không phải checklist để clone game thành công, mà là một tập **invariant trải nghiệm**: nếu thay đổi mechanic mà làm mất các invariant này, game phải chứng minh bằng playtest rằng đã tạo được một cảm giác thay thế tốt hơn.

Các kết luận dưới đây kết hợp: nguồn học thuật về game feel/difficulty [S1, S6, S13, S16, S17], nguồn practitioner/GDC [S5, S14, S15], và phân tích thiết kế. Mọi mục gắn nhãn **[Giả thuyết]** phải được test trên prototype, không trích như kết luận phổ quát.

## Chuẩn chung xuyên mechanic: vòng lặp feeling tối thiểu

```text
Đọc state → hình thành dự đoán → cam kết input → thấy nguyên nhân/kết quả → cập nhật chiến lược
```

Một cải tiến được coi là giữ lõi feeling nếu người chơi vẫn có thể trả lời, bằng lời hoặc hành vi:

1. **State:** “Ngay bây giờ, điều gì quan trọng trên board?”
2. **Possibility:** “Tôi có những lựa chọn có ý nghĩa nào?”
3. **Prediction:** “Nếu chọn A, tôi mong điều gì xảy ra?”
4. **Causality:** “Kết quả vừa rồi đến từ đâu?”
5. **Learning:** “Lần sau tôi sẽ làm gì khác hoặc tốt hơn?”

Nếu người chơi không trả lời được (2) và (3), đó là thiếu agency; không nên dùng juice để che. Nếu không trả lời được (4), đó là thiếu causal feedback. Nếu không trả lời được (5) sau fail, đó là friction xấu. Khung này nối trực tiếp với “puzzle contract” [S3/S4], feedback rõ/kịp thời [S2], và game-feel amplification/support [S1].

## 1. Sort puzzle (water/ball/screw/object sort)

### Hạt nhân của mechanic

Sort puzzle biến một state lộn xộn thành state có trật tự bằng thao tác chuyển/nhóm dưới các ràng buộc. Với water/ball sort điển hình, player chỉ chạm phần tử ở trên; đích phải trống hoặc cùng loại; sức chứa biến ô trống thành tài nguyên chiến lược [S13, S14].

**Feeling cốt lõi [Giả thuyết]:** *“Tôi đang giải phóng và tổ chức lại một hệ thống; mỗi lần dọn đúng là không gian suy nghĩ của tôi rộng hơn.”*

| Invariant cần giữ | Vì sao nó tạo feeling | Dấu hiệu bị phá vỡ |
|---|---|---|
| Ràng buộc nhìn là hiểu | Cái khó đến từ thứ tự và planning, không từ luật ẩn | Người chơi thử mọi cặp để tìm nước đi hợp lệ |
| Workspace là tài nguyên có thể đọc | Ô/chai trống tạo tension, choice và payoff | Player không biết tại sao một move làm board “chết” |
| Một thao tác có kết quả gọn | Thấy block/nhóm được giải phóng và trạng thái đổi rõ | Animation dài hoặc transfer mơ hồ làm mất nhịp suy luận |
| Undo/restart khôi phục thử nghiệm | Cho phép khám phá mà không biến sai thành punishment vô ích | Người chơi né thử nghiệm hoặc reset vì không hiểu lỗi |
| State sau move dễ quét lại | Loop suy nghĩ tiếp tục nhanh | Màu/shape/stack bị che, camera hoặc effect cản đọc |

### Các trục có thể sáng tạo mà không mất lõi

- **Đổi biểu tượng:** nước → bóng → ốc → vật dụng → khách hàng/đơn hàng; nhưng trạng thái top/nhóm/capacity phải vẫn trực quan.
- **Đổi loại ràng buộc:** container có khóa, mục tiêu thứ tự, vùng tạm, vật phẩm che thông tin; chỉ thêm khi player có một cách đáng tin để dự báo và học nó.
- **Đổi payoff:** hoàn tất container có thể kích hoạt chuỗi, thay đổi không gian hoặc kể chuyện; payoff không nên khoá mất workspace mà không báo trước.
- **Đổi pacing:** mode thư giãn không timer, mode score/moves, hoặc meta-progression; phải giữ đủ thời gian để đọc và lên kế hoạch tương ứng với target feeling.

### Câu hỏi gate trước khi thêm mechanic mới

1. Sau 10 giây, người chơi có chỉ đúng phần tử nào có thể thao tác và lý do không?
2. Move hợp lệ có luôn cho feedback khác biệt với move không hợp lệ, nhưng feedback fail có làm họ hiểu luật thay vì thấy bị chặn không?
3. Resource trống/tạm có còn tạo lựa chọn thật, hay chỉ là bước bắt buộc lặp lại?
4. Mechanic mới tăng **không gian quyết định** hay chỉ tăng số màu/đối tượng cần nhớ?
5. Người chơi có thể undo để rút một bài học cụ thể không? Nếu không, fail có thể giải thích được không?
6. Theme/animation có che thứ tự stack, sức chứa hoặc màu/loại không? Có redundancy ngoài màu không?

### Test nhanh

Cho player xem board 5 giây, che lại rồi hỏi: “Bạn muốn đổ gì vào đâu, vì sao?” Theo dõi tỷ lệ dự đoán đúng về tính hợp lệ của move và thời gian từ khi pour xong đến khi chọn nước tiếp. Đây là proxy cho **readability + planning cadence**, không phải KPI thành công cuối cùng.

## 2. Match-3

### Hạt nhân của mechanic

Match-3 là chọn/hoán đổi cục bộ để tạo match, giải phóng board, đạt objective và sinh cascade. Bản khảo sát practitioner về 45 mechanics cho thấy mechanics level quyết định tactics và variety [S15]; King mô tả blockers như drivers của difficulty cần ngôn ngữ chung [S5].

**Feeling cốt lõi [Giả thuyết]:** *“Tôi nhìn ra một nước đi có đòn bẩy; nó biến cơ hội cục bộ thành tiến độ nhìn thấy được, với một phần bất ngờ thú vị nhưng không tước quyền quyết định.”*

| Invariant cần giữ | Vì sao nó tạo feeling | Dấu hiệu bị phá vỡ |
|---|---|---|
| Nước đi có ý nghĩa cục bộ | Player nhìn thấy reason để swap, không chỉ tìm match bất kỳ | Mọi match trông tương đương hoặc best move không thể nhận ra sau khi học |
| Objective và obstacle đọc được | Tactic sinh từ quan hệ giữa match, blocker, mục tiêu | Board bận nhưng không biết ưu tiên nào mở đường |
| Cascade là phần thưởng có quan hệ nhân quả | Surprise khuếch đại nước đi đã chọn | Người chơi gán win/loss hoàn toàn cho board/RNG |
| Special/combo có hierarchy | Tạo mục tiêu ngắn hạn và payoff rõ | Effect đều lớn, combo không đáng nhớ, hoặc chain làm mất track state |
| Fail gợi một chiến lược mới | Retry là cơ hội học chứ không chỉ roll lại | Sau fail player nói “cầu board tốt hơn” thay vì điều chỉnh tactic |

### Các trục có thể sáng tạo mà không mất lõi

- **Board topology:** hex, đường ray, nhiều board, gravity đổi hướng, không gian 3D; affordance tạo match và mục tiêu phải được dạy bằng level, không chỉ bằng overlay.
- **Action economy:** swap, tap, drag, charge hoặc lựa chọn trước turn; giữ latency thấp và kết quả của action có thể giải thích.
- **Objective:** thu thập, mở đường, rescue, xây dựng, combat; objective phải biến “match nào?” thành câu hỏi chiến lược, không thành danh sách việc che board.
- **Uncertainty:** random spawn, fog, biến thể blocker; cho player cách quản trị xác suất (setup, reserve, preview, recovery) thay vì để RNG quyết định toàn bộ.

### Câu hỏi gate trước khi thêm mechanic mới

1. Mechanic này tạo ra ít nhất một **quyết định mới** (trade-off), hay chỉ thêm lượt để clear?
2. Player có thể nhìn một turn và nói nước đi này giúp objective nào không?
3. Nếu cascade xảy ra, họ có còn nhận ra tác nhân đầu tiên là nước đi của mình không?
4. Blocker có hành vi, counterplay, progress state và visual language riêng không? [S5]
5. Thêm randomness có làm một người chơi giỏi tăng xác suất thắng/giảm thiệt hại được không?
6. Khi thua, game có cung cấp thông tin để đổi tactic ở attempt sau, hay chỉ khiến replay giống slot machine?

### Test nhanh

Tạm dừng board trước swap và hỏi: “Bạn chọn nước này để làm gì?” Sau cascade, hỏi: “Điều nào do bạn tạo ra, điều nào là may mắn?” Một match-3 mới giữ lõi feeling khi player vẫn liên kết **ý định → setup → payoff**, kể cả khi kết quả có ngẫu nhiên.

## 3. Physics puzzle

### Hạt nhân của mechanic

Physics puzzle yêu cầu player dùng quy luật chuyển động, lực, va chạm, trọng lực hoặc tính chất vật liệu để đưa object/hệ thống tới goal. Khác với việc mô phỏng chính xác tuyệt đối, điều quyết định feeling là **mô hình vật lý mà player học được có nhất quán và đủ dự báo để hành động**. Điều này khớp với game-feel *physicality* (tuning tạo cohesion/predictability) và *support* (game hỗ trợ ý định người chơi) [S1].

**Feeling cốt lõi [Giả thuyết]:** *“Tôi có một trực giác vật lý trong thế giới này; tôi tưởng tượng, thử và chứng kiến thế giới xác nhận hoặc tinh chỉnh trực giác đó.”*

| Invariant cần giữ | Vì sao nó tạo feeling | Dấu hiệu bị phá vỡ |
|---|---|---|
| Quy luật đủ nhất quán để học | Player xây mô hình tinh thần và dám thử | Cùng input cho kết quả không giải thích được |
| Affordance và phạm vi tác động dễ đọc | Player biết vật nào, lực nào, điểm nào liên quan | Trial-and-error vì không rõ thứ gì interactable |
| Feedforward trước khi cam kết | Quỹ đạo/force/placement có thể ước lượng | Fail xảy ra sau một hành động không thể dự báo |
| Kết quả có độ “nặng” và hierarchy | Va chạm, lực, thành công cho cảm giác embodied | Animation đẹp nhưng không truyền tốc độ, khối lượng, nguyên nhân |
| Iteration nhanh, recovery rõ | Thử nghiệm là gameplay, không là thao tác chờ | Reset/loading/camera khiến chi phí học quá cao |

### Các trục có thể sáng tạo mà không mất lõi

- **Đổi luật vật lý có chủ đích:** gravity xoay, thời gian dừng, từ tính, trạng thái vật liệu; mỗi luật cần một sandbox/level an toàn để player dự đoán rồi kiểm chứng.
- **Đổi input:** vẽ, kéo, bắn, xếp, điều chỉnh tham số; input visual phải nối trực tiếp với lực/tác động mà game sẽ áp dụng.
- **Đổi goal:** đưa vật tới đích, tạo reaction chain, bảo vệ cấu trúc, tối ưu năng lượng; goal cần giúp đọc “thành công vật lý” là gì.
- **Đổi thẩm mỹ:** cartoon, surreal, toy-like; có thể phi hiện thực, nhưng không được thay đổi quy tắc ngầm giữa chừng.

### Câu hỏi gate trước khi thêm mechanic mới

1. Player có thể dự đoán hướng/khoảng kết quả trước khi thả/chạm không? Nếu không chính xác, họ có hiểu sai ở đâu không?
2. Vật thể nào là interactable, vật thể nào là décor, và điều đó có thể phân biệt mà không dựa riêng vào màu không?
3. Camera, hitbox, collision và animation có kể cùng một “câu chuyện vật lý” không?
4. Randomness có làm thí nghiệm không lặp lại? Nếu có, có lý do trải nghiệm thật sự mạnh hơn loss of learnability không?
5. Một thất bại có thể retry nhanh đến mức player thử giả thuyết tiếp theo ngay không?
6. Mechanic mới có tạo câu hỏi vật lý mới, hay chỉ làm timing/hit precision khắt khe hơn?

### Test nhanh

Trước hành động có hậu quả, yêu cầu player vẽ/nói quỹ đạo hoặc kết quả dự kiến; sau hành động hỏi “điều gì làm bạn ngạc nhiên?”. Phân loại: bất ngờ **sinh ích** (sửa mô hình) vs. bất ngờ **không công bằng** (không thể suy nguyên nhân). Đây là test trực tiếp cho predictability, không phải độ thật của mô phỏng.

## Ma trận quyết định: đổi mới hay làm suy lõi?

| Đề xuất thay đổi | Giữ lõi khi… | Cảnh báo |
|---|---|---|
| Thêm object/biến thể | Tạo trade-off hoặc cách giải mới có thể đọc | Chỉ tăng clutter/memory load |
| Thêm RNG | Player quản trị hoặc hồi phục từ variance | RNG xoá liên hệ action–outcome |
| Giảm undo/tăng phạt | Có mục tiêu tension rõ và fail dạy được | Phạt chủ yếu làm player sợ khám phá |
| Thêm VFX/haptic | Làm rõ event quan trọng, không che state | Mọi action “nổ” như nhau hoặc chặn input |
| Thêm meta/progression | Bổ sung động lực mà không phá nhịp puzzle | Xen kẽ màn hình/offer vào lúc player đang suy nghĩ |
| Tự động hoá thao tác | Bỏ việc cơ học, giữ lại lựa chọn thú vị | Auto-play luôn cả phần tạo insight |

## Protocol kiểm chứng trước khi gọi là “cải tiến”

1. Viết một câu feeling target theo format: “Player cảm thấy ___ khi họ tự ___.”
2. Chạy prototype gốc và prototype mới với cùng nhóm đối tượng; randomise thứ tự nếu có thể.
3. Thu prediction trước action, think-aloud chọn lọc, video, event log, số undo/retry và lý do thắng/thua player tự nói.
4. Đánh giá theo năm câu hỏi của vòng lặp feeling, không chỉ completion/retention.
5. Giữ thay đổi nếu nó tạo trải nghiệm mới **và** không làm giảm rõ rệt clarity, agency, causal learning — trừ khi có bằng chứng người chơi thích trade-off đó.

## Khoảng trống research tiếp theo

- Đọc toàn văn S13 để tách property tính toán của sort khỏi cảm nhận người chơi.
- Tìm và đọc case study developer về Portal/Cut the Rope/World of Goo hoặc physics-puzzle tương đương; hiện phần physics dựa nhiều trên S1 và phân tích, nên chưa đủ case-specific.
- Thu 5–8 video playtest cho mỗi họ mechanic, ưu tiên các biến thể có mechanic “lạ”, để kiểm định ma trận này.
