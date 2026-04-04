import sqlite3

def init_db():
    conn = sqlite3.connect("ElderEdge.db")
    cursor = conn.cursor()
    
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS mentors(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            country TEXT,
            currency TEXT,
            domain TEXT,
            past_role TEXT,
            bio TEXT,
            languages TEXT,
            price_usd TEXT,
            photo_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS bookings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mentor_id INT,
            mentee_name TEXT,
            mentee_email TEXT,
            problem TEXT,
            session_date TEXT,
            is_free BOOLEAN,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (mentor_id) REFERENCES mentors(id)
        );
    
        CREATE TABLE IF NOT EXISTS reviews(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mentor_id INT,
            mentee_name TEXT,
            stars INT,
            comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Only insert if mentors table is empty
    cursor.execute("SELECT COUNT(*) FROM mentors")
    count = cursor.fetchone()[0]

    if count == 0:
        mentors = [
            (
                "Dr. James Whitfield",
                "USA", "USD",
                "Medicine",
                "Retired Chief of Cardiology, Mayo Clinic",
                "35 years as a cardiologist at Mayo Clinic. I help medical students, nursing students, and health startups understand clinical concepts, career paths in medicine, and patient care best practices.",
                "English",
                "60",
                "https://randomuser.me/api/portraits/men/32.jpg"
            ),
            (
                "Dr. Ananya Krishnan",
                "India", "INR",
                "Medicine",
                "Retired Professor of Pharmacology, AIIMS Delhi",
                "30 years teaching pharmacology at AIIMS. I mentor MBBS and nursing students on pharmacology, research methodology, and medical exam preparation. First session always free.",
                "English, Tamil, Hindi",
                "8",
                "https://randomuser.me/api/portraits/women/44.jpg"
            ),
            (
                "Mr. Robert Hayes",
                "UK", "GBP",
                "Engineering",
                "Retired Principal Engineer, Rolls-Royce Aerospace",
                "40 years in aerospace engineering. I guide engineering students and early-stage hardware startups on mechanical design, systems engineering, and career growth in the aerospace industry.",
                "English",
                "50",
                "https://randomuser.me/api/portraits/men/55.jpg"
            ),
            (
                "Mrs. Priya Venkataraman",
                "India", "INR",
                "Government / IAS",
                "Retired IAS Officer, Government of Tamil Nadu",
                "32 years in Indian Administrative Service. I help UPSC aspirants with strategy, interview preparation, and understanding how government administration actually works on the ground.",
                "English, Tamil, Telugu",
                "10",
                "https://randomuser.me/api/portraits/women/68.jpg"
            ),
            (
                "Mr. David Okonkwo",
                "Nigeria", "USD",
                "Entrepreneurship",
                "Retired Founder & CEO, AfriTech Ventures",
                "Built and exited three tech companies across West Africa. I mentor founders and small business owners on fundraising, product-market fit, scaling in emerging markets, and avoiding common startup mistakes.",
                "English, Yoruba",
                "20",
                "https://randomuser.me/api/portraits/men/74.jpg"
            ),
            (
                "Ms. Linda Hoffman",
                "Germany", "EUR",
                "Finance / CA",
                "Retired CFO, Deutsche Bank",
                "28 years in corporate finance and investment banking. I help finance students, accounting professionals, and small business owners understand financial modelling, budgeting, and business valuation.",
                "English, German",
                "55",
                "https://randomuser.me/api/portraits/women/12.jpg"
            ),
            (
                "Mr. Rajesh Nair",
                "India", "INR",
                "IT / Software",
                "Retired VP Engineering, Infosys",
                "30 years building enterprise software at Infosys. I help CS students, junior developers, and IT startups with system design, career advice, coding best practices, and technical interview preparation.",
                "English, Malayalam, Hindi",
                "12",
                "https://randomuser.me/api/portraits/men/23.jpg"
            ),
            (
                "Prof. Susan Okafor",
                "Canada", "CAD",
                "Teaching / Academia",
                "Retired Professor of Computer Science, University of Toronto",
                "25 years in academia. I mentor PhD students, researchers, and anyone looking to publish their first paper. I also guide undergraduates struggling with algorithms, data structures, and research writing.",
                "English, French",
                "45",
                "https://randomuser.me/api/portraits/women/90.jpg"
            ),
            (
                "Col. Arvind Sharma (Retd.)",
                "India", "INR",
                "Defence",
                "Retired Colonel, Indian Army",
                "30 years of service in the Indian Army including leadership in high-altitude operations. I mentor NDA/CDS aspirants, defence students, and young professionals on discipline, leadership, and strategic thinking.",
                "English, Hindi",
                "15",
                "https://randomuser.me/api/portraits/men/61.jpg"
            ),
            (
                "Mr. Carlos Mendez",
                "Mexico", "USD",
                "Law",
                "Retired Senior Advocate, Supreme Court of Mexico",
                "35 years practising constitutional and corporate law. I help law students, startups needing legal guidance, and small businesses understand contracts, compliance, and legal risk management.",
                "English, Spanish",
                "35",
                "https://randomuser.me/api/portraits/men/47.jpg"
            ),
        ]
    
        cursor.executemany("""
            INSERT INTO mentors (name, country, currency, domain, past_role, bio, languages, price_usd, photo_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, mentors)
    
        print(f"Inserted {len(mentors)} mentor profiles successfully.")
    else:
        print(f"Database already has {count} mentors. Skipping seed.")

    conn.commit()
    conn.close()
    print("Database ready.")


if __name__ == "__main__":
    init_db()

