"""
Module containing English text and data for Part VIII, Part IX, and Closing/References.
"""

SEC8_PART8 = {
    "part_title": "Part VIII: Genre Playbooks",
    "chapter34": {
        "title": "34. The Emotional Loop",
        "paragraphs": [
            "Start with the exact emotional state your player is looking for, and only then choose the commercial mechanics that support that journey."
        ],
        "table_segment": {
            "headers": ["Genre Segment", "Core Emotional Driver", "Rewarded Ad Fit When", "IAP Fit When", "Critical Risk to Avoid"],
            "rows": [
                ["Casual Puzzle", "Novelty, instant relief, and frictionless sorting", "Placed at natural, clean breakpoints between stages.", "Convenience bundles, permanent remove-ads options.", "Aggressive ad frequency that shreds an already thin gameplay loop."],
                ["Hybrid-Casual", "Snappy core loop paired with a lightweight meta-progression", "Expands player autonomy and unlocks progression shortcuts in the core loop.", "Event access keys, remove-ads bundles, progression accelerators.", "Shallow, unrewarding meta-systems that fail to build long-term retention."],
                ["Classic Puzzle", "Mastery, intellectual rigor, and restoring spatial order", "Enables transparent, predictable tactical choices.", "Precision tools to untangle complex bottlenecks without feeling like a cheat.", "Confusing arbitrary timer stress with authentic intellectual challenge."],
                ["Hybrid-Puzzle", "Deep accomplishment, long-term mastery, and world-building", "Seamlessly integrated into live events and meta-renovation loops.", "Progression battle passes, exclusive cosmetics, seasonal expansion bundles.", "Content production burn rates and economy complexity that overwhelm the studio."]
            ]
        },
        "paragraphs_between_tables": [
            "There is no such thing as a generic 'puzzle gamer,' and therefore there is no single default monetization formula. Every genre satisfies a fundamentally distinct psychological state."
        ],
        "table_mechanics": {
            "headers": ["Sub-Genre / Core Mechanic", "Core Player Emotional Need", "Value Exchange to Test", "Critical Failure Mode to Avoid"],
            "rows": [
                ["Sorting Puzzles (Sort)", "Deep relaxation through restoring order and cleanliness", "Tactical undos, extra tray slots unlocked after clear spatial planning.", "Artificially choking tray space to force immediate tool purchases."],
                ["Traffic / Jam Puzzles (Jam)", "Controlled suspense followed by an explosive burst of relief", "Continue offers on near-miss states bundled with a clear tactical resolution.", "Unfair difficulty spikes where players cannot understand why they failed."],
                ["Physics Puzzles (Physics)", "Curiosity, rapid experimentation, and hilarious surprises", "Instant retry buttons or rewarded ads unlocking unique experimental tools.", "Clunky, slow-loading shop pop-ups that kill the kinetic momentum."],
                ["Match-3 Puzzles (Match-3)", "Long-term mastery, strategic planning, and continuous progression", "Strategic boosters, extra lives, and seasonal live event battle passes.", "Content production requirements that outpace your studio's development capacity."]
            ]
        },
        "paragraphs_after_tables": [
            "When commercial touchpoints align seamlessly with the core emotional loop, players welcome them as organic gameplay lifelines rather than intrusive disruptions."
        ]
    },
    "chapter35": {
        "title": "35. Evidence, Not Blueprint",
        "paragraphs": [
            "Mega-hits like Royal Match, Candy Crush Saga, and Merge Mansion offer masterclass case studies on content cadence, board tension, and live event design. However, they are historical evidence to learn from—not rigid architectural blueprints to copy blindly.",
            "Use public market intelligence to understand genre scale, market momentum, and strategic competitive baselines. But always rely on your own cohort telemetry to balance level difficulty, price in-app bundles, and optimize ad placements."
        ]
    },
    "decision_board": {
        "title": "Decision Board | Part VIII: Genre Playbooks",
        "intro": "Part IX delivers the final master assessment: a surgical 30-minute audit framework to pinpoint trust leaks and value leaks, alongside the non-negotiable Definition of Done before scaling UA.",
        "table": {
            "headers": ["DO THIS NOW", "ASK BEFORE DECIDING"],
            "rows": [
                [
                    "• Pick an active game project and describe its emotional loop in the player's own words—zero feature buzzwords allowed.\n• Select commercial touchpoints that mesh perfectly with that emotional loop and validate them in a lean prototype.\n• Identify fairness risks and flow disruptions before packaging mechanics into paid shop SKUs.",
                    "• What specific emotional state brings players back to this game, and does our design actively deepen that feeling?\n• Does this monetization placement protect the player's flow or violently disrupt their most thrilling moment?\n• Which player cohort should test this mechanic first to validate our genre assumptions?"
                ],
                [
                    "CORE TAKEAWAYS:\n• A genre is defined by mechanics and emotional loops—not a checklist of features to copy.\n• A monetization placement is only valid when it invites the player deeper into the journey they came for.\n• No public market benchmark will ever replace the causal truth inside your own player data.",
                    "TEAM MEETING AGENDA (45 mins):\n• Attendees: Lead Game Designer, Product Lead, Economy Designer, UA Creative Lead.\n• Bring: Genre mechanics map, competitor teardown, gameplay recordings, and lean test plans.\n• Target Outcome: Lock in the primary emotional loop, pick the first commercial placement to test, and set kill conditions."
                ]
            ]
        }
    }
}

SEC9_PART9 = {
    "part_title": "Part IX: The Master Audit",
    "chapter36": {
        "title": "36. The 30-Minute Audit",
        "paragraphs": [
            "Never let an audit devolve into a subjective, emotional debate over personal taste. The sole objective of a 30-minute audit is to construct an unbroken chain of logic from Ad Creative ➔ First-Time User Experience ➔ Monetization Touchpoints ➔ Real Cohort Telemetry. By minute 30, the team must pinpoint exactly: One critical Trust Leak, One critical Value Leak, and One testable intervention plan with a designated owner and a safe rollback protocol."
        ],
        "table": {
            "headers": ["Time Window", "Concrete Forensic Audit Action", "Mandatory Deliverable"],
            "rows": [
                ["00 – 05 min", "Watch top 3 UA video ads; play the first 60 seconds of the live build.", "Promise Map: Contrast the ad's emotional hook against the game's actual onboarding."],
                ["05 – 10 min", "Play Levels 1 to 10 manually; log player agency, fail states, choices, and boosters.", "Identify one fair/unfair fail state and note all remaining free progression paths."],
                ["10 – 15 min", "Locate the first rewarded ad and first interstitial placement.", "Value Exchange Map: What does the player gain, how do they decline, and is the break natural?"],
                ["15 – 20 min", "Open the in-game shop after an organic bottleneck; audit bundles and currencies.", "SKU Breakdown: Concrete problem solved, pricing transparency, stock/flow sinks, and remove-ads clarity."],
                ["20 – 25 min", "Identify the active day-two return hook and current live event loop.", "Live Event Loop: Core Play ➔ Token Sinks ➔ Tiered Choices ➔ Progression ➔ Recovery."],
                ["25 – 30 min", "Overlay revenue curves against retention, difficulty, ad frequency, and reviews.", "Deliver 1 Trust Leak, 1 Value Leak, and 1 testable intervention with an owner and rollback plan."]
            ]
        }
    },
    "chapter37": {
        "title": "37. Definition of Done",
        "paragraphs": [
            "A game ecosystem is only ready to scale user acquisition spend when and only when all 10 empirical quality gates below are rigorously proven through cohort data and backed by designated team owners:"
        ],
        "list_items": [
            "1. The Creative Promise is validated within the first 3 minutes of gameplay and proven by high FTUE completion rates across ad cohorts.",
            "2. Players can explain exactly why they failed a level and always have at least one viable skill-based path forward without paying.",
            "3. Rewarded Ads are 100% voluntary, deliver immediate and reliable value, and maintain healthy long-term player retention.",
            "4. Interstitial Ads appear strictly at natural psychological breakpoints, have strict frequency caps, and automatically vanish for any paying user.",
            "5. Every In-App Offer solves an authentic, present in-game need, features transparent pricing, and provides a frictionless, guilt-free exit path.",
            "6. Currency Sources and Sinks create meaningful tactical choices rather than coercive paywalls, with median wallet balances actively monitored.",
            "7. Monetization Growth is continuously paired against retention benchmarks, app store review sentiment, refund rates, and support ticket volume.",
            "8. The Studio possesses the operational infrastructure to deploy A/B tests, execute instant rollbacks, and document structured learnings.",
            "9. The Live Ops & Content Pipeline can reliably fulfill the marketing promise after scaling UA, with built-in cool-down recovery periods.",
            "10. The Financial Model accurately factors in platform fees, UA spend, and live operational overhead, ensuring safe payback periods and cash flow stability."
        ],
        "decision_board": {
            "title": "Decision Board | Part IX: Product Audit and Scale Readiness",
            "intro": "The conclusion of this playbook introduces no new theoretical frameworks. It brings us right back to the timeless professional and ethical standard that underpins every chapter: After watching an ad, claiming an offer, or completing an in-app transaction, does the player still feel excited and have a compelling reason to keep playing?",
            "table": {
                "headers": ["DO THIS NOW", "ASK BEFORE DECIDING"],
                "rows": [
                    [
                        "• Execute the 30-Minute Forensic Audit on your active game build; document all 3 mandatory deliverables.\n• Select 1 primary Trust Leak and 1 primary Value Leak; draft a 1-page intervention test plan.\n• Benchmark your live build against the 10 Definition of Done criteria before authorizing any UA budget increase.",
                        "• Do the ad creative, first 10 levels, commercial placements, and return hooks form an unbroken chain of logic?\n• Is our primary bottleneck caused by trust, value, technical quality, or economy design—and what data proves it?\n• Has this game earned conclusive empirical proof to scale, or does it merely have enough features to look finished?"
                    ],
                    [
                        "CORE TAKEAWAYS:\n• A great audit ends with a falsifiable decision, not a vague list of subjective opinions.\n• The Definition of Done is an empirical safety threshold for scaling responsibly—not a guarantee that risk has vanished.\n• Fixing one critical trust leak creates far more enterprise value than rushing out five unproven features.",
                        "TEAM MEETING AGENDA (45 mins):\n• Attendees: Product Owner, Lead Game Designer, Data Lead, Monetization Lead, QA Lead, Producer.\n• Bring: 30-minute audit teardown, gameplay screen recordings, cohort dashboards, and intervention test specs.\n• Target Outcome: Lock in the #1 trust leak fix, approve an intervention test with a rollback plan, and assign a DRI and deadline."
                    ]
                ]
            }
        }
    }
}

SEC10_CLOSING = {
    "closing": {
        "title": "Closing: The Player Must Want to Continue",
        "paragraphs": [
            "The most important question in game development is never 'How do we squeeze more cash out of this screen?' The real, foundational question is infinitely deeper: 'What value did the player just experience, what emotional state are they in right now, and what choice will they perceive as 100% fair?'",
            "When the answer is crystal clear, commercial features naturally find their most powerful and dignified place in service of the gameplay. When the answer is muddy, piling on more pop-up ads and discount bundles only adds noise, accelerating the slow death of your product.",
            "Sustainable profit is the inevitable byproduct of a system built to keep its promises from end to end: from the creative ad hook and the first tactile session to polished puzzle levels, respectful ad placements, transparent purchases, emotionally resonant live events, honest dashboards, and rapid customer support. No analytics tool, publisher mandate, or competitor teardown will ever replace that disciplined, craftsman-like execution. They are merely compasses helping your team ask sharper, more uncomfortable questions.",
            "The true art of monetization leaves the player with a compelling, exciting reason to continue their journey after every single transaction. A game has every right to challenge player skill, demand focus, and ask for fair financial support. But that relationship only endures when players experience authentic value, transparent rules, and uncompromised autonomy—and when the development team has the humility and discipline to listen to early warning signs rather than getting drunk on short-term vanity metrics.",
            "That is the highest standard of craftsmanship for any game studio worth building: never pretending a single clever trick makes a business, never hiding behind abstract spreadsheets, and never, ever mortgaging the long-term soul of your game for a quick, unearned buck."
        ]
    },
    "references": {
        "title": "Research Notes and Public Sources",
        "sources": [
            "Sensor Tower: Deep-dive case studies on the commercial rise of Royal Match and global casual mobile gaming trends.",
            "Sensor Tower: State of Mobile Gaming industry reports and in-app purchase spending trajectory forecasts.",
            "Sensor Tower: Specialized genre intelligence reports on the US and global puzzle gaming ecosystem.",
            "AppMagic & GameDev Reports: Casual and Hybrid-Casual Gaming H1 Market Analysis.",
            "AppMagic: Growth model and monetization case study of Epic Plane Evolution.",
            "AppMagic: LiveOps and seasonal event architecture reports across top-grossing casual titles.",
            "Unity Technologies: Mobile Game Monetization Report; empirical analysis on the interplay between rewarded ads, IAP, and D30 retention.",
            "Apple Inc.: Human Interface Guidelines and App Tracking Transparency (ATT) framework architecture documentation.",
            "Federal Trade Commission (FTC): Epic Games enforcement action, settlement decree, and consumer guidance on digital dark patterns.",
            "GameRefinery: Feature taxonomy breakdown, motivational player archetypes, and market segmentation models.",
            "GameAnalytics: Mobile Gaming Industry Benchmarks and core retention/monetization KPI distributions.",
            "Rovio Entertainment: Beacon platform architecture, player lifetime behavioral modeling, and FTUE optimization case studies.",
            "King Digital Entertainment: Data science methodologies, cohort retention analytics, and casual puzzle product strategies.",
            "Supercell: 'What We Have Learned from Failures' – Cultural post-mortems on project kill criteria and quality governance."
        ]
    }
}
print("Part 8-10 modules loaded.")
