"""
Module containing English text and data for Part VI: What Data Can and Cannot Decide.
"""

SEC6_PART6 = {
    "part_title": "Part VI: What Data Can and Cannot Decide",
    "chapter25": {
        "title": "25. Market Intelligence",
        "paragraphs": [
            "Market intelligence platforms like Sensor Tower and AppMagic give you a macro bird's-eye view of top-grossing genres, revenue scale, and user acquisition dynamics. This data is extraordinarily valuable for screening out bad bets and spotting fertile sub-genres before you write a single line of code."
        ],
        "table": {
            "headers": ["Market Signal", "Product Thesis"],
            "rows": [
                ["Filters broad market genres, mechanics, art themes, and macro competitive dynamics.", "Defines the core emotional loop your studio can execute distinctly better than competitors."],
                ["Derived from third-party intelligence platforms (Sensor Tower, AppMagic).", "Forged and validated internally through rapid playable prototypes and internal cohort telemetry."],
                ["Narrows the opportunity space to eliminate weak bets before allocating production capital.", "Creates a unique value proposition and a compelling reason for players to stick around for years."]
            ]
        },
        "paragraphs_after_table": [
            "However, market intelligence only tells you what worked for someone else in the past. It cannot guarantee that your studio possesses the design craft, content velocity, or player empathy required to build a market-leading title in that exact space.",
            "Analytics can report that screw puzzles, rescue themes, or season pass tracks are printing money across the charts. But data will never tell you if your team can make the moment-to-moment loop more tactile and satisfying than the incumbent, preserve player trust, or manage a live economy without breaking it. That is the divide between market intelligence and a Product Thesis.",
            "A Market Signal is external observation: 'Players are spending significant time and cash in this sub-genre.' That is merely your starting clue.",
            "A Product Thesis is an internal commitment: 'Our team has the specific craft to deliver a visibly superior gameplay experience, retain players longer, and operate an economy with positive contribution margins.'",
            "A market signal tells you where to dig; your product thesis determines the quality of the ore you pull out of the ground."
        ]
    },
    "chapter26": {
        "title": "26. Behaviour Needs Interpretation",
        "paragraphs": [
            "A telemetry dashboard only logs what happened after a design update; it never explains what players were thinking or feeling when they took that action. A sudden spike in revenue could be driven by genuine delight, a confusing UI misclick, or a toxic difficulty wall causing panic buys. The question 'What does the data say?' is only step one. The critical question must always be: 'What psychological mechanism drove this behavior, and what evidence would disprove our theory?'",
            "For instance, if tray expansion purchases in Clear Garden spike dramatically at Level 7, that single data point could be caused by four completely different realities: an exhilarating, fair challenge; an irresistible promotional discount; an unfair board state causing desperate panic; or accidental misclicks due to clumsy button placement. Each explanation leads to a completely different future for your game.",
            "Watch actual screen recordings of player sessions, read app store reviews line by line, interview real players, and analyze behavioral cohorts deeply before jumping to conclusions.",
            "Never let cold, abstract numbers blind you to the living, breathing human experience happening on the other side of the glass."
        ]
    },
    "chapter27": {
        "title": "27. Decision Memo",
        "paragraphs": [
            "A standard game design document often reads like an endless wish list of features: 'Build a rescue-themed puzzle game, add a daily quest system, insert a starter pack.' This feature-factory approach is how studios blow through budgets without ever finding product-market fit.",
            "Instead, standardize every product proposal into a crisp, one-page Decision Memo built around five mandatory components:",
            "Player Problem to Solve ➔ Causal Intervention Hypothesis ➔ Supporting Market & Internal Data ➔ Guardrail Metrics & Strategic Risks ➔ Success Criteria or Immediate Kill Conditions.",
            "When an entire studio operates through transparent decision memos, accountability becomes unmistakable and the organization's collective learning velocity skyrockets.",
            "A brilliant decision is measured by the rigor of its logic and the speed at which its hypotheses can be verified—not by the graphic polish of a 50-slide presentation."
        ],
        "table_strategy": {
            "headers": ["Strategic Domain", "Concrete Application for Project: Clear Garden"],
            "rows": [
                ["External Market Signal", "Order-and-clear sorting mechanics are demonstrating immense commercial momentum across top-grossing charts."],
                ["Core Player Motivation", "The psychological satisfaction of restoring order from clutter and watching a neglected garden visibly blossom."],
                ["Product Expression", "A constrained tray capacity, tactile 3D sorting items, and clear, rewarding visual milestones for garden zones."],
                ["Key Differentiator", "High-fidelity garden restoration animations and instant visual payoff delivered within the first 60 seconds of gameplay."],
                ["Monetization Need", "Offering extra tray slots or tactical undos precisely when players realize a spatial planning miscalculation."],
                ["Production Burden", "The studio must reliably produce high-cadence puzzle layouts, 3D botanical assets, and seasonal renovation events."],
                ["Empirical Proof Required", "UA ad creatives match the first 3 minutes of gameplay; Levels 1–10 exhibit healthy pass rates; strong Day 2 return hooks."],
                ["Kill Condition", "The prototype generates early ad clicks but fails to establish organic, unprompted session re-engagement."]
            ]
        },
        "table_memo_template": {
            "headers": ["Decision Memo Section", "Clear Garden Operational Example"],
            "rows": [
                ["1. Core Hypothesis / Problem", "Level 7 fail rates are abnormally high due to cluttered tray space and too many junk item variants."],
                ["2. Proposed Value Proposition", "Grant careful players an optional temporary extra slot to let them solve the tactical bottleneck themselves."],
                ["3. Concrete Intervention", "Trigger a $0.99 rescue pack bundled with 1 undo token exclusively when a player has only 1 remaining target item."],
                ["4. Guardrail Metrics", "D1 retention must not drop by more than 1.0%; post-loss retry rates must remain stable."],
                ["5. Kill / Rollback Criteria", "If post-offer app quit rates exceed 15%, rollback the offer trigger immediately."],
                ["6. Direct Owner & Timeline", "Lead Game Designer paired with Monetization Lead; review cohort telemetry after a 7-day test run."]
            ]
        }
    },
    "chapter28": {
        "title": "28. Copy the Question, Not the Configuration",
        "paragraphs": [
            "When analyzing market leaders like Royal Match or Candy Crush Saga, the most common amateur blunder is blindly copying their exact configuration values: matching their price points, copying their timer durations, and cloning their live event schedules. Teams forget that those specific parameters are supported by an industrial content pipeline producing 200 levels a month, eight-figure UA budgets, and years of accumulated player loyalty.",
            "Copy the core design questions those leaders had to solve:",
            "'How do they generate a continuous sense of momentum?'",
            "'How do they calibrate the balance between tension and relief?'",
            "'What structural mechanics protect the integrity of their economy?'",
            "Then, forge the answers that fit your studio's specific production capabilities, team size, and commercial scale."
        ]
    },
    "chapter29": {
        "title": "29. Clear Garden: From Prompt to Decision",
        "paragraphs": [
            "Let's return to our Clear Garden case study. When a publisher gives you high-level feedback: 'Make a sorting game with garden decorating, add collection albums, and sell rescue packs on losses'—that is merely raw directional feedback.",
            "Your first prototype build doesn't need five in-game currencies, an elaborate battle pass, or dozens of live events. It only needs to prove four existential truths:",
            "1. The ad creative sets an authentic emotional expectation that the first 3 minutes fulfill.",
            "2. The first 10 levels deliver genuine puzzle-solving joy.",
            "3. Players understand why they fail and voluntarily choose to retry.",
            "4. There is a clear, tantalizing cliffhanger that pulls them back into the game tomorrow.",
            "If cohort telemetry proves those four pillars, you have a rock-solid foundation to build out advanced economy systems and live operations. If it fails, killing the prototype early is the smartest, most profitable move you will ever make—preserving your studio's talent and capital for an idea that actually works."
        ]
    },
    "decision_board": {
        "title": "Decision Board | Part VI: What Data Can and Cannot Decide",
        "intro": "Part VII transitions from product strategy to operational reality: value supply chains, kill/iterate/scale governance, memory-driven live ops, and true contribution margin economics.",
        "table": {
            "headers": ["DO THIS NOW", "ASK BEFORE DECIDING"],
            "rows": [
                [
                    "• Convert every feature proposal into a 1-page Decision Memo with explicit hypotheses and kill criteria.\n• Clearly separate external market signals from internal product theses before greenlighting production capital.\n• Extract the fundamental design questions solved by top competitors rather than blindly cloning their live configurations.",
                    "• Does our studio possess the core craft to execute this experience visibly better than the market leader?\n• Is this behavioral metric reflecting authentic player enjoyment or a coping mechanism against frustrating mechanics?\n• If this product bet fails, will the lessons learned systematically elevate our studio's long-term competitive edge?"
                ],
                [
                    "CORE TAKEAWAYS:\n• Market intelligence filters out bad bets; your product thesis determines whether the game survives.\n• Never clone an incumbent's configuration if you don't possess their production scale and marketing machinery.\n• The most valuable unit of work is a falsifiable decision, not an endless backlog of features.",
                    "TEAM MEETING AGENDA (60 mins):\n• Attendees: Studio Director, Head of Game Design, Product Director, Lead Producer.\n• Bring: Market intelligence teardown, 1-page Decision Memo for the upcoming feature, and production capacity model.\n• Target Outcome: Formally approve or kill the feature proposal based strictly on product thesis and kill criteria."
                ]
            ]
        }
    }
}
print("Part 6 module loaded.")
