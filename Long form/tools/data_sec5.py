"""
Module containing English text and data for Part V: Signals, Decisions, and Experiments.
"""

SEC5_PART5 = {
    "part_title": "Part V: Signals, Decisions, and Experiments",
    "chapter21": {
        "title": "21. Reading the Dashboard",
        "paragraphs": [
            "Never open an analytics dashboard just to admire pretty line charts. Approach your data with a blunt, hypothesis-driven product question: 'Is the creative promise holding true through the first ten levels?', 'Are players churning abnormally at our new interstitial placement?', or 'Is this new starter pack generating healthy revenue or quietly destroying the D7 retention of new cohorts?'"
        ],
        "table_diagnostic": {
            "headers": ["Diagnostic Question", "Paired Metrics to Read Together", "Immediate Verification Action"],
            "rows": [
                ["Is the core promise holding true?", "CTR, Store Conversion Rate, FTUE Completion Rate, D1 by Creative Cohort", "Compare the UA video ad, store listing, and the first 3 minutes of gameplay across cohorts."],
                ["Is the first fail state fair?", "Fail Rate, Retry Rate, Session Drop-off Rate, Booster Usage Frequency, Store Reviews", "Watch actual gameplay recordings; distinguish between a thrilling challenge and unfair frustration."],
                ["Does this ad placement add real value?", "Opt-in Rate, IMPDAU, Video Completion Rate, Post-Ad Quit Rate, D1 Retention", "A/B test placement triggers or timing while keeping the reward constant to measure player appetite."],
                ["Does this IAP solve an authentic need?", "Offer Impressions, Conversion Rate, Non-Buyer Retention, Refund Rate, Repeat Payer Rate", "Audit offer transparency, perceived value, and the gameplay experience when players decline to buy."]
            ]
        },
        "paragraphs_between_tables": [
            "A dashboard tracking 500 uncurated metrics without an action plan is just vanity noise. Data only provides real leverage when it reflects the psychological health of the relationship between player and game, pointing directly to where the team needs to intervene."
        ],
        "table_strategic": {
            "headers": ["Diagnostic Domain", "Critical Strategic Metric", "Core Strategic Decision Question"],
            "rows": [
                ["User Acquisition", "CTR, IPM, CPI, Store Page Conversion Rate", "Is the marketing creative attracting the right audience for the actual game?"],
                ["Activation & FTUE", "Load Time, Crash Rate, Tutorial Completion, Levels 1–10 Velocity", "Does the game prove its core promise fast enough to earn trust?"],
                ["Engagement", "Session Count, Session Length, Retry Rate, D1/D3/D7 Retention", "Does the core loop create a compelling reason for players to return?"],
                ["Difficulty Balance", "Level Fail Rate, Churn on Loss, Booster Burn Velocity", "Is game pressure acting as a motivator or an infuriating paywall?"],
                ["Advertising Health", "Rewarded Opt-in Rate, IMPDAU, Post-Ad Drop-off Rate", "Are ad placements structured as helpful, fair value exchanges?"],
                ["IAP & Monetization", "Offer Views, Conversion Rate, Repeat Payer Rate, Refund Volume", "Is the game maintaining long-term economy integrity and buyer trust?"],
                ["Community Trust", "Star Rating, App Store Review Sentiment, Support Ticket Volume", "Is the studio's long-term relationship with its audience strengthening or eroding?"]
            ]
        },
        "paragraphs_after_strategic": [
            "The methodological foundation here is Causal Inference: an observational data point on a dashboard never explains its own root cause. To understand what is actually happening, the team must construct a logical causal hypothesis and test it against cohort-segmented behavior.",
            "Make hypothesis-driven data reviews an unbreakable studio habit: turn every metric review into a rigorous debate about the player experience, culminating in concrete, testable adjustments."
        ]
    },
    "chapter22": {
        "title": "22. Read Metric Pairs",
        "paragraphs": [
            "Never read a growth metric in isolation. Every single change you make to a game creates a double-edged sword: an upward spike in one metric usually carries the risk of damaging another. If you only look at one side of the ledger, you're living in a dangerous fantasy world."
        ],
        "table": {
            "headers": ["Short-Term Growth Metric", "Mandatory Paired Counter-Metric", "Underlying Diagnostic Question"],
            "rows": [
                ["CTR (Ad Click-Through Rate)", "Store Conversion Rate, D1 Retention, Session Depth", "Is the creative attracting genuinely interested players or clickbaiting unqualified traffic?"],
                ["Short-Term IAP Revenue", "D7/D30 Retention, App Store Ratings, Refund Rate", "Did this bundle deliver authentic value or exploit temporary player frustration?"],
                ["IMPDAU (Ad Impressions / User)", "Average Session Duration, Churn Rate", "Is this ad frequency supporting gameplay or violently destroying flow?"],
                ["Level Pass Rate", "Booster Usage Rate, Post-Loss Retry Rate", "Are players conquering the level through mastery or being forced to buy a way out?"],
                ["Live Event Revenue", "Post-Event D7 Retention, Post-Event Wallet Balances", "Did the event create new engagement or merely borrow future spend from next week?"]
            ]
        },
        "paragraphs_after_table": [
            "Always evaluate your game through Paired Metrics:",
            "• Average Revenue Per Daily Active User (ARPDAU) must be read alongside Day 7 Retention (D7).",
            "• IAP Conversion Rate must be read alongside App Store Ratings and Refund Rates.",
            "• Average Ad Impressions (IMPDAU) must be read alongside Session Length and Churn Rates.",
            "• Cost Per Install (CPI) must be read alongside FTUE Completion and Realized LTV."
        ]
    },
    "chapter23": {
        "title": "23. Decision Trees",
        "paragraphs": [
            "When Day 1 retention stumbles, the default knee-jerk reaction in many studios is to immediately slash level difficulty or shower players with free currency. Yet the real culprit might be that your top UA ad is promising an entirely different genre, or that an aggressive iOS tracking permission prompt is firing on the splash screen and killing momentum.",
            "If D1 is solid but D3 and D7 take a nosedive, look elsewhere: check for a lack of day-two return hooks, an artificial difficulty wall, excessive interstitial ad frequency, or a repetitive lack of content in the second session. A Decision Tree forces your team to systematically trace root causes through logical diagnostic branches instead of spraying emotional guesses at the problem.",
            "Standardize your studio's diagnostic workflow:",
            "Observe the Symptom ➔ Formulate Causal Hypotheses ➔ Verify with Paired Cohort Telemetry ➔ Deploy a Controlled Intervention.",
            "The output of a decision tree must always be a falsifiable hypothesis, a single designated owner, and a clear measurement timeframe. When data is inconclusive, having the discipline to say 'we don't know yet' and digging deeper is infinitely better than blindly burning capital on user acquisition."
        ]
    },
    "chapter24": {
        "title": "24. Experimentation",
        "paragraphs": [
            "A/B testing is the ultimate scientific engine for product optimization. But experimentation quickly degenerates into an expensive circus if a team modifies five variables at once or launches tests without an explicit causal hypothesis."
        ],
        "table": {
            "headers": ["Before You Ship", "Proceed Only When"],
            "rows": [
                ["Clear Hypothesis", "You have articulated the exact behavioral mechanism and the minimal viable change required to test it."],
                ["Metric Alignment", "You have locked in a primary metric, guardrail counter-metrics, and a cohort-based evaluation framework."],
                ["Decision Protocol", "You have pre-committed in writing to your keep, iterate, rollback, or kill thresholds before seeing the data."],
                ["Team Memory", "You have assigned a single DRI (Directly Responsible Individual) and logged the test context in a shared repo so mistakes aren't repeated."]
            ]
        },
        "paragraphs_after_table": [
            "A professional experiment must meet four strict criteria: a clear causal hypothesis, sufficient sample size to reach statistical significance, rigid guardrail metrics to safeguard overall player experience, and an instantaneous rollback protocol if the variant harms retention.",
            "Maintain a structured repository of test debriefs: the lessons extracted from a failed experiment frequently provide far more strategic value than an unexplainable short-term revenue bump.",
            "Remote configuration tools give you incredible operational flexibility to deploy and toggle features on the fly, but they will never compensate for sloppy experimental design."
        ]
    },
    "decision_board": {
        "title": "Decision Board | Part V: Signals, Decisions, and Experiments",
        "intro": "Part VI explores an essential strategic frontier: where market intelligence and algorithmic tools can accelerate your team, and the absolute boundaries where data will never replace human product judgment.",
        "table": {
            "headers": ["DO THIS NOW", "ASK BEFORE DECIDING"],
            "rows": [
                [
                    "• Configure dashboards strictly by Paired Metrics (ARPDAU alongside D7 Retention; IMPDAU alongside Churn Rate).\n• Build diagnostic decision trees to isolate the root cause whenever D1 or D7 retention experiences volatility.\n• Standardize your A/B testing workflow: define explicit causal hypotheses, guardrail metrics, and rollback plans.",
                    "• Is this short-term metric gain quietly destroying player trust and long-term retention?\n• What behavioral mechanism explains this trend, and what specific evidence would disprove our hypothesis?\n• Does this experiment eliminate a critical strategic uncertainty, or is it merely random feature tweaking?"
                ],
                [
                    "CORE TAKEAWAYS:\n• A metric is only meaningful when balanced against the hidden cost incurred to achieve it.\n• Telemetry tracks superficial actions; empathy and causal logic uncover the root truth.\n• Admitting 'we don't know yet' is always better than scaling spend on shaky assumptions.",
                    "TEAM MEETING AGENDA (45 mins):\n• Attendees: Head of Product, Data Lead, UA Lead, LiveOps Lead.\n• Bring: Paired metrics dashboard, cohort retention curves, and active A/B test results.\n• Target Outcome: Make definitive ship/rollback decisions on active tests based strictly on guardrail metrics."
                ]
            ]
        }
    }
}
print("Part 5 module loaded.")
