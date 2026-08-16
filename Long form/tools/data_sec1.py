"""
Module containing English text and data for Part I: The System Behind the Store.
"""

SEC1_PART1 = {
    "part_title": "Part I: The System Behind the Store",
    "chapter1": {
        "title": "1. Trust Budget",
        "paragraphs": [
            "In March 2023, the Federal Trade Commission (FTC) finalized a $245 million settlement requiring Epic Games to refund consumers following allegations of dark patterns, deceptive UI tricks, and unintended in-game purchases in Fortnite. By December 2024, the FTC reported distributing over $72 million in initial refunds. This wasn't an academic lecture on retention, LTV, or commercial efficiency. It was a massive public invoice proving the real cost of letting monetization flows obscure what players are actually agreeing to.",
            "This case doesn't reveal Fortnite's exact internal economy math, nor does it pin the blame entirely on a single screen. But it exposes an undeniable truth: the payment flow does not sit outside the game experience. It is an inseparable part of the promise your game makes to the player.",
            "Instead of asking only whether a store screen converts well, ask the harder questions: Does the player understand this choice? Did they have enough time to consider it? And will they still trust the game after the transaction completes? That is the genesis of the Trust Budget.",
            "Every new player arrives with a finite amount of trust. An overpromising creative, a sluggish loading screen, a pushy tutorial, or a hidden close button burns down that reserve. A level that feels blatantly rigged—followed by an immediate booster offer—erodes trust even faster, because the player immediately questions whether the game engineered their failure.",
            "Trust isn't built in dramatic, grand gestures. It is earned through unglamorous, everyday details: crystal-clear objectives, intuitive rules, controls that perform exactly as promised, rewards delivered instantly, transparent pricing, and responsive customer support when an in-game transaction hiccups.",
            "The sum total of these details dictates whether a player sees a rewarded ad as a fair exchange or views your in-game store as a predatory trap. The framework below does not attempt to compress trust into a single synthetic number. Instead, it exposes the exact friction points that nourish or bleed trust across the player journey.",
            "Never look at a revenue spike in isolation. Dropping an extra interstitial ad might inflate short-term ARPDAU today, but it can trigger early cohort churn, tank your store rating, and dramatically increase the cost of re-engaging lapsed users tomorrow.",
            "Collecting money earlier is not the same thing as creating more value."
        ],
        "table": {
            "headers": ["What Builds Trust", "What Bleeds Trust"],
            "rows": [
                ["Clear goals and transparent, predictable game rules", "Creatives that promise an entirely different experience"],
                ["Losing feels fair, with an obvious next move to improve", "Artificial, unexplained difficulty spikes engineered to force spending"],
                ["Rewarded ads are 100% voluntary and deliver immediate value", "Interstitials interrupting players right in the middle of active focus"],
                ["Clear pricing and explicit breakdowns of what is purchased", "Deceptive offer timers or accidental one-click purchases"],
                ["Instant recovery and rapid support when transactions fail", "Lost rewards, broken restores, and sluggish customer service"]
            ]
        },
        "audit_callout": "When auditing your game, pick a single monetization touchpoint—such as your first interstitial or a post-fail offer. What concrete value did the player just receive? Do they understand exactly what they are exchanging? And immediately after this touchpoint, which metric will tell you whether trust was preserved or traded away for a quick buck?"
    },
    "chapter2": {
        "title": "2. Healthy or Borrowed Revenue",
        "paragraphs": [
            "Think about the most recent change your team deployed to boost revenue: adding an interstitial, triggering an offer after a level loss, raising a bundle price, or cranking up difficulty on a specific puzzle. Which metric jumped immediately after the update? And which metrics did your team monitor to measure the hidden costs?",
            "If your answer stops at gross revenue, conversion rate, or ad impressions, you're only looking at half the equation. An aggressive tweak can make this week's dashboard look phenomenal while quietly accelerating player churn, dropping review scores, and inflating content production costs over the following month.",
            "This is the core definition of Borrowed Revenue: a change that inflates short-term metrics while sabotaging the conditions required to generate future revenue. Injecting an interstitial too early might lift ad revenue today while cutting D1 retention in half. A brutal difficulty wall might spike conversions on a post-loss bundle while filling your store reviews with complaints about pay-to-win mechanics. No monetization lever is inherently evil; the fatal mistake is failing to measure the price tag that comes attached to it.",
            "Whenever you review a monetization update, always place the immediate upside side-by-side with its potential downstream costs. The upside might be revenue, conversion rate, ad impressions, or CPI. The cost shows up in retention, repeat payer rates, app store sentiment, refund volume, customer support tickets, and content burn rate. Pair these metrics together before declaring any change a victory.",
            "'We increased ad load' merely describes what you did. 'We improved monetization' is a claim that requires holistic proof. Next, let's examine the foundation of that proof: bright design that ensures players understand the rules, their choices, and the real consequences of spending."
        ]
    },
    "chapter3": {
        "title": "3. Bright Design",
        "paragraphs": [
            "Open the most recent puzzle level in your game. When a player fails, what do they see first: the root cause of their loss, an alternative tactical move, or a pop-up paywall? If a booster pack appears, does the player understand exactly how it alters the board state? And if they choose not to buy, do they still have a viable, satisfying path forward? This is a self-audit, not a market survey: the answers must come directly from your own build and analytics.",
            "Puzzle games thrive on surprise, tension, and calculated risk. If every outcome were fully predictable, the game would devolve into a mindless sequence of taps. Transparency does not mean stripping away challenge; it means giving players enough clear information to understand their options, see why they won or lost, and know exactly what they are paying for.",
            "Bright design makes game rules, odds, pricing, and consequences effortless to parse. Dark patterns do the exact opposite: they obscure mechanics, manufacture confusion, hide exit buttons, or sell relief from artificial problems the developers deliberately engineered. The difference between ethical and exploitative monetization isn't whether your game has payments—it’s whether paying is an informed choice or the only visible escape hatch.",
            "A near-miss is a fantastic, thrilling challenge when the player sees the exact move that could have turned the tide. It becomes toxic the moment the game hides artificial interference, repeats arbitrary failures, and positions a paid booster as the only practical way through. When reviewing a level, ask: After this loss, can the player point to a different move, a free tool, or a legitimate reason to retry?",
            "For every purchase flow, check four vital criteria: Does the player understand the price and the exact contents? Is there a clear, intentional confirmation step? Can they easily find a cancel or refund path? And can they continue playing smoothly without paying? This isn't a rigid dogmatic formula; it is the absolute baseline for ensuring spending remains a voluntary, empowered decision."
        ]
    },
    "chapter4": {
        "title": "4. The Operating Map",
        "paragraphs": [
            "In July 2023, Sensor Tower estimated that Royal Match pulled in roughly $112 million in gross revenue and 14.6 million downloads in a single month, with 61.5% of installs coming from paid user acquisition. Sensor Tower's breakdown also highlighted their aggressive content cadence—adding roughly 200 levels every month—alongside live events like the Royal Pass and the Hidden Temple mini-game.",
            "These figures highlight immense commercial scale and observable live-ops features, but they aren't an internal engineering schematic. They don't reveal how Royal Match balances ad placements, purchase funnels, or underlying economy sinks. A far more productive exercise is asking: How does a top-tier title connect these moving parts to turn traffic, core loops, and fresh content into long-term player lifetime value?",
            "The Operating Map below answers that question. Its six components are not isolated silos. They are six sequential conditions: the player grasps the promise, feels tangible progression, encounters fair pressure, is invited to transact at the right moment, understands what money solves, and has a compelling reason to return tomorrow.",
            "When one link in the chain is broken, the remaining parts might still generate revenue for a few weeks, but the studio will be forced to compensate by pouring in more ad spend, churning out more content, or cranking up artificial pressure. This operating map helps you spot those hidden cracks before vanity metrics obscure them.",
            "Select one of your active projects and audit each row in the table. If you cannot answer a question with concrete player behavior, telemetry data, or a specific screen in your build, that is where your team must focus before building new features.",
            "The next chapter starts at the very first link in the chain: Creative. Long before players evaluate your levels, your rewards, or your in-game store, their expectations have already been set by your ads."
        ],
        "table": {
            "headers": ["Component", "Core Question to Answer", "Common Failure Mode"],
            "rows": [
                ["Promise", "Why does the player want to start playing?", "The creative and the actual gameplay promise two completely different experiences."],
                ["Progress", "Why is spending another five minutes worth it?", "Rewards feel meaningless and fail to show that the player has achieved anything real."],
                ["Pressure", "Why must the player act right now?", "Arbitrary frustration, opaque difficulty spikes, or excessive penalties."],
                ["Permission", "Why is an ad or offer appropriate at this exact moment?", "Monetization interrupts active gameplay flow rather than supporting the session."],
                ["Payment", "What concrete problem does money solve?", "The in-game store pushes abstract currencies when no immediate need exists."],
                ["Persistence", "Why will the player open the game tomorrow?", "Content and live events lack clear, compelling cliffhangers or meaningful goals."]
            ]
        }
    },
    "decision_board": {
        "title": "Decision Board | Part I: The System Behind the Store",
        "intro": "Part II traces the complete player journey: from the very first ad impression to that crucial first return session—where players test whether your game actually keeps the promise that prompted them to hit 'Install.'",
        "table": {
            "headers": ["DO THIS NOW", "ASK BEFORE DECIDING"],
            "rows": [
                [
                    "• Map the complete journey from Creative to First Return; highlight every single touchpoint that demands player attention, time, or cash.\n• Pick your most recent monetization update and simultaneously measure: Gross Revenue, D7 Retention, App Store Rating, and Refund Rate.\n• Run a Bright Design test: Do players understand what they are buying, is there a frictionless exit path, and do they get the exact value promised?",
                    "• Has the game earned a sufficient Trust Budget before triggering its first commercial offer?\n• Is this revenue spike healthy organic growth or borrowed revenue cannibalized from the future?\n• If a player refuses to pay or watch an ad, do they still have a complete, fair, and satisfying gameplay experience?"
                ],
                [
                    "CORE TAKEAWAYS:\n• Monetization starts before the store: players invest attention and patience long before they open their wallets.\n• A revenue increase does not equal value creation if your retention rate is quietly falling apart.\n• Bright design safeguards the long-term relationship between the player and your studio.",
                    "TEAM MEETING AGENDA (45 mins):\n• Attendees: Founder / Product Lead, Game Designer, Monetization Designer, Data Analyst, UA Lead.\n• Bring: Player journey map, paired revenue vs. D7/D30 retention charts, and recent app store reviews.\n• Target Outcome: Identify one critical trust leak to fix immediately and establish automated tracking for paired metrics."
                ]
            ]
        }
    }
}
print("Part 1 module loaded.")
