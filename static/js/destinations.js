let indiaMarkers = [];
let worldMarkers = [];


const DESTINATIONS = [

  /* ================= INDIA ================= */

  // Popular
  "Goa", "Manali", "Jaipur", "Kerala", "Rishikesh", "Varanasi",
  "Agra", "Udaipur", "Shimla", "Darjeeling", "Ooty",
  "Munnar", "Alleppey", "Wayanad", "Coorg",

  
// Kashmir & J&K
"Kashmir",
"Jammu and Kashmir",
"Srinagar",
"Gulmarg",
"Pahalgam",
"Sonamarg",
"Jammu",


  // Hill Stations
  "Mussoorie", "Nainital", "Auli", "Lansdowne", "Chopta",
  "Dalhousie", "Khajjiar", "Kasauli", "Kufri",
  "Gangtok", "Pelling", "Kalimpong",
  "Tawang", "Bomdila",
  "Leh", "Ladakh", "Spiti Valley", "Kasol", "Manikaran",
  "McLeod Ganj", "Dharamshala",

  // Spiritual / Religious
  "Haridwar", "Ayodhya", "Mathura", "Vrindavan",
  "Kedarnath", "Badrinath", "Hemkund Sahib",
  "Amritsar", "Golden Temple",
  "Tirupati", "Vellore",
  "Rameswaram", "Madurai",
  "Kanchipuram", "Srirangam",
  "Bodh Gaya",

  // Cities
  "Delhi", "Mumbai", "Pune", "Bangalore", "Chennai",
  "Hyderabad", "Kolkata", "Ahmedabad", "Surat",
  "Jaipur", "Jodhpur", "Bikaner",
  "Indore", "Bhopal", "Nagpur",
  "Patna", "Ranchi", "Raipur",
  "Bhubaneswar", "Cuttack",
  "Visakhapatnam", "Vijayawada",

  // Beaches & Islands
  "Andaman", "Port Blair", "Havelock Island",
  "Neil Island",
  "Lakshadweep",
  "Gokarna", "Varkala", "Kovalam",
  "Mahabalipuram", "Pondicherry",

  // Wildlife / Nature
  "Jim Corbett", "Ranthambore", "Bandhavgarh",
  "Kanha", "Pench", "Sundarbans",
  "Kaziranga", "Gir National Park",

  

  /* ================= INTERNATIONAL ================= */

  // Europe
  "Paris", "Nice", "Lyon",
  "London", "Edinburgh",
  "Rome", "Venice", "Florence", "Milan",
  "Barcelona", "Madrid",
  "Amsterdam", "Brussels",
  "Zurich", "Geneva",
  "Vienna", "Prague",
  "Budapest", "Warsaw",
  "Santorini", "Athens",
  "Dubrovnik",

  // Middle East
  "Dubai", "Abu Dhabi",
  "Doha",
  "Muscat",
  "Istanbul", "Cappadocia",
  "Jerusalem",

  // Asia
  "Bangkok", "Phuket", "Krabi", "Chiang Mai",
  "Singapore",
  "Kuala Lumpur", "Langkawi",
  "Bali", "Jakarta",
  "Tokyo", "Osaka", "Kyoto",
  "Seoul", "Busan",
  "Hong Kong", "Macau",
  "Hanoi", "Ho Chi Minh City",

  // Islands & Luxury
  "Maldives", "Mahe", "Praslin",
  "Mauritius",
  "Bora Bora",
  "Fiji",
  "Seychelles",

  // Americas
  "New York", "Los Angeles", "San Francisco",
  "Las Vegas", "Chicago",
  "Miami", "Orlando",
  "Washington DC",
  "Toronto", "Vancouver",
  "Mexico City", "Cancun",

  // Australia / NZ
  "Sydney", "Melbourne", "Brisbane",
  "Gold Coast",
  "Auckland", "Queenstown"
];





const MAP_DESTINATIONS = [
  // 🇮🇳 INDIA – Major & Popular Destinations
  { name: "Delhi", lat: 28.6139, lng: 77.2090 },
  { name: "Mumbai", lat: 19.0760, lng: 72.8777 },
  { name: "Goa", lat: 15.2993, lng: 74.1240 },
  { name: "Bangalore", lat: 12.9716, lng: 77.5946 },
  { name: "Chennai", lat: 13.0827, lng: 80.2707 },
  { name: "Hyderabad", lat: 17.3850, lng: 78.4867 },
  { name: "Kolkata", lat: 22.5726, lng: 88.3639 },
  { name: "Jaipur", lat: 26.9124, lng: 75.7873 },
  { name: "Agra", lat: 27.1767, lng: 78.0081 },
  { name: "Manali", lat: 32.2396, lng: 77.1887 },
  { name: "Kashmir", lat: 34.0837, lng: 74.7973 },
  { name: "Rishikesh", lat: 30.0869, lng: 78.2676 },
  { name: "Udaipur", lat: 24.5854, lng: 73.7125 },
  { name: "Kerala", lat: 10.8505, lng: 76.2711 },
  { name: "Andaman", lat: 11.7401, lng: 92.6586 },

  // 🌍 INTERNATIONAL – Top Global Travel Cities
  { name: "Paris", lat: 48.8566, lng: 2.3522 },
  { name: "London", lat: 51.5074, lng: -0.1278 },
  { name: "New York", lat: 40.7128, lng: -74.0060 },
  { name: "Dubai", lat: 25.2048, lng: 55.2708 },
  { name: "Singapore", lat: 1.3521, lng: 103.8198 },
  { name: "Bangkok", lat: 13.7563, lng: 100.5018 },
  { name: "Tokyo", lat: 35.6762, lng: 139.6503 },
  { name: "Rome", lat: 41.9028, lng: 12.4964 },
  { name: "Barcelona", lat: 41.3851, lng: 2.1734 },
  { name: "Amsterdam", lat: 52.3676, lng: 4.9041 },
  { name: "Istanbul", lat: 41.0082, lng: 28.9784 },
  { name: "Zurich", lat: 47.3769, lng: 8.5417 },
  { name: "Sydney", lat: -33.8688, lng: 151.2093 },
  { name: "Bali", lat: -8.3405, lng: 115.0920 },
  { name: "Maldives", lat: 3.2028, lng: 73.2207 }
];

const blueIcon = L.icon({
  iconUrl: "https://cdn-icons-png.flaticon.com/512/684/684908.png",
  iconSize: [32, 32],
  iconAnchor: [16, 32],
  popupAnchor: [0, -32]
});


