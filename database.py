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

    cursor.execute("SELECT COUNT(*) FROM mentors")
    count = cursor.fetchone()[0]

    if count == 0:
        mentors = [

            # Medicine
            ("Dr. James Whitfield","USA","USD","Medicine","Retired Chief of Cardiology, Mayo Clinic","35 years as a cardiologist at Mayo Clinic. I help medical students, nursing students, and health startups understand clinical concepts, career paths in medicine, and patient care best practices.","English","60","https://randomuser.me/api/portraits/men/32.jpg"),
            ("Dr. Ananya Krishnan","India","INR","Medicine","Retired Professor of Pharmacology, AIIMS Delhi","30 years teaching pharmacology at AIIMS Delhi. I mentor MBBS and nursing students on pharmacology, research methodology, and medical exam preparation. First session always free.","English, Tamil, Hindi","8","https://randomuser.me/api/portraits/women/44.jpg"),

            # Engineering
            ("Mr. Robert Hayes","UK","GBP","Engineering","Retired Principal Engineer, Rolls-Royce Aerospace","40 years in aerospace engineering at Rolls-Royce. I guide engineering students and early-stage hardware startups on mechanical design, systems engineering, and career growth in the aerospace industry.","English","50","https://randomuser.me/api/portraits/men/55.jpg"),
            ("Mr. Suresh Iyer","India","INR","Engineering","Retired Senior Engineer, ISRO","32 years at ISRO working on satellite launch systems. I mentor engineering students aspiring to work in space technology, GATE preparation, and research careers in aerospace and electronics.","English, Tamil, Hindi","15","https://randomuser.me/api/portraits/men/41.jpg"),

            # IT / Software
            ("Mr. Rajesh Nair","India","INR","IT / Software","Retired VP Engineering, Infosys","30 years building enterprise software at Infosys. I help CS students, junior developers, and IT startups with system design, career advice, coding best practices, and technical interview preparation.","English, Malayalam, Hindi","12","https://randomuser.me/api/portraits/men/23.jpg"),
            ("Mr. Ian Thompson","Ireland","EUR","IT / Software","Retired Full Stack Developer, CodeWorks","Committed to helping mentees improve their coding skills and advance their careers. Expertise in web development, JavaScript, Python, and agile methodologies.","English","40","https://randomuser.me/api/portraits/men/36.jpg"),
            ("Mr. Bob Smith","UK","GBP","IT / Software","Retired Data Scientist, DataSolutions","Experienced in machine learning and data analysis, eager to share knowledge. I mentor students and professionals on Python, ML algorithms, data visualisation, and breaking into the data science field.","English, French","45","https://randomuser.me/api/portraits/men/15.jpg"),

            # Finance / CA
            ("Ms. Linda Hoffman","Germany","EUR","Finance / CA","Retired CFO, Deutsche Bank","28 years in corporate finance and investment banking at Deutsche Bank. I help finance students, accounting professionals, and small business owners understand financial modelling, budgeting, and business valuation.","English, German","55","https://randomuser.me/api/portraits/women/12.jpg"),
            ("Mr. George Miller","Netherlands","EUR","Finance / CA","Retired Financial Analyst, FinCorp","Dedicated to mentoring aspiring finance professionals and sharing industry knowledge. Expert in investment analysis, portfolio management, and financial planning for individuals and businesses.","English, Dutch","45","https://randomuser.me/api/portraits/men/67.jpg"),

            # Government / IAS
            ("Mrs. Priya Venkataraman","India","INR","Government / IAS","Retired IAS Officer, Government of Tamil Nadu","32 years in Indian Administrative Service. I help UPSC aspirants with strategy, interview preparation, and understanding how government administration actually works on the ground.","English, Tamil, Telugu","10","https://randomuser.me/api/portraits/women/68.jpg"),
            ("Mr. Ramesh Chandra","India","INR","Government / IAS","Retired IPS Officer, Government of India","28 years in the Indian Police Service. I mentor IPS and UPSC aspirants, helping them understand law enforcement, public administration, and the realities of civil service careers.","English, Hindi, Bengali","12","https://randomuser.me/api/portraits/men/52.jpg"),

            # Teaching / Academia
            ("Prof. Susan Okafor","Canada","CAD","Teaching / Academia","Retired Professor of Computer Science, University of Toronto","25 years in academia at University of Toronto. I mentor PhD students, researchers, and anyone looking to publish their first paper. I also guide undergraduates struggling with algorithms and data structures.","English, French","45","https://randomuser.me/api/portraits/women/90.jpg"),
            ("Prof. Meena Pillai","India","INR","Teaching / Academia","Retired Principal, Kendriya Vidyalaya","35 years in education as teacher and principal. I mentor school teachers, education professionals, and students on pedagogy, career guidance, and navigating the Indian education system.","English, Malayalam, Hindi","8","https://randomuser.me/api/portraits/women/55.jpg"),

            # Entrepreneurship
            ("Mr. David Okonkwo","Nigeria","USD","Entrepreneurship","Retired Founder & CEO, AfriTech Ventures","Built and exited three tech companies across West Africa. I mentor founders and small business owners on fundraising, product-market fit, scaling in emerging markets, and avoiding common startup mistakes.","English, Yoruba","20","https://randomuser.me/api/portraits/men/74.jpg"),
            ("Ms. Hannah Davis","Sweden","USD","Entrepreneurship","Retired Founder, StartupHub","Passionate about guiding aspiring entrepreneurs through the challenges of starting a business. Experience in B2B SaaS, Nordic startup ecosystem, and scaling from 0 to 1.","English, Swedish","35","https://randomuser.me/api/portraits/women/33.jpg"),
            ("Mr. Charlie Lee","Canada","CAD","Entrepreneurship","Retired Product Manager, InnovateX","Dedicated to guiding aspiring product managers through their career journeys. Expert in product strategy, agile development, user research, and transitioning from engineering to product roles.","English, Mandarin","50","https://randomuser.me/api/portraits/men/29.jpg"),

            # Law
            ("Mr. Carlos Mendez","Mexico","USD","Law","Retired Senior Advocate, Supreme Court of Mexico","35 years practising constitutional and corporate law. I help law students, startups needing legal guidance, and small businesses understand contracts, compliance, and legal risk management.","English, Spanish","35","https://randomuser.me/api/portraits/men/47.jpg"),
            ("Ms. Fatima Al-Hassan","UAE","USD","Law","Retired Corporate Lawyer, Dubai International Law Firm","25 years in international corporate law across the Middle East. I mentor law students and startups on business law, international contracts, and building legal careers in the Gulf region.","English, Arabic","40","https://randomuser.me/api/portraits/women/25.jpg"),

            # Defence
            ("Col. Arvind Sharma (Retd.)","India","INR","Defence","Retired Colonel, Indian Army","30 years of service in the Indian Army including leadership in high-altitude operations. I mentor NDA/CDS aspirants, defence students, and young professionals on discipline, leadership, and strategic thinking.","English, Hindi","15","https://randomuser.me/api/portraits/men/61.jpg"),
            ("Cdr. John Mitchell (Retd.)","USA","USD","Defence","Retired Commander, US Navy","28 years in the United States Navy. I help military aspirants, veterans transitioning to civilian careers, and leadership students understand military strategy, team management, and career navigation.","English","50","https://randomuser.me/api/portraits/men/78.jpg"),

            # Cybersecurity
            ("Mr. Ethan Brown","Germany","EUR","Cybersecurity","Retired Cybersecurity Analyst, SecureTech","Passionate about mentoring individuals interested in cybersecurity careers. Expert in ethical hacking, network security, CISSP preparation, and building a career in information security.","English, German","55","https://randomuser.me/api/portraits/men/19.jpg"),
            ("Ms. Priya Sharma","India","INR","Cybersecurity","Retired CISO, Tata Consultancy Services","25 years in information security at TCS. I mentor cybersecurity aspirants, IT professionals transitioning to security roles, and startups on building secure systems and compliance frameworks.","English, Hindi, Marathi","20","https://randomuser.me/api/portraits/women/17.jpg"),

            # Architecture
            ("Ms. Julia Martinez","Spain","EUR","Architecture","Retired Senior Architect, DesignPro","Eager to mentor individuals pursuing careers in architecture and urban planning. Expert in sustainable architecture, green building design, and helping fresh graduates build their first portfolio.","English, Spanish","40","https://randomuser.me/api/portraits/women/82.jpg"),

            # Agriculture
            ("Mr. Krishnaswamy Rajan","India","INR","Agriculture","Retired Agriculture Officer, Government of Karnataka","30 years as an agriculture officer promoting sustainable farming across Karnataka. I help farmers, agri-tech startups, and agricultural students with modern farming techniques and government schemes.","English, Kannada, Tamil","8","https://randomuser.me/api/portraits/men/88.jpg"),

            # Journalism / Media
            ("Ms. Fiona Wilson","France","EUR","Journalism / Media","Retired Senior Editor, Le Monde Digital","25 years in journalism and digital media. I mentor aspiring journalists, content creators, and media students on storytelling, investigative journalism, and building a career in the digital media industry.","English, French","35","https://randomuser.me/api/portraits/women/59.jpg"),

            # Social Work
            ("Ms. Diana Garcia","Australia","AUD","Social Work","Retired Lead Social Worker, Community Care Australia","Committed to helping mentees develop careers in social work, community development, and NGO management. 30 years working with vulnerable communities across Australia and Southeast Asia.","English, Spanish","30","https://randomuser.me/api/portraits/women/71.jpg"),
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