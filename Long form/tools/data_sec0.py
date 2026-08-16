"""
Module containing English text and data for Front Matter & Part 1-3.
"""

SEC0_FRONT_MATTER = {
    "title": "THE ART OF MONETIZATION",
    "subtitle": "The Craft of Game Economics & Sustainable Revenue",
    "research_note": {
        "title": "Research Note",
        "paragraphs": [
            "In the game industry, few decisions survive if they lean solely on a single cute mechanic, a flashy creative, or a polished analytics dashboard. A clever mechanic isn't a product strategy; a bold creative won't bandage a broken economy; and dashboards only tell you where to look—they will never replace the visceral reality of playtesting, crisp level design, or the hardest call of all: ruthlessly killing a promising idea.",
            "This research playbook began at a publisher workshop before ballooning into a deep forensic dive into puzzle and hybrid-casual games. The market is always throwing opportunities around, but an opportunity is worthless unless your team knows exactly which arena you’re competing in and what real problem you’re solving.",
            "Game mechanics, themes, and monetization models get cloned far faster than the market actually understands them. Lurking behind every seemingly trivial design choice is a messy knot: player psychology, production bandwidth, and underlying economy logic. This playbook exists to dissect those hidden layers before you rush to trade your game's future for a shiny short-term market signal.",
            "The framework pulls together core game hypotheses, mental models, real market data, and the uncomfortable questions that don't have neat textbook answers. It will continue to evolve through feedback from working developers, live publishing battle scars, behavioral data, and cohort analytics.",
            "The most valuable feedback isn't polite applause. It’s when someone points out the exact edge case where a rule breaks, drops contradictory data, or shares a decision tool that saved their studio from an expensive trainwreck. Those are the real levers that keep this document grounded in reality.",
            "Core mission: Build a clear, unvarnished vocabulary for product decisions—and keep refining it alongside the people in the trenches making games every day."
        ]
    },
    "note_to_reader": {
        "title": "A Note to the Reader",
        "paragraphs": [
            "Making games is brutal. Monetizing them is even harder. Monetization sits at the volatile crossroads where game design, economy, user acquisition, product strategy, data science, and live ops all collide into a single continuous player experience.",
            "Every discipline brings its own lens and blind spots. But if you want a game to scale and survive—whether you’re a Founder, Product Lead, Game Designer, Data Analyst, UA Specialist, Publisher, or Indie Dev—you need a shared reality and a common language, even if you look at the problem from different angles.",
            "Treat every framework in this book as an aggressive stress test for your game: Which creative is worth testing? Which level needs retuning? Which ad placement actually makes sense? Which offer has an earned right to exist? Which paired metrics must be read together? And when should you pull the plug on a dead-end feature?",
            "Keep this playbook open right next to your game build and your analytics dashboard. Its job isn't to spoon-feed you generic answers; its job is to help your team ask sharper, more uncomfortable questions every time you open the project."
        ]
    },
    "key_terms": {
        "title": "Key Terms",
        "intro": "You don't need a PhD in game analytics to read this playbook. The industry terms below are used throughout the text as standard shorthand; each time they appear within a specific framework, they are defined in plain English according to their practical context.",
        "table": {
            "headers": ["Term", "Operational Meaning in this Playbook"],
            "rows": [
                ["Monetization", "The strategic framework for generating revenue through advertising, in-app purchases, and live services without destroying player trust."],
                ["User Acquisition (UA)", "The engine for driving new installs, primarily through paid ad campaigns and creative testing across ad networks."],
                ["In-App Purchase (IAP)", "Direct microtransactions inside the game, including starter packs, virtual currencies, boosters, or permanent remove-ads options."],
                ["Retention", "The percentage of players who return after a specific milestone (e.g., D1 is Day 1 return, D7 is Day 7, D30 is Day 30)."],
                ["Cohort", "A segment of players grouped by a shared starting point or attribute (e.g., installed on the same date, acquired from the same creative)."],
                ["Core Loop", "The primary, repeatable chain of actions a player performs during their moment-to-moment gameplay session."],
                ["Live Ops", "The continuous operation and content renewal of a released game: recurring events, targeted offers, content drops, push notifications, and remote config tuning."],
                ["Creative", "The promotional assets (video ads, playable ads, static banners) engineered to capture attention and trigger an install."],
                ["Offer", "A contextual purchase or rewarded ad prompt triggered at the precise moment and emotional state where player intent is highest."],
                ["Funnel", "The sequential journey players take: Ad Impression ➔ Store Listing ➔ Install ➔ FTUE ➔ Progression ➔ Return ➔ Monetization."],
                ["LTV & CPI", "Lifetime Value (expected cumulative revenue per player) versus Cost Per Install (average marketing spend to acquire one user)."],
                ["ARPDAU & IMPDAU", "Average Revenue Per Daily Active User versus Average Ad Impressions Per Daily Active User."]
            ]
        }
    },
    "contents": {
        "title": "Contents",
        "items": [
            "Part I: The System Behind the Store",
            "Part II: From Creative to First Return",
            "Part III: Progress, Pressure, and Fairness",
            "Part IV: Ads, IAP, and Economy",
            "Part V: Signals, Decisions, and Experiments",
            "Part VI: What Data Can and Cannot Decide",
            "Part VII: The Operating System Behind a Live Game",
            "Part VIII: Genre Playbooks",
            "Part IX: The Master Audit",
            "Closing: The Player Must Want to Continue",
            "Research Notes and Public Sources"
        ]
    },
    "how_to_read": {
        "title": "How to Read this Playbook",
        "paragraphs": [
            "Don't read this like a theoretical blog post. It only works if you use it as a surgical audit tool on an actual game.",
            "Every chapter dissects a critical player touchpoint: from ad creatives and app store listings to the first-time user experience (FTUE), level pacing, fail states, rewarded placements, offer triggers, live events, cohort tables, store reviews, and internal team post-mortems.",
            "• For Live Games: Keep your actual build open while reading. When you read about the first ten levels, play through those ten levels yourself. When you read about rewarded ads, find your first placement and ask: What real itch is the player trying to scratch here? When you read about IAPs, open your shop and identify the exact problem each bundle claims to solve. When you look at metrics, open your dashboard and separate genuine signals from cosmetic noise.",
            "• For Prototypes: Use these chapters as non-negotiable quality gates before soft launch. A game that cannot clearly articulate its core promise, its first three minutes, its pressure curve, its ad value proposition, and its day-two return hook has zero business burning user acquisition budget.",
            "Your goal isn't to blindly agree with every single framework. Your goal is to close every chapter with a sharper, more uncomfortable question for your own project—and a healthy skepticism toward easy answers."
        ]
    },
    "starts_before_store": {
        "title": "Monetization Starts Before the Store",
        "paragraphs": [
            "Games rarely die inside the in-game shop. They bleed out long before the player ever sees a price tag—right at the broken links in the trust chain that make someone willing to spend in the first place:",
            "• The creative promises a chill, satisfying puzzle, but the first 3 minutes deliver a chaotic, high-stress chore.",
            "• The store listing fails to validate the hook that earned the initial click.",
            "• A bloated, hand-holding tutorial robs the player of any sense of autonomy or mastery.",
            "• An unskippable interstitial ad slams into the screen before the player has even decided if the game is worth another sixty seconds of their life.",
            "• The level design creates artificial, unfair frustration, only to immediately shove a booster pack into the player’s face as a paid antidote to a manufactured disease.",
            "• The team celebrates a short-term revenue bump while completely ignoring that retention, store ratings, refund requests, and player goodwill are driving off a cliff.",
            "The in-game shop is just the checkout counter for an exchange of value. It cannot resurrect a product that fails to keep people engaged.",
            "Before asking for a single dollar, what has your game already demanded from the player?",
            "• First, their attention.",
            "• Next, their click, the download, the loading wait, the first-time user experience (FTUE), and that first deliberate return session.",
            "• Cash only flows once the game has accumulated a healthy Trust Budget.",
            "In casual, hybrid-casual, and puzzle games, monetization is the cumulative outcome of an entire conversion journey:",
            "Ad Impression ➔ Click ➔ Store Page ➔ Install ➔ First Launch ➔ First 10 Levels ➔ Day 1 Return ➔ Daily Habit ➔ Voluntary Rewarded Ad ➔ First IAP ➔ Repeat Purchase ➔ Live Ops ➔ Word-of-Mouth Advocacy",
            "Every single touchpoint demands an investment from the player:",
            "• The Creative demands curiosity.",
            "• The Store Page demands initial credibility.",
            "• The Loading Screen demands patience.",
            "• The First 10 Levels build competence and trust.",
            "• The First Ad demands consent.",
            "• The First Offer demands a legitimate reason to spend.",
            "• The First Event demands habitual loyalty.",
            "Profit = Installs × (LTV - CPI)",
            "This classic financial formula is fine for investor decks, but it's too macro and arrives far too late to guide a game designer sitting at their desk on a Tuesday afternoon.",
            "A far more actionable operational formula for development teams is:",
            "Monetization = Core Player Need × Right Context × Accumulated Trust × Execution Speed",
            "• Core Player Need: The psychological driver—relief, a second chance, mastery, progression speed, collection, convenience, status, or taking back control of a chaotic board.",
            "• Right Context: The offer appears exactly when player intent peaks—not when the studio is panicking about hitting monthly revenue targets.",
            "• Accumulated Trust: The quiet conviction that the game plays fair, remains transparent, and respects the player's time and money.",
            "• Execution Speed: The team's agility in reading cohort data, ad funnels, and player sentiment to continuously tune the live loop.",
            "The operating framework of this book rests on six continuous pillars:",
            "Promise ⟷ Progress ⟷ Pressure ⟷ Permission ⟷ Payment ⟷ Persistence",
            "Break any single pillar, and revenue might spike today, but you're walking straight into a fatal trap:",
            "IMPDAU (ad impressions per daily active user) might shoot up while Day 3 retention quietly collapses. A predatory starter pack might convert well today, but your app store listing will get flooded with 1-star reviews about unfair paywalls. An obnoxious interstitial might bump short-term ARPDAU while completely choking your UA team's ability to scale traffic profitably.",
            "• Healthy Revenue gives the player an exciting reason to keep playing after every ad or purchase.",
            "• Borrowed Revenue cannibalizes tomorrow's player base to extract cash from manufactured frustration that your gameplay cannot justify."
        ]
    },
    "case_study": {
        "title": "Case Study: Clear Garden",
        "paragraphs": [
            "Imagine a hypothetical hybrid-puzzle game entering soft launch called Clear Garden.",
            "• Core Loop: Players clear overgrown botanical debris from a neglected garden by sorting matching items into a constrained tray (Match-3D / Grid sorting mechanics), gathering resources to restore garden zones (Meta-progression).",
            "• Creative Promise: The tactile, deeply satisfying sensation of bringing order to chaos, paired with gorgeous visual garden transformations.",
            "The initial prototype build of Clear Garden suffers from a textbook catalog of rookie monetization blunders:",
            "1. Slams the player with an iOS App Tracking Transparency (ATT) permission prompt on the splash screen before they've even touched a single leaf.",
            "2. Drops an unskippable interstitial ad right after Level 2, killing momentum before the player even understands the basic rules.",
            "3. Spikes difficulty artificially at Level 7 with cluttered junk items, then immediately prompts a paid tray expansion when the player fails.",
            "4. Sells a generic $2.99 Starter Pack loaded with abstract virtual coins without explaining what real in-game problem that currency actually solves.",
            "5. Showers the player with generic daily login widgets, but the garden renovation lacks visual payoff or cliffhangers, leaving zero curiosity to reopen the app tomorrow.",
            "If this were your studio's live build, which dashboard metrics would raise the alarm before you incinerate thousands of dollars on paid user acquisition?",
            "Clear Garden is a hypothetical case study. But the mistakes above happen every single day across studios worldwide.",
            "Throughout this playbook, we will continually return to Clear Garden to translate high-level monetization principles into concrete, screen-by-screen design solutions."
        ]
    }
}
print("Front matter module loaded.")
