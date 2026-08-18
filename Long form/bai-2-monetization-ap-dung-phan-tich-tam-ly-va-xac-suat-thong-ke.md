# Monetization không bắt đầu từ cửa hàng

Trong game mobile (game trên điện thoại), đặc biệt là puzzle (game giải đố), hybrid puzzle (game giải đố có thêm meta, progression, live ops hoặc IAP sâu hơn), casual (game dễ tiếp cận cho số đông) và hybrid-casual (game có core đơn giản như casual nhưng có hệ thống giữ chân và kiếm tiền sâu hơn), monetization (kiếm tiền từ game) không bắt đầu từ việc đặt vài gói nạp tiền vào store (cửa hàng trong game).

Monetization bắt đầu từ câu hỏi lớn hơn:

Một user (người chơi/người dùng) được mua về bằng tiền UA (User Acquisition, tức hoạt động chạy quảng cáo để kéo người dùng mới cài game) sẽ tạo ra bao nhiêu giá trị trong toàn bộ vòng đời chơi game?

Nếu câu trả lời thấp hơn CPI (Cost Per Install, chi phí trung bình để có một lượt cài đặt), game không scale được (không thể tăng ngân sách quảng cáo mà vẫn có lời). Nếu câu trả lời cao hơn CPI nhưng chỉ đúng trong một vài cohort nhỏ (nhóm người dùng được gom theo cùng ngày cài, cùng nguồn quảng cáo, cùng quốc gia hoặc cùng phiên bản game), game có thể có tín hiệu nhưng chưa thành business (một mô hình kinh doanh có thể lặp lại). Nếu câu trả lời cao hơn CPI một cách ổn định ở thị trường lớn như Mỹ, với creative (nội dung quảng cáo như video, playable, banner, icon, screenshot) có thể lặp lại, retention (tỷ lệ người chơi quay lại sau khi cài game) đủ sâu, ad inventory (số cơ hội hiển thị quảng cáo trong game) đủ dày, IAP (In-App Purchase, mua hàng trong ứng dụng) đủ tự nhiên và workflow (quy trình làm việc) vận hành đủ nhanh, lúc đó game mới bắt đầu có cơ hội đi tới doanh thu hàng triệu đô.

Vì vậy bài toán thật không phải là:

"Làm sao để kiếm tiền từ người chơi?"

Bài toán đúng hơn là:

"Làm sao để thiết kế toàn bộ hệ thống từ idea (ý tưởng), creative (quảng cáo), gameplay (cách chơi), level (màn chơi), economy (kinh tế trong game như coin, booster, reward, giá gói), UA (mua user bằng quảng cáo), ads (quảng cáo trong game), IAP (mua hàng trong game), analytics (đo lường dữ liệu) và live ops (vận hành sự kiện/nội dung sau khi game đã ra mắt) để mỗi user có khả năng tạo ra LTV cao hơn chi phí đưa họ vào game?"

Công thức kinh tế đơn giản:


Profit = Installs * (LTV - CPI)


Trong đó:

- Profit (lợi nhuận gộp từ user acquisition): phần tiền còn lại sau khi lấy giá trị người dùng trừ chi phí mua người dùng.
- Installs (lượt cài): số người cài game từ quảng cáo hoặc nguồn phân phối.
- LTV (Lifetime Value, giá trị vòng đời người dùng): tổng doanh thu kỳ vọng một user tạo ra trong suốt thời gian họ còn chơi game.
- CPI (Cost Per Install): chi phí trung bình để có một lượt cài.

Nhưng để công thức này đúng trong thực tế, cần mở nó ra:

```text
LTV = Retention * Session Depth * Ad Viewer Rate * IMPDAU * eCPM
    + Payer Conversion * ARPPU
    + Live Ops Uplift
```

Đọc công thức này theo ngôn ngữ đơn giản:

- Retention (giữ chân): người chơi có quay lại không.
- Session Depth (độ sâu phiên chơi): người chơi chơi bao lâu, bao nhiêu màn, bao nhiêu lần mỗi ngày.
- Ad Viewer Rate (tỷ lệ người xem quảng cáo): trong số người chơi hoạt động mỗi ngày, bao nhiêu phần trăm có xem ít nhất một quảng cáo.
- IMPDAU (Impressions Per Daily Active User, số lượt hiển thị quảng cáo trên mỗi người dùng hoạt động hằng ngày): một DAU trung bình xem bao nhiêu quảng cáo.
- eCPM (effective Cost Per Mille, doanh thu ước tính trên 1.000 lượt hiển thị quảng cáo): quảng cáo hiển thị càng có giá trị thì eCPM càng cao.
- Payer Conversion (tỷ lệ chuyển đổi trả tiền): bao nhiêu phần trăm user trở thành người mua IAP.
- ARPPU (Average Revenue Per Paying User, doanh thu trung bình trên mỗi người trả tiền): một payer trung bình trả bao nhiêu.
- Live Ops Uplift (phần tăng thêm nhờ vận hành live ops): doanh thu/retention tăng thêm nhờ event, nhiệm vụ, season, update.

Với puzzle và hybrid puzzle, game không thắng chỉ vì một mechanic (cơ chế chơi cốt lõi như sort màu, match tile, tháo ốc, kéo block) vui. Game thắng vì nhiều lớp cùng kéo nhau lên: quảng cáo đủ hấp dẫn để có CPI thấp, first session (phiên chơi đầu tiên) đủ rõ để có D1 retention (tỷ lệ quay lại vào ngày sau khi cài) tốt, level design (thiết kế màn chơi) đủ có áp lực để tạo replay (chơi lại) và rewarded video (quảng cáo có thưởng), economy đủ có nhu cầu để bán booster (vật phẩm hỗ trợ như búa, shuffle, extra move), interstitial (quảng cáo toàn màn hình chen giữa các điểm nghỉ tự nhiên như sau khi qua màn) đủ khéo để không phá retention, live ops đủ đều để kéo D7/D30 (tỷ lệ quay lại ngày 7/ngày 30), và publisher/studio đủ kỷ luật để đọc dữ liệu thay vì tranh luận bằng cảm tính.

## 1. Vì sao thị trường này không còn là cuộc chơi của một bên

Một studio (đội/công ty trực tiếp làm game) có thể làm gameplay rất tốt nhưng thiếu vốn UA, benchmark CPI (mốc so sánh CPI tốt/xấu theo genre, quốc gia, platform), creative testing (thử nhiều mẫu quảng cáo để xem mẫu nào kéo user rẻ và chất lượng), mediation setup (cài hệ thống trung gian để nhiều ad network cùng cạnh tranh hiển thị quảng cáo trong game) và kinh nghiệm đọc cohort. Một publisher (đơn vị phát hành, thường mạnh về vốn, dữ liệu, UA, monetization và scale) có thể có vốn, data và UA machine (hệ thống mua user, test creative, tối ưu bid và đọc ROAS) nhưng nếu studio không build được core loop (vòng lặp chơi chính khiến user chơi đi chơi lại), không instrument event đúng (gắn tracking để đo hành vi đúng thời điểm), không sửa level nhanh, không hiểu player pain (điểm đau/khó chịu của người chơi), publisher cũng không thể biến một game yếu thành hit lâu dài.

Nói ngắn gọn:

Studio tạo ra sản phẩm có thể chơi được (gameplay, build, level, art, UI, SDK, bug fix).

Publisher tạo ra điều kiện để sản phẩm được thị trường kiểm chứng và scale (test quảng cáo, mua traffic, đọc chỉ số, tối ưu monetization, quyết định tăng ngân sách).

Ad network (mạng quảng cáo như AppLovin, Unity Ads, Google, Meta, ironSource...) phân phối attention (sự chú ý của người dùng trong các app/game khác).

Player (người chơi) trả bằng thời gian, tiền, sự chú ý và dữ liệu hành vi (họ click gì, chơi bao lâu, thua ở đâu, xem ads khi nào, mua gì).

Platform như App Store và Google Play kiểm soát distribution (phân phối app), policy (luật nền tảng), payment (thanh toán) và privacy (quyền riêng tư/tracking).

Vì vậy monetization là một hệ thống phối hợp, không phải một feature.

Trong hybrid-casual, Unity mô tả mô hình này là sự kết hợp giữa core gameplay dễ market (dễ quảng cáo, dễ hiểu qua video ngắn) và các lớp engagement (mức độ gắn bó) sâu hơn như meta (lớp mục tiêu ngoài màn chơi chính, ví dụ xây phòng, sưu tầm, trang trí), progression (tiến trình dài hạn), và economy (hệ thống tiền tệ, vật phẩm, reward, giá trị) để giữ người chơi lâu hơn. Hybrid-casual thường monetization bằng IAP và rewarded video (quảng cáo có thưởng mà người chơi tự chọn xem để nhận lợi ích), còn interstitial được dùng có chọn lọc theo nhóm user hoặc thời điểm trong game. Điều này rất quan trọng: hybrid puzzle không phải hyper-casual (game siêu đơn giản, thường kiếm tiền chủ yếu bằng ads, vòng đời ngắn) gắn thêm store. Nó là một game cần thiết kế cả attention, progression và economy.

## 2. Mục tiêu thật: tối đa hóa tiền kiếm được trên mỗi user

Nếu chỉ nhìn doanh thu tổng, team dễ hiểu sai. Doanh thu cao có thể đến từ việc mua quá nhiều user không lời. Nếu chỉ nhìn CPI, team cũng dễ hiểu sai. CPI thấp có thể đến từ creative hấp dẫn nhưng user vào game không ở lại.

Chỉ số cần nghĩ theo chuỗi (đây là funnel, tức đường đi từ lúc người dùng nhìn thấy quảng cáo đến lúc game tạo doanh thu):

```text
Impression -> CTR -> CPC/CPM -> CPI -> Install -> D1 -> D3 -> D7
-> Session -> Ad View -> IMPDAU -> ARPDAU -> IAP -> LTV -> ROAS
```

Mỗi mắt xích hỏng sẽ kéo cả hệ thống xuống.

Nếu impression (lượt quảng cáo được hiển thị) cao nhưng CTR (Click-Through Rate, tỷ lệ người thấy quảng cáo rồi bấm vào) thấp, creative không đủ hút hoặc message (thông điệp quảng cáo) không đúng tệp.

Nếu CTR cao nhưng install rate (tỷ lệ người đã click rồi thật sự cài game) thấp, store page (trang App Store/Google Play), icon (biểu tượng app), screenshot (ảnh chụp giới thiệu), game promise (lời hứa trải nghiệm mà quảng cáo/store đưa ra) hoặc perceived quality (cảm nhận chất lượng ban đầu) có vấn đề.

Nếu CPI thấp nhưng D1 thấp, creative có thể đang bán sai trải nghiệm, hoặc first session không deliver (không thực sự đem lại) đúng thứ quảng cáo hứa.

Nếu D1 tốt nhưng D7 thấp, game có novelty (cảm giác mới lạ ban đầu) nhưng chưa có habit (thói quen quay lại), progression, collection (sưu tầm), challenge curve (đường cong độ khó) hoặc mục tiêu quay lại.

Nếu D7 tốt nhưng ARPDAU (Average Revenue Per Daily Active User, doanh thu trung bình trên mỗi user hoạt động hằng ngày) thấp, game giữ người chơi nhưng chưa có đủ ad opportunity (cơ hội hiển thị quảng cáo), rewarded video placement (vị trí đặt ads có thưởng), interstitial pacing (nhịp hiển thị quảng cáo chen giữa), hoặc IAP demand (nhu cầu mua hàng trong game).

Nếu RV ad viewer rate (Rewarded Video Ad Viewer Rate, tỷ lệ DAU có xem ít nhất một quảng cáo có thưởng) cao nhưng retention giảm, reward có thể quá cần thiết, placement quá áp lực, hoặc game đang biến ads thành phí bắt buộc để tiếp tục.

Nếu INTER IMPDAU (Interstitial Impressions Per DAU, số quảng cáo interstitial trung bình trên mỗi user hoạt động hằng ngày) cao nhưng session length (thời lượng mỗi phiên chơi) giảm, team đang lấy doanh thu ngắn hạn đổi lấy player fatigue (sự mệt mỏi/chán ghét vì bị quảng cáo quá nhiều).

Do đó chỉ số không phải là bảng điểm sau cùng. Chỉ số là triệu chứng của một hệ thống.

## 3. Các kiểu hợp tác và ai thường làm phần nào

Không phải publisher nào cũng giống nhau, và không phải studio nào cũng ở cùng maturity level. Cách chia việc phụ thuộc vào deal.

### Production vendor

Studio nhận brief (đề bài/yêu cầu sản phẩm), build theo scope (phạm vi công việc đã chốt), nhận phí hoặc milestone (khoản thanh toán theo từng mốc hoàn thành). Publisher giữ IP (Intellectual Property, quyền sở hữu trí tuệ/tài sản game), data (dữ liệu người dùng), UA, monetization và quyết định scale.

Publisher thường làm:

- Market research (nghiên cứu thị trường, đối thủ, genre, creative đang thắng).
- Creative direction (định hướng quảng cáo: hook nào, fantasy nào, visual nào).
- UA test (chạy quảng cáo thử để đọc CPI, CTR, IPM, retention).
- MMP/analytics requirement (yêu cầu về Mobile Measurement Partner như AppsFlyer/Adjust/Singular và hệ thống analytics để đo nguồn user, event, doanh thu).
- Monetization benchmark (mốc so sánh doanh thu, ad viewer rate, IMPDAU, ARPDAU theo game tương tự).
- Kill/iterate/scale decision (quyết định dừng, sửa tiếp, hoặc tăng ngân sách test/scale).

Studio thường làm:

- Prototype (bản thử nghiệm nhanh để kiểm tra core idea).
- Core gameplay (cách chơi chính).
- Art/UI implementation (triển khai hình ảnh và giao diện).
- Level production (sản xuất màn chơi).
- SDK/event integration theo yêu cầu (tích hợp bộ công cụ của bên thứ ba như ads SDK, analytics SDK, MMP SDK và gắn event đo lường).
- Bug fixing và iteration (sửa lỗi và cải tiến qua nhiều vòng).

Nhân sự chính:

- Publisher PM (Product/Publishing Manager): định nghĩa mục tiêu test, timeline, success/failure criteria (tiêu chí thành công/thất bại).
- Publisher UA/creative team: chạy ads, đọc CPI, CTR, IPM (Installs Per Mille, số lượt cài trên 1.000 impression), ROAS (Return On Ad Spend, doanh thu thu về so với tiền quảng cáo đã chi).
- Publisher monetization manager: đọc ARPDAU, IMPDAU, ad viewer rate, eCPM.
- Studio PM (Project/Product Manager phía studio): quản lý scope và communication (giao tiếp, cập nhật, chốt việc).
- Game designer/GD (người thiết kế game): core loop, level, economy, pacing (nhịp trải nghiệm nhanh/chậm/khó/dễ).
- Developer/Dev (lập trình viên): build, analytics events, SDK, ads implementation (triển khai quảng cáo trong game).
- Artist/UI: visual clarity (độ rõ hình ảnh), store assets (icon, screenshot, preview video), creative assets nếu được giao.

Rủi ro của model này là studio học ít nếu không có quyền đọc data sâu.

### Publishing partnership

Studio có game hoặc prototype, publisher đầu tư UA, mentoring (hướng dẫn/coaching), analytics, monetization và launch (phát hành). Revenue share (chia doanh thu sau khi trừ hoặc trước khi trừ một số chi phí, tùy hợp đồng) tùy deal.

Publisher thường làm:

- Tư vấn positioning (định vị game: bán cho ai, bằng thông điệp nào, khác gì đối thủ).
- Creative testing ở nhiều channel (kênh quảng cáo như Meta, Google, TikTok, AppLovin, Unity Ads).
- Soft launch (phát hành thử ở một vài thị trường nhỏ hoặc có kiểm soát trước khi launch global).
- Mediation và ad waterfall/bidding setup (thiết lập hệ thống quảng cáo: waterfall là xếp tầng mạng quảng cáo theo giá dự kiến; bidding là đấu giá realtime giữa nhiều network).
- LTV prediction (dự báo giá trị vòng đời user dựa trên cohort sớm).
- Scale decision (quyết định có tăng ngân sách và mở thị trường không).
- Live ops planning nếu game qua test (lên lịch event, update, level mới, offer mới).

Studio thường làm:

- Product iteration dựa trên data (sửa sản phẩm theo dữ liệu, không chỉ theo cảm giác).
- Level balancing (cân bằng độ khó/dễ của màn chơi).
- Economy tuning (chỉnh lượng tiền thưởng, giá booster, tần suất reward, giá gói).
- IAP pack implementation (triển khai gói mua trong game như starter pack, remove ads, booster pack).
- Event/live ops content (nội dung sự kiện, nhiệm vụ, level/event đặc biệt).
- Technical stability (độ ổn định kỹ thuật: ít crash, load nhanh, ads/IAP không lỗi).

Nhân sự chính:

- Founder/producer studio: giữ direction, negotiate scope, đảm bảo team học được.
- Studio GD/PM: chuyển data thành backlog.
- Dev: đảm bảo event đúng, ads không lỗi, build ổn định.
- Publisher growth team: nhìn portfolio, quyết định vốn UA.

Rủi ro là hai bên nói cùng từ "potential" nhưng hiểu khác nhau. Studio nghĩ game có potential vì chơi vui. Publisher nghĩ game có potential khi creative, CPI, retention và monetization cùng mở ra khả năng scale.

### Co-development / strategic partner

Hai bên cùng tham gia sâu từ idea tới live ops. Publisher không chỉ test game có sẵn, studio không chỉ nhận task. Cả hai cùng xây hệ thống học (mỗi vòng test đều để lại hiểu biết có thể dùng cho vòng sau hoặc game sau).

Publisher cần làm:

- Chia sẻ benchmark và learning theo cohort (ví dụ cohort Mỹ iOS từ creative A có D1 tốt hơn cohort Android từ creative B).
- Đưa creative insight (tín hiệu từ quảng cáo như hook nào nhiều người click) sớm vào product design.
- Thiết kế test plan rõ (test cái gì, đo gì, quyết định thế nào).
- Giải thích vì sao kill hoặc iterate (dừng vì chỉ số nào, sửa vì giả thuyết nào).
- Giữ cadence review đều (nhịp họp/đọc số hằng tuần hoặc theo mốc).

Studio cần làm:

- Chủ động đề xuất hypothesis (giả thuyết cần kiểm chứng, ví dụ "nếu level 3 cho near win rõ hơn thì RV opt-in sẽ tăng").
- Build event taxonomy từ đầu (bộ quy ước tên event và dữ liệu cần gửi, ví dụ level_start, level_fail, ad_show, purchase_success).
- Chuẩn bị tool để sửa level/economy nhanh (không cần dev rebuild quá nhiều lần).
- Tách learning có thể dùng lại cho game sau.
- Không biến mọi feedback thành feature creep (phình tính năng ngoài kiểm soát).

Đây là model tốt nhất để tạo capability dài hạn, nhưng đòi hỏi trust và operating maturity cao.

### Self-publishing

Studio tự làm UA, creative, data, monetization và live ops. Giá trị capture (phần giá trị giữ lại cho mình: IP, data, doanh thu, learning) cao hơn, nhưng rủi ro vốn và năng lực cao hơn.

Studio cần có tối thiểu:

- UA buyer hoặc growth lead (người trực tiếp mua traffic/tối ưu chiến dịch tăng trưởng).
- Creative pipeline (quy trình sản xuất nhiều biến thể quảng cáo liên tục).
- Analytics/MMP setup (hệ thống đo event, attribution và doanh thu).
- Monetization/ad ops knowledge (kiến thức vận hành ads, mediation, eCPM, fill rate, placement).
- Product manager đọc cohort.
- GD hiểu retention và economy.
- Dev đủ mạnh để instrument, release, fix SDK, tối ưu performance (hiệu năng game).

Nếu thiếu một trong các lớp này, self-publishing dễ biến thành "tự chạy quảng cáo bằng niềm tin".

## 4. Publisher có nhiều studio cùng lúc thì phải làm thế nào?

Publisher không thể vận hành từng studio như một ngoại lệ. Khi có nhiều đối tác cùng lúc, đặc biệt trong giai đoạn chạy test, publisher cần một operating system (hệ thống vận hành gồm chuẩn đầu vào, dashboard, nhịp review, tiêu chí quyết định và cách lưu learning).

Không phải hệ thống phức tạp. Nhưng phải có chuẩn.

### Một bộ chuẩn đầu vào

Trước khi test, mỗi game cần có:

- One-line promise (lời hứa một câu của game): người chơi thấy gì trong 3 giây đầu?
- Core loop (vòng lặp chơi chính): người chơi làm gì lặp lại?
- Target audience (tệp người chơi mục tiêu): ai là người có khả năng click và ở lại?
- Creative hypotheses (giả thuyết quảng cáo): quảng cáo sẽ bán fantasy nào?
- Event taxonomy (bộ event cần đo): những hành vi nào phải đo?
- First session map (bản đồ phiên chơi đầu): người chơi trải qua gì trong 5 phút đầu?
- Monetization hypothesis (giả thuyết kiếm tiền): ads/IAP sẽ xuất hiện từ nhu cầu nào?

Nếu thiếu những thứ này, test chỉ cho ra số nhưng không cho ra learning.

### Một dashboard chung

Mỗi game trong portfolio cần được đọc theo cùng một format:

- CPI, CTR, IPM, install rate (nhóm chỉ số marketability: quảng cáo có kéo user vào game hiệu quả không).
- D1, D3, D7 retention (nhóm chỉ số giữ chân: user có quay lại sau 1/3/7 ngày không).
- Session count, average session length, playtime (nhóm chỉ số engagement: user chơi bao nhiêu lần, mỗi lần bao lâu, tổng thời gian bao nhiêu).
- RV ad viewer rate, RV IMPDAU, RV ARPDAU (nhóm rewarded video: bao nhiêu user xem ads có thưởng, mỗi user xem bao nhiêu, tạo bao nhiêu doanh thu).
- INTER IMPDAU, INTER ARPDAU, frequency (nhóm interstitial: quảng cáo chen giữa xuất hiện dày thế nào và tạo bao nhiêu doanh thu).
- IAP conversion, ARPPU, starter pack conversion (nhóm mua hàng: bao nhiêu user mua, payer trả trung bình bao nhiêu, gói đầu tiên bán tốt không).
- Crash rate, load time, ad availability (nhóm kỹ thuật: game có lỗi, tải chậm, thiếu ads để show không).
- Level fail rate, retry rate, booster usage (nhóm level design: user thua ở đâu, có chơi lại không, có dùng booster không).

Không có dashboard chung, publisher sẽ bị kéo vào rất nhiều cuộc tranh luận riêng lẻ. Có dashboard chung, mỗi team biết mình đang thua ở đâu.

### Một decision cadence

Decision cadence (nhịp ra quyết định) là lịch cố định để cả publisher và studio biết tuần nào đọc chỉ số nào, khi nào sửa, khi nào dừng. Ví dụ một chu kỳ 6 tuần:

Tuần 0: chốt scope, hypothesis, event list, success/failure criteria (tiêu chí thế nào là thắng/thua).

Tuần 1: build core, instrument tracking (gắn đo lường event), chuẩn bị creative.

Tuần 2: test marketability (khả năng game được quảng cáo và kéo cài đặt), đọc CTR/CPI/IPM.

Tuần 3-4: đọc D1/D3, first session, level fail, ad engagement (hành vi xem/click ads trong game).

Tuần 5: đọc D7 và early monetization (tín hiệu kiếm tiền sớm từ ads/IAP).

Tuần 6: quyết định kill (dừng), iterate (sửa tiếp trên hướng hiện tại), pivot (đổi hướng lớn), hoặc scale test (tăng ngân sách/traffic để kiểm tra ở quy mô lớn hơn).

Điểm quan trọng: mỗi game chết cũng phải để lại learning. Publisher có nhiều studio không thắng bằng việc mọi prototype đều thành công. Publisher thắng bằng việc mỗi prototype làm portfolio thông minh hơn.

## 5. Studio và dev cần làm gì để không chỉ là người nhận task

Studio Việt thường mạnh ở tốc độ build. Nhưng puzzle/hybrid puzzle muốn đi global và kiếm tiền lớn cần thêm một lớp năng lực: đọc hệ thống.

Studio cần hỏi publisher:

- Success criteria (tiêu chí thành công) của test này là gì?
- Game đang được test ở thị trường nào?
- Creative nào thắng, creative nào thua?
- CPI thấp vì hook (móc câu quảng cáo trong vài giây đầu) nào?
- D1 thấp ở bước nào trong first session?
- D7 thấp vì thiếu content (nội dung), thiếu habit hay difficulty curve sai?
- Ads placement (vị trí đặt quảng cáo trong flow game) nào tạo revenue nhưng làm session xấu đi?
- Studio có được dùng learning này cho game tiếp theo không?

Game designer cần làm hơn việc thiết kế level. GD cần biết level đang phục vụ chỉ số nào:

- Onboarding level (màn hướng dẫn đầu) phục vụ D1.
- Early challenge (thử thách sớm) phục vụ clarity (độ rõ) và flow (trạng thái chơi trôi chảy, không quá dễ/khó).
- Mid-level pressure (áp lực ở giữa progression) phục vụ retry (chơi lại), RV và booster demand.
- Event level (màn trong sự kiện) phục vụ return reason (lý do quay lại).
- Hard level (màn khó) phục vụ near miss (cảm giác suýt thắng/suýt thua), nhưng không được phá trust (niềm tin rằng game công bằng).

Developer cũng không chỉ "gắn SDK". Dev có vai trò rất lớn vì data sai sẽ làm quyết định sai. Dev cần đảm bảo:

- Event gửi đúng thời điểm (ví dụ level_complete phải gửi khi thật sự qua màn, không gửi sớm hoặc gửi lặp).
- Level ID (mã màn), attempt number (lần thử thứ mấy), fail reason (lý do thua), booster usage (dùng booster nào, khi nào) được track sạch.
- Ads event phân biệt request (game gọi quảng cáo), loaded (quảng cáo tải xong), show (đã hiển thị), complete (user xem xong), reward granted (đã trao thưởng).
- IAP event phân biệt offer shown (hiện gói), click (bấm vào gói), purchase success (mua thành công), purchase fail (mua lỗi/thất bại).
- Build không crash (thoát đột ngột) ở thiết bị phổ biến.
- Ads không làm load time và session flow tệ.

PM cần nối các bên:

- Chuyển chỉ số thành backlog.
- Chốt owner cho từng metric.
- Không để feedback UA biến thành feature loạn.
- Không để studio sửa game theo cảm giác của người nói to nhất.

## 6. Giải phẫu từng chỉ số quan trọng

### Potential

Potential (tiềm năng thương mại của game) không phải là "game này nhìn hay".

Potential là xác suất game có thể scale lời sau khi được tối ưu. Với publisher, potential thường có nghĩa rất thực dụng: nếu bỏ thêm tiền, thêm creative, thêm level, thêm event và thêm thời gian tối ưu, game này có khả năng tạo ROAS dương không.

Công thức thực dụng:

```text
Potential = Marketability * Retention * Monetization * Scalability * Operating Fit
```

Marketability (khả năng quảng cáo được): creative có dễ bán không? Người xem hiểu trong vài giây không? Hook có đủ mạnh không?

Retention (khả năng giữ chân): user có quay lại không? D1/D3/D7 nói gì?

Monetization (khả năng kiếm tiền): user có xem ads, mua booster, mua remove ads (gói bỏ quảng cáo), mua pack không?

Scalability (khả năng mở rộng): creative có nhiều angle (góc quảng cáo) để lặp lại không? CPI có giữ được khi tăng spend (ngân sách quảng cáo) không?

Operating fit (độ phù hợp vận hành): team có sửa nhanh và đúng không?

Publisher thường đọc potential theo portfolio. Studio thường đọc potential theo cảm giác sản phẩm. Hai góc nhìn này cần gặp nhau bằng số liệu.

### CPI

CPI (Cost Per Install, chi phí cho một lượt cài) cao thường đến từ:

- Creative hook yếu (3 giây đầu không đủ khiến người xem dừng lại).
- Visual không rõ trên màn hình nhỏ (người xem không hiểu đang xảy ra gì).
- Game promise không khác biệt (nhìn giống quá nhiều game khác).
- Audience quá cạnh tranh (tệp người chơi đó đang bị nhiều game/app khác cùng mua).
- Store page làm mất người sau click (click rồi nhưng trang store không đủ thuyết phục để cài).
- Quảng cáo bán fantasy quá niche (ảo tưởng/trải nghiệm quảng cáo quá hẹp, chỉ hợp nhóm rất nhỏ).

Muốn CPI thấp, không chỉ UA team làm. GD và artist cũng tham gia.

Creative cần:

- Hook rõ trong 1-3 giây đầu.
- Gameplay readable (người xem hiểu cách chơi dù chưa từng chơi game).
- Một tension đơn giản: sai/sắp thua/sắp thắng/cần cứu.
- CTA rõ (Call To Action, lời kêu gọi hành động như "Play now", "Try it", hoặc nút tải).
- Không quá nhiều text nhỏ.
- Nhiều biến thể màu, camera, speed (tốc độ), difficulty (độ khó), fail scenario (kịch bản thất bại).

Ingame cần khớp với quảng cáo. Nếu quảng cáo bán cảm giác "tôi giải được puzzle thông minh" nhưng game thật mở đầu bằng tutorial dài, CPI có thể ổn nhưng D1 sẽ trả giá.

### Install và Install Rate

Install rate (tỷ lệ chuyển từ click sang cài đặt) nằm giữa click và install. Nó chịu ảnh hưởng bởi:

- Icon (biểu tượng game trên store).
- App name (tên game).
- Screenshot (ảnh giới thiệu trên store).
- Preview video (video xem trước trên store).
- Rating/review (điểm sao và bình luận).
- Store page localization (bản địa hóa trang store theo ngôn ngữ/văn hóa thị trường).
- Dung lượng app.
- Độ tin cậy của visual (nhìn có giống game thật, chất lượng thật, không lừa người dùng không).

Nếu CTR cao nhưng install rate thấp, vấn đề có thể không nằm ở creative đầu phễu mà nằm ở store conversion. Publisher UA team có thể phát hiện, nhưng studio art/UI và PM phải sửa asset.

Với thị trường Mỹ, store page cần cực kỳ rõ. Người dùng có nhiều lựa chọn và ít kiên nhẫn. Screenshot phải cho thấy ngay game thuộc loại gì, cảm giác thắng là gì, và vì sao nó đáng thử.

### D1 Retention

D1 retention (Day 1 Retention, tỷ lệ người cài hôm nay quay lại vào ngày kế tiếp) trả lời:

"Người chơi có thấy đủ giá trị để quay lại sau ngày đầu không?"

Nó thường đến từ:

- First open nhanh (mở game lần đầu không phải chờ lâu).
- Tutorial ngắn, tương tác được, không giảng quá nhiều.
- Core loop rõ trong 30-60 giây.
- Level đầu cho cảm giác thông minh và kiểm soát.
- Reward đầu đủ dễ hiểu.
- Không hiện quá nhiều popup (cửa sổ hiện lên như login, offer, daily bonus, rating).
- Không ép ads/IAP quá sớm.
- Game deliver đúng promise từ quảng cáo.

Nếu D1 thấp, đừng sửa store trước. Hãy xem first session recording (video/recording hành vi phiên đầu nếu có), funnel tutorial (từng bước trong tutorial rớt bao nhiêu user), level 1-5, crash rate (tỷ lệ lỗi thoát game), load time (thời gian tải), ad timing (thời điểm hiện quảng cáo), và rage quit (thoát game vì bực/frustration).

GameAnalytics nhấn mạnh retention không chỉ đo từ install; có thể đo return (quay lại) sau những event cụ thể như tutorial_complete (hoàn thành hướng dẫn), purchase (mua hàng), level_complete (qua màn), hoặc feature_usage (dùng tính năng). Đây là cách đọc tốt hơn cho product team: không chỉ "D1 thấp" mà là "user hoàn thành tutorial có quay lại không?" hoặc "user dùng booster lần đầu có quay lại không?"

### D3 Retention

D3 retention (Day 3 Retention, tỷ lệ người chơi quay lại sau 3 ngày) trả lời:

"Novelty có đang chuyển thành thói quen ban đầu không?"

D1 có thể được cứu bằng onboarding tốt. D3 cần game có reason để tiếp tục:

- Level curve bắt đầu mở ra (đường cong level bắt đầu có thay đổi, không lặp y hệt).
- Player thấy mục tiêu kế tiếp.
- Unlock feature vừa đủ (mở tính năng mới đúng lúc, không quá sớm/quá muộn).
- Reward cadence tạo cảm giác tiến bộ (nhịp trao thưởng đều và có ý nghĩa).
- Daily bonus không rẻ tiền (quà đăng nhập hằng ngày không nên tạo cảm giác vô giá trị).
- Challenge tăng nhưng chưa gây frustration.

Nếu D1 tốt nhưng D3 rơi mạnh, game có thể vui lần đầu nhưng thiếu chiều sâu. Hybrid puzzle cần thêm collection, progression, environment change, room/building/meta, quest hoặc event nhẹ.

### D7 Retention

D7 retention (Day 7 Retention, tỷ lệ người chơi quay lại sau 7 ngày) trả lời:

"Game có bắt đầu trở thành một thói quen không?"

Với puzzle/hybrid puzzle, D7 thường đến từ:

- Difficulty curve có nhịp (có màn dễ, màn vừa, màn khó, màn giải tỏa; không khó đều hoặc dễ đều).
- Người chơi có mục tiêu dài hơn level tiếp theo.
- Booster có vai trò nhưng không bắt buộc.
- Event hoặc challenge khiến user quay lại.
- Progression/meta đủ mở nhưng không quá nặng.
- Game không làm người chơi thấy bị lừa bởi ads hoặc level.

Unity gợi ý rằng hyper-casual có D7 retention khoảng 5-10% có thể là ứng viên để chuyển sang hybrid-casual. Ý này quan trọng vì nó cho thấy D7 không chỉ là chỉ số giữ chân, mà còn là tín hiệu game có đủ engagement để thêm economy/IAP sâu hơn hay không.

### RV Ad Viewer Rate

Rewarded video ad viewer rate (tỷ lệ người dùng hoạt động hằng ngày có xem ít nhất một quảng cáo có thưởng) là tỷ lệ DAU (Daily Active Users, số người dùng hoạt động trong ngày) xem ít nhất một rewarded video.

Chỉ số này cao khi người chơi có lý do tự nguyện xem ads.

Placement tốt:

- Xem ads để hồi sinh sau near win (sắp thắng nhưng thiếu một chút).
- Xem ads để nhân đôi reward sau khi thắng.
- Xem ads để nhận booster trước level khó.
- Xem ads để mở rương.
- Xem ads để tiếp tục event.
- Xem ads để giảm chờ đợi.

Placement xấu:

- Xem ads để sửa một frustration do game cố tình tạo.
- Reward quá mạnh khiến không xem ads thì chơi thấy tệ.
- Ads hiện khi player chưa hiểu giá trị.
- Reward không liên quan đến mục tiêu hiện tại.

Muốn RV ad viewer rate cao, GD phải thiết kế nhu cầu; dev phải đảm bảo ad load nhanh và reward granted chính xác; publisher monetization/ad ops phải tối ưu fill, eCPM và placement performance.

### RV IMPDAU

RV IMPDAU (Rewarded Video Impressions Per DAU) là số rewarded video impressions (lượt hiển thị quảng cáo có thưởng) trên mỗi DAU. Ví dụ RV IMPDAU = 1.5 nghĩa là trung bình mỗi user hoạt động trong ngày xem 1.5 quảng cáo có thưởng.

Chỉ số này tăng khi:

- Có nhiều placement tự nhiên (vị trí ads xuất hiện đúng lúc người chơi cần).
- User chơi nhiều session (nhiều phiên trong ngày).
- Reward có giá trị theo ngữ cảnh.
- Difficulty tạo enough pressure (đủ áp lực để user muốn nhận hỗ trợ).
- Event tạo thêm cơ hội xem ads.
- Ads availability tốt (khi game gọi ads thì có quảng cáo để hiển thị, không bị no fill).

Nhưng RV IMPDAU không nên tăng bằng cách nhồi placement. Nếu mỗi level đều cần ads để dễ chịu, retention sẽ suy giảm. AppLovin cũng khuyến nghị khi tối ưu IMPDAU ở interstitial và rewarded video cần theo dõi ARPDAU và cân bằng số ads hiển thị, đặc biệt với frequency cap cho interstitial.

### INTER IMPDAU

Interstitial (quảng cáo toàn màn hình không có thưởng, thường xuất hiện tự động) là fullscreen ad xuất hiện ở điểm chuyển cảnh tự nhiên, ví dụ sau level hoặc giữa màn hình. AppLovin mô tả interstitial là placement ở natural breaks (điểm nghỉ tự nhiên), còn rewarded là ads người chơi yêu cầu để đổi lấy reward.

INTER IMPDAU cao khi:

- Session có nhiều level ngắn.
- Level end flow rõ (luồng sau khi kết thúc màn: thắng/thua, reward, next level, ads).
- Frequency cap hợp lý (giới hạn số lần show ads trong một khoảng thời gian).
- Ads không hiện giữa lúc player đang tập trung.
- Có segment logic (phân nhóm user): payer (người đã trả tiền), high-retention user (người có khả năng ở lại cao), new user (user mới), ad-fatigued user (user đã xem quá nhiều ads) không bị đối xử giống nhau.

Với hybrid puzzle, interstitial không nên là nguồn monetization duy nhất. Nếu lạm dụng, nó làm giảm session length, D1/D3 và rating. Interstitial nên giống "thuế nhẹ ở điểm nghỉ", không phải vật cản giữa người chơi và niềm vui.

### Impression, CTR, CPC, CPM, CPI

Đây là lớp UA creative.

Impression (lượt hiển thị quảng cáo) cao nghĩa là quảng cáo được phân phối, chưa nói nó tốt.

CTR (Click-Through Rate) cao nghĩa là người xem muốn click, nhưng chưa nói user chất lượng.

CPC (Cost Per Click, chi phí cho một lượt bấm) thấp có thể tốt, nhưng nếu install rate thấp thì click rẻ vẫn lãng phí.

CPM (Cost Per Mille, chi phí cho 1.000 lượt hiển thị quảng cáo) phản ánh cạnh tranh inventory và giá trị audience (tệp người xem quảng cáo).

CPI là kết quả của CTR, CPC/CPM, install rate và thuật toán phân phối.

Creative tốt cho puzzle thường có:

- Một trạng thái lỗi rõ: người chơi thấy ngay vấn đề.
- Một hành động thỏa mãn: kéo, xếp, xoay, match, tháo, cứu.
- Một near miss (suýt thắng/suýt thua): còn một bước là thắng.
- Một fail vui nhưng không quá giả.
- Màu sắc đọc được trên mobile.
- Âm thanh/caption (phụ đề) hỗ trợ khi sound off (người xem tắt tiếng).

AppLovin chỉ ra rằng nhiều mobile gamers tắt âm, vì vậy caption rõ rất quan trọng; họ cũng nhấn mạnh hook sớm trong vài giây đầu và narrative (câu chuyện/quỹ đạo cảm xúc trong video) trong video dài hơn. Với game puzzle, điều này có nghĩa là không nên chỉ quay gameplay thô. Creative cần dựng một câu chuyện ngắn: vấn đề -> nỗ lực -> sai lầm -> gần thắng -> CTA.

### Average Session và Average Session Length

Average session count (số phiên chơi trung bình mỗi user mỗi ngày) cho biết người chơi quay lại bao nhiêu lần trong ngày. Average session length (thời lượng trung bình mỗi phiên chơi) cho biết mỗi lần chơi kéo dài bao lâu.

Puzzle có thể thắng bằng nhiều session ngắn hoặc ít session dài hơn. Không có một công thức cố định. Nhưng hai chỉ số này phải khớp với monetization.

Nếu game có level ngắn, interstitial và rewarded placement có thể xuất hiện nhiều hơn nhưng phải rất cẩn thận về fatigue.

Nếu game có session dài, rewarded video, event progress, streak, collection và IAP offer theo ngữ cảnh có nhiều đất hơn.

Session length tăng nhưng retention giảm có thể là tín hiệu người chơi bị kéo quá lâu một cách mệt mỏi. Session ngắn nhưng session count cao có thể là thói quen tốt. Đừng đọc một chỉ số một mình.

## 7. Từ chỉ số quay lại hành động thiết kế

### Khi muốn CPI thấp

UA/creative cần:

- Test nhiều hook (mở đầu quảng cáo khác nhau để xem người dùng phản ứng với kiểu nào).
- Làm playable/video sớm (playable ads là quảng cáo cho người xem thử chơi một phiên bản nhỏ ngay trong quảng cáo).
- Tách creative theo angle: satisfying (thỏa mãn khi sắp xếp/gỡ rối), fail (thất bại gây tò mò), IQ challenge (thử thách trí tuệ), rescue (cứu nhân vật/vật thể), decorate (trang trí), collection (sưu tầm).
- Localize cho Mỹ bằng visual dễ hiểu, caption rõ, pacing nhanh (nhịp video nhanh, ít giải thích dài).

GD cần:

- Chọn mechanic có thể hiểu bằng mắt.
- Thiết kế moment có thể quay thành ads (một khoảnh khắc nhìn 3-5 giây đã hiểu vì sao hấp dẫn).
- Tạo các level/situation có tension rõ (nguy cơ thua, thiếu một bước, mắc lỗi dễ thấy).

Artist cần:

- Đảm bảo contrast (độ tương phản màu sắc đủ rõ).
- Màu block/object phân biệt tốt.
- UI không nhiễu (không quá nhiều nút, icon, chữ làm người xem rối).
- Animation có satisfying feedback (phản hồi hình ảnh tạo cảm giác đã tay, ví dụ nổ nhẹ, rung, bay reward).

Dev cần:

- Export build/creative capture nhanh (xuất bản build hoặc quay gameplay phục vụ quảng cáo nhanh).
- Có tool tạo scenario cho video (tạo sẵn level/situation để quay ads).
- Nếu có playable ads, hỗ trợ bản playable nhẹ và đúng cảm giác.

### Khi muốn D1 cao

Product cần:

- First session không dài dòng.
- Level 1-5 cho người chơi thắng nhanh và hiểu sâu dần.
- Không overload tính năng (không dồn quá nhiều hệ thống vào đầu game).
- Không hỏi rating, login, purchase quá sớm.

GD cần:

- Dạy bằng tương tác, không dạy bằng text.
- Tạo early mastery (cảm giác "mình hiểu rồi, mình làm được").
- Cho player thấy mục tiêu tiếp theo.

Dev cần:

- Load nhanh.
- Không crash.
- Event tracking đủ sạch để biết user rớt ở đâu.

Publisher cần:

- So sánh cohort theo creative. Creative nào đem user D1 tốt hơn có thể đáng scale dù CPI cao hơn.

### Khi muốn D3/D7 cao

Game cần:

- Progression đủ rõ.
- Difficulty curve có nhịp thở (khó/dễ xen kẽ, có lúc căng, có lúc giải tỏa).
- Meta nhẹ nhưng có ý nghĩa.
- Daily objective (nhiệm vụ hằng ngày), collection, event hoặc unlock.
- Reward không bị lặp nhàm.

GD cần:

- Xác định level nào dạy, level nào thử, level nào tạo pressure (áp lực).
- Dùng FAR (First Attempt Rate, tỷ lệ qua màn ngay lần đầu), APS (Attempts Per Success, số lần thử trung bình để qua màn), SR (Success Rate, tỷ lệ qua màn tổng), fail point (điểm người chơi thường thua), retry rate (tỷ lệ chơi lại) để sửa level.
- Tránh level khó vì confusing (khó vì không rõ luật/mục tiêu, không phải khó vì thử thách hợp lý).

PM cần:

- Đọc cohort theo version (phiên bản game), creative source (nguồn creative/campaign kéo user), và country (quốc gia).
- Không kết luận quá sớm khi sample nhỏ (quá ít user khiến số liệu dễ nhiễu).

### Khi muốn RV Ad Viewer Rate và RV IMPDAU cao

Thiết kế cần:

- Reward đặt đúng lúc có nhu cầu.
- Near win/near miss đủ thật (người chơi thật sự cảm thấy thiếu một chút, không phải bị game dàn dựng quá lộ).
- Booster hữu dụng nhưng không phá game.
- Rewarded placement nhiều loại nhưng không spam.

Dev cần:

- Reward granted không lỗi.
- Ads load sớm để không chờ.
- Track ad request, loaded, show, complete, reward.

Publisher monetization cần:

- Theo dõi fill (fill rate, tỷ lệ có quảng cáo để hiển thị khi game gọi ads), eCPM, ARPDAU, ad viewer rate.
- Segment theo country, payer status (đã trả tiền/chưa trả tiền), session depth.

### Khi muốn INTER IMPDAU cao mà không phá retention

Thiết kế cần:

- Chỉ show ở natural break (điểm nghỉ tự nhiên như sau khi thắng/thua màn).
- Có frequency cap.
- Tránh show trong first few minutes (vài phút đầu) nếu D1 nhạy.
- Segment new user và loyal user (người dùng trung thành/quay lại nhiều) khác nhau.

PM/GD cần:

- Đọc session length sau khi tăng frequency (tần suất show ads).
- Đọc D1/D3 theo ad exposure (mức độ tiếp xúc quảng cáo: user xem 0 ads, 1 ads, 3 ads, 5 ads...).
- Nếu ARPDAU tăng nhưng D3 giảm, cần tính lại LTV chứ không ăn mừng sớm.

## 8. IAP trong puzzle: bán giải pháp, không bán sự bất lực

Puzzle IAP thường xoay quanh:

- Booster (vật phẩm hỗ trợ qua màn).
- Extra moves/time (mua thêm lượt đi hoặc thời gian).
- Remove ads (gói bỏ quảng cáo interstitial/banner, thường vẫn giữ rewarded video tự chọn).
- Starter pack (gói đầu game giá thấp để chuyển user thành payer lần đầu).
- Piggy bank (heo đất tích lũy tiền/gem rồi bán lại cho user với giá hấp dẫn).
- Battle pass/season pass (vé mùa, user làm nhiệm vụ để nhận reward theo tầng).
- Limited event pack (gói giới hạn theo sự kiện).
- Cosmetic/meta decoration (đồ trang trí, skin, vật phẩm cho meta).

Người chơi mua khi họ cảm thấy:

- Mình hiểu vì sao mình cần món này.
- Món này giúp mình vượt qua mục tiêu hiện tại.
- Game vẫn công bằng nếu không mua.
- Giá trị cảm nhận cao hơn giá tiền.
- Khoảnh khắc mua xuất hiện đúng ngữ cảnh.

Các nguyên tắc tâm lý cũ vẫn đúng:

- Neo giá (đặt một gói đắt bên cạnh để gói trung bình trông hợp lý hơn).
- Khan hiếm (giới hạn thời gian/số lượng để tăng cảm giác đáng mua).
- FOMO (Fear Of Missing Out, sợ bỏ lỡ cơ hội).
- Tiến độ gần hoàn thành (thiếu một chút là đạt mục tiêu nên dễ mua hơn).
- Sở hữu trước (cho xem/dùng thử để user tưởng tượng mình đã có vật phẩm).
- Cam kết nhỏ (gói rẻ đầu tiên giúp phá rào cản trả tiền).
- Sưu tầm (mong muốn hoàn thành bộ sưu tập).

Nhưng trong puzzle/hybrid puzzle, IAP mạnh nhất thường không đến từ popup ngẫu nhiên. Nó đến từ level design và economy.

Một offer (đề nghị mua hàng) sau khi thua sát nút có lý do rõ hơn popup lúc mới mở game. Một starter pack sau khi player hiểu booster có giá trị sẽ tự nhiên hơn starter pack xuất hiện trước khi player biết booster là gì. Một piggy bank có giá trị hơn nếu người chơi thấy mình đã tích lũy nó bằng công sức.

Ranh giới nằm ở trust. Nếu game tạo cảm giác "tôi thua vì mình thiếu một chút", monetization tự nhiên. Nếu game tạo cảm giác "tôi thua vì game cố tình khóa", monetization trở thành khai thác.

## 9. Xác suất thống kê và cảm giác công bằng

Với gacha (hệ thống quay/mở thưởng ngẫu nhiên), loot box (hộp phần thưởng), chest (rương), random booster (booster nhận ngẫu nhiên), hoặc reward pool (danh sách phần thưởng có thể rơi ra), xác suất không chỉ là toán. Xác suất là cảm xúc.

Công thức expected value (EV, giá trị kỳ vọng trung bình nếu lặp lại rất nhiều lần):

```text
EV = P1 * V1 + P2 * V2 + P3 * V3 + ...
```

Nhưng player không cảm nhận EV như bảng tính. Họ cảm nhận:

- Kết quả thấp nhất có quá tệ không?
- Phần thưởng trùng có vô dụng không?
- Có tiến độ sau mỗi lần mở không?
- Có pity hoặc guarantee không? (pity là cơ chế bảo hiểm sau nhiều lần không trúng; guarantee là đảm bảo nhận một loại phần thưởng sau điều kiện nhất định)
- Có minh bạch không? (user có biết xác suất/luật thưởng không)

Một reward pool có EV tốt nhưng kết quả thường xuyên gây thất vọng vẫn làm giảm trust. Một hệ thống có EV vừa phải nhưng luôn cho player cảm giác tiến bộ có thể giữ retention tốt hơn.

Trong puzzle, xác suất còn xuất hiện trong spawn (vật phẩm mới xuất hiện), shuffle (xáo lại), booster drop (rơi booster), chest reward, daily bonus và event reward. Nếu random làm player thấy game không công bằng, họ không chỉ không mua. Họ rời đi.

## 10. Workflow từ idea tới game kiếm tiền lớn

Một workflow thực dụng:

### Bước 1: Market và player hypothesis

Hỏi:

- Tệp Mỹ nào sẽ click game này? (Mỹ là thị trường có eCPM/IAP cao nhưng cạnh tranh UA cũng cao.)
- Họ thích cảm giác gì: relax (thư giãn), challenge (thử thách), clean-up (dọn dẹp hỗn loạn), decorate (trang trí), IQ (thử trí thông minh), rescue (cứu), order (sắp xếp trật tự), chaos-to-control (biến hỗn loạn thành kiểm soát)?
- Game có thể được giải thích bằng video 5 giây không?
- Đối thủ đang bán angle nào?

Output:

- 3-5 creative angles (3-5 góc quảng cáo khác nhau để test).
- 1 core promise (lời hứa trải nghiệm chính).
- 1 target audience chính.
- 1 risk list (danh sách rủi ro: CPI cao, D1 thấp, mechanic khó hiểu, ads khó quay...).

### Bước 2: Prototype và creative test sớm

Đừng đợi game xong mới làm ads. Với puzzle, nhiều khi creative signal (tín hiệu từ quảng cáo: CTR, CPI, IPM, comment, watch time nếu có) nên đến trước khi build quá sâu.

Test:

- Video gameplay (quay gameplay thật).
- Fake gameplay (mô phỏng một tình huống chưa có trong game thật để test market interest, cần cẩn thận để không lừa user quá xa trải nghiệm thật).
- Playable đơn giản.
- Icon/screenshot.
- Hook variants (nhiều phiên bản mở đầu quảng cáo).

Output:

- CTR/IPM/CPI signal.
- Creative angle thắng.
- Câu hỏi product cần trả lời (ví dụ user thích rescue angle, vậy game thật có cần meta cứu nhân vật không?).

### Bước 3: Build first session và event tracking

Trước khi soft launch, phải biết sẽ đo gì.

Minimum events (bộ event tối thiểu để không bị mù dữ liệu):

- First open (mở game lần đầu).
- Tutorial start/complete.
- Level start/complete/fail.
- Attempt count.
- Booster shown/used.
- Ad request/loaded/show/complete.
- Reward granted.
- Offer shown/click/purchase.
- Session start/end.
- Crash/load time.

Output:

- Funnel rõ (biết user rớt ở bước nào).
- Dữ liệu đủ để debug retention và monetization (tìm nguyên nhân chỉ số xấu).

### Bước 4: Soft launch và đọc cohort

Không đọc trung bình chung quá sớm. Cần đọc theo:

- Country (quốc gia).
- Platform (iOS/Android).
- Creative source (creative/campaign nào kéo user đó vào).
- Campaign (chiến dịch quảng cáo).
- Version (phiên bản build).
- New/returning user (user mới/quay lại).
- Payer/non-payer (đã mua/chưa mua).
- Ad viewer/non-ad viewer (có xem ads/không xem ads).

Output:

- Bottleneck chính (điểm nghẽn lớn nhất đang giới hạn game).
- Decision: iterate, kill, pivot, scale test.

### Bước 5: Monetization tuning

Khi retention có tín hiệu, mới tăng monetization sâu hơn.

Test:

- RV placements (vị trí quảng cáo có thưởng).
- Interstitial frequency (tần suất interstitial).
- Starter pack timing (thời điểm hiện gói đầu).
- Remove ads price (giá gói bỏ ads).
- Booster economy (giá, số lượng, cách nhận, cách tiêu booster).
- Event reward (phần thưởng sự kiện).
- Piggy bank.

Output:

- ARPDAU/LTV tăng mà không phá D1/D3/D7.

### Bước 6: Scale và live ops

Khi LTV > CPI ổn định, game mới bước vào bài toán scale:

- Creative fatigue management (quản lý việc quảng cáo bị mỏi: cùng một creative chạy lâu sẽ giảm hiệu quả).
- New channel expansion (mở thêm kênh UA).
- Event calendar (lịch sự kiện).
- Level production pipeline (quy trình sản xuất level đều và có QA/data review).
- Economy balancing.
- Payer segmentation (phân nhóm người trả tiền theo mức chi/hành vi).
- Re-engagement (kéo user cũ quay lại).
- Localization (bản địa hóa ngôn ngữ, visual, store page, creative).

Ở giai đoạn này, publisher và studio không còn đang "test một game". Họ đang vận hành một business.

## 11. Công thức của game có thể đem về hàng triệu đô

Không có công thức chắc chắn. Nhưng có một khung đủ thực dụng:

```text
Million-Dollar Game =
    Big Market
  * Low Enough CPI
  * Strong Enough Retention
  * Deep Enough Session
  * Natural Enough Ads
  * Meaningful Enough IAP
  * Repeatable Creative Pipeline
  * Fast Enough Iteration
  * Trust-Preserving Design
```

Trong đó:

Big Market (thị trường đủ lớn): Mỹ và các Tier 1 market (nhóm thị trường giá trị cao như Mỹ, Canada, UK, Đức, Nhật, Hàn...) có đủ người dùng trả giá cao.

Low Enough CPI (CPI đủ thấp): không nhất thiết thấp nhất, nhưng phải thấp hơn LTV đủ margin (khoảng chênh đủ để có lợi nhuận sau phí, sai số và chi phí vận hành).

Strong Enough Retention (retention đủ mạnh): D1 chứng minh first impression (ấn tượng đầu), D3 chứng minh early habit (thói quen sớm), D7 chứng minh game có chiều sâu.

Deep Enough Session (phiên chơi đủ sâu): người chơi có đủ thời gian và tình huống để tạo revenue.

Natural Enough Ads (ads đủ tự nhiên): rewarded video có lý do tự nguyện, interstitial không phá flow.

Meaningful Enough IAP (IAP đủ có ý nghĩa): player mua vì thấy giá trị, không vì bị ép.

Repeatable Creative Pipeline (pipeline creative có thể lặp lại): một creative thắng không đủ. Cần nhiều angle, nhiều variant (biến thể), nhiều thị trường.

Fast Enough Iteration (vòng lặp sửa đủ nhanh): team sửa đúng bottleneck trước khi tiền test cháy hết.

Trust-Preserving Design (thiết kế giữ niềm tin): người chơi tin game công bằng.

Nếu thiếu một lớp, game vẫn có thể kiếm tiền. Nhưng để đi tới hàng triệu đô, các lớp phải cùng hoạt động.

## 12. Kết luận: không có monetization độc lập với product

Monetization không phải phần gắn thêm sau gameplay.

UA không phải việc riêng của publisher.

Level design không phải việc riêng của GD.

Ads implementation không phải việc riêng của dev.

IAP không phải việc riêng của store.

Tất cả nằm trong một hệ thống chung: biến attention thành retention, biến retention thành cơ hội monetization, biến monetization thành LTV, và biến LTV thành khả năng mua thêm user.

Đối với publisher, lợi thế không chỉ là có tiền chạy ads. Lợi thế là có operating system để đọc nhiều studio, nhiều prototype, nhiều cohort và biến thất bại thành learning.

Đối với studio, lợi thế không chỉ là build nhanh. Lợi thế là hiểu vì sao game thắng hoặc thua, giữ lại learning, và dần sở hữu nhiều lớp hơn trong chuỗi giá trị: data, IP, live ops, monetization và product judgment.

Đối với dev, giá trị không chỉ là code đúng task. Giá trị là làm cho game đo được, vận hành được, sửa được và scale được.

Game kiếm tiền lớn không đến từ việc làm nhiều thứ không có căn cứ. Nó đến từ một workflow trong đó mỗi quyết định đều có giả thuyết, mỗi giả thuyết có chỉ số kiểm chứng, mỗi chỉ số có owner, và mỗi vòng test làm cả hệ thống thông minh hơn.

Nếu phải rút gọn thành một câu:

```text
Revenue hàng triệu đô = Market insight + Creative signal + Retention design + Monetization design + Operating discipline.
```

Làm game là sản xuất. Làm game kiếm tiền lớn là thiết kế một hệ thống kinh tế hành vi có khả năng học nhanh hơn thị trường.

## Nguồn nghiên cứu dùng để neo bài

- Unity - Hybrid-casual games: https://unity.com/glossary/hybrid-gaming
- AppLovin MAX - User Activity reporting, DAU/DAV/ARPDAU/Ad Viewer Rate/IMPDAU: https://legacy-support.axon.ai/en/max/max-dashboard/reports/user-activity-reporting/
- AppLovin - Video ad insights, interstitial/rewarded placement và creative video: https://www.applovin.com/en/video-insights
- GameAnalytics - Retention theo install/event trigger: https://docs.gameanalytics.com/products-and-features/analytics-iq/engagement-tools/retention/
- Liftoff/Singular - 2025 Casual Gaming Apps Report release: https://www.prnewswire.com/news-releases/28-of-casual-game-installs-from-non-gaming-publishers-come-from-utility-apps-liftoffs-casual-gaming-apps-report-reveals-302441607.html
- AppsFlyer - 2025 App Marketing Outlook: https://www.appsflyer.com/blog/measurement-analytics/2025-app-marketer-survey/
- Adjust - Gaming app insights 2026: https://www.adjust.com/resources/ebooks/gaming-app-insights/
