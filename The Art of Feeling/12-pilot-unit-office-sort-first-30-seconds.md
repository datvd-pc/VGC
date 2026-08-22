# Pilot Unit -- Office Micro-Breaker x Sort Puzzle x First 30 Seconds

> **Loại trang:** Field manual / pilot format
> **Dùng khi:** Publisher brief nhắm US mobile puzzle và team cần kiểm tra 30 giây đầu có tôn trọng một phiên chơi ngắn, dễ bị gián đoạn hay không.
> **Decision question:** Người chơi có thể vào game, đọc board, thực hiện một nước đi có chủ đích và sẵn sàng dừng/quay lại mà không mất mạch suy luận không?

## 1. Điều kiện và giới hạn

| Trường | Giá trị pilot | Nhãn evidence |
|---|---|---|
| Market | US mobile puzzle | `Verified baseline`: ESA 2026 xác nhận mobile và puzzle có độ phủ lớn ở người chơi Mỹ; không chứng minh riêng hành vi nhân viên văn phòng |
| Primary segment | `US-PZ-02` Office micro-breaker | `Segment hypothesis`: cần xác nhận bằng playtest/telemetry của dự án |
| Mechanic | Abstract sort: chuyển phần tử trên cùng vào container trống hoặc cùng loại | `Evidence-supported mechanic`: xem `04-mechanic-family-research.md` |
| Journey moment | Cold start đến nước đi đầu và trạng thái dừng/quay lại | `Project test scope` |
| Non-goal | Tối ưu doanh thu, difficulty dài hạn hoặc art final | Không kết luận từ pilot này |

## 2. Theory card -- Micro-session không có nghĩa puzzle nông

**Nguyên tắc:** giảm ma sát thực thi, không giảm giá trị suy luận. Người chơi phải biết mình đang làm gì, dự đoán được kết quả và được phép dừng bất cứ lúc nào. Thử thách nằm ở quyết định chuyển vật thể, không nằm ở việc chờ animation, tìm nút hoặc nhớ luật mơ hồ.

| Cần bảo toàn | Biểu hiện trong sort puzzle | Không phải giải pháp |
|---|---|---|
| Clarity | Nhìn là biết goal, container nào có thể nhận, phần tử nào đang ở trên | Text tutorial dài hoặc highlight mọi thứ cùng lúc |
| Agency | Player chọn source/destination và dự đoán được valid/invalid move | Auto-play nước giải đố tốt nhất |
| Causal feedback | Sau move, state và lý do valid/invalid được đọc được | VFX/screen shake không giải thích rule |
| Resume recovery | Sau gián đoạn, player nhận lại goal, state thay đổi gần nhất và next action | Bắt load lại level hoặc lặp cutscene |

**Nguồn sử dụng:** `MKT-02` chỉ làm baseline US population; `S1/S3/S4/S13/S14` trong `02-source-library.md` và sort research tại `04-mechanic-family-research.md` hỗ trợ vocabulary/mechanic. Các threshold trong unit này là `Project benchmark` để test, không phải benchmark thị trường US.

## 3. Visual -- 30-second player loop

```text
0s                  3s                 8s                 15s                 30s
|-------------------|------------------|------------------|-------------------|
Open board           Read goal/state    Predict + move     Understand result   Continue or stop
     |                      |                 |                    |                |
     v                      v                 v                    v                v
No blocking splash    Goal, capacity,    Source/destination  Validity, transfer  Save exact state;
or forced tutorial    colors/shapes,     are unmistakable;    and new possibility show resumable next
                        active element    input is forgiving   are visible         action on return

Failure at any point: capture the player quote, screen state, event timestamp, and hypothesis.
```

### Abstract board before/after

```text
GOAL: Group each shape.  MOVE: 0/12

Before                         Player predicts                     After
 [A B] [A] [ ]                 Move top A -> empty                 [A B] [ ] [A]
 source  target  buffer        because empty accepts A             source target buffer

What must be visible:          What feedback proves:               What player learns:
 - top movable item A          - transfer happened                 - empty space is a resource
 - target capacity             - move count changed                - next move is still theirs
 - empty buffer                - no hidden rule intervened
```

## 4. Field memo -- Fill before implementation

| Prompt | Project answer |
|---|---|
| Publisher Brief ID | |
| Primary segment evidence | `US-PZ-02` hypothesis; source/owner/date: |
| Singular promise | "In a short break, I can make one smart move and leave without losing my place." |
| First meaningful action | |
| Rule player must infer in 30 seconds | |
| State signifiers | Goal / movable top item / valid target / capacity / buffer: |
| Intentional cognitive friction | |
| Friction to remove | |
| Accessibility alternatives | Color + shape / haptic optional / sound optional / text size: |
| Stop-and-resume behavior | Save point, resume cue, no-ad condition: |
| Owner | Design: / UX: / Art: / Engineering: / QA: / Data: |

## 5. Build checklist -- First 30 seconds

### A. Before the first move

- [ ] The goal appears without a blocking modal.
- [ ] The board shows only enough objects to learn one rule; no irrelevant decoration competes with state.
- [ ] Movable top items, capacity and empty buffers use redundant visual signals, not color alone.
- [ ] The first valid move is discoverable but not automatically performed.
- [ ] Input targets tolerate normal thumb imprecision; no precision drag is required unless it is the intended puzzle skill.

### B. During the first move

- [ ] Before release, feedforward shows valid/invalid destination without revealing the whole solution.
- [ ] An invalid move has a calm, causal explanation and preserves the player state.
- [ ] A valid move displays source change, destination change and move/resource cost in a readable order.
- [ ] Animation duration supports reading the transfer; it does not make the player wait to think again.

### C. At interruption or return

- [ ] App pause/background preserves exact state.
- [ ] Resume does not replay an intro, tutorial modal or unrelated offer.
- [ ] Resume cue restores goal and last state change without obscuring the board.
- [ ] No interstitial appears on resume, while a player is executing a move, or immediately after a confusing failure.

## 6. Creative-to-FTUE alignment audit

Use this table for every creative concept before spending UA budget.

| Creative promise | FTUE proof by 30s | Alignment verdict | Owner/action |
|---|---|---|---|
| "A satisfying sort in your break" | Player makes one readable transfer and sees a clean state change | Pass only if playtest player can explain why it worked | UA + design |
| "Think one move ahead" | Board exposes a non-trivial buffer/choice before first win | Hold if first move is purely scripted | Design |
| "Relaxing, no pressure" | No timer, forced ad, aggressive failure or noisy visual competition | Fail if monetization interrupts the proof moment | Product + ads |

## 7. Playtest protocol

### Recruit

- 5--8 US-based mobile players for the first qualitative pass; mix people who play puzzle regularly and people new to sort puzzles.
- Treat office/micro-break context as a screening question, not a job-title assumption.
- Include at least one participant who uses accessibility settings or reports a relevant visual/motor need when feasible.

### Run

1. Open the playable cold; do not explain the rule.
2. Ask: "What do you think you need to do?" before the first touch.
3. Ask: "What do you think will happen if you move that?" before release.
4. Interrupt after the first completed move; resume after a short unrelated task.
5. Ask: "What changed? What would you do next? Could you stop here without losing your thought?"
6. Record behavior, quotes, screen/video timestamp and build version; do not turn a suggested fix into the finding.

## 8. Telemetry specification

| Event | Required properties | Diagnostic question |
|---|---|---|
| `ftue_board_shown` | build, level, segment_hypothesis_id, country, platform | Did the player reach the board? |
| `ftue_goal_visible` | elapsed_ms, goal_id | Is the goal rendered before interaction? |
| `ftue_first_touch` | elapsed_ms, object_type, object_state | What does the player assume is actionable? |
| `ftue_move_previewed` | source, destination, validity, elapsed_ms | Can they find and evaluate a move? |
| `ftue_move_committed` | source, destination, validity, elapsed_ms, move_number | Is first action intentional and valid? |
| `ftue_invalid_move` | reason_code, source, destination, recovery_action | Which rule/signifier is unclear? |
| `app_backgrounded` | elapsed_ms, board_state_hash | When does the session get interrupted? |
| `ftue_resumed` | absence_ms, board_state_hash, resume_cue_shown | Was exact state restored? |
| `ftue_post_resume_move` | elapsed_ms, validity | Can the player recover the plan? |
| `ad_impression` | placement_id, elapsed_ms, game_moment | Did an ad interrupt a protected moment? |
| `ftue_abandoned` | elapsed_ms, last_event, board_state_hash | At which moment does the loop break? |

## 9. Audit findings and intervention menu

| Finding | Likely cause to test | Intervention | Do not do |
|---|---|---|---|
| Player cannot state goal | Goal visually weak or mixed with decorative UI | Reduce competing signals; show compact goal state | Add a paragraph of tutorial text |
| Player touches invalid object repeatedly | Affordance/signifier mismatch | Clarify movable top item and invalid state | Increase VFX intensity everywhere |
| Player cannot predict move | Capacity/validity rule invisible | Add destination preview and one safe example | Auto-complete all early moves |
| Player returns and restarts thinking | Resume state lacks orientation | Show last action/goal cue and preserve board exactly | Reset level or sell a booster |
| Player stops after an ad | Placement breaks proof moment | Remove ad from FTUE/resume; retest at natural break | Compensate by raising reward value only |

## 10. Decision gate

### Initial project benchmarks -- replace after baseline collection

These are **starting hypotheses**, not US industry targets.

| Condition | Initial rule | Decision |
|---|---|---|
| Goal comprehension | At least 4 of 5 qualitative participants explain the goal without tester instruction | Otherwise `iterate` goal/signifiers |
| Prediction | At least 4 of 5 can state a plausible first-move outcome before committing | Otherwise `iterate` feedforward/rule teaching |
| Causal learning | At least 4 of 5 explain why their first move was valid/invalid | Otherwise `hold` progression expansion |
| Resume recovery | At least 4 of 5 make a purposeful next move after interruption without re-teaching | Otherwise `iterate` resume cue/state persistence |
| Trust guardrail | No participant reports that an ad/offer interrupted the first proof moment | Otherwise `remove placement` before retest |

Record the final decision in the Decision Log:

```text
Pilot ID:
Build/version:
Evidence reviewed:
Finding severity:
Owner and due date:
Decision: KEEP / ITERATE / HOLD / KILL
Reason and linked claim IDs:
Next retest condition:
```

## 11. Sources and label check

| ID | Used for | Allowed conclusion |
|---|---|---|
| `MKT-02` / ESA 2026 | US game/mobile/puzzle population baseline | US puzzle/mobile is broad across generations; not a claim about office behavior or optimal session length |
| `S1` | Game feel vocabulary: physicality, amplification, support | Feedback and input can be designed intentionally; not proof of puzzle trust alone |
| `S3/S4` | Puzzle contract | Players need information sufficient for fair inference; not a standard ad frequency rule |
| `S13/S14` | Sort state/rule vocabulary | Defines mechanic constraints; does not prove user experience |
| Project playtest and events | `US-PZ-02` and all decision thresholds in this unit | Supports only this project/build/cohort until replicated |

