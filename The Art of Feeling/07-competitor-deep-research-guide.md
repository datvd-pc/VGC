# Đọc đối thủ để tránh trùng ý — Game Feel, Book of Lenses, và Designing Game Feel

**Mục tiêu:** đây là bản đồ nghiên cứu thủ công, không phải bản thay thế ba tác phẩm gốc. Nó tóm tắt luận điểm và chỉ ra phần nào ebook *The Art of Feeling* không nên “đóng gói lại”. Nội dung sách của Swink và Schell được diễn giải ở mức khái niệm; không sao chép chương, lens card, bài tập hay văn bản có bản quyền.

## Cách dùng file này

Khi đọc một tác phẩm gốc, ghi vào cột “Ghi chú của tôi” ba thứ: (1) luận điểm tác giả thật sự đưa ra, (2) ví dụ/case họ dùng, (3) công cụ thiết kế hay câu hỏi họ đưa cho reader. Sau đó đối chiếu cột “Quyết định cho ebook”. Một ý chỉ nên giữ nếu ebook có thể áp dụng nó riêng cho puzzle hoặc biến nó thành phép đo/playtest mới.

| Tác phẩm | Vai trò trong field | Nguy cơ trùng cao nhất với ebook |
|---|---|---|
| Steve Swink, *Game Feel* (2009) | Nền tảng practitioner về virtual sensation và sự điều khiển trong tương tác thời gian thực | Gọi feedback/juice/polish là “feeling” rồi lặp lại taxonomy input–response–context–polish–metaphor–rules |
| Jesse Schell, *The Art of Game Design* | Khung thiết kế tổng quát bằng các lens/câu hỏi chẩn đoán | Viết một tuyển tập câu hỏi game design chung, hoặc trình bày playtest/prototype như khám phá mới |
| Pichlmair & Johansen, *Designing Game Feel. A Survey* (2022) | Tổng quan học thuật, chuẩn hóa vocabulary game feel từ hơn 200 nguồn | Đổi tên physicality/amplification/support thành framework mới mà không có evidence hoặc khác biệt vận hành |

---

## A. Steve Swink — *Game Feel: A Game Designer’s Guide to Virtual Sensation*

### 1. Luận điểm trung tâm

Swink đặt “game feel” vào trải nghiệm điều khiển một đối tượng/thân thể ảo trong không gian mô phỏng, nơi phản hồi được làm nổi bật bằng polish. Khái niệm này không đồng nhất với mọi cảm xúc trong game, chất lượng art, hay toàn bộ game experience. Nó quan tâm trước hết tới cảm giác khoảnh khắc khi **ý định → input → phản hồi** diễn ra.

Tác dụng chiến lược cho ebook của bạn: dùng định nghĩa này làm ranh giới. Một puzzle có thể có game feel tốt nhưng puzzle trust thấp; ví dụ, thao tác swap rất mượt và có VFX hấp dẫn nhưng player không thể giải thích tại sao cascade giúp hoặc làm hỏng goal.

### 2. Bản đồ nội dung khái niệm

| Cụm ý | Swink quan tâm điều gì | Câu hỏi nghiên cứu thủ công | Không đủ cho puzzle nếu… |
|---|---|---|---|
| **Vì sao “feel” quan trọng** | Feel là thành phần thường bị xem nhẹ nhưng tác động mạnh tới cảm giác tham gia, mastery và empowerment | Tác giả phân ranh giới feel với fun/flow/graphics ra sao? Ông dùng evidence hay ví dụ nào? | Player thấy thao tác pleasurable nhưng không biết puzzle đòi hỏi gì |
| **Vị trí của feel trong game design** | Feel là một building block trong trải nghiệm rộng hơn, không thay thế rules, challenge hoặc meaning | Quan hệ được mô tả giữa feel, flow, empowerment và game experience là gì? | Ebook tuyên bố “feel là tất cả” |
| **Trường hợp ít virtual sensation** | Có game digital không lấy việc điều khiển/thể hiện physical skill làm lõi; nó giúp giới hạn phạm vi khái niệm | Puzzle bạn đang xét có realtime control/virtual body không? | Áp định nghĩa action game một cách máy móc cho turn-based puzzle |
| **Input** | Thiết bị, mapping, độ nhạy, latency và cách player diễn đạt ý định | Hành động nào player muốn làm? Input có tạo ra sai khác hữu ích không? | Tap/drag puzzle bị đánh giá chỉ qua “mượt” thay vì ý nghĩa lựa chọn |
| **Response** | Hành động game trả lại: chuyển động, acceleration/deceleration, va chạm, timing và khả năng dự báo | Player mong kết quả nào trước action? Khi sai, họ học gì? | Response đẹp nhưng không cho thấy state transition |
| **Context** | Không gian, camera, đối tượng, luật và mục tiêu làm một phản hồi có nghĩa | Cùng response đặt trong context khác có đổi quyết định không? | Board/objective không đọc được, nên feedback không có cái gì để “làm rõ” |
| **Polish** | Các lớp tăng cường nhận thức: animation, VFX, sound, camera, indicators… | Tín hiệu nào biểu thị event quan trọng? Tín hiệu nào chỉ làm rối? | Mọi event đều được khuếch đại như nhau và hierarchy biến mất |
| **Metaphor** | Ẩn dụ/logic thế giới giúp player hiểu action và kỳ vọng kết quả | Theme nói cùng một câu chuyện với rule và visual language không? | Theme che hoặc mâu thuẫn với ràng buộc puzzle |
| **Rules** | Cảm giác có nền tảng ở quy luật của mô phỏng, không chỉ hiệu ứng bề mặt | Rule có ổn định và learnable không? | Một puzzle fail vì luật ngầm/RNG nhưng team chỉ tăng screen shake |
| **Perception & mastery** | Player xây một mô hình cảm nhận và học skill; việc làm chủ mapping có thể pleasurable | Player đang học motor skill, mental model, hay cả hai? | Coi cognitive friction như lỗi điều khiển, hoặc coi UI friction là “thử thách puzzle” |
| **Phân tích ví dụ và nguyên tắc** | Sách dùng ví dụ để suy ra cách tạo cảm giác dự báo được, có phản hồi và đáng làm chủ | Ghi lại cấu trúc: claim → example → design variable → test của từng ví dụ | Copy nguyên tắc sang ebook mà không chứng minh nó áp dụng vào suy luận puzzle |

### 3. Taxonomy sáu thành phần: phần dễ trùng nhất

Publisher của sách mô tả taxonomy gồm **input, response, context, polish, metaphor, rules**. Khi dùng trong ebook, luôn ghi đây là taxonomy của Swink và dùng nó làm “nền” thay vì đóng gói lại như đóng góp mới.

| Thành phần của Swink | Ứng dụng puzzle hợp lệ | Góc mở rộng riêng cho ebook |
|---|---|---|
| Input | Swap, drag, tap, draw, undo, commit | Input nào là quyết định chiến lược, input nào chỉ là thao tác cơ học? |
| Response | Board/state thay đổi sau move | Player có nói được **vì sao** state thay đổi? |
| Context | Objective, blocker, topology, move budget | Player có nhận ra move đang phục vụ objective nào? |
| Polish | Sound/VFX/haptic/animation/indicator | Tín hiệu có giúp truy vết nguyên nhân đầu tiên của cascade không? |
| Metaphor | Nước chảy, vật thể rơi, hộp lồng nhau, v.v. | Metaphor có dạy affordance mà không tạo false intuition không? |
| Rules | Constraint, resource, win/fail condition, RNG | Rule có thể dự đoán, kiểm chứng và hồi phục sau sai lầm không? |

### 4. Những phần tuyệt đối không nên tuyên bố là mới

- Feedback nghe/nhìn có thể làm event quan trọng nổi bật hơn.
- Predictability và responsiveness quan trọng cho cảm giác kiểm soát.
- Animation, sound, camera, particle và indicator ảnh hưởng cảm nhận interaction.
- Player học và làm chủ một mapping/skill có thể thấy thích thú.
- Metaphor, context và rules tham gia tạo feel; không phải chỉ “juice”.

### 5. Khoảng trống còn lại cho ebook

Swink không phải một manual chuyên về thiết kế puzzle. Lời hứa riêng có thể là kiểm tra vòng **state → possibility → prediction → causality → learning**. Đó là lớp nhận thức có thể sử dụng taxonomy của Swink, nhưng không cùng câu hỏi: *feedback có làm player cập nhật chiến lược đúng không?*

### 6. Checklist khi bạn đọc sách gốc

- [ ] Ghi nguyên nghĩa tác giả dùng cho “game feel” và các phạm vi ông loại trừ.
- [ ] Lập bảng cho mọi ví dụ puzzle/non-action mà sách có; không giả định sách chỉ nói về action.
- [ ] Ghi tất cả biến mà tác giả coi là controllable trong prototype.
- [ ] Đánh dấu mọi đoạn về predictability, feedback, metaphor, rules, learning/mastery.
- [ ] Với từng ý định đưa vào ebook, viết “điều gì ở puzzle làm ý này khác?” Nếu không trả lời được, chỉ cite Swink hoặc bỏ.

---

## B. Jesse Schell — *The Art of Game Design: A Book of Lenses*

### 1. Luận điểm trung tâm

Schell trình bày game design như việc đưa ra nhiều quyết định nhằm tạo trải nghiệm. “Lens” là một góc nhìn/cognitive checklist: nó đặt một nhóm câu hỏi cụ thể để team nhìn game qua một vấn đề như challenge, flow, risk, toy, community hay economy. Sức mạnh của sách là **độ bao quát** và việc biến design critique thành câu hỏi chung của đội, chứ không hứa một công thức duy nhất.

Ghi chú phiên bản: trang chính thức hiện giới thiệu hơn 100 lenses; bài giới thiệu audiobook tháng 07-2026 nói Third Edition có 116 câu hỏi chẩn đoán và bổ sung bối cảnh hiện đại như VR/AR/MR/live-ops. Khi nghiên cứu, ghi rõ bạn đang đọc edition nào — không gán nội dung bản 3 cho bản cũ.

### 2. Bản đồ nội dung khái niệm

| Cụm ý | Sách giải quyết | Câu hỏi nghiên cứu thủ công | Rủi ro nếu ebook lặp lại |
|---|---|---|---|
| **Trải nghiệm trước tiên** | Designer thiết kế cho trải nghiệm player, không phải cho feature list | Tác giả hướng dẫn mô tả desired experience thế nào? | “Feeling target” chỉ là đổi tên của experience goal |
| **Designer và quá trình sáng tạo** | Ra quyết định, giao tiếp, vượt qua giả định và bias | Lens nào giúp team nhận ra tự tin sai? | Biến ebook thành self-help cho designer |
| **Elemental Tetrad** | Mechanics, story, aesthetics, technology tương tác nhưng không ngang nhau trong mọi vấn đề | Một issue puzzle thuộc mechanics, aesthetics, technology hay story? | Tuyên bố một lớp (như VFX) tự giải toàn bộ vấn đề |
| **Mục tiêu, challenge, puzzle** | Thiết kế cấu trúc challenge, choice, problem và payoff | Lens/passage nào trực tiếp nói về puzzle? Nó phù hợp với systemic puzzle hay narrative puzzle? | Đưa “puzzle contract” chung chung mà không có diagnostic có thể test |
| **Flow, curiosity, surprise, fun** | Các trạng thái/motivations khác nhau cần góc nhìn riêng | Sách phân biệt chúng ra sao? Khi nào chúng mâu thuẫn? | Đồng nhất flow với “không có ma sát” |
| **Player & psychology** | Lấy người chơi thật, empathy và động lực làm tâm điểm | Lens nào yêu cầu quan sát, không chỉ suy đoán? | Dùng personas thay cho playtest |
| **Theme/story/world** | Ý nghĩa, narrative, world và aesthetics có thể giúp hoặc cản tương tác | Theme puzzle có hỗ trợ affordance/goal không? | Dùng fiction để hợp thức hóa một rule không đọc được |
| **Iteration & playtest** | Prototype, test và revise giúp thiết kế học từ player | Dấu hiệu nào khiến tác giả yêu cầu prototype/test lại? | Tuyên bố vòng lặp prototype-test-revise là phương pháp độc quyền |
| **Team, documentation, business** | Design sống trong điều kiện team, scope, communication và thị trường | Phần nào không thuộc phạm vi ebook puzzle feeling? | E-book phình thành handbook game design tổng quát |

### 3. Lens: nên hiểu đúng cách

Lens không phải là “quy tắc” hay đáp án. Nó là cách ép team đổi câu hỏi khi thiết kế bị bế tắc. Ví dụ từ trang chính thức: lens có thể xét toy, flow, community, challenge, economy hoặc risk. Vì vậy, ebook không nên đối đầu bằng cách tạo 100 “puzzle feeling lenses”.

Thay vào đó, chỉ tạo 5 lens có đầu ra vận hành:

| Lens hẹp đề xuất | Câu hỏi | Evidence cần thu | Đòn bẩy sửa prototype |
|---|---|---|---|
| **State** | Player có biết điều gì quan trọng ngay bây giờ không? | Ghi nhớ board 5 giây, verbal scan | Signifier, grouping, hierarchy, camera |
| **Possibility** | Họ nhìn được ít nhất hai lựa chọn có ý nghĩa không? | Nêu lựa chọn trước action | Affordance, objective đọc được, topology |
| **Prediction** | Họ dự đoán hệ quả của move không? | Prediction trước commit | Preview, metaphor, tutorial/sandbox |
| **Causality** | Sau event, họ quy nguyên nhân đúng không? | Giải thích sau cascade/fail | Feedback ordering, log, VFX hierarchy |
| **Learning/recovery** | Lần thử sau có strategy thay đổi không? | Quote sau fail, undo/retry pattern | Hint theo tầng, undo, failure explanation |

Đây là đóng góp hợp lý chỉ khi mỗi lens có protocol và case thực tế. Nếu chỉ có câu hỏi, nó vẫn là biến thể hẹp của Schell.

### 4. Những phần tuyệt đối không nên tuyên bố là mới

- Design cần nhiều góc nhìn thay vì một công thức.
- Experience của player quan trọng hơn ý định/feature của designer.
- Prototype, playtest, iteration là cốt lõi của game design.
- Challenge, curiosity, flow, choice, story, aesthetics và mechanics có liên hệ.
- Câu hỏi chẩn đoán là công cụ hữu ích để team thảo luận.

### 5. Khoảng trống còn lại cho ebook

Schell bao quát nhiều loại game và nhiều tầng production. Ebook của bạn có thể làm tốt hơn ở độ **cụ thể hóa**: không chỉ hỏi “challenge có tốt không?” mà đưa state snapshot, prediction prompt, coding scheme, event log và quy tắc quyết định sửa gì trước.

### 6. Checklist khi bạn đọc sách gốc

- [ ] Lập index tất cả lens liên quan: challenge, puzzle, flow, curiosity, surprise, choice, control, risk, feedback, playtest, accessibility (nếu edition có).
- [ ] Ghi câu hỏi lens theo cách hiểu của bạn, không copy card/đoạn sách vào ebook.
- [ ] Với mỗi lens, gắn đúng một chương ebook hoặc ghi “ngoài phạm vi”.
- [ ] Đánh dấu các lens đủ tổng quát để chỉ trích dẫn, không cần diễn giải lại.
- [ ] So sánh Feeling Brief với cách Schell mô tả desired experience; sửa tên/cấu trúc nếu quá giống.

---

## C. Pichlmair & Johansen — *Designing Game Feel: A Survey*

### 1. Phạm vi và giá trị học thuật

Đây là bài survey peer-reviewed xuất bản năm **2022** trong *IEEE Transactions on Games* (14(2), pp. 138–152; DOI: 10.1109/TG.2021.3072241). Bản arXiv có từ 2020 nên cả hai năm có thể xuất hiện trong ghi chú; khi trích chuẩn thư mục, dùng 2022. Tác giả phân tích hơn 200 nguồn học thuật và practitioner, rồi tổ chức chúng theo **mục đích thiết kế**, không phải chứng minh một causal model thực nghiệm mới.

Điều đó có nghĩa: đây là nguồn rất mạnh để dùng vocabulary và chỉ ra field đã nói gì; nó không tự mình chứng minh rằng một mechanic puzzle cụ thể sẽ tạo cảm giác X ở mọi player.

### 2. Khung 3 × 3 cần thuộc

| Intended player experience | Hành động “polishing” tương ứng | Tác động được bài survey gán | Ví dụ puzzle để nghiên cứu | Cảnh báo khi dùng |
|---|---|---|---|---|
| **Physicality** | **Tuning** | Cohesion và predictability của đối tượng/chuyển động; movement còn tác động tới level design | Nước chảy trong sort, quỹ đạo physics, gravity match-3 | Đừng hiểu là realism. Cartoon vẫn có physicality nếu luật nhất quán và đọc được. |
| **Amplification** | **Juicing** | Empowerment và clarity of feedback bằng cách truyền tầm quan trọng của event | Match/special combo, clear blocker, complete container | “Clarity of feedback” không đồng nghĩa “clarity of puzzle rule”; effect có thể nói event lớn nhưng không giải thích strategy. |
| **Support** | **Streamlining** | Game hành động theo intention, hỗ trợ thực thi action | Snap, smart selection, forgiving input, undo, skip thao tác vụn | Streamlining có thể xóa một quyết định thú vị; phân biệt execution friction với cognitive challenge. |

### 3. Cách đọc ba domain cho puzzle

#### Physicality / tuning

Hỏi: thế giới puzzle có nhất quán để player học không? Motion, collision, spacing, transfer, trajectory, timing và camera có giúp player dự đoán không? Trong sort puzzle, hoạt ảnh “pour” không cần thật nhưng phải biểu đạt chính xác thứ tự, capacity và kết quả transfer. Trong physics puzzle, player cần hiệu chỉnh mental model sau fail, không chỉ thấy animation hấp dẫn.

**Không trùng ý nếu ebook thêm:** một test prediction trước action và phân loại bất ngờ *có ích* (sửa mô hình) vs. *không công bằng* (không quy nguyên nhân được).

#### Amplification / juicing

Hỏi: event nào thực sự đáng chú ý, và player có phân biệt được chúng? Animation, sound, haptic, UI, camera, particles và delay có thể tạo hierarchy cho move, combo, completion, near-miss và failure. 

**Không trùng ý nếu ebook thêm:** Causal Feedback Map theo thứ tự “move của player → state change → chain reaction → objective progress”, kiểm tra player có còn biết điều nào do mình khởi tạo sau cascade hay không.

#### Support / streamlining

Hỏi: game hỗ trợ ý định của player ở đâu? Snap, hit target lớn, input buffering, camera, undo, quick retry, automation, accessibility option và hint đều có thể giảm ma sát thực thi. Nhưng puzzle game đôi khi cần giữ ma sát nhận thức để tạo insight.

**Không trùng ý nếu ebook thêm:** một tiêu chí giữ/bỏ ma sát: giữ khi player đang tạo và kiểm tra hypothesis; bỏ khi UI, camera, animation hoặc thao tác lặp khiến họ không thể làm điều đó.

### 4. Những điều không được diễn đạt quá đà

- Survey không nói “juice chỉ là trang trí” hoặc “juice không thể tạo depth”. Nó đặt juice trong amplification, liên hệ với empowerment và clarity of feedback.
- Survey không cung cấp một scale đo “puzzle fairness”, “puzzle trust”, “aha” hay retention cho mọi game.
- Ba domain không phải checklist thay thế playtest; chúng là vocabulary để mô tả/cùng thảo luận về minute details of interactivity.
- “Intelligibility” của ebook là luận đề/khung của tác giả ebook. Nó có thể đối thoại với survey, nhưng không nên gán cho Pichlmair & Johansen nếu bài không dùng nó như dimension độc lập.

### 5. Checklist đọc bài gốc

- [ ] Đọc abstract, introduction và conclusion để ghi chính xác scope/method của survey.
- [ ] Vẽ lại 3 × 3 bằng lời của mình, kèm một example *ngoài* action game.
- [ ] Ghi các nguồn primary mà survey trích cho tuning, juicing, streamlining; ưu tiên đọc những nguồn liên quan trực tiếp puzzle.
- [ ] Đánh dấu bằng chứng nào là practitioner framing, evidence nào là academic study.
- [ ] Tìm mọi giới hạn/future work tác giả nêu; đây là nơi ebook có thể bổ sung mà không “đổi nhãn” framework cũ.

---

## D. Ma trận quyết định: dùng, trích dẫn, hay tránh

| Ý định viết trong ebook | Tình trạng sau khi đối chiếu | Cách xử lý an toàn |
|---|---|---|
| “Feedback/juice làm event rõ và mạnh hơn” | Đã có ở Swink + survey | Trích nguồn; chỉ thêm ví dụ puzzle riêng |
| “Input responsive và predictability tạo sense of control” | Đã có ở Swink + survey | Trích nguồn; không đóng khung như discovery |
| “Design nên hướng tới player experience và test lặp” | Đã có ở Schell | Dùng như premise, không dành một chương giới thiệu dài |
| “Nhiều câu hỏi/lenses giúp critique” | Đã có ở Schell | Chỉ giữ 5 lens puzzle nếu có measure + intervention rõ |
| “Clarity/agency là quan trọng với puzzle” | Có quan hệ với cả ba, nhưng chưa đủ đặc thù | Xây dựng evidence bằng case/playtest, định nghĩa vận hành riêng |
| “Puzzle fairness là information contract” | Có practitioner precedent (Fernández-Vara) | Cite; mở rộng sang RNG/retry/live balancing bằng case riêng |
| “Causal feedback phải bảo toàn attribution trong cascade” | Khoảng trống khả thi | Xác nhận bằng 3–5 micro-case và observation protocol |
| “Friction tốt vs. friction xấu” | Có liên hệ với support/streamlining và puzzle pedagogy | Định nghĩa bằng hành vi quan sát được, không chỉ khẩu hiệu |

## E. Output bắt buộc sau nghiên cứu thủ công

Chỉ bắt đầu bản thảo khi có đủ 5 artefact sau:

1. **Overlap ledger:** ý → nguồn gốc → trích dẫn cần dùng → phần ebook thêm vào.
2. **Do-not-repeat list:** ít nhất 15 ý đã được Swink/Schell/survey xử lý tốt và không cần giải thích lại.
3. **Puzzle-specific claims:** 5–7 luận điểm hẹp; mỗi luận điểm có định nghĩa, phản ví dụ, case, và phép quan sát.
4. **Evidence map:** phân biệt research / practitioner / dữ liệu playtest / suy luận tác giả.
5. **Chapter exclusion rule:** bất kỳ chương nào không tạo ra một artifact hay protocol có thể áp dụng trên prototype thì cắt hoặc gộp.

## Nguồn chính thức và thư mục

- Swink, S. (2009). [*Game Feel: A Game Designer’s Guide to Virtual Sensation*](https://www.routledge.com/Game-Feel-A-Game-Designers-Guide-to-Virtual-Sensation/Swink/p/book/9780123743282). CRC Press/Routledge. Publisher mô tả sách 376 trang, cùng taxonomy sáu thành phần và playset đi kèm.
- Schell, J. [*The Art of Game Design: A Book of Lenses*](https://schellgames.com/art-of-game-design). Trang chính thức của Schell Games mô tả phương pháp lens và deck/app hỗ trợ workshop.
- Pichlmair, M., & Johansen, M. (2022). [*Designing Game Feel: A Survey*](https://pure.itu.dk/da/publications/designing-game-feel-a-survey/). *IEEE Transactions on Games*, 14(2), 138–152. DOI: [10.1109/TG.2021.3072241](https://doi.org/10.1109/TG.2021.3072241).
