# ElderEdge — Unlock the World's Retired Expertise

> *"The greatest waste in the world is the difference between what we are 
> and what we could become."*

## The Problem Nobody Is Solving

Every day, thousands of brilliant professionals retire — surgeons who 
performed 10,000 surgeries, engineers who built bridges and satellites, 
IAS officers who ran entire districts, entrepreneurs who built companies 
from nothing. They leave their careers carrying **decades of irreplaceable, 
hard-won knowledge.**

And that knowledge quietly disappears.

At the same time, a student in Madurai can't afford career guidance. A 
small business owner in Lagos doesn't know how to file taxes. A nursing 
student in Brazil is failing pharmacology with no one to turn to. A 
first-generation entrepreneur in rural India has a great idea but zero 
mentorship.

**Quality expertise has always been a privilege of geography and wealth.**

---

## What ElderEdge Does

ElderEdge is a **global micro-mentoring platform** that turns retirement 
into impact — and turns inaccessible expertise into affordable opportunity.

Retired professionals across **12+ domains** — medicine, engineering, IT, 
law, finance, government, defence, entrepreneurship and more — offer 
**30-minute sessions** to students and small businesses worldwide.

A mentee describes their problem in plain language. Our **Llama 3 AI** 
reads every mentor profile and returns the **top 3 best-fit matches** — 
not keyword filters, but genuine semantic understanding of who can help 
and why.

Sessions are priced in **local currency**, making the same world-class 
guidance affordable whether you're in New York or Nairobi, London or 
Lucknow. **The first session is always free.**

---

## Why ElderEdge Is Different

| Platform | What they do | What's missing |
|---|---|---|
| LinkedIn | Connects working professionals | Ignores retired experts entirely |
| Internshala | Connects students to companies | Not mentor-focused |
| Toptal / Clarity | Expert consulting | Expensive, not accessible |
| **ElderEdge** | **Retired pros → students & SMEs** | **Nothing like this exists** |

No platform today specifically activates **retired professionals** as 
affordable micro-mentors across every domain, every country, every 
currency. That gap is exactly where ElderEdge lives.

---

## Two Problems. One Platform.

**For retired professionals:**
- Turn lifetime expertise into supplemental income
- Stay intellectually active and socially connected
- Leave a legacy — pass knowledge before it's lost
- Reach learners across the world from home

**For students and small businesses:**
- Access genuine expertise at a fraction of consulting rates
- No geographic barriers — mentor anywhere, anytime
- First session free — zero risk, zero commitment
- Priced in your local currency — genuinely affordable

---

## Features

- **AI-Powered Matching** — Describe your problem in plain language. Llama 3 ranks the top 3 mentors with personalised reasons
- **12+ Domains** — Medicine, Engineering, IT, Finance, Government, Law, Defence, Teaching, Entrepreneurship, and more
- **Global Pricing** — Sessions auto-priced in local currency (USD, GBP, INR, EUR, CAD, NGN...)
- **Free First Session** — Zero risk for every new mentee
- **Mentor Signup** — Any retired professional can join and start earning
- **Booking System** — Pick a slot, confirm session goal, get a Google Meet link instantly
- **Reviews** — Star ratings and feedback build mentor trust scores

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, Vanilla JS |
| Backend | Python, Flask, Flask-CORS |
| Database | SQLite (built into Python) |
| AI Matching | Llama 3.3 70B via Groq API (free tier) |
| Deployment | Render.com (backend), served via Flask |
| Total Cost | ₹0 |

---

## Project Structure

```
elderedge/
├── app.py              # Flask backend — all 8 API routes
├── database.py         # SQLite setup + seed mentor data
├── ElderEdge.db        # Auto-generated database
├── .env                # API keys (not committed)
├── requirements.txt    # Python dependencies
└── frontend/
    ├── index.html      # Home — mentor search & discovery
    ├── profile.html    # Mentor profile page
    ├── booking.html    # Book a session
    ├── ai_match.html   # AI mentor matching
    ├── signup.html     # Mentor onboarding
    ├── style.css       # Global dark luxury theme
    └── utils.js        # Shared API helpers
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/mentors` | List all mentors (filter by domain, country, search) |
| GET | `/mentors/<id>` | Get single mentor profile |
| POST | `/mentors` | Register a new mentor |
| POST | `/bookings` | Create a booking |
| GET | `/bookings/<mentor_id>` | Get bookings for a mentor |
| GET | `/reviews/<mentor_id>` | Get reviews for a mentor |
| POST | `/reviews` | Submit a review |
| POST | `/ai/match` | AI mentor matching via Llama 3 |

---

## Getting Started

### Prerequisites

- Python 3.10+
- A free [Groq API key](https://console.groq.com)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/elderedge.git
cd elderedge

# 2. Install dependencies
pip install flask flask-cors groq python-dotenv

# 3. Add your Groq API key
echo "GROQ_API_KEY=your_key_here" > .env

# 4. Set up the database with seed mentors
python database.py

# 5. Start the Flask server
python app.py
```

### Open the App

```
http://127.0.0.1:5000/app/index.html
```

---

## How It Works

```
Mentee types a problem
        ↓
Llama 3 reads all mentor profiles
        ↓
Returns top 3 matches with reasons
        ↓
Mentee views profile → books slot
        ↓
Google Meet link generated instantly
        ↓
30-min session happens
        ↓
Mentee leaves review · Mentor earns
```

---

## Mentor Domains

Engineering · Medicine · IT / Software · Finance / CA · Government / IAS · Teaching / Academia · Entrepreneurship · Law · Defence · Agriculture · Architecture · Journalism

---

## Global Pricing

| Country | Price per session |
|---|---|
| USA | $20 – $80 |
| UK | £15 – £60 |
| India | ₹100 – ₹500 |
| Germany | €15 – €70 |
| Nigeria | $5 – $15 |
| Canada | CA$25 – CA$90 |

Mentor sets their own base price in USD. Platform displays it in the mentee's local currency.

---

## Social Impact

**For retired professionals**
- Earn supplemental income post-retirement
- Stay intellectually active and connected
- Share lifetime expertise before it's lost

**For students & small businesses**
- Access world-class expertise affordably
- No geographic barriers
- First session always free — zero risk

---

## Built With

- [Flask](https://flask.palletsprojects.com/) — Python web framework
- [Groq](https://groq.com/) — Free Llama 3 inference API
- [SQLite](https://sqlite.org/) — Lightweight embedded database
- [Llama 3.3 70B](https://llama.meta.com/) — Open source AI model

---

## Team

Built solo for **Quantum Sprint 2026** hackathon in under 24 hours.

---

## PPT link

https://in.docworkspace.com/d/sbCaem0Q4RhaZAeE_lyjcl6n4d2bw5ezgha?sa=601.1037
