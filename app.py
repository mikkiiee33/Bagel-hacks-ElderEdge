from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()

app = Flask(__name__)
CORS(app)

DB = "ElderEdge.db"
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ── Serve Frontend ─────────────────────────────────────────

@app.route("/app")
@app.route("/app/")
def serve_home():
    return send_from_directory("frontend", "index.html")

@app.route("/app/<path:filename>")
def serve_page(filename):
    return send_from_directory("frontend", filename)

# ── DB helper ──────────────────────────────────────────────
def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def row_to_dict(row):
    return dict(row) if row else None

def rows_to_list(rows):
    return [dict(r) for r in rows]

# ── MENTORS ────────────────────────────────────────────────

@app.route("/mentors", methods=["GET"])
def get_mentors():
    domain  = request.args.get("domain")
    country = request.args.get("country")
    search  = request.args.get("search")

    query  = "SELECT * FROM mentors WHERE 1=1"
    params = []

    if domain:
        query += " AND domain = ?"
        params.append(domain)
    if country:
        query += " AND country = ?"
        params.append(country)
    if search:
        query += " AND (name LIKE ? OR bio LIKE ? OR domain LIKE ? OR country LIKE ?)"
        like = f"%{search}%"
        params.extend([like, like, like, like])

    query = query.replace("SELECT *", "SELECT *, price as price_usd")
    query += " ORDER BY created_at DESC"

    conn = get_db()
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return jsonify(rows_to_list(rows))


@app.route("/mentors/<int:mentor_id>", methods=["GET"])
def get_mentor(mentor_id):
    conn = get_db()
    row  = conn.execute("SELECT * FROM mentors WHERE id = ?", (mentor_id,)).fetchone()
    conn.close()
    if not row:
        return jsonify({"error": "Mentor not found"}), 404
    return jsonify(row_to_dict(row))


@app.route("/mentors", methods=["POST"])
def create_mentor():
    data = request.get_json()
    required = ["name", "country", "currency", "domain", "past_role", "bio", "languages", "price_usd"]
    for field in required:
        if not data.get(field):
            return jsonify({"error": f"Missing field: {field}"}), 400

    conn = get_db()
    cur  = conn.execute("""
        INSERT INTO mentors (name, country, currency, domain, past_role, bio, languages, price_usd, photo_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["name"], data["country"], data["currency"],
        data["domain"], data["past_role"], data["bio"],
        data["languages"], str(data["price_usd"]),
        data.get("photo_url", "")
    ))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return jsonify({"id": new_id, "message": "Mentor created successfully"}), 201


# ── BOOKINGS ───────────────────────────────────────────────

@app.route("/bookings", methods=["POST"])
def create_booking():
    data = request.get_json()
    required = ["mentor_id", "mentee_name", "mentee_email", "problem", "session_date"]
    for field in required:
        if not data.get(field):
            return jsonify({"error": f"Missing field: {field}"}), 400

    import random, string
    def rand(n): return "".join(random.choices(string.ascii_lowercase, k=n))
    meet_link = f"https://meet.google.com/{rand(3)}-{rand(4)}-{rand(3)}"

    conn = get_db()
    conn.execute("""
        INSERT INTO bookings (mentor_id, mentee_name, mentee_email, problem, session_date, is_free)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["mentor_id"], data["mentee_name"], data["mentee_email"],
        data["problem"], data["session_date"], bool(data.get("is_free", False))
    ))
    conn.commit()
    conn.close()
    return jsonify({
        "message": "Booking confirmed",
        "meet_link": meet_link
    }), 201


@app.route("/bookings/<int:mentor_id>", methods=["GET"])
def get_bookings(mentor_id):
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM bookings WHERE mentor_id = ? ORDER BY created_at DESC",
        (mentor_id,)
    ).fetchall()
    conn.close()
    return jsonify(rows_to_list(rows))


# ── REVIEWS ────────────────────────────────────────────────

@app.route("/reviews/<int:mentor_id>", methods=["GET"])
def get_reviews(mentor_id):
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM reviews WHERE mentor_id = ? ORDER BY created_at DESC",
        (mentor_id,)
    ).fetchall()
    conn.close()
    return jsonify(rows_to_list(rows))


@app.route("/reviews", methods=["POST"])
def create_review():
    data = request.get_json()
    required = ["mentor_id", "mentee_name", "stars", "comment"]
    for field in required:
        if not data.get(field):
            return jsonify({"error": f"Missing field: {field}"}), 400

    if not (1 <= int(data["stars"]) <= 5):
        return jsonify({"error": "Stars must be between 1 and 5"}), 400

    conn = get_db()
    conn.execute("""
        INSERT INTO reviews (mentor_id, mentee_name, stars, comment)
        VALUES (?, ?, ?, ?)
    """, (data["mentor_id"], data["mentee_name"], int(data["stars"]), data["comment"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Review submitted"}), 201


# ── AI MATCHING ────────────────────────────────────────────

@app.route("/ai/match", methods=["POST"])
def ai_match():
    data    = request.get_json()
    problem = data.get("problem", "").strip()

    if not problem:
        return jsonify({"error": "Problem description is required"}), 400

    conn    = get_db()
    mentors = rows_to_list(conn.execute("SELECT * FROM mentors").fetchall())
    conn.close()

    if not mentors:
        return jsonify({"matches": []})

    mentor_lines = "\n".join([
        f'ID:{m["id"]} | {m["name"]} | {m["past_role"]} | Domain: {m["domain"]} | Country: {m["country"]}'
        for m in mentors
    ])

    prompt = f"""You are a mentor-matching assistant for ElderEdge, a global micro-mentoring platform.

A mentee has described their problem:
"{problem}"

Here are the available mentors:
{mentor_lines}

Your task: Pick the top 3 best-matching mentors for this problem.
Return ONLY a valid JSON array with exactly 3 objects, each having:
- "id": the mentor's integer ID
- "reason": a 1-2 sentence explanation of why this mentor is a great match

Example format:
[
  {{"id": 2, "reason": "Dr. Ananya has 30 years in pharmacology and specializes in helping medical students."}},
  {{"id": 1, "reason": "Dr. James brings 35 years of clinical experience ideal for health-related queries."}},
  {{"id": 7, "reason": "Rajesh has deep IT industry experience perfect for software career guidance."}}
]

Return ONLY the JSON array. No explanation, no markdown, no extra text."""

    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.3
        )
        raw = response.choices[0].message.content.strip()

        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        raw = raw.strip()

        matched = json.loads(raw)

        mentor_map = {m["id"]: m for m in mentors}
        results = []
        for item in matched:
            mid = int(item["id"])
            if mid in mentor_map:
                mentor_data = dict(mentor_map[mid])
                mentor_data["reason"] = item.get("reason", "Strong domain match.")
                results.append(mentor_data)

        return jsonify({"matches": results})

    except json.JSONDecodeError:
        fallback = mentors[:3]
        for m in fallback:
            m["reason"] = "Recommended based on your domain needs."
        return jsonify({"matches": fallback})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── HEALTH CHECK ───────────────────────────────────────────

@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ElderEdge API running",
        "endpoints": [
            "GET  /mentors",
            "GET  /mentors/<id>",
            "POST /mentors",
            "POST /bookings",
            "GET  /bookings/<mentor_id>",
            "GET  /reviews/<mentor_id>",
            "POST /reviews",
            "POST /ai/match"
        ]
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)