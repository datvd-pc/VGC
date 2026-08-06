# The Art of Monetization - Outline & Notes

File này là blueprint trước khi rewrite bài `bai-2-monetization-ap-dung-phan-tich-tam-ly-va-xac-suat-thong-ke.md`.

Mục tiêu: biến bài hiện tại từ một bài giải thích chỉ số monetization thành một nghiên cứu tổng hợp về **hành trình người chơi, động cơ hành vi, thiết kế game, UA/creative, ads, IAP, live ops và operating system** cho casual, hybrid-casual, puzzle và hybrid puzzle.

## 0. Định vị bài

Tên đề xuất:

```text
The Art of Monetization: Thiết kế hành trình kiếm tiền cho casual, hybrid-casual, puzzle và hybrid puzzle
```

Luận điểm chính:

```text
Monetization không bắt đầu từ cửa hàng.
Monetization bắt đầu từ việc hiểu vì sao người chơi click, cài, chơi, quay lại, xem ads, trả tiền và chia sẻ game.
```

Bài này không nên được viết như một checklist gắn SDK/IAP. Nó cần là một nghiên cứu có tính hệ thống:

- Nhìn monetization từ hành trình người chơi.
- Nối hành vi người chơi với chỉ số.
- Nối chỉ số với quyết định thiết kế.
- Nối thiết kế với cách publisher/studio vận hành.
- Đưa ví dụ theo genre cụ thể: sort, jam, physics, match-3, match-2.
- Đưa tip thực thi, bao gồm AI creative pipeline, dynamic level, 10 level đầu, booster, remove ads, rewarded ads, sharing loop.

## 1. Mở bài: bài này dành cho ai

Mục tiêu mở bài: thu hút đúng nhóm người đọc trên LinkedIn. Không mở bằng công thức LTV ngay. Mở bằng lời hứa rõ: nếu bạn đang làm game casual/puzzle và muốn hiểu cách biến game thành business, bài này là bản đồ.

Draft hướng viết:

```text
Đây là bài kinh nghiệm / kiến thức chuyên sâu dành cho những người đang xây casual, hybrid-casual, puzzle và hybrid puzzle game, đặc biệt khi mục tiêu không chỉ là làm game chơi được, mà là làm game có khả năng scale thành business.
```

Chân dung người đọc:

- Nếu bạn là PM của một publisher: đây là framework để đọc một game không chỉ qua CPI/D1/ARPDAU, mà qua toàn bộ player journey.
- Nếu bạn là CEO/founder của một studio: đây là bản đồ để hiểu vì sao build nhanh chưa đủ, và studio cần học thêm player insight, monetization, UA, creative, data.
- Nếu bạn là game designer: đây là cách nhìn level, booster, difficulty, reward, meta và economy như một hệ thống hành vi.
- Nếu bạn là UA/creative lead: đây là cách nối creative hook với game promise, first session, retention và LTV.
- Nếu bạn là monetization manager: đây là cách đặt ads/IAP theo nhu cầu thật, không phá trust.
- Nếu bạn là developer/tech lead: đây là lý do event tracking, ad flow, IAP reliability, remote config và level tooling quyết định chất lượng decision.
- Nếu bạn là artist/UI/creative producer: đây là cách visual clarity, screenshot, playable, AI variation và feedback animation ảnh hưởng trực tiếp tới CPI, retention và purchase intent.
- Nếu bạn là investor/operator: đây là cách phân biệt game có tín hiệu sản phẩm với game có khả năng thành business.

Ghi chú giọng văn:

- Vẫn giữ cách giải thích thuật ngữ Anh-Việt như bài hiện tại.
- Nhưng giảm cảm giác textbook.
- Tăng ví dụ, tình huống, quyết định thực thi.
- Mỗi section nên có: `Insight -> Ví dụ genre -> Tip thực thi -> Chỉ số cần đọc`.

## 2. Core thesis: monetization là hệ thống hành vi

Thay vì bắt đầu bằng `Profit = Installs * (LTV - CPI)`, nên đặt công thức kinh tế sau khi đã đặt player journey.

Công thức trung tâm:

```text
Monetization = Player Need * Right Context * Trust * Execution Speed
```

Mở rộng:

```text
LTV = Acquisition Quality
    * First Session Value
    * Return Motivation
    * Session Depth
    * Fair Ad Exchange
    * Natural IAP Demand
    * Live Ops Habit
    * Social/Sharing Loop
```

Ý chính:

- Người chơi không phải traffic.
- Người chơi trả bằng thời gian trước khi trả bằng tiền.
- Nếu họ vào để giải trí nhưng bị biến thành công cụ xem ads, trust vỡ.
- Nếu game tạo cảm giác công bằng, tiến bộ và có quyền lựa chọn, monetization tự nhiên hơn.

## 3. Player journey tổng quát

Section này là xương sống mới của bài.

Journey:

```text
See Ad -> Click -> Store -> Install -> First Open
-> First 10 Levels -> First Return -> Habit
-> Ads Opt-in -> First Purchase -> Repeat Purchase
-> Event/Live Ops -> Share/Recommend
```

Mỗi bước cần trả lời:

- Player đang kỳ vọng gì?
- Game cần deliver điều gì?
- Team đo chỉ số nào?
- Sai lầm thường gặp là gì?
- Tip thực thi là gì?

### 3.1 See Ad: người chơi thấy gì trong 1-3 giây đầu

Insight:

- Creative không bán feature. Creative bán fantasy.
- Puzzle/casual thường thắng bằng visual problem rõ: hỗn loạn, kẹt, thiếu một bước, fail dễ thấy, satisfying resolution.

Ví dụ theo genre:

- Sort: chai/ống màu lộn xộn, chỉ cần một nước để giải.
- Jam: xe kẹt, bãi đỗ thiếu slot, hướng thoát rõ nhưng căng.
- Physics: vật rơi, nước chảy, pin kéo sai gây fail vui.
- Match-3: cascade lớn, blocker gần bị phá, rescue objective.
- Match-2: tap cụm lớn, chain clear nhanh, board từ rối thành sạch.

Tip thực thi:

- Dùng AI để tạo nhiều biến thể màn chơi/hook không đụng bản quyền.
- Tạo `creative scenario library`: near miss, fail, chaos-to-order, rescue, impossible-looking board, one-move-away.
- Dùng AI để biến hình cùng một core board thành nhiều skin/theme: kitchen, garden, traffic, toys, candy, wood, glass, water.
- Không copy IP, mascot, UI, level layout đặc trưng của đối thủ.
- Fake creative được dùng để test interest, nhưng phải `fake-but-faithful`: game thật cần deliver cùng cảm xúc, không lừa user quá xa.

Chỉ số:

- CTR, IPM, CPI, store conversion, D1 theo creative source.

### 3.2 Store: người chơi kiểm tra lời hứa

Insight:

- Store page là nơi người chơi hỏi: "Game này có thật như ads không?"
- Icon, screenshot, preview video phải khớp promise.

Tip:

- Screenshot 1 phải nói rõ mechanic.
- Screenshot 2-3 cho progression/meta/reward.
- Preview video không nên chỉ là gameplay thô; cần có micro-story.
- A/B test icon theo genre fantasy: chaos/order, rescue, decorate, challenge.

### 3.3 First open: người chơi cho game vài chục giây

Insight:

- First open không phải nơi giới thiệu mọi feature.
- Mục tiêu là đưa player vào hành động nhanh.

Tip:

- Load nhanh.
- Không login/rating/purchase popup sớm.
- Tutorial bằng thao tác, không bằng text dài.
- First interaction trong 5-10 giây nếu có thể.

Chỉ số:

- Load time, crash rate, tutorial start/complete, level 1 start/complete, first session length.

## 4. First 10 Levels: dạy mà không làm chán

Luận điểm:

```text
10 level đầu không phải tutorial.
10 level đầu là hợp đồng cảm xúc giữa game và người chơi.
```

Mục tiêu:

- Dạy luật chơi.
- Tạo cảm giác "mình hiểu rồi".
- Tạo early mastery.
- Cho thấy game sẽ có chiều sâu.
- Không ép ads/IAP quá sớm.
- Cài mầm cho booster/meta sau này.

Khung 10 level:

- Level 1: một hành động đúng, thắng nhanh, không text dài.
- Level 2: lặp lại luật với biến thể nhẹ.
- Level 3: cho player tự giải, tạo cảm giác thông minh.
- Level 4: thêm một constraint nhỏ.
- Level 5: milestone đầu, reward rõ.
- Level 6: mở objective hoặc blocker nhẹ.
- Level 7: cho thấy nếu đi sai có thể kẹt, nhưng vẫn cứu được.
- Level 8: giới thiệu strategic choice.
- Level 9: near-miss tự nhiên, không dàn dựng quá lộ.
- Level 10: mở meta/event/collection hoặc reward lớn hơn.

Ví dụ theo genre:

- Sort:
  - L1 dạy đổ cùng màu.
  - L2 dạy dùng ống trống.
  - L3 dạy không đổ bừa.
  - L7 tạo board có thể kẹt nếu không nhìn trước.
  - L10 unlock undo/hint hoặc collection bottle skin.
- Jam:
  - L1 dạy kéo xe theo hướng.
  - L2 dạy slot đỗ.
  - L4 thêm xe chắn.
  - L7 tạo bottleneck một slot.
  - L10 unlock garage/meta.
- Physics:
  - L1 dạy cause-effect.
  - L2 dạy gravity.
  - L4 thêm timing.
  - L7 fail vui nhưng replay nhanh.
  - L10 unlock tool/skin.
- Match-3:
  - L1 dạy swap.
  - L2 dạy match 4.
  - L3 dạy objective.
  - L6 thêm blocker.
  - L10 mở room/progression.
- Match-2:
  - L1 dạy tap group.
  - L2 dạy bigger group = better reward.
  - L4 thêm target.
  - L7 thêm limited moves.
  - L10 mở booster hoặc event.

Tip:

- 10 level đầu nên được instrument riêng.
- Đọc drop-off từng level, không chỉ D1.
- Nếu player bỏ ở L2-L3: clarity có vấn đề.
- Nếu bỏ ở L6-L8: difficulty/pace có vấn đề.
- Nếu qua L10 nhưng không quay lại: thiếu return reason.

## 5. Dynamic Level Design

Luận điểm:

```text
Dynamic level không phải gian lận người chơi.
Dynamic level là cách điều chỉnh độ khó, nhịp cảm xúc và cơ hội monetization theo hành vi thật.
```

Các loại dynamic level:

- Dynamic difficulty: điều chỉnh độ khó theo skill/attempt/session depth.
- Dynamic board generation: tạo board theo rule thay vì hard-code toàn bộ.
- Dynamic objective: thay đổi mục tiêu hoặc target count.
- Dynamic reward: reward theo trạng thái user.
- Dynamic offer context: offer khác nhau theo level fail, near-miss, session, payer status.

Nguyên tắc:

- Không làm player thấy game lật luật.
- Không giảm fairness.
- Không spawn xấu để ép mua.
- Dùng để giữ flow, không dùng để bóp người chơi.

Ví dụ:

- Sort: tăng/giảm số màu, số ống trống, độ sâu stack, quyền undo.
- Jam: điều chỉnh mật độ xe, slot trống, hướng thoát, obstacle.
- Physics: điều chỉnh object count, friction, timing window, reset speed.
- Match-3: điều chỉnh move count, blocker density, board shape, drop rate.
- Match-2: điều chỉnh group density, target count, bomb frequency.

Chỉ số:

- FAR (First Attempt Rate).
- APS (Attempts Per Success).
- Fail rate.
- Retry rate.
- Booster use rate.
- Rage quit after fail.
- D1/D3 by difficulty segment.

Tip:

- Hard level nên có "readable failure": player hiểu vì sao thua.
- Near-miss phải có thật: thiếu 1-2 moves/objectives, không phải thiếu quá xa.
- Nếu fail liên tục nhưng retry thấp: level gây bực.
- Nếu fail cao và retry cao: level có thể đang tạo challenge tốt.

## 6. Booster: khi nào thêm, khi nào bán

Luận điểm:

```text
Booster tốt tạo thêm lựa chọn.
Booster xấu giải thay game hoặc sửa lỗi thiết kế level.
```

Khi nên thêm booster:

- Player đã hiểu core rule.
- Game đã có trạng thái kẹt hợp lý.
- Booster giải quyết một pain cụ thể.
- Booster có thể được dùng như reward trước khi được bán.

Không nên thêm booster:

- Quá sớm khi player chưa hiểu game.
- Vì level design thiếu công bằng.
- Vì muốn ép monetization.
- Khi booster phá toàn bộ skill expression.

Booster theo genre:

- Sort: undo, extra tube, hint, shuffle.
- Jam: extra slot, clear car, reverse move, path hint.
- Physics: slow time, remove object, freeze, extra attempt.
- Match-3: hammer, rocket, bomb, color wipe, extra moves.
- Match-2: bomb, color clear, shuffle, row/column clear.

Flow tốt:

```text
Teach booster as reward -> let player use once -> create natural need -> offer bundle later
```

Ví dụ:

- Cho free hammer ở match-3 sau khi đã thấy blocker.
- Cho undo miễn phí ở sort sau lần đầu player tự làm kẹt.
- Cho extra slot ở jam sau khi player hiểu pressure của slot.

## 7. Ads: utility, không phải punishment

Luận điểm:

```text
Người chơi sẵn sàng xem ads khi ads là trao đổi công bằng.
Người chơi phản cảm khi ads biến họ thành công cụ tạo tiền.
```

Rewarded ads tốt:

- Sau near-miss để thêm move/continue.
- Sau win để nhân đôi reward.
- Trước hard level để nhận booster chuẩn bị.
- Khi đang chờ building/countdown.
- Khi thiếu tài nguyên để tiếp tục event.
- Khi mở rương/free bonus.

Rewarded ads xấu:

- Ads thay cho game loop.
- Reward quá bắt buộc.
- Không xem ads thì game trở nên khó chịu.
- Placement xuất hiện trước khi player hiểu giá trị.

Interstitial tốt:

- Chỉ ở natural break.
- Không trong vài phút đầu.
- Có frequency cap.
- Segment new user, loyal user, payer, ad-heavy user khác nhau.

Remove ads:

- Nên bán sau khi player đã thích game.
- Nên định vị là "chơi sạch hơn", không phải "thoát khỏi tra tấn".
- Có thể bundle với starter pack.
- Không nên remove rewarded ads vì rewarded ads là lựa chọn tự nguyện.

Ví dụ theo genre:

- Sort: rewarded ads để undo/extra tube khi board gần cứu được.
- Jam: rewarded ads để thêm slot khi traffic đang kẹt.
- Physics: rewarded ads để retry nhanh hoặc nhận tool sau fail vui.
- Match-3: rewarded ads để thêm 5 moves khi còn 1-2 objective.
- Match-2: rewarded ads để nhận bomb khi còn ít target.

Chỉ số:

- Rewarded ad viewer rate.
- RV IMPDAU.
- Interstitial IMPDAU.
- Session length after ad.
- D1/D3 by ad exposure.
- Rating/review after ad frequency change.

## 8. IAP: pay to solve needs

Luận điểm:

```text
Người chơi không mua item.
Người chơi mua cách giải quyết một nhu cầu trong đúng ngữ cảnh.
```

Nhóm động cơ:

- Protect effort: trả tiền để không mất công sức đã xây.
- Restore flow: trả tiền để giữ nhịp giải trí.
- Support game: trả tiền để tưởng thưởng team/game.
- Express identity: trả tiền để thể hiện cái tôi.
- Advance goal: trả tiền để đạt thêm một nấc tiến bộ.
- Economic value: trả tiền vì deal đúng nhu cầu.
- Social belonging: trả tiền để thuộc về, đóng góp hoặc khoe thành tựu.

IAP theo genre:

- Sort:
  - Extra tube/undo pack sau level có kẹt hợp lý.
  - Remove ads cho relax players.
  - Cosmetic bottle/tube skin nếu có collection/meta.
- Jam:
  - Extra slot/clear car pack.
  - Event pack cho timed challenge.
  - Garage/vehicle skin nếu có meta.
- Physics:
  - Remove ads nếu retry loop ngắn.
  - Tool pack nếu fail/retry vui.
  - Cosmetic/theme nếu physics toy có visual appeal.
- Match-3:
  - Extra moves, hammer, rocket, booster bundle.
  - Starter pack sau khi user hiểu blocker.
  - Battle pass/event pack khi progression đủ sâu.
- Match-2:
  - Booster bundle cho objective pressure.
  - Event pack cho clear target.
  - Piggy bank nếu currency loop rõ.

Tip:

- Tag offer theo động cơ.
- Đọc payer retention, không chỉ conversion.
- Nếu payer mua một lần rồi rời game: offer có thể đang phá trust.
- Nếu non-payer retention cao nhưng IAP thấp: nhu cầu mua chưa rõ hoặc offer sai timing.

## 9. Return journey: vì sao người chơi quay lại

Luận điểm:

```text
Retention không chỉ đến từ game vui.
Retention đến từ lý do quay lại đủ rõ.
```

Return reasons:

- Level tiếp theo.
- Meta/progression.
- Daily reward.
- Event.
- Streak.
- Collection.
- Team/clan.
- Building/timer complete.
- Battle pass progress.

Theo persona:

- Relax player: quay lại vì game dễ chịu, ít áp lực.
- Challenge player: quay lại vì hard level, mastery, fair challenge.
- Progression player: quay lại vì xây/mở khóa.
- Collector/decorator: quay lại vì hoàn thành bộ/trang trí.
- Value seeker: quay lại vì free reward/deal/daily.

Tip:

- Không spam notification chung chung.
- Notification nên gắn với mục tiêu thật: building complete, event ending, reward ready.
- D3 cần reason, D7 cần habit, D30 cần live ops.

## 10. Sharing loop: vì sao người chơi giới thiệu game

Luận điểm:

```text
Người chơi chia sẻ khi game tạo được khoảnh khắc đáng khoe, đáng cứu, đáng tranh luận hoặc đáng rủ.
```

Sharing moments:

- Before/after transformation.
- Hard level cleared.
- Impossible-looking board solved.
- Funny physics fail.
- Huge combo/cascade.
- Room/decor showcase.
- Collection completed.
- Team event contribution.

Theo genre:

- Sort: board cực rối được giải sạch.
- Jam: bãi xe nhìn bất khả thi nhưng thoát được.
- Physics: fail/win hài, vật lý bất ngờ.
- Match-3: combo/cascade lớn, rescue thành công.
- Match-2: board clear chain đẹp.

Tip:

- Tạo share card sau milestone, không popup bừa.
- Dùng replay/GIF ngắn nếu engine hỗ trợ.
- Cho người chơi khoe thành quả, không ép invite.
- Referral nên có reward nhẹ, không phá economy.

## 11. UA/Creative + AI pipeline

Luận điểm:

```text
Creative pipeline là một phần của product pipeline.
```

AI có thể dùng cho:

- Tạo nhiều biến thể hook.
- Tạo visual theme khác nhau cho cùng mechanic.
- Tái tạo level state thành hình ảnh/video concept.
- Sinh caption, CTA, angle.
- Tạo storyboard 5-15 giây.
- Tạo playable prototype idea.
- Tạo fake-but-faithful ad scenario.

Không nên dùng AI để:

- Clone IP/character/UI của game khác.
- Tạo promise game không deliver.
- Dùng asset không rõ quyền.
- Làm creative gây CPI thấp nhưng D1 thấp vì sai kỳ vọng.

Creative angles theo genre:

- Sort: chaos-to-order, one wrong move, satisfying fill.
- Jam: trapped car, one slot left, escape puzzle.
- Physics: curiosity, fail comedy, cause-effect.
- Match-3: cascade, rescue, blocker destruction.
- Match-2: fast clear, chain reaction, big tap.

Chỉ số cần nối:

- Creative angle -> CPI.
- Creative angle -> store conversion.
- Creative angle -> D1/D3.
- Creative angle -> payer conversion.
- Creative angle -> ad viewer rate.

## 12. Operating system cho publisher/studio

Giữ lại nhiều nội dung hiện tại nhưng đặt sau player journey.

Các phần cần có:

- Một bộ chuẩn đầu vào.
- Dashboard chung.
- Decision cadence.
- Role theo team.
- Learning repository.
- Kill/iterate/scale criteria.

Điểm cần nhấn:

- Publisher không chỉ có vốn UA.
- Studio không chỉ build task.
- Game designer không chỉ làm level.
- Dev không chỉ gắn SDK.
- Creative không chỉ làm ads.

Tất cả cần cùng đọc player journey.

## 13. Suggested research extensions

Bài này là pillar content. Các bài sau có thể tách:

1. `The First 10 Levels`: thiết kế 10 level đầu cho puzzle/hybrid puzzle.
2. `Dynamic Level Design`: rule, fairness, near-miss, difficulty curve.
3. `Rewarded Ads Without Breaking Trust`: thiết kế ads như utility.
4. `IAP Motivation Taxonomy`: vì sao người chơi mua.
5. `AI Creative Pipeline for Puzzle Games`: test creative không clone IP.
6. `Genre Monetization Playbooks`: sort, jam, physics, match-3, match-2.
7. `Publisher Operating System`: dashboard, cadence, studio management.
8. `From D1 to D30`: retention, live ops, event, habit.
9. `Remove Ads, Starter Pack, Piggy Bank, Battle Pass`: khi nào dùng từng sản phẩm.
10. `Player Personas in Casual Puzzle`: persona, journey, monetization response.

## 14. Rewrite notes cho bài hiện tại

Nên rewrite mạnh, không chỉ chèn thêm.

Giữ lại:

- LTV/CPI logic.
- Publisher/studio role.
- Dashboard/chỉ số.
- IAP motivation section vừa bổ sung.
- Xác suất và fairness.
- Workflow từ idea tới scale.

Cần thêm:

- Mở bài đúng LinkedIn audience.
- Player journey làm xương sống.
- Persona-based journey.
- First 10 levels.
- Dynamic level.
- Genre examples xuyên suốt.
- Practical tips.
- AI creative pipeline.
- Sharing loop.

Cần giảm:

- Đoạn giải thích thuật ngữ quá dài nếu làm chậm nhịp.
- Lặp lại vai trò publisher/studio.
- Công thức quá sớm ở mở bài.

## 15. Proposed final structure

```text
# The Art of Monetization

## 0. Bài này dành cho ai
## 1. Monetization không bắt đầu từ cửa hàng
## 2. Player journey: từ click tới share
## 3. Không có một user journey duy nhất: persona khác nhau, monetization khác nhau
## 4. UA/Creative: bán fantasy, không bán feature
## 5. Store và first open: lời hứa phải được kiểm chứng ngay
## 6. First 10 levels: dạy cách chơi mà không làm chán
## 7. Dynamic level design: độ khó, near-miss và trust
## 8. Retention: lý do quay lại theo từng nhóm người chơi
## 9. Ads as utility: khi nào người chơi sẵn sàng xem ads
## 10. Booster: thêm lựa chọn, không sửa lỗi thiết kế
## 11. IAP: pay to solve needs
## 12. Remove ads, starter pack, piggy bank, battle pass: dùng khi nào
## 13. Sharing loop: khi nào người chơi rủ người khác
## 14. Áp dụng theo genre: sort, jam, physics, match-3, match-2
## 15. Publisher/studio operating system
## 16. Metrics, dashboard và decision cadence
## 17. Từ nghiên cứu tổng hợp tới các bài chuyên sâu tiếp theo
## 18. Kết luận
## Nguồn nghiên cứu
```

## 16. Notes về cách viết từng section

Mỗi section nên có format:

```text
Insight:
Vì sao phần này quan trọng.

Player psychology:
Người chơi đang nghĩ/cảm thấy gì.

Genre examples:
Sort / Jam / Physics / Match-3 / Match-2.

Execution tips:
Team làm gì được ngay.

Metrics:
Đọc chỉ số nào để biết đúng/sai.

Common mistakes:
Sai lầm thường gặp.
```

Không phải section nào cũng cần đủ 6 phần nếu quá dài, nhưng nên giữ logic này trong đầu để bài không trôi thành lý thuyết suông.

## 17. Câu lõi nên xuất hiện trong bài

```text
Người chơi trả bằng thời gian trước khi trả bằng tiền.
```

```text
Nếu người chơi vào để giải trí nhưng flow bị biến thành lịch xem ads, game không còn monetization. Nó trở thành sự phản bội kỳ vọng.
```

```text
Booster tốt tạo thêm lựa chọn. Booster xấu sửa lỗi thiết kế level.
```

```text
Rewarded ads tốt là trao đổi tự nguyện. Interstitial tốt là thuế nhẹ ở điểm nghỉ tự nhiên.
```

```text
10 level đầu không phải tutorial. 10 level đầu là hợp đồng cảm xúc.
```

```text
Không có một công thức monetization dùng nguyên xi cho mọi puzzle. Sort bán cảm giác gỡ rối. Jam bán áp lực không gian. Physics bán tò mò và thử lại. Match-3 bán tiến độ dài hạn. Match-2 bán nhịp clear nhanh và reward đều.
```

```text
Creative pipeline là một phần của product pipeline.
```

```text
Revenue tốt không phải là ép được một lần mua. Revenue tốt là tạo được lý do mua mà sau đó user vẫn muốn tiếp tục chơi.
```

