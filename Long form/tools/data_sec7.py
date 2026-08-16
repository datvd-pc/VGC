"""
Module containing English text and data for Part VII: The Operating System Behind a Live Game.
"""

SEC7_PART7 = {
    "part_title": "Part VII: The Operating System Behind a Live Game",
    "chapter30": {
        "title": "30. Monetization as a Supply Chain",
        "paragraphs": [
            "The player only sees a single screen at any given moment. But for that screen to appear at the right second, offer authentic value, and execute flawlessly, your entire studio must function as an integrated value supply chain:",
            "Market Research shapes the strategic angle ➔ Playable Prototypes validate the core loop ➔ Level Design engineers engaging friction ➔ Art & Audio breathe life into the world ➔ Engineering guarantees rock-solid performance ➔ User Acquisition attracts the right audience ➔ Data Science uncovers behavioral truth ➔ Customer Support defends player trust."
        ],
        "table": {
            "headers": ["Supply Chain Link", "Early Warning Signal of Failure", "Mandatory Monetization Reality Check"],
            "rows": [
                ["Prototyping & Level Design", "Players do not understand the value proposition or why they failed a level.", "Is there a real, organic in-game problem for ads, boosters, or IAPs to solve?"],
                ["Creative & Store Listing", "UA campaigns acquire users through messaging disconnected from actual gameplay.", "Do low CPIs and high CTRs translate into healthy store conversion, D1 retention, and session depth?"],
                ["Analytics & Remote Config", "The team cannot rollback bad updates instantly or explain the causal drivers behind metric shifts.", "Does every ad placement or commercial offer have an active control group and strict guardrails?"],
                ["QA & Customer Support", "Buyer trust is damaged by payment bugs, crashing ads, and rising refund rates.", "Are reward delivery, purchase consent, and dispute resolution 100% transparent and reliable?"],
                ["Content Pipeline & LiveOps", "Content cadence stalls out or recurring events degenerate into an exhausting, predatory grind.", "Does the studio possess the content velocity to maintain the core promise after scaling UA spend?"]
            ]
        },
        "paragraphs_after_table": [
            "If a single link in the chain snaps—whether it's a slow level-production pipeline leaving veteran players stranded, sloppy QA letting payment bugs slip through, or misleading marketing acquiring the wrong audience—your entire monetization engine stalls out.",
            "Regularly audit the health of every link in your supply chain: pinpoint the exact operational bottleneck choking your game's growth, and focus your studio's collective firepower on fixing it."
        ]
    },
    "chapter31": {
        "title": "31. Kill, Iterate, or Scale",
        "paragraphs": [
            "A pretty pitch deck is not a strategy. Before turning a prototype into a full-scale production project, write down explicit, unyielding Kill Criteria covering promise clarity, FTUE conversion, early retention benchmarks, and long-term content production costs.",
            "Every project must navigate three explicit strategic forks:",
            "• Kill: When empirical evidence proves there is no viable path to achieving sustainable unit economics within your studio's resource constraints.",
            "• Iterate: When there is a specific, falsifiable hypothesis that can be tested within a locked timeframe and budget.",
            "• Scale: When all core benchmarks for retention, player trust, and marginal contribution economics are proven across real player cohorts.",
            "Supercell is legendary for celebrating when they kill projects that fail to meet elite quality standards (such as Hay Day Pop), freeing up their best talent to hunt for genuine breakthrough hits. Having the courage to ruthlessly kill a mediocre game is the ultimate hallmark of a world-class studio."
        ]
    },
    "chapter32": {
        "title": "32. Live Ops with Memory",
        "paragraphs": [
            "A live operations system is not an automated spam cannon blasting pop-ups at random. It must operate with contextual memory: recognizing whether a player just suffered an exhausting losing streak or just conquered a major milestone, how many ads they've watched today, and what their current wallet balances look like before triggering an interaction."
        ],
        "table": {
            "headers": ["Event Archetype", "What the Player Must Feel", "Key Metrics & Safety Guardrails"],
            "rows": [
                ["Teach / Skill Mastery", "Discovers a fresh mechanic or tactical tool that enriches the core loop.", "Event completion rate, feature adoption, confusion drop-off rate."],
                ["Reactivate Lapsed Players", "A familiar, beloved objective is refreshed with an exciting new spin.", "Return rate, session depth, conversion from contextual push notifications."],
                ["Collector Milestone", "Visible progress toward completing an exclusive, permanent album or zone.", "Set completion velocity, repeat session frequency, economic sink health."],
                ["Spend / Monetization Moment", "An exciting option to accelerate progress without paywalling the free path.", "Offer conversion rate, non-buyer retention, refund volume."],
                ["Recovery / Cool-down", "A relaxing, low-pressure breathing space between intense competitive events.", "Churn rate, player sentiment scores, Day 7 return rates following the break."]
            ]
        },
        "paragraphs_after_table": [
            "Every live event on your calendar must serve an explicit purpose: teaching a new skill (Teach), re-engaging lapsed players (Reactivate), driving collection goals (Collector Goal), creating natural monetization moments (Monetization Moment), or giving players a relaxing breather to recharge (Recovery). Never turn your live ops calendar into an endless, exhausting marathon that burns out your player base."
        ]
    },
    "chapter33": {
        "title": "33. Contribution Economics",
        "paragraphs": [
            "Gross Revenue is a vanity metric designed for press releases. A real game business survives and thrives entirely on Contribution Margin—the actual cash remaining after every single operational tax, fee, and expense has been paid in full.",
            "The Real Contribution Margin Equation:",
            "Gross Revenue",
            "Minus: ( Platform Fees [30% Apple / Google] + Ad Tech & Server Infrastructure + Paid UA Marketing Spend + Content Production, QA, Customer Support & Live Operations Overhead )",
            "Equals: True Contribution Margin (Net Studio Profit)",
            "Every single cost line item must have a designated DRI (Directly Responsible Individual) and be tracked ruthlessly across player cohorts.",
            "Pay hyper-vigilant attention to your Payback Period and Cash Flow Dynamics. A user acquisition campaign might project a gorgeous theoretical 180-day LTV on a spreadsheet, but if your cash collection cycle takes six months while your ad networks demand payment in 30 days, your studio will run out of cash and go bankrupt while celebrating theoretical profitability."
        ]
    },
    "decision_board": {
        "title": "Decision Board | Part VII: The Operating System Behind a Live Game",
        "intro": "Part VIII narrows these operational principles into concrete, genre-specific playbooks—ensuring your monetization architecture flows naturally from the specific emotional needs of your players.",
        "table": {
            "headers": ["DO THIS NOW", "ASK BEFORE DECIDING"],
            "rows": [
                [
                    "• Map your Value Supply Chain: assign owners, quality benchmarks, and early failure signals to every link.\n• Establish strict Kill, Iterate, or Scale criteria before authorizing any increase in user acquisition spend.\n• Build a dynamic financial model calculating true Contribution Margin, payback periods, and real-world cash flow.",
                    "• Which link in our supply chain is breaking the core promise before the player ever experiences value?\n• Does this project possess conclusive empirical proof of retention and marginal unit economics to justify scaling?\n• After accounting for every operational cost required to keep the game healthy, is this player cohort truly profitable?"
                ],
                [
                    "CORE TAKEAWAYS:\n• Scaling UA is only rational when empirical retention proof and content production capacity coexist.\n• Gross revenue is vanity; net contribution margin determines whether your studio stays in business.\n• Having the guts to kill an average game to fund an extraordinary opportunity is peak professionalism.",
                    "TEAM MEETING AGENDA (60 mins):\n• Attendees: Studio Director, Product Owner, Production Lead, UA Manager, Finance Lead.\n• Bring: Supply chain map, cohort contribution margin models, content production burn rates, and scale benchmarks.\n• Target Outcome: Make definitive kill/iterate/scale decisions for active projects and eliminate operational bottlenecks."
                ]
            ]
        }
    }
}
print("Part 7 module loaded.")
