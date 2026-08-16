# Domain Dossier — Feeling trong Puzzle Game

## Định nghĩa vận hành

Theo khảo sát học thuật của Pichlmair & Johansen, game feel là thiết kế có chủ ý tác động cảm xúc của tương tác từng-khoảnh-khắc; họ nhóm các ý đồ thành **physicality, amplification, support**, tương ứng với tuning, juicing và streamlining [S1]. Đây là điểm xuất phát tốt, nhưng với puzzle game cần bổ sung một tầng: **intelligibility** — người chơi phải đọc được hệ thống để cảm giác là “tôi suy ra”, thay vì “game chạy đẹp”.

Mô hình đề xuất cho bài viết:

```text
Luật dễ đọc + input tin cậy
          ↓
Người chơi hình thành giả thuyết
          ↓
Phản hồi đúng lúc, đúng nguyên nhân
          ↓
Người chơi cập nhật mô hình tinh thần
          ↓
Khó hơn nhưng vẫn công bằng ──→ cảm giác làm chủ / fiero
          ↑
Nhịp level, retry và phần thưởng giữ cho vòng lặp tiếp tục
```

Đây là **mô hình biên tập**, không phải một kết luận thực nghiệm độc lập; từng mắt xích cần được đối chiếu bằng nguồn và playtest.

## Những đặc thù của puzzle game

### 1. Feedback là bằng chứng, không chỉ là phần thưởng

Trong action game, người chơi đôi khi vẫn có thể vui dù chưa hiểu hết nguyên nhân. Với puzzle, feedback phải giúp trả lời: *nước đi vừa rồi đã thay đổi trạng thái nào, vì sao, và điều đó mở/đóng khả năng gì?* Nguồn GDC về puzzle writing gọi puzzle là một “hợp đồng” mà designer phải cung cấp đủ thông tin để giải mà vẫn duy trì thử thách [S4].

Hệ quả: highlight, rung, âm thanh, cascade, preview, undo và thông báo fail đều là công cụ giải thích nhân quả. Lạm dụng chúng dễ chuyển thử thách từ suy luận thành thử-sai.

### 2. Agency quan trọng hơn sự phô trương

*Juicing* giúp làm rõ tầm quan trọng của event và tạo empowerment [S1]. Nhưng cảm giác mạnh chỉ bền khi người chơi quy được kết quả về quyết định của mình. Hãy theo dõi những câu nói trong test như “board tự cho tôi thắng”, “tôi không biết vì sao thua”, “nước này chắc chắn đúng” — chúng đo *perceived agency*, không chỉ mức hài lòng.

### 3. Difficulty là một đường cong trải nghiệm

Nghiên cứu về mô hình độ khó puzzle lưu ý rằng xác suất thắng cổ điển là không đủ; phân phối hành động trong một level là một mô tả phong phú hơn [S6]. Trong match-3, bài nói chuyện của King còn xem blockers là một nguồn tạo difficulty có thể mô tả bằng bộ chỉ số và ngôn ngữ chung [S5].

Vì vậy, thiết kế/đo lường nên ghi cả: success rate, số move, số retry, thời gian, điểm kẹt, hint use, thời gian từ thất bại đến retry, và lời giải thích bằng lời của người chơi.

### 4. Onboarding là lời hứa về ngôn ngữ game

Tutorial tốt không chỉ chỉ dẫn thao tác; nó thiết lập cách game giao tiếp. Một case reflection về Puzzledorf cho thấy người chơi tin puzzle hơn khi nhận ra mọi phần tử đều có mục đích [S7]. Mỗi mechanic mới nên có chuỗi: **thấy → thử an toàn → hiểu kết quả → dùng có mục đích → kết hợp/đảo kỳ vọng**.

### 5. Flow không đồng nghĩa với không ma sát

Khung flow nhấn mạnh mục tiêu rõ, thử thách vừa sức, feedback kịp thời và ít nhiễu [S2]. Với puzzle, ma sát nhận thức là nguyên liệu của khoảnh khắc “à ha”; ma sát giao diện, luật ngầm và feedback mơ hồ lại là nhiễu. Bài viết nên phân biệt hai loại này thật rõ.

## Quy trình đề xuất cho đội phát triển

1. **Viết feeling target:** “Sau 30 giây, người chơi nên cảm thấy ___ vì họ đã tự nhận ra ___.”
2. **Lập bản đồ nhân quả:** mỗi input, state change và feedback trả lời cho người chơi điều gì?
3. **Greybox không polish:** kiểm tra luật, khả năng đọc và alternative solutions trước.
4. **Tuning:** chỉnh timing, easing, camera, âm thanh, haptic và độ rõ để hành động đáng tin.
5. **Juicing:** khuếch đại event theo mức quan trọng; giữ hierarchy để tín hiệu lớn không bị chìm.
6. **Streamlining:** giảm thao tác thừa, nhưng không tự động hoá mất quyết định thú vị.
7. **Playtest quan sát:** đo hành vi và ngôn ngữ người chơi; đừng chỉ hỏi “có vui không?”.
8. **Đặt ngưỡng bảo vệ:** nếu clarity/agency giảm, không dùng hiệu ứng hay phần thưởng để che nó.

## Rủi ro đặc thù và tín hiệu cảnh báo

| Rủi ro | Triệu chứng | Hướng xử lý để kiểm thử |
|---|---|---|
| Feedback quá to, quá đều | Mọi event nghe/nhìn như chiến thắng | Thiết lập hierarchy theo tầm quan trọng |
| RNG che mờ quyết định | Người chơi không giải thích được thắng/thua | Show causal feedback; review seed/board logic |
| Hint giải hộ | Người chơi làm theo mà không có mô hình | Hint theo tầng: chú ý → quan hệ → gợi ý hành động |
| Difficulty spike | Nhiều retry nhưng không có giả thuyết mới | Tách mechanic, thêm level luyện hoặc đọc board |
| UI/animation làm chậm loop | Người chơi chờ nhiều hơn suy nghĩ | Cho skip, rút animation và đo time-to-next-attempt |
| Chỉ số thắng đẹp nhưng puzzle nhạt | Người chơi thắng mà không nhớ insight | Thêm câu hỏi “điều gì khiến bạn thắng?” sau level |

## Accessibility là một phần của feeling

Khi màu, flash hoặc thao tác là kênh duy nhất để nhận luật/feedback, một phần người chơi bị loại khỏi vòng lặp hiểu–thử–học. Phản hồi cộng đồng Candy Crush nêu trực tiếp các rào cản về colour blindness, hiệu ứng chớp và thao tác cuộn [S10]. Các case study cần bao gồm redundancy: hình dạng/biểu tượng, âm thanh có thể thay thế, điều chỉnh flash, tốc độ và input.
