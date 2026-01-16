# List of Indian destinations (can be expanded)
INDIAN_DESTINATIONS = [
    # 🌴 Beaches
    "goa",
    "andaman",
    "lakshadweep",
    "kovalam",
    "varkala",
    "gokarna",
    "pondicherry",
    "alibaug",

    # 🏔️ Hills & Mountains
    "manali",
    "shimla",
    "mussoorie",
    "nainital",
    "darjeeling",
    "gangtok",
    "leh",
    "ladakh",
    "spiti",
    "kasol",
    "kashmir",
    "gulmarg",
    "pahalgam",
    "sonmarg",
    "auli",

    # 🕌 Heritage & Culture
    "jaipur",
    "udaipur",
    "jodhpur",
    "jaisalmer",
    "agra",
    "khajuraho",
    "hampi",
    "madurai",
    "thanjavur",
    "amritsar",
    "varanasi",
    "ayodhya",

    # 🌿 Nature & Wildlife
    "kerala",
    "munnar",
    "thekkady",
    "wayanad",
    "coorg",
    "chikmagalur",
    "ooty",
    "kodaikanal",
    "rishikesh",
    "haridwar",
    "jim corbett",

    # 🏙️ Major Cities
    "delhi",
    "mumbai",
    "bangalore",
    "chennai",
    "hyderabad",
    "kolkata",
    "pune",
    "ahmedabad",
    "surat",
    "indore",
    "bhopal",
    "nagpur",
    "lucknow",
    "kanpur",
    "patna",
    "ranchi",
    "raipur",
    "bhubaneswar",

    # 🌄 North-East India
    "shillong",
    "cherrapunji",
    "tawang",
    "kaziranga",
    "imphal",
    "aizawl",
    "kohima",
    "dimapur",

    # 🛕 Spiritual & Pilgrimage
    "tirupati",
    "shirdi",
    "vaishno devi",
    "kedarnath",
    "badrinath",
    "dwarka",
    "somnath",
    "rameswaram",
    "kanyakumari",

    # 🌇 Weekend / Popular Escapes
    "lonavala",
    "mahabaleshwar",
    "mount abu",
    "saputara",
    "panchgani"
]


DOMESTIC_TRAVEL_COST = {
    "short": {"Train": 1500, "Flight": 4000},
    "medium": {"Train": 3000, "Flight": 7000},
    "long": {"Train": 5000, "Flight": 12000}
}

DESTINATION_DISTANCE_MAP = {
    # Short distance (within / near same state or nearby)
    "delhi": "short",
    "noida": "short",
    "gurgaon": "short",
    "faridabad": "short",
    "ghaziabad": "short",
    "mumbai": "short",
    "navi mumbai": "short",
    "thane": "short",
    "pune": "short",
    "bangalore": "short",
    "mysore": "short",
    "chennai": "short",
    "pondicherry": "short",
    "hyderabad": "short",
    "secunderabad": "short",
    "kolkata": "short",
    "howrah": "short",
    "ahmedabad": "short",
    "surat": "short",
    "vadodara": "short",

    # Medium distance (inter-state but reasonable)
    "jaipur": "medium",
    "udaipur": "medium",
    "jodhpur": "medium",
    "ajmer": "medium",
    "rishikesh": "medium",
    "haridwar": "medium",
    "dehradun": "medium",
    "shimla": "medium",
    "chandigarh": "medium",
    "amritsar": "medium",
    "agra": "medium",
    "varanasi": "medium",
    "ayodhya": "medium",
    "bhopal": "medium",
    "indore": "medium",
    "nagpur": "medium",
    "patna": "medium",
    "gaya": "medium",
    "bhubaneswar": "medium",
    "cuttack": "medium",
    "raipur": "medium",
    "ranchi": "medium",
    "gangtok": "medium",
    "darjeeling": "medium",
    "shillong": "medium",

    # Long distance (cross-country / tourism heavy)
    "goa": "long",
    "kerala": "long",
    "kochi": "long",
    "munnar": "long",
    "alleppey": "long",
    "ooty": "long",
    "kodaikanal": "long",
    "manali": "long",
    "kasol": "long",
    "spiti": "long",
    "leh": "long",
    "ladakh": "long",
    "srinagar": "long",
    "gulmarg": "long",
    "pahalgam": "long",
    "port blair": "long",
    "lakshadweep": "long",
    "kanyakumari": "long",
    "tirupati": "long",
    "madurai": "long",
    "trivandrum": "long"
}

ISLAND_DESTINATIONS = {
    "andaman",
    "andaman and nicobar",
    "andaman and nicobar islands",
    "lakshadweep"
}

# Kashmir & J&K
"kashmir",
"srinagar",
"gulmarg",
"pahalgam",
"sonamarg",
"jammu",
"jammu and kashmir"

DESTINATION_DISTANCE_MAP.update({
    "kashmir": "long",
    "srinagar": "long",
    "gulmarg": "long",
    "pahalgam": "long",
    "sonamarg": "long",
    "jammu": "medium",
    "jammu and kashmir": "long"
})



INDIAN_DESTINATIONS = set(DESTINATION_DISTANCE_MAP.keys())


DESTINATION_ITINERARIES = {


    "goa": [
        "Baga & Calangute Beach",
        "Fort Aguada & Candolim",
        "Dudhsagar Waterfalls",
        "Anjuna Beach & Water Sports",
        "Casino Cruise & Nightlife",
        "Shopping at Panaji "
    ],

    "manali": [
        "Mall Road & Local Sightseeing",
        "Solang Valley Adventure",
        "Rohtang Pass / Atal Tunnel",
        "Hadimba Temple & Old Manali",
        "Local Markets"
    ],

    "jaipur": [
        "Amber Fort",
        "City Palace & Jantar Mantar",
        "Hawa Mahal & Bapu Bazaar",
        "Nahargarh Fort Sunset",
        
    ],

    "kerala": [
        "Munnar Tea Gardens",
        "Eravikulam National Park",
        "Alleppey Houseboat Cruise",
        "Kovalam Beach",
        
    ],

    "ooty": [
        "Ooty Lake & Botanical Garden",
        "Doddabetta Peak",
        "Tea Estates & Factory",
        "Coonoor & Toy Train",
        
    ],

    "udaipur": [
        "City Palace & Lake Pichola Boat Ride",
        "Jag Mandir & Local Markets",
        "Sajjangarh Palace Sunset",
        
    ],

    "shimla": [
        "Mall Road & Ridge",
        "Jakhoo Temple",
        "Kufri Excursion",
        "Local Shopping "
    ],

    "rishikesh": [
        "Ganga Aarti at Triveni Ghat",
        "River Rafting",
        "Laxman Jhula & Cafes",
        "Yoga "
    ],

    "darjeeling": [
        "Tiger Hill Sunrise",
        "Batasia Loop & War Memorial",
        "Tea Gardens",
        
    ],

    "varanasi": [
        "Ganga Aarti",
        "Boat Ride on Ganges",
        "Kashi Vishwanath Temple",
        
    ],

    "agra": [
        "Taj Mahal",
        "Agra Fort",
        "Mehtab Bagh",
        
    ],

    "mysore": [
        "Mysore Palace",
        "Chamundi Hills",
        "Brindavan Gardens",
        
    ],

    "leh": [
        "Leh Palace & Local Market",
        "Pangong Lake",
        "Nubra Valley",
        "Monasteries"
    ],

    "amritsar": [
        "Golden Temple",
        "Jallianwala Bagh",
        "Wagah Border Ceremony",
       
    ],

    "andaman": [
        "Cellular Jail & Light Show",
        "Radhanagar Beach",
        "Snorkeling & Water Sports",
        
    ],

    "delhi": [
        "India Gate & Rashtrapati Bhavan",
        "Red Fort & Chandni Chowk",
        "Qutub Minar & Lotus Temple",
        "Connaught Place & Shopping",
        
    ],

    "mumbai": [
        "Gateway of India & Marine Drive",
        "Elephanta Caves",
        "Juhu Beach & Bandra",
        "Shopping & Nightlife",
       
    ],

    "bangalore": [
        "Cubbon Park & MG Road",
        "Lalbagh Botanical Garden",
        "Nandi Hills",
        "Shopping & Cafés",
        
    ],

      # 🌍 INTERNATIONAL DESTINATIONS (15)

    "paris": [
        "Eiffel Tower & Seine Cruise",
        "Louvre Museum",
        "Notre-Dame & Latin Quarter",
        "Versailles Palace",
        
    ],

    "dubai": [
        "Burj Khalifa & Dubai Mall",
        "Desert Safari",
        "Palm Jumeirah & Atlantis",
        "Dubai Marina Cruise",
        
    ],

    "bali": [
        "Ubud Rice Terraces",
        "Monkey Forest & Temples",
        "Nusa Penida Tour",
        "Beach Clubs & Sunset",
       
    ],

    "maldives": [
        "Resort Check-in & Relaxation",
        "Snorkeling & Water Sports",
        "Island Hopping",
        "Spa & Leisure",
        
    ],

    "london": [
        "Buckingham Palace & Big Ben",
        "London Eye & Thames Cruise",
        "British Museum",
        "Oxford Street Shopping",
        
    ],

    "rome": [
        "Colosseum & Roman Forum",
        "Vatican City",
        "Trevi Fountain",
       
    ],

    "new york": [
        "Statue of Liberty",
        "Times Square",
        "Central Park",
        "Brooklyn Bridge",
        
    ],

    "bangkok": [
        "Grand Palace",
        "Wat Pho & Wat Arun",
        "Floating Market",
       
    ],

    "singapore": [
        "Marina Bay Sands & Merlion",
        "Sentosa Island",
        "Universal Studios",
        "Gardens by the Bay",
        
    ],

    "istanbul": [
        "Hagia Sophia",
        "Blue Mosque",
        "Bosphorus Cruise",
        "Grand Bazaar",
        
    ],

    "tokyo": [
        "Shibuya Crossing",
        "Asakusa Temple",
        "Tokyo Tower",
        
    ],

    "seoul": [
        "Gyeongbokgung Palace",
        "Bukchon Hanok Village",
        "Myeongdong Shopping",
       
    ],

    "sydney": [
        "Sydney Opera House",
        "Harbour Bridge",
        "Bondi Beach",
        
    ],

    "barcelona": [
        "Sagrada Familia",
        "Park Güell",
        "La Rambla",
       
    ],

    "amsterdam": [
        "Canal Cruise",
        "Anne Frank House",
        "Van Gogh Museum",
        
    ]
}