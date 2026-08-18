# The Art of Feeling — Tổng hợp nghiên cứu, phản biện và chiến lược ebook

> Cập nhật: 18-08-2026. Tài liệu này tổng hợp và diễn giải bằng tiếng Việt toàn bộ tri thức có liên quan trong workspace, không phải bản dịch hay thay thế toàn văn các sách/bài nói có bản quyền. Với tài liệu thương mại, chỉ giữ ý niệm, khung làm việc và cách áp dụng; trích dẫn/đọc nguyên tác theo nguồn hợp pháp.

## 1. Luận đề trung tâm

Puzzle game có “feeling” tốt không phải chỉ vì thao tác mượt, hiệu ứng nổ đẹp hay phần thưởng dày. Nó xuất hiện khi người chơi liên tiếp xây được một mô hình đúng về game:

```text
Tôi thấy trạng thái → tôi dự đoán được hệ quả → tôi chọn một nước đi
→ game cho thấy nguyên nhân/kết quả rõ → tôi học được điều mới → tôi muốn thử tiếp.
```

Tên ngắn cho lời hứa ấy là **puzzle trust**: người chơi tin rằng game đưa đủ thông tin để suy luận, tôn trọng ý định của họ, và xử lý thất bại như một cơ hội học chứ không như sự mơ hồ cần trả phí để vượt qua.

“Feeling” trong ebook phải tách làm ba lớp liên quan nhưng không đồng nghĩa:

| Lớp | Câu hỏi | Ví dụ trong puzzle | Rủi ro khi gộp lẫn |
|---|---|---|---|
| Game feel vi mô | Thao tác và phản hồi có dễ chịu/dễ đọc không? | tap, drag, latency, animation, âm thanh, haptic | Gọi VFX là toàn bộ trải nghiệm |
| Puzzle cognition | Tôi hiểu state, rule, khả năng và hệ quả không? | nhận ra blocker, suy luận cascade, chọn undo | Nhầm bực bội vì mơ hồ với “độ khó” |
| Player experience vĩ mô | Tôi có autonomy, mastery, curiosity, meaning không? | tiến trình, nhịp level, social event, câu chuyện | Dùng một chỉ số retention để kết luận cảm xúc |

MDA cung cấp đường đi **mechanics → dynamics → aesthetics**; PXI chuyển một phần đường đi đó thành các biến có thể hỏi/đo: control, clarity, challenge, progress feedback, audiovisual appeal, mastery, curiosity, immersion, autonomy và meaning.[^mda][^pxi]

## 2. Nền evidence hiện có — giá trị và giới hạn

| Cụm nguồn | Đóng góp thực sự | Không nên suy quá đà | Cách dùng trong ebook |
|---|---|---|---|
| Swink, *Game Feel* | Input–response–context–polish giúp nói chính xác về cảm giác tương tác | Không tự chứng minh puzzle dễ hiểu hay công bằng | Là nền cho chương feedback/embodiment, không phải mô hình toàn sách |
| Pichlmair & Johansen, *Designing Game Feel* | Vocabulary research về physicality, amplification, support | “Clarity” chưa phải một dimension độc lập đã được survey xác lập | Căn cứ để định nghĩa và gắn nhãn claim |
| Schell, *Book of Lenses* | Câu hỏi chẩn đoán, prototype, iteration, nhìn design đa chiều | Không được bán lại một danh sách câu hỏi chung như phát hiện mới | Chỉ chọn những lens puzzle có metric và intervention rõ |
| MDA | Liên kết rule, hành vi lúc chơi và phản ứng cảm xúc | Không phải công thức dự báo cảm xúc cho từng người chơi | Dùng làm xương sống causal map |
| GDC puzzle design / Patrick's Parabox / Relic Ruins | Kinh nghiệm làm puzzle, level và playtest từ practitioner | Case nổi tiếng không thay thế nghiên cứu đối chứng | Dùng làm micro-case; nêu rõ đây là practitioner evidence |
| PXI, HEP, GUESS, NASA-TLX, MEC-SPQ | Chuyển cảm nhận mơ hồ thành quan sát, survey và workload/presence | Thang đo không thay thế việc xem người chơi suy luận | Ghép với video, think-aloud, event log và quote |
| Game Accessibility Guidelines | Accessibility là điều kiện để nhận thức state/tín hiệu, không chỉ là compliance | Checklist không tự bảo đảm puzzle hay | Mỗi lab có ít nhất một accessibility test |
| Nghiên cứu Việt Nam và Thổ Nhĩ Kỳ | Góc nhìn practitioner, casual mobile, UI, playability/usability, platform và spatial puzzle | Báo chí, job post hay product page không phải claim học thuật | Dùng ngang hàng như context/case; gắn nhãn loại nguồn |

### Các tài liệu Việt Nam và Thổ Nhĩ Kỳ đóng góp gì?

- Nguồn Lihuhu cho thấy workflow casual/puzzle ở Việt Nam đặt **pacing, gameplay flow, win/lose rate, retry, hành vi và playtest** vào cùng một chu trình. Đây là dữ liệu nghề nghiệp tốt để “dịch” framework sang ngôn ngữ đội sản xuất, không phải bằng chứng nhân quả.[^lihuhu]
- Game Talks (RMIT/Gameloft Việt Nam) nhấn mạnh prototype để thử lựa chọn và trải nghiệm người chơi. Nó củng cố vị trí của prototype như một phép thử giả thuyết hơn là một bản demo đẹp.[^gametalk]
- Bài casual mobile Thổ Nhĩ Kỳ phỏng vấn 34 người chơi; tutorial, control, visual UI và flow xuất hiện như các thành phần kinh nghiệm liên kết. Hạn chế: mẫu nhỏ và tự báo cáo, vì vậy không được biến thành định luật phổ quát.[^turkey-casual]
- Bài game RTS-puzzle dùng prototype test và Heuristic Evaluation for Playability với bảy người; có giá trị để thiết kế protocol, nhưng quy mô mẫu không đủ cho khẳng định định lượng lớn.[^turkey-hep]
- Bài *Keep Talking and Nobody Explodes* đối chiếu desktop/VR cho thấy performance không nhất thiết đi cùng satisfaction, còn presence và workload có thể đổi theo platform. Đây là phản ví dụ quan trọng chống lại lời nói đơn giản kiểu “immersive hơn = feel tốt hơn”.[^turkey-vr]
- Case *Superliminal* mở một nhánh spatial puzzle: perception, không gian và phép biến đổi luật có thể là nguồn của tò mò/aha, nhưng đây là một case diễn giải chứ không phải blueprint cho mọi game.[^turkey-superliminal]

## 3. Phản biện đa nguyên

Không có một “người chơi trung bình”, một định nghĩa duy nhất của fun, hay một mô hình doanh thu không đánh đổi điều gì. Ebook cần giữ những căng thẳng sau thay vì cố xóa chúng.

| Trục căng thẳng | Lập luận hợp lý ở mỗi phía | Kết luận thực hành |
|---|---|---|
| Clarity ↔ mystery | Quá rõ làm mất khám phá; quá mơ hồ làm hỏng suy luận | Công khai **luật và observable state**, giấu **combination/insight** |
| Challenge ↔ accessibility | Một số người thích áp lực; người khác cần thời gian/đầu mối phụ | Giữ bài toán, mở thêm kênh tín hiệu, undo, nhịp, assist và hint có tầng |
| Agency ↔ authored pacing | Tự do tuyệt đối dễ loãng; rail quá chặt làm choice giả | Cho phép nhiều đường giải hợp lệ, nhưng kiểm soát thứ tự dạy và độ phức tạp |
| RNG ↔ fairness | RNG tạo surprise/replayability; RNG không đọc được tạo learned helplessness | Chỉ dùng RNG khi người chơi hiểu distribution, có counterplay hoặc đánh đổi có ý nghĩa |
| Monetisation ↔ trust | IAP/ads tài trợ content dài hạn; chặn tiến trình để ép trả tiền phá attribution | Bán tiện lợi, cá nhân hóa, expression hoặc content phụ; không bán việc hiểu rule cơ bản |
| Mass market ↔ auteur craft | Mainstream cần onboarding/lặp lại; puzzle auteur sống nhờ bất ngờ và độ nén | Tách “core contract” phổ quát khỏi “signature insight” khác biệt |

### Phê bình các giả định thường gặp

1. **“Juice làm game hay hơn.”** Chỉ đúng khi juice tăng salience của một state change thật. Nếu animation mạnh cho một event ít quan trọng, nó làm nhiễu hierarchy; nếu phản hồi đẹp nhưng không chỉ ra nguyên nhân, nó tạo cảm giác thao tác chứ không tạo understanding.
2. **“Khó là sâu.”** Độ khó có thể đến từ combinatorial depth, từ thiếu information, từ UI friction hoặc từ yêu cầu nhớ. Chỉ loại đầu tiên mặc định có cơ hội tạo insight. Ba loại sau phải được chẩn đoán trước.
3. **“Metrics nói sự thật.”** Retry có thể là engagement, thất bại học được, hay bế tắc. Conversion có thể đi cùng satisfaction, hoặc được mua bằng short-term pressure. Mỗi metric cần một video/quote và một giả thuyết hành vi đi kèm.
4. **“Người chơi nói chính xác điều họ cần.”** Người chơi là chuyên gia về cảm nhận của họ, nhưng không tất yếu là chuyên gia về nguyên nhân thiết kế. Moderator hỏi prediction trước action, ghi hành vi, rồi mới hỏi retrospective.
5. **“Game kiếm tiền cao là design tốt.”** Doanh thu phản ánh đồng thời product, distribution, UA, brand, live ops, giá, mạng xã hội và retention. Nó là tín hiệu để nghiên cứu hệ thống, không phải phán quyết thẩm mỹ/đạo đức.

## 4. Hệ thống puzzle: từ thao tác đến kinh doanh

```text
Thiết kế rule / UI / feedback
            ↓
Người chơi hình thành dự đoán và chọn nước đi
            ↓
Kết quả, learning, cảm xúc, accessibility
            ↓
Retention / lời kể / cộng đồng / willingness-to-pay
            ↓
Data & doanh thu tài trợ content, live ops, UA
            ↓
Quyết định thiết kế vòng sau
```

Vòng lặp này có hai loại feedback loop.

- **Vòng lành mạnh:** clarity → học → mastery → quay lại → dữ liệu chất lượng → level/hint tốt hơn → clarity.
- **Vòng độc hại:** mơ hồ hoặc difficulty spike → bực bội → booster/ads bị ép → short-term revenue → team tăng friction → trust giảm → churn/negative word of mouth.

Ebook nên bảo vệ vòng đầu tiên. “Biến nghệ thuật thành tiền” bền vững nghĩa là biến năng lực tạo insight đáng tin thành sản phẩm, năng lực đội ngũ, case study và quyết định game tốt hơn; không phải dạy cách che giấu odds hay tạo bế tắc giả.

### Góc nhìn lý thuyết trò chơi

Puzzle F2P là một **trò chơi lặp lại** giữa studio và người chơi, không phải giao dịch một lần.

| Khái niệm | Trong puzzle | Hàm ý thiết kế |
|---|---|---|
| Signaling | Tutorial, UI, animation và pricing phát tín hiệu về luật/ý định studio | Tín hiệu phải khớp hành vi thật: “fair” không thể đi với rule mập mờ hoặc offer ép buộc |
| Information asymmetry | Studio biết xác suất, economy và difficulty curve; player không biết | Công khai điều cần để ra quyết định; tránh biến thiếu hiểu biết thành bẫy monetisation |
| Commitment | Người chơi đầu tư thời gian, bộ sưu tập, đội nhóm; studio hứa content và fairness | Undo, progress safety, minh bạch event và hỗ trợ accessibility làm cam kết đáng tin |
| Principal–agent | Designer/PM/UA có KPI ngắn hạn; player muốn trải nghiệm dài hạn | Dashboard phải đặt retention, complaint, accessibility barrier và satisfaction cạnh conversion |
| Repeated cooperation | Player ở lại khi kỳ vọng lần sau vẫn được tôn trọng | Monetize aspiration/expression/time-saving, không monetize sự mù mờ của rule |

**Bài test ngắn:** nếu designer phải giấu cơ chế kiếm tiền thì nó gần với extraction hơn là value exchange. Nếu có thể giải thích thẳng “bạn trả tiền để nhận gì, không trả tiền vẫn học/tiến thế nào”, nó có cơ hội duy trì trust.

## 5. Thị trường hiện tại: case để học, không phải để sao chép

Số liệu thị trường là ước tính IAP mobile, có thể loại trừ doanh thu quảng cáo, web shop, phí nền tảng và một số kênh Android. Vì vậy dùng để so sánh hướng, không dùng như số kế toán.

| Case | Tín hiệu thị trường gần đây | Điều nên mổ xẻ | Điều không nên sao chép mù quáng |
|---|---|---|---|
| **Royal Match** (Dream Games, Türkiye) | Ước tính hơn $1.4B IAP năm 2025; thuộc nhóm game mobile doanh thu lớn.[^market-naavik] | Match-3 dễ đọc + meta castle + competition/team/live event; bản chính thức liệt kê team battle, race, treasure, contest và event đa dạng.[^royal-match] | Chỉ thêm event/booster mà không có core loop và content cadence đủ mạnh |
| **Candy Crush Saga** (King) | Ước tính hơn $1.1B IAP năm 2025; hệ thống content ở quy mô hàng chục nghìn level.[^market-naavik][^candy-ai] | Difficulty operations, level supply, player segmentation và cách tool/AI hỗ trợ đội tạo/sửa content | Dùng AI để tăng số level nhưng không kiểm tra fairness/insight từng level |
| **Gardenscapes/Homescapes/Fishdom** (Playrix) | Portfolio puzzle có doanh thu lớn; Gardenscapes khoảng $442M IAP 2025 theo ước tính AppMagic được tổng hợp công khai.[^market-publishers] | Meta tiến trình, decoration/story và cách một family vận hành portfolio | Coi narrative/decor là lớp sơn có thể cứu core puzzle nhàm |
| **Gossip Harbor** (Microfun) | Merge/story nổi lên mạnh; nguồn industry estimate ghi $677M lifetime và vai trò của story, accessible loop, frequent event.[^gossip] | Energy economy, merge board, emotional narrative, meta renovation và event cadence | Gating bằng energy quá mạnh đến mức biến tò mò thành nợ chờ đợi |
| **Block Blast!** (Hungry Studio) | Dẫn free-chart nhiều năm; mô hình chủ yếu là quảng cáo, nên IAP thấp không đồng nghĩa với quy mô người dùng thấp.[^blockblast] | Low-friction loop, legibility tức thời, revive rewarded-ad như trao đổi rõ ràng | Ép interstitial dày hoặc lẫn clickbait creative với gameplay thật |
| **Patrick's Parabox / Relic Ruins / Superliminal** | Không phải benchmark doanh thu mobile, nhưng là benchmark craft cho system insight, environmental puzzle và spatial perception | Cách dạy rule, tạo twist và ghi hình playtest để xem aha có thật | Ép một game casual phải mang cognitive load của puzzle hardcore |

**Điểm then chốt:** thị trường puzzle không chỉ có match-3. Match-3, merge và blast vẫn giữ phần lớn doanh thu; sort, match-pair, block và hybrid puzzle mở cơ hội. Ebook phải đọc chúng như các **family có economy, nhịp và social wrapper khác nhau**, nhưng vẫn dùng chung puzzle-trust model.[^market-naavik]

## 6. Khung chẩn đoán có thể trở thành IP của ebook

### 6.1. Feeling Brief (trước prototype)

> Người chơi sẽ cảm thấy **[cảm xúc/năng lực]** khi tự nhận ra **[rule/pattern]**, chọn **[hành động]**, và thấy game xác nhận bằng **[state change + signal]**. Sau fail, họ biết **[điều gì phải thử khác]** mà không cần trả phí để hiểu luật.

### 6.2. Causal Feedback Map

| Bước | Ghi trong prototype | Câu hỏi kiểm tra |
|---|---|---|
| Input | Player đã làm gì, với ý định nào? | Họ có thể diễn đạt prediction trước khi chạm không? |
| State transition | Rule nào thực sự chạy? | Có hidden state/RNG nào làm attribution đứt không? |
| Signal | Visual, audio, haptic, text, camera phản hồi gì? | Signal có phân biệt action quan trọng với trang trí không? |
| Next prediction | Player tin điều gì sẽ xảy ra tiếp? | Prediction sau event có đúng hơn trước event không? |

### 6.3. Puzzle Trust Audit

Chấm mỗi câu `Có / Chưa rõ / Không`.

1. Goal và win/lose condition có đọc được ngay khi cần không?
2. Mỗi object/state quan trọng có ít nhất hai signifier khi accessibility yêu cầu không?
3. Trước action, player có thể dự đoán kết quả chính không?
4. Sau action, game có cho biết rule nào gây kết quả không?
5. Failure có chỉ ra hypothesis nào bị sai không?
6. Undo/retry có giữ nhịp học, thay vì làm lại thao tác vô nghĩa không?
7. RNG có minh bạch, có counterplay hoặc được đặt ngoài core inference không?
8. Hint có mở theo tầng: remind → point → reveal, thay vì spoil ngay không?
9. VFX/audio/haptic có khớp importance của transition không?
10. Difficulty spike có được kiểm chứng với player mới lẫn player quen không?
11. Offer/ads có xuất hiện sau một choice rõ ràng, không sau một moment mơ hồ không?
12. Player có thể tiếp tục hiểu rule dù không mua gì không?
13. Metric dashboard có giữ ít nhất một chỉ báo trust (confusion quote, perceived fairness, tutorial clarity) không?
14. Một người chơi có nhu cầu vision/motor/cognitive khác có đọc state và hoàn thành core action không?
15. Team có biết chính xác thay đổi design nào sẽ được test tiếp và criterion pass/fail là gì không?

## 7. Các hướng nội dung khả thi cho ebook

### Hướng A — Khuyến nghị: *The Art of Feeling: Designing Puzzle Games Players Trust*

**Khán giả:** designer, level designer, producer và founder casual/puzzle; đặc biệt đội nhỏ cần một cách biến feedback “chưa đã” thành thay đổi prototype.

**Lời hứa:** sau mỗi chương, reader biến một cảm nhận mơ hồ thành hypothesis, một thay đổi nhỏ, một phép đo/playtest và một quyết định tiếp theo.

**Điểm khác biệt:** không dạy “làm game vui” chung chung; dạy **bảo toàn prediction và attribution** qua mechanics, UI, feedback, difficulty, monetisation và live ops.

### Hướng B — *The Economics of Aha: Puzzle Craft Without Breaking Trust*

**Khán giả:** product/game designer, PM và founder mobile F2P.

**Lời hứa:** nối craft puzzle với retention/revenue bằng hệ thống và game theory. Royal Match, Candy Crush, Gossip Harbor, Block Blast là case đối chiếu.

**Rủi ro:** dễ thành sách monetisation nông hoặc bị hiểu là cẩm nang dark pattern. Chỉ chọn hướng này nếu có dữ liệu case/metric thực tế và giữ chương ethics mạnh.

### Hướng C — *Puzzle Labs: 12 Experiments in Clarity, Agency and Aha*

**Khán giả:** educator, indie designer, đội prototype.

**Lời hứa:** mỗi lab có board/level trước–sau, observation sheet và redesign. Có thể bán kèm worksheet, workshop và template.

**Rủi ro:** cần asset/case gốc hoặc quyền dùng asset; không đủ nếu chỉ mô tả game nổi tiếng.

**Quyết định:** lấy A làm sách chính; B là một phần cuối/chương riêng về sustainable value exchange; C là format bài tập và sản phẩm phụ. Như vậy, mục tiêu tiền không nuốt mất mục tiêu nghệ thuật.

## 8. Outline đề xuất: 8 chương, 3 lab, 1 công cụ thương mại

1. **Feeling nào?** Tách game feel, puzzle cognition và player experience; đặt tiêu chuẩn evidence.
2. **Hợp đồng suy luận.** State, affordance, goal, feedforward và causal feedback.
3. **Một nước đi có ý nghĩa.** Choice, trade-off, RNG, cascade, undo, retry và fairness cảm nhận.
4. **Dạy mà không giảng.** See → safe try → understand → purposeful use → twist; tutorial/hint có tầng.
5. **Nhịp, juice và embodied feedback.** Animation/audio/haptic như hierarchy thông tin; accessibility-by-design.
6. **Đo điều khó nói.** Playtest protocol, think-aloud, event log, PXI, coding sheet và cách xử lý contradiction.
7. **Ba phòng thí nghiệm.** Sort; match-3/merge; spatial/environmental puzzle. Mỗi lab có cùng Trust Audit.
8. **Từ craft đến value exchange.** Live ops, content supply, pricing, ads/IAP, trust debt và decision dashboard.

Phụ lục nên có Feeling Brief, Causal Feedback Map, Trust Audit, PXI routing sheet, observation codes `CL/AG/FR/AM/AC`, cùng một `Metric → Behaviour → Hypothesis → Intervention` template.

## 9. Biến ebook thành sản phẩm có tiền mà không làm nghèo nội dung

| Tầng sản phẩm | Giá trị cho người đọc | Doanh thu hợp lý | Bằng chứng cần có trước khi bán |
|---|---|---|---|
| Ebook lõi | Framework, case, worksheet | Bán trực tiếp/ebook bundle | 3–5 micro-case thật, reviewer practitioner |
| Template pack | Notion/Sheets/PDF cho brief, audit, playtest | Add-on giá thấp hoặc bonus email | Template đã dùng trên prototype thực |
| Workshop 90 phút | Team tự audit một level | B2B/team license | Facilitation guide, exercise timing, sample output |
| Prototype clinic | Review theo evidence với team | Dịch vụ cao hơn | Quy tắc scope, consent, không hứa doanh thu |
| Newsletter/case notes | Insight cập nhật từ market và playtest | Audience building/sponsorship chọn lọc | Tách rõ research, observation, opinion |

Không nên hứa “đọc sách này sẽ tăng doanh thu”. Lời hứa đáng tin hơn: **giảm số quyết định design mù mờ, tăng chất lượng evidence trước khi đầu tư production/UA, và tạo được trải nghiệm người chơi sẵn sàng quay lại/giới thiệu.**

## 10. Roadmap trước khi viết bản thảo

1. Làm một **overlap ledger**: claim → nguồn → loại evidence → phần khác biệt của ebook → citation cần dùng.
2. Chọn ba game/lab đại diện: một match-3/merge, một sort/block, một spatial/system puzzle. Không cần ba game đang hot; cần ba prototype/case có thể quan sát kỹ.
3. Chạy tối thiểu 6–10 session discovery, gồm player mới và quen. Ghi screen/video, prediction trước move, pause/hint/retry và quote sau level.
4. Chỉ dùng PXI nguyên bản khi đủ điều kiện; nếu dùng câu hỏi tự viết, gọi nó là **pulse check**, không gọi là PXI validated.
5. Viết ba micro-case trước khi viết Chương 1. Nếu case không thể cho thấy thay đổi → prediction → kết quả, framework chưa đủ sắc.
6. Với mỗi claim monetisation, ghi rõ kênh (IAP/ads), thời kỳ, phạm vi nền tảng và rằng số liệu là estimate.
7. Xin quyền dùng asset/video hoặc tự tạo board minh họa. Không dùng screenshot/game content như mặc định được phép.

## Nguồn và tài liệu trong workspace

### Nguồn nội bộ

- `00-research-brief.md`, `01-domain-dossier.md`, `03-research-backlog.md`, `04-mechanic-family-research.md`, `05-positioning-and-validation.md`, `06-competitor-content-summary.md`, `07-competitor-deep-research-guide.md`, `08-legal-access-and-full-reading-index.md`.
- `Research/MDA.pdf`; `Research/Daniel Wewerinke - GDC24 - Relic Ruins - Creating Environmental Puzzles.pdf`; `Research/external-sources/README.md` và các PDF/HTML/TXT song hành.

### Tham chiếu web

[^mda]: Hunicke, LeBlanc & Zubek, *MDA: A Formal Approach to Game Design and Game Research* — bản PDF trong workspace.
[^pxi]: [PXI Bench: theoretical model and user guide](https://playerexperienceinventory.org/instrument).
[^lihuhu]: [Lihuhu Vietnam Game Designer brief](https://www.fit.hcmus.edu.vn/vn/UserFiles/8357_LHHVN_JD_Junior-Game-Designer_Apr-2026.pdf).
[^gametalk]: [VnExpress: Game Talks với RMIT/Gameloft Việt Nam](https://vnexpress.net/chuyen-gia-chia-se-cach-thiet-ke-mot-game-tot-4752238.html).
[^turkey-casual]: [Akel (2023), casual mobile games UX](https://dergipark.org.tr/tr/pub/iuyd/issue/80567/1345872).
[^turkey-hep]: [Game development process and playability/usability analysis](https://dergipark.org.tr/tr/pub/gujsb/article/1734187).
[^turkey-vr]: [Berkman, Çatak & Eremektar, puzzle UX in VR vs desktop](https://dergipark.org.tr/tr/pub/ajit-e/article/742608).
[^turkey-superliminal]: [Gündüz & Özener (2024), *Digital Surrealism: Video Game Space*](https://dergipark.org.tr/tr/pub/jcode/article/1419955).
[^market-naavik]: [Naavik, match-3 and merge in 2025](https://naavik.co/digest/what-leading-match-3-and-merge-games-do-differently/).
[^royal-match]: [Royal Match official game elements/events](https://www.royalmatch.com/).
[^candy-ai]: [AP: how King uses AI to scale Candy Crush levels](https://apnews.com/article/547254aaa06bf026df5b41458ac62dcc).
[^market-publishers]: [AppMagic-based 2025 puzzle-publisher estimates](https://www.linkedin.com/posts/aslashcev_top-puzzle-publishers-yearly-revenue-in-2025-activity-7394343211701469186-iCMk). Treat as a secondary industry estimate.
[^gossip]: [Udonis analysis of Gossip Harbor using AppMagic estimates](https://www.blog.udonis.co/mobile-marketing/mobile-games/gossip-harbor). Treat revenue figures as estimates.
[^blockblast]: [Balancy analysis of Block Blast monetisation](https://balancy.co/blog/2025/03/26/how-could-block-blast-by-hungry-studio-earn-more-monetization-and-gameplay-deconstruction/).
