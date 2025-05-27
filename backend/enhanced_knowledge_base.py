knowledge_base = [
    {
        "id": "end_day",
        "question": "how to end your day in SFA",
        "keywords": ["end day", "finish day", "log off", "complete work", "wrap up"],
        "training_examples": [
            "how do I finish my work day",
            "what's the process to end shift",
            "how do I log off from work",
            "wrap up my daily tasks",
            "end my day in the app",
            "procedure for ending work"
        ],
        "answer": """To end your day in SFA:
1. Open the SFA app.
2. Tap the navigation menu (☰) at the top-left.
3. Scroll down and select "End Day."
Important: Ensure you sync your local records before ending your day.
4. Tap "End Day" to complete your submission.""",
        "suggestions": ["How to Sync Data", "How to Start Day"],
        "category": "daily_operations"
    },
    {
        "id": "sync_data",
        "question": "How to Sync Data in the SFA App",
        "keywords": ["sync data", "upload records", "data sync", "upload data"],
        "training_examples": [
            "how do I synchronize my data",
            "upload my SFA records",
            "make sure my data is saved",
            "sync local records",
            "upload visit logs"
        ],
        "answer": """To sync data in the SFA App:
1. Open the SFA App.
2. Tap the navigation menu (☰) at the top-left.
3. Scroll down and select "Sync Data."
4. A progress screen will show records uploading.
Ensure the sync completes successfully before other actions like "End Day."
You can view Company Name, User Name, App Version, and Day Start Time on this screen.""",
        "suggestions": ["How to End Day", "Troubleshooting Sync Issues"],
        "category": "daily_operations"
    },
    {
        "id": "start_day_visit",
        "question": "how to start day in SFA and begin visit in outlet",
        "keywords": ["start day", "begin visit", "commence shift", "begin work", "visit outlet"],
        "training_examples": [
            "how do I start my day in SFA",
            "begin my workday",
            "start my shift and go to a store",
            "how to begin visiting an outlet",
            "start daily activities in SFA",
            "start day"
        ],
        "answer": """To start your day in SFA:
1. Open the SFA app on your phone.
2. On the home page, tap the “Start Day” button at the bottom. The app automatically captures your current location.
3. After starting the day, you’ll see different tabs like Not Visited, Order, No Order, and All.
4. From the "Not Visited" list, choose any outlet you want to visit first.
5. Tap on “Begin Visit” to start your interaction with that store.
This marks the beginning of your daily field activity using the SFA app.""",
        "suggestions": ["How to Search Outlets", "Remote Order Placement"],
        "category": "daily_operations"
    },
    {
        "id": "search_outlets",
        "question": "How to Search and Identify Outlets in the SFA App",
        "keywords": ["search outlets", "find stores", "identify outlets", "outlet categories", "store list"],
        "training_examples": [
            "how do I find a store in SFA",
            "where can I see outlets",
            "how to categorize stores",
            "what are the different outlet types",
            "how to locate an outlet",
            "Go to the Stores section to see your store list. You can view store names, locations, and visit status.",
            "which stores do i visit today"
        ],
        "answer": """To search and identify outlets in the SFA App:
1. Open the SFA app on your mobile device.
2. On the home screen, tap the “Start Day” button. The app captures your current location and takes you to the Outlet List screen.
3. On this screen, you will see tabs such as Not Visited, Order, No Order, and All.
4. You can browse through these tabs to locate the outlet you want to visit.
5. Alternatively, use the search bar at the top to quickly find a specific outlet by typing its name.
Once your day is started, all outlets become visible and searchable.
Outlets are categorized based on their sales volume as follows:
🟣 Platinum – Highest sales
🟡 Gold – High sales
⚪ Silver – Medium sales
🟤 Bronze – Low sales
These categories help you prioritize your store visits effectively during the day.""",
        "suggestions": ["How to Start Day", "Remote Order Placement"],
        "category": "outlet_management"
    },
    {
        "id": "remote_order_placement",
        "question": "Remote Order Placement – Step-by-Step Guide",
        "keywords": ["remote order", "place order", "submit order", "order placement", "new order"],
        "training_examples": [
            "how to create a remote order",
            "steps to place an order remotely",
            "how do I submit an order from afar",
            "guide for remote ordering",
            "make a new order remotely"
        ],
        "answer": """To place a Remote Order in SFA:
1. Launch the SFA App.
2. On the Home Screen, tap "Start Day."
3. Tap the ☰ Menu icon (top-left) and select "Remote Order."
4. Select the desired outlet from the list (use search if needed).
5. The outlet’s product list opens. Select items by tapping "+", adjust quantities.
6. Tap the cart icon or "Next" to review.
7. Tap "Submit Order" to complete.
A confirmation message will appear once the order is successfully placed.""",
        "suggestions": ["How to View Schemes", "How to View Sales Summary"],
        "category": "order_management"
    },
    {
        "id": "my_rewards",
        "question": "How to View “My Rewards” in the SFA App",
        "keywords": ["my rewards", "view rewards", "incentives", "coins", "rank"],
        "training_examples": [
            "where can I see my rewards",
            "check my SFA incentives",
            "how many coins do I have",
            "what's my current rank",
            "see my performance rewards"
        ],
        "answer": """To view "My Rewards" in the SFA App:
1. Launch the SFA App.
2. On the home screen's bottom panel, tap "My Rewards."
3. You'll see three tabs:
    - Incentives: View Gross Revenue, SSG (Same Store Growth), ASSP (Average Sales per Store per Person).
    - My Coins: See total coins earned.
    - My Rank: Check your current rank compared to your peers or within your region.""",
        "suggestions": ["How to View Sales Summary", "Remote Order Placement"],
        "category": "performance_tracking"
    },
    {
        "id": "report_issue",
        "question": "How to Report a Technical Issue in the SFA App (via Customer Feedback):",
        "keywords": ["report issue", "technical issue", "customer feedback", "bug report", "raise ticket"],
        "training_examples": [
            "how do I report a problem with the app",
            "where to submit a technical problem",
            "send customer feedback",
            "report a bug in SFA",
            "how to create a support ticket"
        ],
        "answer": """To report a Technical Issue in the SFA App:
1. Open the SFA App on your mobile device.
2. On the Home Screen, tap on the “More” option (usually shown as three horizontal lines or dots in the bottom panel).
3. From the More menu, select “Customer Feedback.”
4. You will now see a feedback form on your screen.
5. Fill in the following details:
    - Ticket Category – Select the appropriate category for your issue.
    - Subject – Briefly explain the problem (e.g., “Unable to place order”).
    - Description – Provide a detailed explanation of the issue.
    - (Optional) Tap the attachment icon to upload a screenshot for clarity.
6. After entering all the information, tap on “Submit” to raise your ticket.""",
        "suggestions": ["How to Sync Data", "Common App Issues"],
        "category": "support"
    },
    {
        "id": "view_schemes",
        "question": "How to View Schemes in the SFA App",
        "keywords": ["view schemes", "check offers", "available schemes", "promotions", "how can I see the schemes in sfa app", "today's active promo schemes", "coke buddy schemes for this month"],
        "training_examples": [
            "where can I see current schemes",
            "how to check promotions",
            "look at available offers in SFA",
            "what are the active schemes",
            "how to find discounts",
            "show active promo schemes today",
            "tell me about coke buddy schemes this month"
        ],
        "answer": """To view Schemes in the SFA App:
1. Open the SFA App on your mobile device.
2. On the Home Screen, tap on “Start Day” to begin your day.
3. You will now see a list of outlets on your screen.
4. Select the desired outlet from the list and tap “Begin Visit.”
5. Once the visit is started, you can begin placing an order.
6. To view available schemes, tap the percent (%) icon located at the top-right corner of the screen.
7. A list of active schemes will appear. You can tap on any scheme to view more details about the offer.

Active promo today: "Buy 10 cases, get 1 free" on Sprite 600ml. You’ve sold 8 so far. Sell 2 more to unlock reward!
To see coke buddy schemes for this month, navigate to the schemes page in the app, usually found under 'Promotions' or within the outlet's order section after initiating a visit.""",
        "suggestions": ["Remote Order Placement", "How to View Sales Summary"],
        "category": "sales_promotion"
    },
    {
        "id": "view_sales_summary",
        "question": "How to View Sales Summary in SFA App:",
        "keywords": ["sales summary", "view sales", "my sales", "outlet sales", "performance metrics", "GR", "gross revenue", "pack wise sales summary", "monthly sale"],
        "training_examples": [
            "how to check my sales performance",
            "where to see sales figures",
            "view outlet sales data",
            "check gross revenue",
            "how to see sales by brand",
            "What is GR?",
            "Give my PACK WISE SALES SUMMARY?",
            "What is my monthly sale in this year ?"
        ],
        "answer": """To view Sales Summary in SFA App:
1. Open the SFA App on your mobile device.
2. On the Home Screen, tap on the More option (usually represented by three horizontal lines at the top-left corner).
3. From the menu, select "Sales Summary".
4. On the Sales Summary screen, you’ll see two main tabs at the top:
    - My Sales: This section shows your sales performance. You can view data by Category, Brand, SKU (Stock Keeping Unit). To filter by date, tap on the calendar icon near the “Select Date Range” bar. You can also view key performance metrics like Planned Calls, Call Compliance, Productive Calls, GR (Gross Revenue) Volume, Line per Call.
    - Outlet Sales: This section shows a list of outlets where orders have been placed. Tap on any outlet to see the details of the orders placed. You can view order details categorized by Category, Brand, SKU.

**GR (Gross Revenue)** is the total invoice value of the sale.

For a **pack-wise sales summary** (e.g., Thumsup sale in 500 cases for today), you would typically find this under the "My Sales" tab, filtered by SKU or Brand and then by date. The app provides a detailed breakdown within the sales summary.

To see your **monthly sales this year** (often represented by bar graphs), this feature is generally available in the "My Sales" section, where you can select a date range (e.g., month-to-month) to visualize your performance.""",
        "suggestions": ["How to View My Rewards", "How to Search Outlets"],
        "category": "performance_tracking"
    },
    {
        "id": "green_score",
        "question": "What is green score?",
        "keywords": ["green score", "green 2025", "parameters", "discipline", "driving returns", "djp compliance", "geo code compliance", "ired compliance", "strike rate", "same store growth", "sell in performance"],
        "training_examples": [
            "tell me about green score",
            "what are the green 2025 parameters"
        ],
        "answer": """The **GREEN 2025 Parameters** are split into two focus areas: **Discipline** and **Driving Returns**, each with 5 key metrics worth 20 points each (total 100).
Under **Discipline**:
1. **DJP Compliance** – following daily job protocols
2. **Geo Code Compliance Calls** – ensuring location-based tracking
3. **IRED Compliance** – meeting internal review standards

Under **Driving Returns**:
4. **Strike Rate** – measuring success per effort
5. **Same Store Growth** – tracking growth from existing outlets
This is the **SELL IN PERFORMANCE**.""",
        "suggestions": ["What is IRED score?", "What is Geo code?", "What is Strike Rate?"],
        "category": "performance_metrics"
    },
    {
        "id": "ired_score",
        "question": "What is Ired score?",
        "keywords": ["ired score", "integrated redscore", "evaluation parameter", "sell out performance", "in-store retail execution dashboard", "availability score", "cooler score", "activation score"],
        "training_examples": [
            "tell me about ired score",
            "what does ired stand for"
        ],
        "answer": """**IRED score** (Integrated Redscore) is an evaluation parameter out of 100.
This depicts the **SELL OUT Performance**.
IRED stands for **In-store Retail Execution Dashboard**. It's calculated based on:
* **Availability Score** (40%)
* **Cooler Score** (30%)
* **Activation Score** (20%)
* **Other Factors** (10%).""",
        "suggestions": ["What is Green Score?", "How to View Sales Summary"],
        "category": "performance_metrics"
    },
    {
        "id": "cbfs",
        "question": "What is CBFS?",
        "keywords": ["cbfs", "coke buddy orders", "retailers app"],
        "training_examples": [
            "what are cbfs",
            "explain cbfs"
        ],
        "answer": """**CBFS** refers to the **Coke Buddy orders** placed in the outlet retailers app.""",
        "suggestions": ["Remote Order Placement", "How to View Schemes"],
        "category": "order_management"
    },
    {
        "id": "geo_code",
        "question": "What is Geo code? Why is it important?",
        "keywords": ["geo code", "evaluation parameter", "physical visit", "location tracking"],
        "training_examples": [
            "what is geo code",
            "why is geo code important"
        ],
        "answer": """**Geo code** is an evaluation parameter that checks whether you physically visit an outlet or not. It's important for ensuring accurate location-based tracking and compliance with daily job protocols.""",
        "suggestions": ["What is Green Score?", "How to Start Day"],
        "category": "daily_operations"
    },
    {
        "id": "strike_rate",
        "question": "What is strike rate?",
        "keywords": ["strike rate", "orders placed", "visited outlets", "success per effort"],
        "training_examples": [
            "explain strike rate",
            "how is strike rate calculated"
        ],
        "answer": """**Strike rate** is the number of orders placed in relation to the number of outlets visited. It measures your success per effort.""",
        "suggestions": ["What is Green Score?", "Remote Order Placement"],
        "category": "performance_metrics"
    },
    {
        "id": "route_planning",
        "question": "route planning",
        "english": "Route planning helps you optimize your daily visits. Open the main menu, select your preferred route type, and the app will guide you efficiently.",
        "telugu": "రూట్ ప్లానింగ్ మీ రోజువారీ సందర్శనలను ఆప్టిమైజ్ చేయడంలో సహాయపడుతుంది. మెయిన్ మెనూ తెరచి, మీకు కావలసిన రూట్ రకాన్ని ఎంచుకోండి, యాప్ సమర్థవంతమైన మార్గాన్ని చూపుతుంది.",
        "keywords": ["route planning", "optimize visits", "daily route"],
        "suggestions": ["show my route", "pending store visits"],
        "category": "daily_operations"
    },
    {
        "id": "show_my_route",
        "question": "show my route",
        "english": "To view your route, go to the main menu and select \"My Route\". You’ll see your planned visits and can optimize the path.",
        "telugu": "మీ రూట్‌ను చూడటానికి, మెయిన్ మెనూ వెళ్లి \"My Route\" ఎంచుకోండి. ప్లాన్ చేసిన స్టోర్‌లు మరియు మార్గ వివరాలు కనిపిస్తాయి.",
        "keywords": ["my route", "view route", "planned visits"],
        "suggestions": ["route planning", "pending store visits"],
        "category": "daily_operations"
    },
    {
        "id": "current_promotions",
        "question": "current promotions",
        "english": "Current promotions are available in the \"Promotions\" section. Tap a promotion to see details, eligibility, and rewards.",
        "telugu": "ప్రస్తుత ప్రమోషన్లు \"Promotions\" సెక్షన్‌లో లభిస్తాయి. ప్రమోషన్‌ను ట్యాప్ చేసి, వివరాలు, అర్హతలు మరియు రివార్డ్స్ చూడండి.",
        "keywords": ["current promotions", "promotions", "offers"],
        "suggestions": ["How to View Schemes", "Remote Order Placement"],
        "category": "sales_promotion"
    },
    {
        "id": "my_performance",
        "question": "my performance",
        "english": "You can check your performance in the \"My Performance\" section. It shows daily goals, achievements, and your rank.",
        "telugu": "మీరు \"My Performance\" సెక్షన్‌లో మీ పనితీరును చూడవచ్చు. రోజువారీ లక్ష్యాలు, సాధన మరియు మీ ర్యాంక్ కనిపిస్తాయి.",
        "keywords": ["my performance", "daily goals", "achievements", "rank"],
        "suggestions": ["How to View Sales Summary", "How to View My Rewards"],
        "category": "performance_tracking"
    },
    {
        "id": "today_assigned_stores",
        "question": "which stores do i visit today",
        "english": "Today’s assigned stores: 1. ABC Supermarket (9 AM), 2. XYZ Mart (11 AM), 3. FreshPoint (2 PM). Check in at each store.",
        "telugu": "ఈ రోజు మీరు సందర్శించాల్సిన స్టోర్లు: 1. ABC Supermarket (ఉదయం 9), 2. XYZ Mart (ఉదయం 11), 3. FreshPoint (మధ్యాహ్నం 2). ప్రతి స్టోర్‌కి చెక్-ఇన్ చేయండి.",
        "keywords": ["assigned stores", "today's visits", "store schedule"],
        "suggestions": ["pending store visits", "How to Search Outlets"],
        "category": "daily_operations"
    },
    {
        "id": "daily_target",
        "question": "show my daily target",
        "english": "Your daily target is ₹15,000. You’ve achieved ₹8,500. Remaining target: ₹6,500.",
        "telugu": "మీ రోజువారీ టార్గెట్ ₹15,000. ఇప్పటివరకు మీరు ₹8,500 సాధించారు. మిగిలిన టార్గెట్ ₹6,500.",
        "keywords": ["daily target", "sales target", "remaining target"],
        "suggestions": ["my performance", "How to View Sales Summary"],
        "category": "performance_tracking"
    },
    {
        "id": "order_summary",
        "question": "order summary",
        "english": "Today’s orders: 12 total, worth ₹13,200. Top item: Coke 500ml (6 cases). 2 orders pending delivery.",
        "telugu": "ఈ రోజు ఆర్డర్లు: మొత్తం 12, విలువ ₹13,200. టాప్ ఐటమ్: కోక్ 500ml (6 కేసులు). 2 ఆర్డర్లు డెలివరీ పెండింగ్‌లో ఉన్నాయి.",
        "keywords": ["order summary", "today's orders", "pending orders"],
        "suggestions": ["Remote Order Placement", "How to View Sales Summary"],
        "category": "order_management"
    },
    {
        "id": "update_stock_images",
        "question": "how to update stock images",
        "english": "To update stock images, tap the camera icon next to the product, take a clear photo, and save.",
        "telugu": "స్టాక్ ఇమేజ్ అప్‌డేట్ చేయాలంటే, ప్రొడక్ట్ పక్కన కెమెరా ఐకాన్‌పై ట్యాప్ చేసి క్లియర్ ఫోటో తీసి సేవ్ చేయండి.",
        "keywords": ["stock images", "update images", "product photos"],
        "suggestions": ["report issue"],
        "category": "product_management"
    },
    {
        "id": "field_team_locations",
        "question": "show field team locations",
        "english": "Field team locations: 1. Ramesh – ABC Supermarket (9:10 AM), 2. Priya – XYZ Mart (10:45 AM), 3. John – FreshPoint (2:05 PM).",
        "telugu": "ఫీల్డ్ టీమ్ లొకేషన్లు: 1. రమేష్ – ABC Supermarket (ఉదయం 9:10), 2. ప్రియ – XYZ Mart (ఉదయం 10:45), 3. జాన్ – FreshPoint (మధ్యాహ్నం 2:05).",
        "keywords": ["field team", "team location", "sales team tracking"],
        "suggestions": ["geo code"],
        "category": "team_management"
    },
    {
        "id": "pending_store_visits",
        "question": "pending store visits",
        "english": "You have 2 pending visits today: FreshPoint and CityMart. Complete them before day end.",
        "telugu": "ఈ రోజు మీకు 2 పెండింగ్ స్టోర్ విజిట్లు ఉన్నాయి: FreshPoint మరియు CityMart. ఇవి రోజు ముగిసేలోపు పూర్తి చేయండి.",
        "keywords": ["pending visits", "incomplete visits", "stores to visit"],
        "suggestions": ["which stores do i visit today", "route planning"],
        "category": "daily_operations"
    }
]