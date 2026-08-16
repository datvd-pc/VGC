"""
Module containing English text and data for Part IV: Ads, IAP, and Economy.
"""

SEC4_PART4 = {
    "part_title": "Part IV: Ads, IAP, and Economy",
    "chapter15": {
        "title": "15. Rewarded Ads",
        "paragraphs": [
            "A rewarded ad is an explicit, voluntary contract between the player and the game: the player trades 30 seconds of their attention in exchange for an immediate, tangible in-game benefit. At its core, a rewarded ad is not a forced commercial disruption—it is a well-timed, player-driven utility.",
            "Architect every rewarded ad placement around an unmistakable value exchange: 'After facing situation X, the player can voluntarily watch an ad to receive benefit Y, which directly solves their immediate hurdle.' If the reward is insulting or completely disconnected from the player's immediate goal, they will ignore it; if the reward is so ridiculously overpowered that it collapses your entire game economy, players will lose all motivation to solve puzzles skillfully or ever consider an in-app purchase."
        ],
        "table": {
            "headers": ["Player Need", "Value Exchange", "Guardrail Condition"],
            "rows": [
                ["Extend Session", "Extra moves or an instant revive after a near-miss", "Never used to patch artificial, hidden difficulty walls."],
                ["Preserve Rewards", "Double earned soft currency or event tokens", "Base rewards must remain meaningful without the multiplier."],
                ["Test Power-ups", "Free trial of a premium booster on a tricky board", "Clearly explain what happens after the single-use trial ends."],
                ["Reduce Wait Times", "Instant partial energy refill or speed-up", "Core game loop must never be fully paywalled."]
            ]
        },
        "paragraphs_after_table": [
            "There is no universal 'ideal' rewarded ad opt-in benchmark that fits every genre. Audit your placements against your own empirical telemetry: opt-in engagement rate, average daily impressions per active user, video completion rate, and most importantly, retention curves following reward claims. Ensure that rewards are granted accurately, instantly, and reliably.",
            "When rewarded ads are built as a fair, dignified lifeline, they don't just protect retention—they actively deepen player goodwill toward your game."
        ]
    },
    "chapter16": {
        "title": "16. Interstitials",
        "paragraphs": [
            "Interstitial ads are the most aggressive, high-risk format in mobile gaming. When dropped without warning while a player is deep in strategic thought, or immediately after an infuriating loss, an interstitial triggers instant visceral rage and sparks immediate uninstalls. The monetization equation of an interstitial demands extreme caution: the micro-cents generated from an ill-timed impression will never compensate for the lost Lifetime Value (LTV) of a churned player.",
            "Research on cognitive distraction (Stothart, Mitchum & Yehnert, 2015) proves that even brief, jarring interruptions completely derail human working memory and flow. Consequently, the only defensible placement for an interstitial is at natural psychological breakpoints—such as immediately after completing a stage, claiming final victory rewards, and transitioning to a new world map.",
            "Enforce strict operational guardrails: implement aggressive frequency capping, never trigger interstitials during the first few onboarding levels, automatically purge all forced interstitials for any user who purchases an IAP, and always provide a prominent, responsive close button. Always monitor IMPDAU side-by-side with D1/D7 retention to catch early signs of player fatigue."
        ]
    },
    "chapter17": {
        "title": "17. Boosters",
        "paragraphs": [
            "A booster is a precision tactical tool that empowers the player to influence the board state—clearing a stubborn obstacle, shuffling impossible tiles, or adding crucial extra moves. A well-designed booster makes the player feel clever and in command of their strategy. Conversely, if a level is engineered so unfairly that victory is mathematically impossible without burning a booster, that booster ceases to be a strategic tool—it becomes an extortion fee that strips away all satisfaction of winning.",
            "Examine booster consumption data level-by-level: if a specific stage exhibits a massive spike in booster usage paired with a surge in player churn, that level is broken—players aren't thrilled to spend; they're quitting in frustration. Forcing booster burn through unfair difficulty quickly depletes a player's resource reserves and pushes them into an insurmountable dead end.",
            "Position boosters as creative expansions of tactical freedom. Ensure a steady, baseline trickle of free boosters through progression milestones and live events so players can experience their power before deciding to buy more in the store."
        ]
    },
    "chapter18": {
        "title": "18. IAP and Present Need",
        "paragraphs": [
            "An in-game shop is a static catalog. A contextual offer is an urgent solution presented at the exact moment a player encounters a pressing problem. Players don't open their wallets because a shop interface is pretty; they spend because they are facing an immediate obstacle and your offer provides an honest, compelling, and reasonably priced resolution.",
            "Generic bundles filled with abstract virtual currencies only appeal to deeply engaged veterans who already have a master's degree in your game's economy. For everyone else, offers tied directly to real-time context—such as a last-second rescue offer on a near-miss, a high-value Starter Pack bundled with permanent ad removal, or an event-themed progression bundle—generate significantly higher conversion rates and far greater customer satisfaction."
        ],
        "table": {
            "headers": ["Product SKU", "Legitimate Operational Purpose", "Predatory Failure Mode"],
            "rows": [
                ["Remove-Ads Bundle", "Protects gameplay flow for dedicated players", "Vague terms that still force banner or event ads."],
                ["Starter Pack", "Delivers an exciting early-game power surge", "Pushed aggressively before the core loop proves its fun."],
                ["Piggy Bank Vault", "Converts accumulated progress into an optional purchase", "Deliberately starves the base economy to force bank unlocks."],
                ["Continue Offer", "Saves a high-stakes, hard-fought run on a near-miss", "Appears after an incomprehensible, unfair defeat."],
                ["Battle / Season Pass", "Celebrates and rewards long-term engagement", "Content cadence is too slow to support the pass track."]
            ]
        },
        "paragraphs_after_table": [
            "Ensure every IAP offer explicitly communicates three things: exactly what the player gets, the concrete problem those items solve, and a frictionless, guilt-free decline button that never makes the player feel like a second-class citizen.",
            "Commercial transparency and respect during checkout are the golden keys that turn free-to-play users into loyal, repeat payers throughout the life of your game."
        ]
    },
    "chapter19": {
        "title": "19. Economy Integrity",
        "paragraphs": [
            "The in-game economy is the circulatory system that pumps resources and currencies through your game. A resilient economy obeys the physical laws of Stock-and-Flow balance: every currency must have tightly regulated sources (faucets), compelling sinks (drains), and maintain a healthy median wallet balance so players always have a hunger to engage with live events and features.",
            "Currency inflation is the silent killer of mobile games: when a game showers players with soft currency without providing irresistible sinks, the currency becomes worthless. Future event rewards lose all psychological value, and in-game shop bundles become irrelevant. On the flip side, an economy choked by extreme scarcity leaves players feeling exhausted and triggers mass abandonment.",
            "Regularly audit core economic health across player cohorts: track median wallet balances, accumulation velocity, sink distribution, and spending allocation across product categories. Protecting your economy's integrity is protecting the very soul of your game."
        ]
    },
    "chapter20": {
        "title": "20. Event Economy",
        "paragraphs": [
            "Live events and battle passes exist to rejuvenate the core rhythm, establish high-energy short-term goals, and cultivate community momentum.",
            "A masterclass live event is a self-contained, virtuous loop:",
            "Engage in Core Gameplay ➔ Accumulate Event Tokens ➔ Unlock Tiered Choices ➔ Climb Leaderboards ➔ Cross Finish Line ➔ Claim Milestone Rewards.",
            "According to Sensor Tower estimates, Royal Match consistently generates over $100 million in gross monthly revenue by seamlessly rotating high-cadence live events like the Royal Pass and Hidden Temple alongside an relentless content rollout. This data proves the power of live ops; however, the lesson isn't to blindly copy their calendar. The real insight is understanding how they tier objectives: free-to-play users always have an achievable milestone path, while the premium pass offers massive acceleration for invested spenders.",
            "During post-event post-mortems, isolate event-driven revenue from downstream health: check post-event D1/D7 retention, post-event currency balances, return rates the following week, and community sentiment. Ensure the event left players energized—not completely burned out and financially drained."
        ]
    },
    "decision_board": {
        "title": "Decision Board | Part IV: Ads, IAP, and Economy",
        "intro": "Part V shifts focus from product design mechanics to data-driven decision frameworks: dashboard diagnostics, paired metric analysis, and rigorous experimentation protocols to avoid being deceived by vanity metrics.",
        "table": {
            "headers": ["DO THIS NOW", "ASK BEFORE DECIDING"],
            "rows": [
                [
                    "• Map all rewarded and interstitial ad placements: specify triggers, reward values, natural breakpoints, and frequency caps.\n• Implement an automatic rule that permanently disables all forced interstitials for any user who purchases an IAP.\n• Build a Stock-and-Flow balance sheet: monitor median currency balances and sink consumption velocity by cohort.",
                    "• Is this ad placement supporting player flow or violently interrupting their focus?\n• Does this IAP bundle solve an authentic player problem, or is it an artificial attempt to hit studio revenue KPIs?\n• After this live event concludes, will the base economy suffer from inflation, and will players still want to return?"
                ],
                [
                    "CORE TAKEAWAYS:\n• High ad impressions or conversion rates do not prove long-term value creation or player retention.\n• Boosters are tactical expansion tools, not structural bandages for poor level design.\n• A successful event leaves players feeling satisfied and eager for the next chapter.",
                    "TEAM MEETING AGENDA (60 mins):\n• Attendees: Product Lead, Monetization Lead, Economy Designer, LiveOps Manager.\n• Bring: Ad placement performance reports, IAP conversion funnels, currency inflation tracking, and the live event calendar.\n• Target Outcome: Rebalance underperforming offers, optimize rewarded ad placements, and finalize event economy parameters."
                ]
            ]
        }
    }
}
print("Part 4 module loaded.")
