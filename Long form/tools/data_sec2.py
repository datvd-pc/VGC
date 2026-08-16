"""
Module containing English text and data for Part II: From Creative to First Return.
"""

SEC2_PART2 = {
    "part_title": "Part II: From Creative to First Return",
    "chapter5": {
        "title": "5. Creative Sells a Feeling",
        "paragraphs": [
            "Nobody installs a mobile game because they're eager to examine an economy balance sheet or browse a monetization matrix. They install it because the ad promised a very specific emotional state: the deep satisfaction of sorting chaos into order, the adrenaline rush of a rescue puzzle, or the crisp triumph of conquering a fair challenge.",
            "The commercial touchpoint of an ad creative isn't its click-through rate (CTR) or a vanity low Cost Per Install (CPI) on a spreadsheet. It is the specific feeling that attracted the player in the first place, and whether the first five minutes of gameplay actually deliver on that emotional promise. A bait-and-switch ad might generate dirt-cheap installs today, but the invoice arrives immediately: rampant early churn, 1-star reviews, and a completely decimated Day 1 retention rate.",
            "The psychology behind this rests on Expectancy-Disconfirmation Theory (Oliver, 1980) and Self-Discrepancy Theory (Higgins, 1987). When there is a jarring gap between what marketing promised and what the software delivers, human psychology reacts with immediate disappointment and defensive withdrawal. This doesn't mean creative experimentation is useless. But it establishes an unbending rule: the wider the chasm between your ad promise and your first ten levels, the faster you incinerate your player's initial trust budget.",
            "Take your top three user-acquisition creatives and put them side-by-side with the first three minutes of your actual gameplay. Does the player immediately recognize the mechanic they just watched in the ad? Do they experience the exact same emotional payoff? If the answer is no, your team isn't just wasting marketing budget—you're actively sabotaging your conversion funnel before players even know your store exists."
        ]
    },
    "chapter6": {
        "title": "6. Store Listing and First Open",
        "paragraphs": [
            "Your app store listing is where players double-check your marketing claims, and that very first app launch is where they pass their final verdict.",
            "Track a cohort from your best-performing ad creative through three critical milestones: the ad-to-store conversion rate, the install rate, and their first sequence of taps after opening the app. If an ad promotes a clean, relaxing sorting puzzle, but the store page showcases an elaborate mansion-building meta-game, you've forced the player to reconcile two conflicting narratives before they've even touched level one. If the first launch immediately ambushes them with login dialogs, privacy disclaimers, push notification prompts, and leaderboard pop-ups, the question isn't 'which prompt converts better.' The real question is: Did the player experience the value they came for before you started making aggressive demands on their attention?",
            "The cognitive science foundation here is John Sweller's Cognitive Load Theory (1988). Sweller differentiates between the intrinsic cognitive load required to master a task and the extraneous load caused by clumsy, cluttered presentation. Research on worked examples (Sweller, Chen, Retnowati & Kalyuga, 2020) proves that novices learn significantly faster when their attention is strictly focused on core structural patterns. In the first few minutes, every pop-up that doesn't directly validate your core promise is actively competing with the player's cognitive bandwidth and dwindling patience.",
            "Design the first-open experience as a rapid sequence of undeniable proof. If your ad promised a high-stakes rescue scenario, the player's very first interaction should be solving that exact rescue scenario—not navigating a bloated main menu. If your ad promised tactile sorting bliss, let them immediately clear a messy board, enjoy the crisp visual feedback, and only then introduce the next objective. Once that initial micro-victory is secured, you've earned the right to offer a meaningful choice—like an opt-in rewarded ad for extra moves or a well-timed starter pack. A/B test these interaction timings against tutorial completion, D1 retention, permission opt-in rates, and user sentiment.",
            "Compliance requirements like Apple's App Tracking Transparency (ATT) or privacy consents are non-negotiable. The difference lies in timing and context: Does the player understand why you're asking for permission in relation to the fun they just experienced? Treat your store listing as the promise, the first launch as the proof, and permission prompts as requests you only trigger once you've delivered tangible value. Once that initial trust is cemented, the first ten levels must answer the next existential question: Does your game teach players how to win, how to accept failure, and how to use monetization options fairly?"
        ]
    },
    "chapter7": {
        "title": "7. The First Ten Levels",
        "paragraphs": [
            "Open the first ten levels of your current build and lay them alongside their raw telemetry event logs. With each passing level, did the player actually learn a new rule, gain greater tactical agency, or did they simply slam into artificial roadblocks? Did they receive their first booster before or after they understood how it alters the board state? Was your first in-game offer triggered by an organic, relatable bottleneck that they just experienced?",
            "These questions form the economic bedrock of your early game: a commercial offer only holds perceived value if the player clearly understands the specific headache it solves. Otherwise, any initial conversion is merely an emotional reaction to artificial frustration, and the real cost will show up as early abandonment, plummeting retry rates, and angry store reviews.",
            "Cognitive Load Theory offers a vital operational rule: new players require clear visual scaffolding to build an internal mental model of the game, after which that scaffolding must fade so they can apply their skills independently. In puzzle games, guidance doesn't mean walls of tutorial text. It means a compact board, an unmistakable visual objective, a subtle ghosted hint, and immediate feedback on their choices. Ask yourself: Is this level illuminating a mechanic, or is it overloading the player with too many variables before they've even grasped the basics?",
            "A best-in-class onboarding ramp moves from an intuitive guided demonstration, to a similar puzzle with less hand-holding, to that first genuine fail state where the player completely understands why they lost. During level design reviews, evaluate four core criteria for every stage: What is the player learning? Which decision triggers a win or a loss? What free tactical alternative remains after a defeat? And does a booster expand strategic freedom or merely patch up sloppy level tuning? Track fail rates alongside retry rates, level progression velocity, booster usage, and hard churn. A high fail rate paired with high retries indicates an addictive, well-balanced challenge; a high fail rate paired with instant app quits is a code-red warning sign that your level design is broken."
        ]
    },
    "chapter8": {
        "title": "8. The First Return",
        "paragraphs": [
            "Before your team spends hours drafting clever push notification copy, pull up the cohort of players who closed your app after their very first session and ask: At the exact moment they exited, what unfinished goal were they excited to complete next?",
            "If your team cannot point to a concrete, cliffhanger objective inside the game, then your push notification is nothing more than spam begging them to return to a void. This is the financial reality of the first return: Day 1 retention unlocks every downstream opportunity—rewarded ads, progression offers, live events, and long-term monetization. It cannot be compensated for by sending a notification at 7:00 PM on schedule.",
            "The behavioral mechanism here is the Goal-Gradient Hypothesis (Hull, 1932; empirically validated by Kivetz, Urminsky & Zheng, 2006): human effort, motivation, and velocity accelerate dramatically as people perceive themselves closing in on a finish line. Seeing the goalpost within reach triggers an instinctual urge to re-engage. This raises an essential product question: Is the in-game goal concrete enough? Is the remaining progress visually obvious? And is the pending reward enticing enough to compel the player to reopen the game tomorrow to claim it?",
            "An effective return hook doesn't have to rely on artificial energy meters, daily login checklists, or countdown timers. It could be an enticing new garden area just waiting to be unlocked, a card album missing one final piece, a construction project one step from completion, or a tricky puzzle where the player figured out the solution right as their previous session ended. The golden rule is that players must know exactly why they are coming back. Run an A/B split: Group A exits after claiming a generic reward popup; Group B exits while looking at a tantalizing, nearly completed milestone. Compare D1 retention, session frequency, and first-offer conversions to let real player behavior guide your design.",
            "Energy systems only provide real value when they serve as rhythm modulators—such as limiting attempts in a competitive event, enforcing strategic stakes, or protecting long-term content pacing. Once the first return is secured, the challenge evolves: With every return session, does the player experience meaningful progress? Part III dives deep into the architecture of meaningful progression, balanced pressure, and unwavering fairness."
        ]
    },
    "decision_board": {
        "title": "Decision Board | Part II: From Creative to First Return",
        "intro": "Part III examines the quality of player progression, psychological pressure, and design fairness—the bedrock conditions that transform initial return sessions into sustainable, long-term commercial value.",
        "table": {
            "headers": ["DO THIS NOW", "ASK BEFORE DECIDING"],
            "rows": [
                [
                    "• Map the Promise Chain: Creative ➔ Store Listing ➔ First 3 Minutes; flag every emotional discrepancy.\n• Audit your First 10 Levels: Record player mastery, win/loss clarity, and free non-monetized options after failure.\n• A/B Test Session Endings: Compare exiting after a generic reward versus exiting on a visible, unfinished milestone.",
                    "• Did the player experience the core promise before being prompted for permissions or ads?\n• Does the early game teach mastery and autonomy, or does it merely force players through artificial hurdles?\n• When a player exits, do they know the exact objective they will return to complete tomorrow?"
                ],
                [
                    "CORE TAKEAWAYS:\n• The ad creative buys the install but simultaneously sets the ceiling for FTUE, D1 retention, and LTV.\n• Premature permission dialogs compete directly with a new player's limited cognitive bandwidth.\n• A tangible, unfinished in-game goal drives retention far more effectively than any push notification.",
                    "TEAM MEETING AGENDA (45 mins):\n• Attendees: Game Design, UA Creative Lead, Data Analyst, Product Lead.\n• Bring: Top 3 UA video creatives, screen recordings of Levels 1–10, FTUE funnel data, and D1 by creative cohort.\n• Target Outcome: Identify one creative-gameplay mismatch to fix immediately, test permission re-timing, and assign owners."
                ]
            ]
        }
    }
}
print("Part 2 module loaded.")
