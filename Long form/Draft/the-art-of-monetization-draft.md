# The Art of Monetization

## Research note: A living framework for better decisions

In a game business, a sound decision rarely comes from one mechanism, one striking creative, or one dashboard. A popular mechanic is not yet a product thesis. A bold creative cannot compensate for weak economics. A dashboard cannot replace game feel, level craft, or the judgement required to stop a promising idea.

This research began with a publisher-led game event and a close look at the puzzle category. The market opportunity was visible. So was the noise: successful mechanics, themes, and monetization patterns are copied faster than teams can explain the player need, production burden, or economic logic beneath them.

This ebook is a living framework of hypotheses, tools, public evidence, and questions. It will be updated through reader feedback, shipped-game experience, player behaviour, and cohort evidence.

Questions, counterarguments, and real operating cases are welcome. Please share the condition that limits a framework, the evidence that contradicts it, or the decision tool that helped your team avoid a bad bet. The aim is to contribute a clearer decision language for game teams, and to improve it with the support of people who work closest to the product.

## A Note to the Reader

Games are hard enough to make. Monetization makes them harder because it forces several disciplines to meet in the same place: design, economy, user acquisition, product, data, operations, and judgement.

This book was written for the person who has to make those disciplines work together. You may be a founder, product lead, game designer, analyst, UA lead, publisher, or a small team wearing all six hats before lunch.

You will find principles here, but no sermon. Each framework is a working hypothesis. It earns its place only when it changes a decision: which creative to test, which level to inspect, where an ad belongs, which offer has a reason to exist, which metric deserves attention, or when the right answer is to stop.

Read with a pen. Keep your build and dashboard close. A good book on monetization should make you reopen the game with less certainty and better questions.

## Contents

1. The System Behind the Store
2. From Creative to First Return
3. Progress, Pressure, and Fairness
4. Ads, IAP, and Economy
5. Signals, Decisions, and Experiments
6. What Data Can and Cannot Decide
7. The Operating System Behind a Live Game
8. Genre Playbooks
9. The Audit
10. Research Notes and Public Sources

## How To Read This Ebook

Do not read this ebook like a blog post.

Read it like an audit.

Every chapter should send you back to a real part of your game: an ad, a store page, a first session, a level, a fail moment, a rewarded ad, an offer, an event, a dashboard, a review, a team meeting.

If you have a live game, keep the build close. When the chapter talks about the first ten levels, play the first ten levels. When it talks about rewarded ads, find the first rewarded ad placement and ask what the player needed at that moment. When it talks about IAP, open the store and name the exact problem each offer solves. When it talks about metrics, open the dashboard and separate signal from noise.

If you are still prototyping, use the chapters as gates before soft launch. A game that cannot explain its promise, first session, pressure, ad exchange, offer logic, and return reason is not ready for scale. It may still be fun. It may still have potential. It is not yet a monetization system.

This book is worth more when you read it with a pen, a notebook, and a game you are willing to question.

One useful note per chapter is enough.

One fixed leak can change retention.

One cleaner offer can change payer conversion.

One better ad placement can protect trust and still raise revenue.

One sharper creative promise can save weeks of UA waste.

The point is not to agree with every framework. The point is to leave each chapter with a sharper question for your own game, and a better way to challenge the answer.

## Introduction: Monetization Starts Before The Store

Most games do not fail to monetize inside the shop.

They fail earlier.

They fail when the ad promises one emotion and the first session delivers another. They fail when the store page cannot prove the creative. They fail when the first level teaches too slowly, or too much, or nothing at all. They fail when the first interstitial arrives before the player has decided the game deserves another minute. They fail when a level feels unfair, then sells the cure. They fail when the team reads revenue as health while retention, reviews, refunds, and trust begin to bleed.

The store collects money. It does not create permission.

Permission is earned long before the first purchase. A player pays with attention first. Then with a click. Then with an install. Then with waiting. Then with a first session. Then with a return. Money comes later, if the game has kept enough trust alive.

This is why monetization cannot be treated as a layer added after the game works.

In casual, hybrid-casual, puzzle, and hybrid puzzle games, monetization is the product of a full journey:

```text
See Ad -> Click -> Store -> Install -> First Open
-> First 10 Levels -> First Return -> Habit
-> Ads Opt-in -> First Purchase -> Repeat Purchase
-> Event/Live Ops -> Share or Recommend
```

Every step asks for something.

The ad asks for attention.

The store asks for belief.

The first open asks for patience.

The first ten levels ask for trust.

The first ad asks for permission.

The first offer asks for money.

The first event asks for a habit.

A weak monetization strategy treats these moments as separate surfaces. A stronger one treats them as one system.

The useful formula is not only:

```text
Profit = Installs * (LTV - CPI)
```

That formula is true, but it arrives too late. It tells you whether the machine works after the machine has already run.

For design and operation, a more useful formula is:

```text
Monetization = Player Need * Right Context * Trust * Execution Speed
```

Player need means the game understands what the player wants at that moment: relief, retry, mastery, speed, progress, collection, convenience, status, or control.

Right context means the ad or offer appears when the need is alive, not when the spreadsheet wants inventory.

Trust means the player still believes the game is fair enough to deserve more time or money.

Execution speed means the team can learn from signals quickly: creative data, level funnel, ad exposure, offer conversion, cohort retention, review language, refund pressure, live ops performance.

This is the operating map of the ebook:

```text
Monetization System = Promise * Progress * Pressure * Permission * Payment * Persistence
```

Promise is what the creative, store, screenshots, and first impression say the game will feel like.

Progress is how the game makes the player feel smarter, further ahead, more skilled, more invested.

Pressure is the tension created by limits, scarcity, blockers, near-misses, deadlines, and goals.

Permission is the player's sense that watching an ad or paying is fair, voluntary, and relevant.

Payment is the product sold: a booster, remove ads, a starter pack, a piggy bank, a pass, a revive, a bundle, a shortcut, a refill.

Persistence is the reason to come back: habit, event cadence, content supply, collection, social loop, seasonal rhythm, portfolio operation.

When one part breaks, revenue may still rise for a while. That is the danger.

Revenue can grow while trust falls.

IMPDAU can rise while D3 weakens.

Fail offers can convert while reviews begin to mention unfair levels.

Interstitials can lift ARPDAU while the game becomes harder to scale.

Short-term monetization can create long-term debt.

The work is to know the difference between healthy revenue and borrowed revenue.

Healthy revenue gives the player a reason to keep playing after the ad, after the offer, after the purchase.

Borrowed revenue extracts value from pressure the game cannot defend.

This ebook is about that difference. It makes no claim to replace a shipped-game team's judgement. It offers a shared language for challenging that judgement with more discipline.

It is about designing monetization as a behavior system, not a shop screen. It is about reading the player journey before reading the revenue chart. It is about knowing when ads are utility, when IAP solves a real need, when pressure becomes unfair, when randomness creates replay value, when live ops adds life, and when a team is only squeezing a game that has stopped earning trust.

The goal is simple.

Build games that can make money without making players regret the time they gave you.

## A Running Example: Clear Garden

To make the framework concrete, imagine a soft-launch hybrid puzzle called *Clear Garden*. Its core loop asks the player to sort overgrown garden objects into limited trays, clear space, and restore small areas of a neglected garden. The initial creative sells relief through order and a visible transformation.

The first version has familiar problems. It asks for tracking permission before the player has touched the puzzle. It places an interstitial after level two. Level seven introduces too many object types at once, then shows an extra-tray offer after failure. Its starter pack sells coins without explaining what coins will change. Its daily reward is generous, yet nothing in the garden gives the player a reason to return tomorrow.

Clear Garden is fictional. The decisions are common. Each part of the book returns to this example because most monetization failures become visible when a team moves from a general principle to one specific moment in a build.

## Part I: The System Behind the Store

### 1. Trust Is the First Balance Sheet

Every player arrives with a limited willingness to believe you. Call it a trust budget.

The budget is spent before they know the name of a single SKU. A misleading creative spends it. A slow load spends it. A tutorial that confiscates control spends it. A close button that hides in the corner spends it. An impossible-feeling level followed by a booster offer spends it fast.

Trust is renewed by small, ordinary things: rules the player can read, inputs that do what they promise, rewards that arrive, prices that are plain, failure that teaches, and support that resolves a broken purchase. None makes a dramatic slide deck. Together they determine whether an ad feels like a fair exchange or whether a purchase feels like a trap.

This is why a revenue increase cannot be judged on revenue alone. Add an interstitial and ARPDAU may rise. The same cohort may leave earlier, rate the game lower, or become harder to reacquire after creative fatigue. You have moved cash forward in time. You have not necessarily created value.

Use a simple ledger during reviews:

| Trust investment | Trust withdrawal |
| --- | --- |
| Clear goal and readable rules | Creative promises a different game |
| Fair loss with a visible next move | Hidden difficulty intervention |
| Voluntary rewarded exchange | Forced interruption during concentration |
| Precise price and deliverable | Ambiguous bundle or accidental purchase path |
| Fast recovery from purchase errors | Missing rewards, weak restore flow, slow support |

The question for every monetization surface is direct: does this take trust, renew trust, or both? A mature team can answer it without pretending that revenue and player welfare are enemies. They are linked through time.

### 2. Revenue Can Be Healthy or Borrowed

Monetization debt appears when a team improves a short-term metric by damaging the conditions that make future revenue possible.

An early interstitial may lift ad revenue while weakening D1 and store rating. A hard wall can improve extra-move conversion while creating reviews that call the game rigged. A highly dramatic creative can lower CPI while sending the wrong audience into the funnel. A reward economy can be inflated until every future event must pay more merely to feel normal.

None of these choices is automatically wrong. The error is declaring victory before reading the bill.

Treat every material monetization change as a trade:

```text
Immediate gain: revenue, conversion, ad impressions, or CPI.
Possible cost: retention, payer retention, review sentiment, refunds, support load, and future content cost.
```

The language matters. "We increased ad load" describes a mechanism. "We improved monetization" is a conclusion that requires evidence.

A useful cohort review asks four questions:

1. Did the change improve the intended metric?
2. Did behavior deteriorate after the new exposure point?
3. Did the effect persist beyond the first session or first purchase?
4. Would we make the same choice if ratings, refunds, and future UA cost were included in the result?

If the first answer is yes and the other three are unclear, you have a hypothesis, not a win.

### 3. Bright Design Has a Clear Contract

Games create tension. They should. A puzzle without uncertainty is paperwork.

The ethical line sits at the contract between game and player. Bright design makes the rules, odds, price, and consequences understandable. It lets a player make a real choice. Dark patterns obscure a rule, manufacture confusion, hide the way out, or sell relief from a problem the game secretly caused.

Near-miss design is a good test. A near miss can be satisfying when the player sees the one decision that would have changed the outcome. It becomes corrosive when the game conceals its intervention, repeatedly pushes the same loss, then presents payment as the only intelligible path.

The same test applies to limited-time offers, streaks, random rewards, remove-ads products, and dynamic difficulty. Ask whether a capable player can explain what happened and choose freely after it happened.

Public enforcement provides the practical warning. The U.S. Federal Trade Commission's 2022 action against Epic Games alleged dark patterns that led to unwanted charges, alongside other consumer-protection issues. The point is broader than one company or one genre: payment design, consent, and disclosure are product responsibilities, not legal decoration. See the FTC's [settlement announcement](https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations) and [business guidance](https://search.ftc.gov/business-guidance/blog/2022/12/245-million-ftc-settlement-alleges-fortnite-owner-epic-games-used-digital-dark-patterns-charge).

### 4. The Six-Part Operating Map

The rest of the book uses six terms. They are deliberately plain.

| Component | The question it answers | Typical failure |
| --- | --- | --- |
| Promise | Why did this player arrive? | Creative and game sell different emotions |
| Progress | Why does another minute feel worthwhile? | Rewards arrive without meaning or mastery |
| Pressure | Why act now? | Friction feels arbitrary or punitive |
| Permission | Why is an ad or offer acceptable here? | The exchange interrupts rather than helps |
| Payment | What problem does money solve? | Store sells currency with no live need |
| Persistence | Why return after today? | Content and events lack a calendar or purpose |

This map is more useful than a list of features because it exposes the missing link. A team may have payment products and no permission. It may have pressure and no readable progress. It may have excellent UA and no persistent reason to stay.

The multiplication sign in the earlier formula matters. If one factor approaches zero, the rest cannot rescue it for long.

### Case Note: Royal Match Shows the Size of the Whole Machine

In July 2023, Sensor Tower reported that Royal Match generated about $112 million in gross mobile revenue and 14.6 million downloads during the month, while paid installs accounted for 61.5% of its downloads. The exact configuration inside the game is not public. The operating lesson is still clear: category leadership came from a machine that joined UA, a comprehensible core loop, large content output, and live operations. It did not come from a clever shop screen in isolation. Read the original [Sensor Tower analysis](https://sensortower.com/blog/royal-match-surpasses-candy-crush-saga-in-revenue-and-downloads-for-the) for the reported figures.

### Part I Field Notes

Before moving on, write one sentence for each component of the operating map. Use your current game, not an ideal version of it.

```text
Our promise is:
Our player's first meaningful progress is:
Our strongest pressure moment is:
Our first ad or offer is permitted because:
Our first purchase solves:
Our reason to return tomorrow is:
```

Blank answers are more valuable than elegant ones. They show where the work begins.

## Part II: From Creative to First Return

### 5. Creative Sells a Feeling Before It Sells a Feature

Players rarely install because they admire your feature list. They install because a short video offers a feeling: rescue, order, cleverness, speed, a satisfying clear, a comeback, a collection that grows, a mess put right.

The creative should identify the emotional job of the game. A screw puzzle can sell release from visual clutter. A sorting game can sell the pleasure of restoring order. A match-3 game can sell a chain reaction and the prospect of building something over time. These are distinct promises, even when the screenshots look broadly similar.

Creative may dramatize the feeling. It cannot survive for long when it sells a different game. The usual cost is hidden in the funnel: good click-through rate followed by weak store conversion, poor D1, low session depth, and review language that says "the ad was fake." Cheap attention becomes expensive traffic.

Build a creative library around scenarios, not isolated assets. For each concept, record the fantasy, the visible conflict, the payoff, the intended persona, the actual first-session proof, and the cohort outcome. AI tools can accelerate production. They cannot decide whether the scenario is faithful to the product.

AppMagic's public 2025 UA trend summaries point to a market filled with AI-made concepts, live-ops-led messaging, native short-form formats, niche hooks, and celebrity campaigns. That widens the creative menu. It also raises the cost of vague promises. The game still has to cash the cheque written by the ad.

### 6. The Store and First Open Must Prove the Same Claim

The store page is a verification surface. The first open is the verdict.

If an ad promised a rescue puzzle, show a rescue puzzle before the player reaches a generic menu. If it promised an orderly sort, let the player touch the sort loop before asking for notification, tracking, login, rating, or a special offer. Every early interruption asks the player to trust a game that has not yet earned the right.

This does not mean the first session must be bare. It means sequence matters. A strong opening usually follows this order:

```text
Show the fantasy.
Give control quickly.
Create a small, readable success.
Reveal a next goal.
Introduce one useful choice.
Ask for consent only when the value is visible.
```

Privacy permissions deserve the same care as payment. On Apple platforms, App Tracking Transparency requires a system permission request before tracking across apps and websites. Treat that prompt as a trust moment with a real product cost, not as a button to fire at launch. Apple's [ATT documentation](https://developer.apple.com/documentation/apptrackingtransparency) explains the platform requirement; your job is to decide when the player has enough context to understand it.

### 7. The First Ten Levels Form an Emotional Contract

The first ten levels teach more than rules. They teach the moral character of the game.

Players learn whether losses are readable. They learn whether a booster is an interesting option or a compulsory repair kit. They learn whether rewards have weight. They learn whether the game respects their time between rounds.

Use those levels to establish one primary competence, then add difficulty through combinations, timing, space, or planning. Do not use early complexity as proof of depth. A player who cannot explain a loss cannot learn from it. Repeated unreadable loss becomes suspicion.

For every early level, record:

| Question | Why it matters |
| --- | --- |
| What is the player meant to learn? | Prevents decorative tutorials |
| What decision causes success or failure? | Keeps the loss legible |
| What feeling should the win create? | Aligns reward, audio, and pacing |
| What happens after failure? | Reveals whether pressure is fair |
| Is a booster introduced as choice or rescue? | Protects future offer trust |

Do not aim for a low fail rate everywhere. Aim for interpretable failure. High fail plus high retry can signal satisfying challenge. High fail plus low retry often signals confusion, exhaustion, or a broken promise.

### 8. First Return Needs a Reason, Not a Reminder

Notifications can remind a player about a reason to return. They cannot manufacture one.

The return hook may be a new board, a construction timer, a collection completion, a daily goal, a social obligation, an event milestone, or the memory of an unfinished puzzle. Choose one early. Make it understandable. Then let the player leave with a small amount of unfinished business.

Avoid a return loop built only on currency refill. It can work briefly, but it teaches the player that the game is withholding play rather than offering a world worth revisiting. Energy is stronger when it regulates a larger rhythm: event attempts, meaningful decisions, social cadence, or long-form progression.

Merge Mansion is a useful public example of persistence as an operational capability. Public AppMagic-related analysis reported a material revenue recovery alongside a much denser event cadence in 2024 and early 2025. The inference is not that every game needs twenty events a month. It is that live ops is a system of content calendar, economy, narrative, segmentation, and measurement. A board alone rarely carries a mature hybrid puzzle forever.

### Part II Field Notes

Play your first session with the sound on and a stopwatch running. Write down every request your game makes before the player reaches level three.

```text
Request for attention:
Request for consent:
Request for data:
Request for money:
Request for patience:
```

Then write what the player has received before each request. The gap between those lists is a useful measure of early trust.

## Part III: Progress, Pressure, and Fairness

### 9. Different Players Buy Different Forms of Relief

There is no universal player journey. A game may contain several audiences whose motivations overlap only at the surface.

| Persona | They seek | They dislike | Monetization that may fit |
| --- | --- | --- | --- |
| Relaxer | Calm, clarity, gentle competence | Harsh interruption, unreadable loss | Remove ads, optional hints, cosmetic comfort |
| Solver | A problem worth understanding | Randomness that hides causality | Extra move, undo, targeted tools |
| Collector | Completion, ownership, visible growth | Rewards with no place to live | Albums, decoration, themed bundles |
| Optimizer | Efficient progress and planning | Wasteful currencies, weak information | Passes, milestone rewards, resource bundles |
| Rescuer | Repair, care, visible transformation | Fantasy that never appears in play | Story progress, task acceleration, cosmetics |
| Ad Trader | A clear exchange of time for utility | Forced ads and vague rewards | Rewarded retries, currency, double rewards |
| Convenience Payer | Fewer interruptions and less waiting | Repeated tiny obstacles | Remove ads, starter packs, refills |

These labels are working tools, not a claim that people fit into sealed boxes. Use them to ask whether your first offer solves a recognizable need for the cohort that reaches it.

A common mistake is treating every player who fails as a rescuer for sale. Some want a second attempt. Some want to understand the level. Some would rather leave than pay. A monetization system becomes stronger when it leaves room for all three responses.

### 10. Progress Must Change the Player's Situation

Progress can take several forms: mastery, completion, collection, streak, identity, narrative movement, or greater control over a system. The currency counter is only evidence of progress when it changes one of those states.

The test is simple. Remove the reward from a session. Would the player still know what improved? If the answer is no, the game may be producing activity without advancement.

Good progression does two jobs. It gives the player a reason to continue now, and it makes future choices richer. A new mechanic changes future levels. A collection unlocks a visual home for effort. A construction step changes the world. A growing tool set creates new solutions. These create a base on which offers can be useful.

Do not confuse quantity with weight. Ten currencies often add accounting before they add desire. One scarce resource with a clear source, sink, and decision point can do more work than a page of counters.

### 11. Pressure Should Create a Decision

Pressure is the interval between desire and resolution. Limited moves, crowded slots, a timer, an event deadline, a near miss, a streak, and a scarce input can all create it.

Pressure works when the player understands the situation and can name at least two paths forward. Retry. Change approach. Use a free tool. Watch an ad. Spend currency. Buy a bundle. Pause and return later. The game can prefer one path commercially. The player must still be able to see the others.

Pressure fails when it merely removes agency. Examples include a blocker that arrives before the player has learned counterplay, a timer too short to read, a "limited" offer that restarts endlessly, or a forced ad placed in the middle of a cognitive task.

Use this wording in design review: "What decision does this pressure create?" If the answer is "pay or suffer," the design needs more work.

### 12. Dynamic Difficulty Is a Trust Mechanism

Dynamic level design is often treated as a revenue dial. That is too crude.

Difficulty shapes the player's explanation of the game. When a player wins, they decide whether the game let them win or whether they earned it. When they lose, they decide whether a better decision would help. That private explanation governs retry, booster use, purchase willingness, and word of mouth.

Track difficulty by level and cohort. At minimum, inspect:

```text
Start rate
Fail rate
Retry rate
Next-level start rate
Booster use before and after failure
Exit rate after failure
```

The pairings are more informative than any one number:

| Pattern | Likely reading | First action |
| --- | --- | --- |
| High fail, high retry | Demanding but engaging | Check whether players learn and progress |
| High fail, low retry | Confusing or unfair | Watch replays, inspect rule clarity and pacing |
| Low fail, low session depth | Too easy or low stakes | Add meaningful choices, not raw complexity |
| High booster use, poor next-level start | Tool patches a bad experience | Repair the level before selling harder |

Public AppMagic summaries of hybrid-casual puzzle games have described fail-point offers contributing a meaningful portion of IAP revenue in some titles. That observation is useful only with its guardrail: a fail offer proves that pressure can convert. It does not prove that the level was good, fair, or durable. Read post-offer retention, review wording, and refunds before you declare the mechanic healthy.

### 13. Randomness Must Leave Room for Skill

Randomness can make repeated play lively. It can create surprises, shape puzzle states, and keep a familiar loop from becoming a solved worksheet. It also creates a fairness problem whenever players cannot distinguish luck from hidden control.

Use randomness where it changes the situation without erasing agency. Let the player respond, plan, and learn. Explain odds where the reward is sold or where regulation and platform rules require it. Do not use randomness as a cover for invisible monetization pressure.

The best near-miss says, "I see what I could do differently." The worst says, "The game decided I should lose."

### 14. Sound, Haptics, and the Feel of a Reward

Audio and haptics regulate expectation. A small sound can make a clear feel final. A restrained vibration can mark a risky move. A reward sound can tell the player that effort changed the state of the game.

Their value is practical. They make feedback legible at speed. They should not lie. A tiny reward should not receive a jackpot fanfare; a failed action should not be masked with cheerful noise. Inflated feedback trains players to stop believing their own senses.

Test sound with the same seriousness as UI. Watch for mute rates, session behavior with audio enabled, and qualitative feedback. If your game depends on a reward beat to feel satisfying, make sure the beat serves a real reward.

### Case Note: Puzzle Is a Large Market, Not a Single Product

Sensor Tower's U.S. puzzle analysis reported a market worth roughly $5 billion in 2022, with classic match-3 alone contributing about $1.6 billion. Later AppMagic summaries showed how strongly revenue could concentrate around market leaders and specific puzzle families. The practical conclusion is modest: do not borrow a match-3 monetization mechanic for a sort or jam game merely because both live under "puzzle." The emotional loop, session length, ad tolerance, and viable IAP need can differ sharply. See [Sensor Tower's category analysis](https://sensortower.com/blog/us-mobile-puzzle-game-analysis-2022).

### Part III Field Notes

Choose one failure moment in your game. Document it as if you were a player seeing it for the first time.

```text
What did I want?
What stopped me?
What rule explains the stop?
What can I do now without spending?
What can I do now by trading time?
What can I do now by spending money?
Would I understand the difference?
```

If the answer is cloudy, monetization is trying to stand on a level-design problem.

## Part IV: Ads, IAP, and Economy

### 15. Rewarded Ads Are a Contract of Utility

Rewarded ads work best when they extend an action the player already values. A second chance after a readable loss. A double reward after a meaningful win. A small refill that lets a player continue a self-chosen plan. A tool that resolves an obvious bottleneck.

The exchange must be clear before the ad begins and reliable when it ends. State the reward. Grant it promptly. Preserve the value if the ad fails. Do not place it where it turns a normal task into a waiting room.

Unity's monetization guidance frames rewarded placements around player value and placement design, while its reporting encourages reading ad engagement with retention and IAP behavior rather than in isolation. That is the correct level of discipline. An opt-in rate tells you that players accepted an exchange. It does not tell you whether the surrounding experience caused the need fairly. Start with [Unity's monetization strategy guide](https://docs.unity.com/en-us/monetization/getting-started/monetization-strategy).

Useful rewarded placements answer one of these needs:

| Need | Possible exchange | Guardrail |
| --- | --- | --- |
| Continue a comprehensible attempt | Extra move or revive | Do not use it to repair invisible difficulty |
| Preserve a hard-earned reward | Reward multiplier | Keep the base reward meaningful |
| Explore without committing money | Trial of a tool | Explain post-trial behavior |
| Reduce a temporary wait | Small refill | Avoid blocking all play behind waits |
| Make a deliberate choice | Reroll or undo | Keep the decision readable |

### 16. Interstitials Need Natural Rest Points

An interstitial is a tax on attention. It can be tolerated at a natural rest point: after a short completed loop, after a player has banked a reward, or between sessions. It is far more expensive when it cuts through concentration, hides a response, or arrives before the game has earned its first minute.

Treat frequency caps as product settings, not network defaults. Segment by early versus mature player, session depth, prior ad exposure, platform, and purchase state. A player who bought remove ads should never have to wonder whether the product worked.

When evaluating an interstitial change, compare exposed and control cohorts on session depth, next-session return, review sentiment, and store rating trend. Revenue per daily active user is only one side of the exchange.

### 17. Boosters Should Expand Choice

A booster earns its place when it lets the player express a strategy, recover from a known mistake, or move through a chosen bottleneck. It becomes suspect when it is the only answer to unclear design.

Introduce a booster in a safe context. Let the player see its value. Give at least one free use. Then wait until a relevant need is alive before offering more. Selling a tool before the player understands the job is just selling an icon.

The same standard applies to undo, extra slots, extra moves, rockets, hammers, shuffles, and pre-level power-ups. Each needs an explicit player problem and an economy cost that does not make normal play feel broken.

### 18. IAP Should Solve a Present Need

The store is a catalogue. The offer is a sentence spoken at a moment.

Generic currency packs ask the player to perform the design work. They must infer the need, calculate the conversion, and decide whether the pack has a future use. Contextual products reduce that burden. A clean offer tells the player what it solves, why now, what they receive, and what remains optional.

Common products can have clear jobs:

| Product | A defensible job | Common misuse |
| --- | --- | --- |
| Remove ads | Protect a valued, repeated experience | A promise undermined by exclusions or confusing scope |
| Starter pack | Give early players a legible head start | Selling before the loop has value |
| Piggy bank | Turn accumulated progress into a choice | Artificially starving the base economy |
| Continue bundle | Preserve a meaningful run | Appearing after opaque or forced failure |
| Pass | Reward sustained engagement | Adding a pass before content cadence can support it |
| VIP membership | Bundle convenience, access, and rhythm | Using subscription as a substitute for retention |

AppMagic's August 2025 case study of Epic Plane Evolution illustrates the point. It described a rise in monthly IAP revenue from about $592,000 in April to $1.4 million in May, alongside a product mix involving tickets, hard currency, remove ads, and VIP-style benefits. It also reported major platform and regional differences. The lesson is not to copy the bundle. The lesson is to build products around actual uses, then read outcomes by cohort rather than treating all players as the same market. See [AppMagic's case study](https://appmagic.rocks/blog/epic-plane).

### 19. An Economy Needs Sources, Sinks, and Consequences

Every currency needs a source, a sink, a cadence, and a purpose.

Sources include play, events, ads, purchases, and social rewards. Sinks include retries, upgrades, cosmetics, unlocks, progression gates, and event acceleration. Cadence is how quickly both move. Purpose is the player decision that remains after the numbers are removed.

Economy inflation happens when rewards rise faster than meaningful uses. Scarcity becomes artificial when the game removes ordinary play merely to force a sink. Both leave the team with fewer choices. The first makes rewards feel cheap. The second makes the game feel hostile.

Review the economy with a simple balance sheet:

```text
What do free players earn in a normal week?
What do they spend to continue, progress, and participate?
What does a payer buy that remains useful after the first purchase?
Which rewards have become expected rather than exciting?
Which sinks create a real decision rather than a toll?
```

### 20. Events Are Small Economies With a Deadline

An event creates a temporary loop: earn, choose, spend, progress, and finish. The deadline gives it energy. The event currency protects the core economy from constant disruption. Premium acceleration gives players a way to spend without making free participation meaningless.

Do not run events as a pile of pop-ups. A mature event calendar has cadence, segmentation, reward policy, content supply, and recovery time. Players need room to understand the next goal. Teams need room to learn whether an event strengthened return behavior or merely pulled future spend into the current week.

### Part IV Field Notes

Open every current ad placement and offer in your game. Complete this sentence for each one:

```text
At this exact moment, the player wants ________.
This exchange gives them ________.
The player can decline by ________.
The metric that would show harm is ________.
```

Where a sentence cannot be completed, remove the placement from the roadmap until the product reason is clear.

## Part V: Signals, Decisions, and Experiments

### 21. A Dashboard Is a Map of Player Decisions

Most dashboards fail by reporting too much and explaining too little. A useful dashboard follows the journey and groups signals by the decision they illuminate.

| Area | Core signals | The decision they support |
| --- | --- | --- |
| Acquisition | CTR, IPM, CPI, store conversion, creative fatigue | Is the promise reaching the right player? |
| Activation | Load time, crash-free users, tutorial completion, L1-L10 funnel | Does the game prove its promise quickly? |
| Engagement | Sessions, session depth, retries, next-level starts, D1/D3/D7 | Is the loop worth returning to? |
| Difficulty | Fail rate, exits after failure, booster use, near-miss rate | Is pressure creating learning or resentment? |
| Ads | Viewer rate, impressions per DAU, completion, post-ad churn | Is the exchange voluntary and useful? |
| IAP | Offer views, conversion, ARPPU, repeat purchase, refund | Is the product useful and honestly delivered? |
| Trust | Ratings, review themes, support tickets, purchase failures | Is monetization weakening the relationship? |
| Operations | Creative output, experiment cycle time, content throughput | Can the team learn before the market moves? |

Do not ask one metric to answer every question. Low D1 can come from a misleading creative, a poor store page, a slow first open, a crash, a tutorial problem, or a level-one problem. The work is to narrow the field before prescribing a fix.

### 22. Read Metric Pairs, Not Isolated Numbers

The following pairs prevent many bad decisions:

| If you see | Also inspect | Why |
| --- | --- | --- |
| CTR rising | Store CVR, D1, session depth | The creative may be attracting the wrong promise-seekers |
| RV opt-in rising | Retention by exposure, level friction | High opt-in may mean useful value or manufactured pain |
| IAP conversion rising | Refunds, reviews, payer retention | Conversion can be borrowed from trust |
| Fail rate rising | Retry, exit, booster use | Difficulty needs behavioral context |
| ARPDAU rising | D3/D7, ad-exposure churn, ratings | The extra revenue may carry future cost |
| Event revenue rising | Return rate after event, resource inflation | An event can pull spend forward rather than expand value |

Market data requires the same discipline. AppMagic's H1 2025 casual-market summary estimated $12 billion in revenue and showed heavy concentration in a few categories and leaders. A large category can be economically real and still be brutally selective. Separate category growth from leader effect before turning a chart into a green light. The reported perspective is available in [Mobile Casual Games in H1 2025](https://gamedevreports.substack.com/p/appmagic-mobile-casual-games-in-h125).

### 23. Decision Trees That Keep Teams Honest

Use practical heuristics rather than pretending that a single metric diagnoses a game.

#### When D1 is weak

1. Compare the ad promise with the first playable minute.
2. Inspect store conversion by creative concept.
3. Check load time, crash rate, device coverage, and SDK overhead.
4. Watch L1 to L3 with no commentary from the player.
5. Remove or defer early pop-ups, permissions, and interruptions.

#### When D1 is stable and D3 falls

1. Inspect the first return reason.
2. Find the first difficulty spike and first ad exposure.
3. Compare content novelty between the first and second session.
4. Check whether early rewards created a meaningful next goal.
5. Segment the decline by acquisition source and creative promise.

#### When a fail offer converts well

1. Compare post-offer retention for buyers, decliners, and control cohorts.
2. Review failure replay data and qualitative feedback.
3. Check refund and support themes.
4. Test a fairer level version before increasing offer pressure.
5. Keep the offer only if value survives the full cohort view.

#### When store opens are high and purchases are weak

1. Identify the player need at store entry.
2. Check whether the product names and contents explain that need.
3. Inspect price ladder, local purchasing power, and platform differences.
4. Look for purchase failure or restore-purchase issues.
5. Test one contextual offer instead of adding more generic packs.

### 24. Experimentation Is a Production Discipline

A/B testing is valuable when it lowers uncertainty. It becomes theatre when teams test several interdependent changes, ship without a guardrail, or call a result from too little data.

Start with a written decision card:

```text
Problem observed:
Hypothesis:
Change:
Primary metric:
Guardrail metrics:
Audience and exclusions:
Minimum decision window:
Rollback condition:
Owner:
```

Use remote configuration for changes that merit quick rollback. Keep a learning repository that records the result, the cohort, the creative context, and the decision. A result without context becomes a superstition within two quarters.

Do not run an experiment because a competitor has a feature. Run it because you can explain the player decision it might improve and the harm you are prepared to detect.

### Part V Field Notes

Pick one revenue chart that looks encouraging. Put it beside retention, ratings, refunds, support volume, and session depth for the same cohorts. Write down whether the revenue is healthy, borrowed, or still unproven. "Unproven" is an acceptable answer.

## Part VI: What Data Can and Cannot Decide

### 25. Market Intelligence Can Narrow a Bet. It Cannot Make the Bet for You.

Large publishers do use large datasets. They track mechanics, themes, pricing, live-event cadence, creative patterns, player motivations, markets, and cohorts. GameRefinery publicly describes a database of more than 100,000 games, including feature-level market intelligence, player-persona data, and live-event tracking. Rovio has described an internal operating platform with dashboards, A/B testing, remote content configuration, UA attribution, and a live-ops calendar. King says its analysts and engineers use data from billions of gameplay events to inform game design and strategy.

That capability changes the speed and quality of a decision. It does not turn the decision into a lookup.

Data can tell a publisher that a screw puzzle, a rescue fantasy, a collection mechanic, or a certain live-event structure has appeared in successful products. It can estimate market appetite and reduce the cost of being ignorant. It cannot answer the questions that determine whether a specific team should build a specific version:

```text
Can this team make the core loop feel better than the alternatives?
Can it produce content at the cadence the promise requires?
Does the mechanic create a player need we can serve without corrupting trust?
Can the art, theme, creative, and meta form one believable product?
What will this team learn if the bet fails?
```

The distinction is between a market signal and a product thesis.

A market signal says: players are spending time and money in this territory.

A product thesis says: this team can create a distinct, durable experience in this territory, operate it at the required quality, and acquire the audience profitably.

The first is observable from outside. The second must be earned inside the studio.

### 26. Data Shows Behaviour. It Does Not Supply Meaning.

Every large publisher knows the power of data. The serious ones also know its limits.

Rovio's Director of Analytics has written that a seemingly strong test result can come from random variation or a novelty effect, and that analysts need an estimate of player experience before a new feature goes live. That is a crucial sentence. A dashboard records what happened after a design choice. It does not explain the player's private interpretation of the choice.

The difference matters in monetization.

Suppose Clear Garden's extra-tray offer converts at level seven. The data records a conversion. It does not tell the team whether players bought because the level was tense in a satisfying way, because the board was difficult but fair, because the offer was well framed, or because the game hid too many object types and made the player desperate to escape. Those paths can produce the same purchase event. They create very different futures.

Qualitative observation and product judgement close the gap. Watch recordings. Read the exact reviews. Ask the player to narrate their decision. Inspect the board before the offer appears. Compare buyers, decliners, and control cohorts over time. The aim is not to replace data with intuition. It is to give the data a causal story worth testing.

Supercell's public account of cancelled projects makes the warning sharper. It described Hay Day Pop as a puzzle game whose team shipped quickly and responded to data, but did not have a strong feeling for the genre or innovate in the core puzzle. The team was not short of information. It was short of a product conviction strong enough to produce a distinct game. See Supercell's [reflection on failure](https://supercell.com/en/news/learning-from-failures/).

This is where a good ebook can earn its place. It should not offer secret mechanics that publishers have already indexed. It should teach a team to formulate better hypotheses, inspect the behaviour beneath a metric, and recognize when a profitable-looking action is weakening the product.

### 27. The Useful Unit of Work Is a Decision Memo

Teams often receive a greenlight list in this form:

```text
Build a screw puzzle.
Use a rescue theme.
Add a collection meta.
Test a starter pack.
Run a win-streak event.
```

These may be reasonable prompts. They are not decisions yet.

Turn each one into a memo before it becomes a roadmap item:

| Field | Example for Clear Garden |
| --- | --- |
| Market signal | Order-and-clear puzzle cores are attracting commercial attention |
| Player job | I want the calm satisfaction of restoring order and seeing a garden improve |
| Product expression | Limited trays, readable sorting choices, visible garden restoration |
| Differentiator | A restoration fantasy that appears within the first playable minute |
| Monetization need | Extra tray, undo, or ad exchange after a legible space mistake |
| Production burden | New board patterns, restoration art, weekly tasks, event variants |
| Evidence required | Creative-to-first-session match, L1-L10 clarity, retry health, return reason |
| Kill condition | The core loop acquires attention but cannot produce comprehensible repeat play |

The memo forces the essential separation: a mechanic is an ingredient; a product is a coherent promise delivered repeatedly.

Publishers can supply valuable market intelligence and pre-built hypotheses. They may also steer a team toward categories they can acquire, operate, or cross-promote efficiently. That is rational portfolio management. An independent team should understand the difference between a publisher's portfolio fit and the team's own durable advantage.

### 28. Copy the Question, Not the Configuration

When a competitor succeeds, the reflex is to copy the visible answer: its theme, meta, store, event, or creative format. The more durable practice is to copy the question the product appears to have solved.

Royal Match invites a question about content cadence and long-term operational depth. Merge Mansion invites a question about how board pressure, narrative, and events create a return rhythm. A hybrid-casual hit invites a question about how a short core loop can carry a useful exchange without losing its speed. None asks for a replica.

The same principle protects teams from stale market data. By the time a mechanic becomes obvious in a benchmark report, many teams have already copied the surface. The opportunity shifts to execution quality, audience fit, production efficiency, and a better explanation of the player's desire.

Use market intelligence in three passes:

1. Screen out bad bets. Is there evidence that players engage with this general need, mechanic, and market?
2. Form a narrow hypothesis. Which player job, emotional loop, and execution advantage will make our version worth trying?
3. Learn from the cohort. Does observed behaviour support the hypothesis after novelty, source mix, and operational cost are considered?

The book's job is strongest in the second and third pass. Big data is strongest in the first.

### 29. Clear Garden: Turning a Publisher Prompt Into a Product Decision

Imagine that a publisher recommends an organizational puzzle with a cozy restoration theme, a collection layer, and fail-point offers. The recommendation is plausible. The question is whether the team can make it coherent.

For Clear Garden, the first build should not begin with five currencies and an event pass. It should prove four things:

```text
The creative promise of restoring order is visible in play.
The tray constraint creates readable planning rather than panic.
The garden changes enough to make completion feel tangible.
An extra tray or undo helps after a known mistake rather than covering a hidden rule.
```

If those conditions hold, the team has a product foundation. Collection, events, tickets, pricing, segmentation, and paid UA can be layered with more confidence. If they do not hold, the publisher's market map has still saved time by pointing to a testable territory. It has not removed the need to kill, revise, or find a different core feeling.

The hard value of this exercise is intellectual honesty. It prevents a team from using market evidence as a substitute for product judgement.

### Part VI Field Notes

Take one mechanic or theme recommended by a publisher, a competitor scan, or a market-data tool. Write two columns:

| The market evidence says | Our product thesis says |
| --- | --- |
|  |  |
|  |  |
|  |  |

If the second column remains vague, you have a direction to research, not a game to build.

## Part VII: The Operating System Behind a Live Game

### 30. Monetization Is a Supply Chain

The player sees one screen. The studio runs a supply chain.

Market intelligence shapes the bet. Prototyping tests the core loop. Level design produces reasons to play. Art, UI, audio, and performance determine whether the game feels trustworthy. Data and mediation determine whether the team can see and serve the player. QA, store operations, policy, localization, support, and live ops determine whether the product survives contact with the market.

Weak links show up as monetization problems. Slow builds slow experiments. Missing events weaken persistence. Thin QA creates purchase distrust. A poor creative pipeline makes UA expensive. Unreliable data turns debates into taste. These are operating failures with revenue consequences.

Create ownership around the journey rather than around isolated features. Someone owns early activation. Someone owns level health. Someone owns ad experience. Someone owns offer quality. Someone owns live-ops calendar. Someone owns the measurement contract. A single person can own more than one area in a small team. The decision rights must still be visible.

### 31. Market Research Must End in a Kill, Iterate, or Scale Decision

Market intelligence is useful when it changes allocation. A category chart is not a strategy.

Before a prototype becomes a project, write kill criteria that cover more than CPI. Include promise clarity, activation, early retention, production feasibility, content cost, creative volume, and the first believable monetization need. A game that acquires cheaply but cannot retain or support a scalable content loop is often a costly lesson.

AppMagic's casual and hybrid-casual reporting offers the right caution. Puzzle formats have produced substantial revenue, while success has been heavily concentrated and many recent launches have failed to break through. Use that evidence to narrow a thesis, not to declare a genre easy.

An early review should end in one of three verbs:

```text
Kill: the promise or loop has no credible path after evidence.
Iterate: a specific uncertainty can be tested within a defined time and cost.
Scale: the cohort evidence and operational capacity support more spend.
```

Anything else is usually a way to avoid choosing.

### 32. Live Ops Is Content Production With Memory

Live ops succeeds when each event has a role in a larger calendar. Some events teach. Some reactivate. Some give collectors a home. Some create a spend opportunity. Some provide recovery after a demanding period. The calendar should have a memory of what players saw, spent, and completed last week.

The content team needs a production system: reusable event components, economy rules, localization lead times, QA plans, segmentation, creative support, and post-event review. Without it, every event becomes a rush job and every result becomes hard to interpret.

Royal Match's widely reported content cadence offers a visible example of the production challenge. Sensor Tower's 2023 analysis noted roughly 200 new levels per month. The exact number is less important than the implication: durable puzzle performance requires content throughput and operational rhythm, not one successful board.

### 33. Contribution Economics Must Survive Contact With Scale

Revenue is gross. A business lives on what remains.

Review contribution economics by cohort:

```text
Gross revenue
- platform fees
- ad-tech and service costs
- UA spend
- content, support, and vendor cost allocated to the cohort
= contribution margin
```

Add payback period and cash timing. A campaign can look profitable on modeled lifetime value and still create a funding problem if the payback period is too long or retention is unstable. The finance model does not replace product judgement. It forces the same judgement to survive numbers.

### Part VII Field Notes

Draw your delivery chain from creative concept to player support. Mark the slowest handoff and the least trusted data source. Either one can be the bottleneck behind the next monetization debate.

## Part VIII: Genre Playbooks

### 34. Start With the Emotional Loop

Genre labels are a first filter. The emotional loop is the usable model.

| Category | Dominant feeling | Ads tend to fit when | IAP tends to fit when | Main risk |
| --- | --- | --- | --- | --- |
| Casual | Novelty, quick relief, playful surprise | At clear breakpoints | Convenience or remove ads has obvious value | Ad load exhausts a thin loop |
| Hybrid-casual | Fast core play with light progression | Utility extends a short loop | Meta, tickets, no-ads, targeted acceleration | Shallow meta fails to hold payer value |
| Puzzle | Mastery, order, clever recovery | A reward supports a legible decision | Tools solve known, fair bottlenecks | Pressure is mistaken for difficulty |
| Hybrid puzzle | Puzzle competence plus long-term investment | Exchanges support an event or meta goal | Progress, collection, pass, event acceleration | Content and economy outgrow the team |

#### Sort and organizational puzzles

The primary emotion is relief through order. Players often value undo, extra containers, temporary slots, and clear visual feedback. Rewarded ads can fit as a deliberate recovery tool. Interstitials placed during a thinking chain do disproportionate damage because they break the very concentration the genre sells.

#### Jam, parking, and space-pressure puzzles

The primary emotion is controlled panic followed by release. Slot scarcity and sequencing are the product. Continue offers can fit after a readable near miss. The guardrail is strict: the player must understand why space ran out and see a possible different route.

#### Physics and fail-fun games

The primary emotion is curiosity and fast retry. Tool utility and quick replay matter more than deep catalogues. Do not bury the loop under slow offers or long ad breaks. A physics failure can be funny. A slow restart turns it into a complaint.

#### Match-3 and match-2

The primary emotion is mastery inside a long progression system. Boosters, lives, construction or collection meta, events, and a deep content calendar can all make sense. They require more economy discipline and content capacity than a lightweight casual loop. The reward must preserve the player's belief that skill and planning still matter.

### 35. A Category Example Is Evidence, Not a Blueprint

Royal Match, Candy Crush Saga, Merge Mansion, and a successful hybrid-casual puzzle can teach different lessons. None gives you permission to clone an economy or a funnel from public observation.

Use public data for scale, market movement, visible feature cadence, and strategic context. Use your own data for level tuning, product timing, segmentation, price, and the causal effects of a change. Public numbers are anchors. Your cohort is the decision-maker.

### Part VIII Field Notes

Write the sentence your game is selling emotionally. Then write the product decisions that protect it.

```text
Our game sells the feeling of ________.
An ad is acceptable when ________.
A purchase is acceptable when ________.
A level has gone too far when ________.
Our return loop strengthens the feeling by ________.
```

## Part IX: The Audit

### 36. The Thirty-Minute Monetization Audit

Run this on a live game, a competitor build, or your soft-launch candidate. Do not start with the store.

#### Minutes 0-5: Promise

- Watch three current creatives with no sound, then with sound.
- Name the emotion each one sells.
- Compare the promise with the first playable minute.
- Note every consent, login, notification, or tracking request.

#### Minutes 5-10: First-session contract

- Play the first ten levels.
- Mark the first moment of real control, real success, real failure, and real choice.
- Record every interruption.
- Ask whether each loss is explainable without a booster.

#### Minutes 10-15: Ad exchange

- Find the first rewarded ad and first interstitial.
- State the value before and after each ad.
- Check whether a player can decline without losing normal play.
- Write the guardrail metric for each placement.

#### Minutes 15-20: Offer and economy

- Open the store after a natural need appears.
- Name the job of every visible product.
- Check price clarity, reward delivery, restore purchase, and remove-ads scope.
- Identify one source and one sink for each important currency.

#### Minutes 20-25: Return and event

- Find the next reason to return.
- Inspect the active event's earn, spend, milestone, and deadline loop.
- Ask whether the event supports the core game or merely interrupts it.

#### Minutes 25-30: Evidence

- Open the cohort dashboard.
- Compare revenue with retention, difficulty, exposure, reviews, and refunds.
- Choose one leak in trust and one leak in value.
- Write one experiment. Give it a rollback condition.

### 37. Definition of Done

A monetization system is ready for more scale when the following statements are true:

- The creative promise appears in the early product experience.
- The player can explain their first meaningful loss and their options after it.
- Rewarded ads provide a clear voluntary exchange.
- Interstitials respect natural rest points and purchase states.
- Every offer solves a named player need.
- Currency sources and sinks create decisions rather than tolls.
- Revenue is reviewed with retention, reviews, refunds, and support.
- The team can test, roll back, and preserve learning at a useful pace.
- Content and live-ops plans match the promise made to acquired players.
- The financial model includes the cost of keeping the game healthy.

No game clears this list once and stays clear. A live game changes each week. The list is a discipline for noticing when the player relationship has changed before the revenue chart makes the problem impossible to ignore.

## Closing: The Player Must Want to Continue

The useful question is never "How can we make this player spend?" It is "What value has the player just earned, what tension do they now feel, and what choice would they consider fair?"

Profit comes from the answers, repeated across a system that can keep its word.

Good monetization leaves the player with a reason to continue after the ad, after the offer, after the purchase. The game may still challenge them. It may still ask for time. It may still charge money. The relationship remains intact because the player can see the value, the rule, and the choice.

That is the standard worth operating toward.

## Research Notes and Public Sources

The sources below are used for market context and public case notes. Product-level data, particularly private funnels and configurations, should never be inferred from public estimates alone.

- [Sensor Tower: Royal Match surpasses Candy Crush Saga](https://sensortower.com/blog/royal-match-surpasses-candy-crush-saga-in-revenue-and-downloads-for-the)
- [Sensor Tower: Global mobile games market outlook](https://sensortower.com/blog/state-of-mobile-games-market-outlook-2024-report)
- [Sensor Tower: U.S. mobile puzzle game analysis](https://sensortower.com/blog/us-mobile-puzzle-game-analysis-2022)
- [AppMagic / GameDev Reports: Mobile Casual Games in H1 2025](https://gamedevreports.substack.com/p/appmagic-mobile-casual-games-in-h125)
- [AppMagic / GameDev Reports: Top hybrid-casual games in Q2 2025](https://gamedevreports.substack.com/p/appmagic-top-10-hybrid-casual-games)
- [AppMagic: Epic Plane Evolution case study](https://appmagic.rocks/blog/epic-plane)
- [AppMagic: Casual LiveOps Report H1 2025](https://appmagic.rocks/files/img-blog/Casual_LiveOps_Report_H1_2025.pdf)
- [PocketGamer.biz: Royal Match and match-3 revenue](https://www.pocketgamer.biz/royal-match-earned-51-of-all-match-3-revenue-in-2024/)
- [GameRefinery: Mobile game intelligence platform](https://www.gamerefinery.com/)
- [GameRefinery: Prototype audience forecasting](https://docs.gamerefinery.com/en/articles/6618475-who-would-be-my-prototypes-users)
- [GameAnalytics: The limits and value of benchmarking](https://www.gameanalytics.com/blog/the-power-of-benchmarking-in-your-game)
- [Unity: Monetization strategy](https://docs.unity.com/en-us/monetization/getting-started/monetization-strategy)
- [Unity: Rewarded ads, IAP, retention, and engagement](https://unity.com/kr/blog/understanding-the-impact-of-rewarded-ads-on-iap-retention-and-engagement)
- [Rovio: Beacon operating platform](https://www.rovio.com/articles/beacon-by-rovio-the-games-platform/)
- [Rovio: Analytics and player experience](https://www.rovio.com/articles/using-data-to-improve-player-experience-insights-from-rovios-game-analytics/)
- [Rovio: Tailoring FTUE with UA data](https://www.rovio.com/articles/using-beacon-and-ua-data-to-tailor-ftue-in-rovio-games/)
- [King: Data, Analytics, and Strategy](https://careers.king.com/us/en/data%2C-analytics-strategy-page)
- [Supercell: What We Have Learned from Failures](https://supercell.com/en/news/learning-from-failures/)
- [Apple: App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency)
- [Apple: User privacy and data use](https://developer.apple.com/app-store/user-privacy-and-data-use/)
- [FTC: Epic Games settlement announcement](https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations)
- [FTC: Digital dark patterns guidance](https://search.ftc.gov/business-guidance/blog/2022/12/245-million-ftc-settlement-alleges-fortnite-owner-epic-games-used-digital-dark-patterns-charge)
- [King 2015 SEC filing](https://www.sec.gov/Archives/edgar/data/1580732/000156459015004363/king-6k_20150331.htm)
- [Microsoft 2024 Annual Report](https://www.microsoft.com/investor/reports/ar24/)
