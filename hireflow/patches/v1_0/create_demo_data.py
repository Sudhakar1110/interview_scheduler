# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.utils import today, add_days, now_datetime


def execute():
    """Create comprehensive demo data for all HireFlow modules"""
    _create_job_locations()
    _create_companies()
    _create_recruiters()
    _create_panel_members()
    _create_candidates()
    _create_job_postings()
    _create_job_applications()
    _create_interview_schedules()
    _create_interview_feedback()
    _create_offer_letters()
    _create_onboarding()
    _create_subscriptions()
    _create_payment_transactions()
    _create_messages()
    _create_notifications()
    frappe.db.commit()
    print("Comprehensive demo data created successfully.")
    print("=" * 50)


def _create_job_locations():
    locations = [
        {"location_name": "Remote - Global", "city": "", "state": "", "country": ""},
        {"location_name": "New York, USA", "city": "New York", "state": "New York", "country": "United States"},
        {"location_name": "San Francisco, USA", "city": "San Francisco", "state": "California", "country": "United States"},
        {"location_name": "Chicago, USA", "city": "Chicago", "state": "Illinois", "country": "United States"},
        {"location_name": "Austin, USA", "city": "Austin", "state": "Texas", "country": "United States"},
        {"location_name": "London, UK", "city": "London", "state": "England", "country": "United Kingdom"},
        {"location_name": "Berlin, Germany", "city": "Berlin", "state": "", "country": "Germany"},
        {"location_name": "Bangalore, India", "city": "Bangalore", "state": "Karnataka", "country": "India"},
        {"location_name": "Mumbai, India", "city": "Mumbai", "state": "Maharashtra", "country": "India"},
        {"location_name": "Toronto, Canada", "city": "Toronto", "state": "Ontario", "country": "Canada"},
    ]
    for loc in locations:
        if not frappe.db.exists("Job Location", loc["location_name"]):
            frappe.get_doc({"doctype": "Job Location", **loc}).insert(ignore_permissions=True)
    print("  Created 10 job locations")


def _create_companies():
    companies = [
        {
            "company_name": "TechCorp Inc.",
            "website": "https://techcorp.com",
            "industry": "Enterprise Software",
            "company_size": "501-1000",
            "description": "<p>TechCorp is a leading enterprise software company serving over 10,000 businesses worldwide. Our platform helps organizations streamline their operations, manage talent, and drive growth through innovative technology solutions.</p>",
            "founded_year": 2012,
            "headquarters": "San Francisco, USA",
            "contact_email": "hr@techcorp.com",
            "contact_phone": "+1-555-0100",
            "address": "123 Market Street, Suite 400",
            "city": "San Francisco",
            "state": "California",
            "country": "United States",
            "pincode": "94105",
            "social_links": "https://linkedin.com/company/techcorp\nhttps://twitter.com/techcorp",
            "is_active": 1,
        },
        {
            "company_name": "InnovateSoft Solutions",
            "website": "https://innovatesoft.com",
            "industry": "Healthcare Technology",
            "company_size": "51-200",
            "description": "<p>InnovateSoft is building the future of healthcare with AI-powered diagnostic tools and patient management platforms. Our mission is to make quality healthcare accessible to everyone through technology.</p>",
            "founded_year": 2018,
            "headquarters": "New York, USA",
            "contact_email": "careers@innovatesoft.com",
            "contact_phone": "+1-555-0200",
            "address": "456 Broadway Avenue",
            "city": "New York",
            "state": "New York",
            "country": "United States",
            "pincode": "10013",
            "social_links": "https://linkedin.com/company/innovatesoft\nhttps://twitter.com/innovatesoft",
            "is_active": 1,
        },
        {
            "company_name": "DataFlow Analytics",
            "website": "https://dataflow.io",
            "industry": "Data Analytics & BI",
            "company_size": "11-50",
            "description": "<p>DataFlow Analytics provides cutting-edge data visualization and business intelligence platforms for mid-market enterprises. We help companies make data-driven decisions with ease.</p>",
            "founded_year": 2020,
            "headquarters": "London, UK",
            "contact_email": "jobs@dataflow.io",
            "contact_phone": "+44-20-5555-0100",
            "address": "88 King's Road",
            "city": "London",
            "state": "England",
            "country": "United Kingdom",
            "pincode": "SW1A 1AA",
            "social_links": "https://linkedin.com/company/dataflow",
            "is_active": 1,
        },
        {
            "company_name": "CloudBase Systems",
            "website": "https://cloudbase.io",
            "industry": "Cloud Infrastructure",
            "company_size": "201-500",
            "description": "<p>CloudBase Systems provides enterprise-grade cloud infrastructure and DevOps solutions. We power thousands of applications worldwide with our reliable and scalable platform.</p>",
            "founded_year": 2016,
            "headquarters": "Austin, USA",
            "contact_email": "recruiting@cloudbase.io",
            "contact_phone": "+1-555-0300",
            "address": "789 Tech Boulevard",
            "city": "Austin",
            "state": "Texas",
            "country": "United States",
            "pincode": "73301",
            "is_active": 1,
        },
    ]
    for c in companies:
        if not frappe.db.exists("Company Profile", c["company_name"]):
            frappe.get_doc({"doctype": "Company Profile", **c}).insert(ignore_permissions=True)
    print("  Created 4 companies")


def _create_recruiters():
    recruiters = [
        {"recruiter_name": "Alice Johnson", "company": "TechCorp Inc.", "email": "alice.johnson@techcorp.com", "phone": "+1-555-0101", "designation": "Senior Recruiter", "department": "Talent Acquisition", "skills": "Technical Recruitment, Interviewing, HR Operations, Boolean Search", "is_active": 1},
        {"recruiter_name": "Carol Davis", "company": "TechCorp Inc.", "email": "carol.davis@techcorp.com", "phone": "+1-555-0102", "designation": "Recruiter", "department": "Talent Acquisition", "skills": "Screening, Interview Coordination, Offer Management, Campus Recruitment", "is_active": 1},
        {"recruiter_name": "Bob Smith", "company": "InnovateSoft Solutions", "email": "bob.smith@innovatesoft.com", "phone": "+1-555-0201", "designation": "Recruitment Lead", "department": "Human Resources", "skills": "Executive Search, Employer Branding, Talent Strategy, ATS Management", "is_active": 1},
        {"recruiter_name": "Diana Lee", "company": "CloudBase Systems", "email": "diana.lee@cloudbase.io", "phone": "+1-555-0301", "designation": "Technical Recruiter", "department": "People Operations", "skills": "Technical Recruitment, Engineering Hiring, DevOps Hiring, Diversity Sourcing", "is_active": 1},
    ]
    for r in recruiters:
        if not frappe.db.exists("Recruiter Profile", r["recruiter_name"]):
            frappe.get_doc({"doctype": "Recruiter Profile", **r}).insert(ignore_permissions=True)
    print("  Created 4 recruiters")


def _create_panel_members():
    members = [
        {
            "full_name": "Dr. James Wilson",
            "email": "james.wilson@techcorp.com",
            "phone": "+1-555-2001",
            "designation": "Engineering Director",
            "department": "Engineering",
            "company": "TechCorp Inc.",
            "skills": [
                {"skill": "Python", "proficiency_level": "Expert"},
                {"skill": "System Design", "proficiency_level": "Expert"},
                {"skill": "Architecture", "proficiency_level": "Expert"},
            ],
            "availability": [
                {"day_of_week": "Monday", "start_time": "09:00:00", "end_time": "12:00:00", "is_available": 1},
                {"day_of_week": "Wednesday", "start_time": "13:00:00", "end_time": "17:00:00", "is_available": 1},
                {"day_of_week": "Friday", "start_time": "09:00:00", "end_time": "12:00:00", "is_available": 1},
            ],
            "max_interviews_per_day": 4,
            "is_active": 1,
        },
        {
            "full_name": "Sarah Chen",
            "email": "sarah.chen@techcorp.com",
            "phone": "+1-555-2002",
            "designation": "Senior Software Engineer",
            "department": "Engineering",
            "company": "TechCorp Inc.",
            "skills": [
                {"skill": "Python", "proficiency_level": "Expert"},
                {"skill": "React", "proficiency_level": "Advanced"},
                {"skill": "PostgreSQL", "proficiency_level": "Advanced"},
            ],
            "availability": [
                {"day_of_week": "Tuesday", "start_time": "10:00:00", "end_time": "14:00:00", "is_available": 1},
                {"day_of_week": "Thursday", "start_time": "10:00:00", "end_time": "16:00:00", "is_available": 1},
            ],
            "max_interviews_per_day": 3,
            "is_active": 1,
        },
        {
            "full_name": "Michael Torres",
            "email": "michael.torres@innovatesoft.com",
            "phone": "+1-555-2003",
            "designation": "Product VP",
            "department": "Product",
            "company": "InnovateSoft Solutions",
            "skills": [
                {"skill": "Product Strategy", "proficiency_level": "Expert"},
                {"skill": "Agile", "proficiency_level": "Expert"},
                {"skill": "Data Analysis", "proficiency_level": "Advanced"},
            ],
            "availability": [
                {"day_of_week": "Monday", "start_time": "14:00:00", "end_time": "17:00:00", "is_available": 1},
                {"day_of_week": "Wednesday", "start_time": "09:00:00", "end_time": "12:00:00", "is_available": 1},
                {"day_of_week": "Friday", "start_time": "13:00:00", "end_time": "17:00:00", "is_available": 1},
            ],
            "max_interviews_per_day": 3,
            "is_active": 1,
        },
        {
            "full_name": "Emily Watson",
            "email": "emily.watson@cloudbase.io",
            "phone": "+1-555-2004",
            "designation": "Infrastructure Lead",
            "department": "Infrastructure",
            "company": "CloudBase Systems",
            "skills": [
                {"skill": "AWS", "proficiency_level": "Expert"},
                {"skill": "Kubernetes", "proficiency_level": "Expert"},
                {"skill": "Terraform", "proficiency_level": "Advanced"},
                {"skill": "CI/CD", "proficiency_level": "Expert"},
            ],
            "availability": [
                {"day_of_week": "Tuesday", "start_time": "09:00:00", "end_time": "13:00:00", "is_available": 1},
                {"day_of_week": "Thursday", "start_time": "09:00:00", "end_time": "13:00:00", "is_available": 1},
            ],
            "max_interviews_per_day": 5,
            "is_active": 1,
        },
        {
            "full_name": "Robert Kim",
            "email": "robert.kim@techcorp.com",
            "phone": "+1-555-2005",
            "designation": "Data Science Lead",
            "department": "Data Science",
            "company": "TechCorp Inc.",
            "skills": [
                {"skill": "Machine Learning", "proficiency_level": "Expert"},
                {"skill": "Python", "proficiency_level": "Expert"},
                {"skill": "TensorFlow", "proficiency_level": "Advanced"},
                {"skill": "Statistics", "proficiency_level": "Expert"},
            ],
            "availability": [
                {"day_of_week": "Monday", "start_time": "10:00:00", "end_time": "16:00:00", "is_available": 1},
                {"day_of_week": "Wednesday", "start_time": "10:00:00", "end_time": "16:00:00", "is_available": 1},
                {"day_of_week": "Friday", "start_time": "10:00:00", "end_time": "14:00:00", "is_available": 1},
            ],
            "max_interviews_per_day": 4,
            "is_active": 1,
        },
    ]
    for m in members:
        if not frappe.db.exists("Panel Member", m["full_name"]):
            doc = frappe.get_doc({
                "doctype": "Panel Member",
                "full_name": m["full_name"],
                "email": m["email"],
                "phone": m["phone"],
                "designation": m["designation"],
                "department": m["department"],
                "company": m["company"],
                "max_interviews_per_day": m["max_interviews_per_day"],
                "is_active": m["is_active"],
            })
            for skill in m["skills"]:
                doc.append("skills", skill)
            for avail in m["availability"]:
                doc.append("availability", avail)
            doc.insert(ignore_permissions=True)
    print("  Created 5 panel members with skills & availability")


def _create_candidates():
    candidates_data = [
        {
            "full_name": "John Doe", "email": "john.doe@email.com", "phone": "+1-555-1001",
            "date_of_birth": "1991-03-15", "gender": "Male",
            "current_location": "San Francisco, CA", "city": "San Francisco", "state": "California",
            "current_company": "WebDev Studios", "current_designation": "Senior Software Engineer",
            "total_experience": 7.5, "current_salary": 135000, "expected_salary": 160000,
            "notice_period": "30 days", "source": "LinkedIn",
            "linkedin_url": "https://linkedin.com/in/johndoe",
            "is_active": 1,
            "skills": [
                {"skill": "Python", "proficiency": "Expert"},
                {"skill": "Django", "proficiency": "Expert"},
                {"skill": "PostgreSQL", "proficiency": "Advanced"},
                {"skill": "Docker", "proficiency": "Advanced"},
                {"skill": "AWS", "proficiency": "Intermediate"},
            ],
            "education": [
                {"degree": "B.S. Computer Science", "institution": "Stanford University", "field_of_study": "Computer Science", "start_date": "2009-09-01", "end_date": "2013-06-30", "grade": "3.8 GPA"},
            ],
            "experience": [
                {"company_name": "WebDev Studios", "designation": "Senior Software Engineer", "from_date": add_days(today(), -1460), "to_date": "", "is_current": 1, "description": "Leading backend development team building scalable microservices architecture."},
                {"company_name": "StartupHub", "designation": "Software Engineer", "from_date": add_days(today(), -2555), "to_date": add_days(today(), -1460), "is_current": 0, "description": "Built RESTful APIs and managed cloud infrastructure on AWS."},
            ],
            "certifications": [
                {"certification_name": "AWS Solutions Architect", "issuing_organization": "Amazon Web Services", "issue_date": "2021-08-15", "credential_id": "AWS-ARCH-12345"},
                {"certification_name": "Certified Kubernetes Administrator", "issuing_organization": "CNCF", "issue_date": "2023-02-20", "credential_id": "CKA-67890"},
            ],
        },
        {
            "full_name": "Jane Smith", "email": "jane.smith@email.com", "phone": "+1-555-1002",
            "date_of_birth": "1993-07-22", "gender": "Female",
            "current_location": "New York, NY", "city": "New York", "state": "New York",
            "current_company": "FinanceHub Inc.", "current_designation": "Product Manager",
            "total_experience": 5.0, "current_salary": 120000, "expected_salary": 145000,
            "notice_period": "60 days", "source": "Referral", "referred_by": "Alice Johnson",
            "linkedin_url": "https://linkedin.com/in/janesmith",
            "is_active": 1,
            "skills": [
                {"skill": "Product Strategy", "proficiency": "Expert"},
                {"skill": "Agile", "proficiency": "Expert"},
                {"skill": "Data Analysis", "proficiency": "Advanced"},
                {"skill": "User Research", "proficiency": "Advanced"},
                {"skill": "SQL", "proficiency": "Intermediate"},
            ],
            "education": [
                {"degree": "MBA", "institution": "Columbia Business School", "field_of_study": "Business Administration", "start_date": "2017-09-01", "end_date": "2019-05-31", "grade": "3.9 GPA"},
                {"degree": "B.A. Economics", "institution": "NYU", "field_of_study": "Economics", "start_date": "2011-09-01", "end_date": "2015-05-31", "grade": "3.6 GPA"},
            ],
            "experience": [
                {"company_name": "FinanceHub Inc.", "designation": "Product Manager", "from_date": "2021-01-15", "to_date": "", "is_current": 1, "description": "Leading product roadmap for the company's flagship fintech application serving 2M+ users."},
                {"company_name": "TechStart Inc.", "designation": "Associate Product Manager", "from_date": add_days(today(), -2555), "to_date": add_days(today(), -1825), "is_current": 0, "description": "Managed feature development lifecycle and coordinated cross-functional teams."},
            ],
            "certifications": [
                {"certification_name": "Certified Scrum Product Owner", "issuing_organization": "Scrum Alliance", "issue_date": "2020-03-10", "credential_id": "CSPO-54321"},
            ],
        },
        {
            "full_name": "Mike Chen", "email": "mike.chen@email.com", "phone": "+1-555-1003",
            "date_of_birth": "1995-11-08", "gender": "Male",
            "current_location": "Bangalore, India", "city": "Bangalore", "state": "Karnataka",
            "current_company": "GlobalTech Systems", "current_designation": "DevOps Engineer",
            "total_experience": 4.5, "current_salary": 30000, "expected_salary": 45000,
            "notice_period": "45 days", "source": "Job Portal",
            "linkedin_url": "https://linkedin.com/in/mikechen",
            "portfolio_url": "https://github.com/mikechen",
            "is_active": 1,
            "skills": [
                {"skill": "Docker", "proficiency": "Expert"},
                {"skill": "Kubernetes", "proficiency": "Advanced"},
                {"skill": "AWS", "proficiency": "Advanced"},
                {"skill": "Terraform", "proficiency": "Advanced"},
                {"skill": "CI/CD", "proficiency": "Expert"},
                {"skill": "Linux", "proficiency": "Expert"},
                {"skill": "Python", "proficiency": "Intermediate"},
            ],
            "education": [
                {"degree": "B.Tech Computer Science", "institution": "Indian Institute of Technology, Bombay", "field_of_study": "Computer Science", "start_date": "2014-07-01", "end_date": "2018-05-31", "grade": "8.7 CGPA"},
            ],
            "experience": [
                {"company_name": "GlobalTech Systems", "designation": "DevOps Engineer", "from_date": "2020-04-01", "to_date": "", "is_current": 1, "description": "Managing Kubernetes clusters and building CI/CD pipelines for 50+ microservices."},
                {"company_name": "InfraTech Solutions", "designation": "Junior DevOps Engineer", "from_date": add_days(today(), -2900), "to_date": add_days(today(), -2190), "is_current": 0, "description": "Automated deployment processes and maintained cloud infrastructure."},
            ],
            "certifications": [
                {"certification_name": "AWS Certified DevOps Engineer", "issuing_organization": "Amazon Web Services", "issue_date": "2022-06-15", "credential_id": "AWS-DO-11223"},
                {"certification_name": "Certified Kubernetes Administrator", "issuing_organization": "CNCF", "issue_date": "2023-01-20", "credential_id": "CKA-44556"},
            ],
        },
        {
            "full_name": "Sarah Williams", "email": "sarah.williams@email.com", "phone": "+1-555-1004",
            "date_of_birth": "1994-09-12", "gender": "Female",
            "current_location": "London, UK", "city": "London", "state": "England",
            "current_company": "DataDriven Ltd", "current_designation": "Data Scientist",
            "total_experience": 3.0, "current_salary": 65000, "expected_salary": 85000,
            "notice_period": "30 days", "source": "LinkedIn",
            "linkedin_url": "https://linkedin.com/in/sarahwilliams",
            "is_active": 1,
            "skills": [
                {"skill": "Python", "proficiency": "Advanced"},
                {"skill": "Machine Learning", "proficiency": "Advanced"},
                {"skill": "TensorFlow", "proficiency": "Intermediate"},
                {"skill": "SQL", "proficiency": "Advanced"},
                {"skill": "Statistics", "proficiency": "Advanced"},
                {"skill": "Data Visualization", "proficiency": "Advanced"},
            ],
            "education": [
                {"degree": "M.Sc. Data Science", "institution": "University College London", "field_of_study": "Data Science", "start_date": "2020-09-01", "end_date": "2021-09-30", "grade": "Distinction"},
                {"degree": "B.Sc. Mathematics", "institution": "University of Oxford", "field_of_study": "Mathematics", "start_date": "2016-10-01", "end_date": "2019-06-30", "grade": "First Class"},
            ],
            "experience": [
                {"company_name": "DataDriven Ltd", "designation": "Data Scientist", "from_date": "2021-10-01", "to_date": "", "is_current": 1, "description": "Developing ML models for predictive analytics and building data pipelines."},
            ],
            "certifications": [
                {"certification_name": "TensorFlow Developer Certificate", "issuing_organization": "Google", "issue_date": "2022-04-10", "credential_id": "TF-DEV-78901"},
            ],
        },
        {
            "full_name": "David Brown", "email": "david.brown@email.com", "phone": "+1-555-1005",
            "date_of_birth": "1997-02-28", "gender": "Male",
            "current_location": "Austin, TX", "city": "Austin", "state": "Texas",
            "current_company": "StartupXYZ", "current_designation": "Frontend Developer",
            "total_experience": 2.5, "current_salary": 85000, "expected_salary": 110000,
            "notice_period": "15 days", "source": "Direct Application",
            "linkedin_url": "https://linkedin.com/in/davidbrown",
            "portfolio_url": "https://davidbrown.dev",
            "is_active": 1,
            "skills": [
                {"skill": "React", "proficiency": "Expert"},
                {"skill": "TypeScript", "proficiency": "Expert"},
                {"skill": "Next.js", "proficiency": "Advanced"},
                {"skill": "CSS", "proficiency": "Advanced"},
                {"skill": "Node.js", "proficiency": "Intermediate"},
                {"skill": "GraphQL", "proficiency": "Intermediate"},
            ],
            "education": [
                {"degree": "B.S. Computer Science", "institution": "University of Texas at Austin", "field_of_study": "Computer Science", "start_date": "2015-08-01", "end_date": "2019-05-31", "grade": "3.5 GPA"},
            ],
            "experience": [
                {"company_name": "StartupXYZ", "designation": "Frontend Developer", "from_date": "2022-01-01", "to_date": "", "is_current": 1, "description": "Building modern web applications using React, TypeScript, and Next.js."},
                {"company_name": "WebAgency Co.", "designation": "Junior Developer", "from_date": add_days(today(), -2555), "to_date": add_days(today(), -1460), "is_current": 0, "description": "Developed responsive websites and web applications for various clients."},
            ],
            "certifications": [],
        },
        {
            "full_name": "Priya Patel", "email": "priya.patel@email.com", "phone": "+1-555-1006",
            "date_of_birth": "1992-05-20", "gender": "Female",
            "current_location": "Mumbai, India", "city": "Mumbai", "state": "Maharashtra",
            "current_company": "FinTech Innovations", "current_designation": "Backend Engineer",
            "total_experience": 6.0, "current_salary": 35000, "expected_salary": 55000,
            "notice_period": "60 days", "source": "LinkedIn",
            "linkedin_url": "https://linkedin.com/in/priyapatel",
            "is_active": 1,
            "skills": [
                {"skill": "Java", "proficiency": "Expert"},
                {"skill": "Spring Boot", "proficiency": "Expert"},
                {"skill": "Microservices", "proficiency": "Expert"},
                {"skill": "Kafka", "proficiency": "Advanced"},
                {"skill": "MongoDB", "proficiency": "Advanced"},
                {"skill": "System Design", "proficiency": "Advanced"},
            ],
            "education": [
                {"degree": "M.Tech Computer Science", "institution": "IIT Delhi", "field_of_study": "Computer Science", "start_date": "2016-07-01", "end_date": "2018-05-31", "grade": "9.1 CGPA"},
                {"degree": "B.Tech Information Technology", "institution": "NIT Surat", "field_of_study": "Information Technology", "start_date": "2012-07-01", "end_date": "2016-05-31", "grade": "8.5 CGPA"},
            ],
            "experience": [
                {"company_name": "FinTech Innovations", "designation": "Senior Backend Engineer", "from_date": "2021-03-01", "to_date": "", "is_current": 1, "description": "Designing and building high-throughput payment processing systems handling $1B+ transactions."},
                {"company_name": "PayCore Solutions", "designation": "Backend Engineer", "from_date": add_days(today(), -2900), "to_date": add_days(today(), -1460), "is_current": 0, "description": "Built RESTful APIs and event-driven microservices for banking platform."},
            ],
            "certifications": [
                {"certification_name": "Oracle Certified Java Architect", "issuing_organization": "Oracle", "issue_date": "2022-11-15", "credential_id": "OCJA-99887"},
                {"certification_name": "Confluent Certified Kafka Developer", "issuing_organization": "Confluent", "issue_date": "2023-03-20", "credential_id": "CCKD-55443"},
            ],
        },
        {
            "full_name": "Alex Thompson", "email": "alex.thompson@email.com", "phone": "+1-555-1007",
            "date_of_birth": "1990-08-14", "gender": "Male",
            "current_location": "Chicago, IL", "city": "Chicago", "state": "Illinois",
            "current_company": "MarketingPro Agency", "current_designation": "Marketing Director",
            "total_experience": 8.0, "current_salary": 110000, "expected_salary": 135000,
            "notice_period": "30 days", "source": "Referral", "referred_by": "Bob Smith",
            "linkedin_url": "https://linkedin.com/in/alext",
            "is_active": 1,
            "skills": [
                {"skill": "Digital Marketing", "proficiency": "Expert"},
                {"skill": "SEO", "proficiency": "Expert"},
                {"skill": "Content Strategy", "proficiency": "Expert"},
                {"skill": "Analytics", "proficiency": "Advanced"},
                {"skill": "Team Leadership", "proficiency": "Expert"},
            ],
            "education": [
                {"degree": "MBA Marketing", "institution": "University of Chicago Booth", "field_of_study": "Marketing", "start_date": "2014-09-01", "end_date": "2016-06-30", "grade": "3.7 GPA"},
                {"degree": "B.A. Communications", "institution": "University of Illinois", "field_of_study": "Communications", "start_date": "2008-08-01", "end_date": "2012-05-31", "grade": "3.5 GPA"},
            ],
            "experience": [
                {"company_name": "MarketingPro Agency", "designation": "Marketing Director", "from_date": "2019-01-01", "to_date": "", "is_current": 1, "description": "Leading a team of 12 marketers driving brand strategy and demand generation."},
                {"company_name": "BrandBuilders Inc.", "designation": "Senior Marketing Manager", "from_date": add_days(today(), -3285), "to_date": add_days(today(), -2555), "is_current": 0, "description": "Developed and executed multi-channel marketing campaigns."},
            ],
            "certifications": [
                {"certification_name": "Google Analytics Certified", "issuing_organization": "Google", "issue_date": "2022-01-15", "credential_id": "GAC-44321"},
            ],
        },
        {
            "full_name": "Lisa Anderson", "email": "lisa.anderson@email.com", "phone": "+1-555-1008",
            "date_of_birth": "1996-12-03", "gender": "Female",
            "current_location": "Berlin, Germany", "city": "Berlin", "state": "",
            "current_company": "UX Labs GmbH", "current_designation": "UX/UI Designer",
            "total_experience": 3.5, "current_salary": 55000, "expected_salary": 70000,
            "notice_period": "30 days", "source": "Direct Application",
            "portfolio_url": "https://lisaanderson.design",
            "linkedin_url": "https://linkedin.com/in/lisaanderson",
            "is_active": 1,
            "skills": [
                {"skill": "Figma", "proficiency": "Expert"},
                {"skill": "User Research", "proficiency": "Advanced"},
                {"skill": "Prototyping", "proficiency": "Expert"},
                {"skill": "UI Design", "proficiency": "Expert"},
                {"skill": "Design Systems", "proficiency": "Advanced"},
                {"skill": "HTML/CSS", "proficiency": "Intermediate"},
            ],
            "education": [
                {"degree": "B.A. Interaction Design", "institution": "University of the Arts Berlin", "field_of_study": "Interaction Design", "start_date": "2016-10-01", "end_date": "2020-06-30", "grade": "1.3 (German Scale)"},
            ],
            "experience": [
                {"company_name": "UX Labs GmbH", "designation": "UX/UI Designer", "from_date": "2020-08-01", "to_date": "", "is_current": 1, "description": "Designing user interfaces and experiences for B2B SaaS products."},
            ],
            "certifications": [
                {"certification_name": "Google UX Design Certificate", "issuing_organization": "Google", "issue_date": "2021-06-30", "credential_id": "GUX-11223"},
            ],
        },
        {
            "full_name": "Ryan Martinez", "email": "ryan.martinez@email.com", "phone": "+1-555-1009",
            "date_of_birth": "1988-04-18", "gender": "Male",
            "current_location": "Toronto, Canada", "city": "Toronto", "state": "Ontario",
            "current_company": "CloudScale Inc.", "current_designation": "Solutions Architect",
            "total_experience": 10.0, "current_salary": 150000, "expected_salary": 180000,
            "notice_period": "30 days", "source": "LinkedIn",
            "linkedin_url": "https://linkedin.com/in/ryanmartinez",
            "is_active": 1,
            "skills": [
                {"skill": "Cloud Architecture", "proficiency": "Expert"},
                {"skill": "AWS", "proficiency": "Expert"},
                {"skill": "GCP", "proficiency": "Advanced"},
                {"skill": "Microservices", "proficiency": "Expert"},
                {"skill": "System Design", "proficiency": "Expert"},
                {"skill": "Python", "proficiency": "Advanced"},
                {"skill": "Go", "proficiency": "Intermediate"},
            ],
            "education": [
                {"degree": "M.Sc. Computer Science", "institution": "University of Toronto", "field_of_study": "Distributed Systems", "start_date": "2013-09-01", "end_date": "2015-06-30", "grade": "4.0 GPA"},
                {"degree": "B.Sc. Computer Engineering", "institution": "University of Waterloo", "field_of_study": "Computer Engineering", "start_date": "2007-09-01", "end_date": "2012-06-30", "grade": "3.8 GPA"},
            ],
            "experience": [
                {"company_name": "CloudScale Inc.", "designation": "Solutions Architect", "from_date": "2020-03-01", "to_date": "", "is_current": 1, "description": "Designing cloud-native architectures for enterprise customers migrating to AWS/GCP."},
                {"company_name": "BigCorp Systems", "designation": "Senior Software Engineer", "from_date": add_days(today(), -3285), "to_date": add_days(today(), -2190), "is_current": 0, "description": "Led migration of monolithic application to microservices architecture on AWS."},
                {"company_name": "StartupBay", "designation": "Software Engineer II", "from_date": add_days(today(), -4015), "to_date": add_days(today(), -3285), "is_current": 0, "description": "Built distributed data processing system handling TB-scale datasets."},
            ],
            "certifications": [
                {"certification_name": "AWS Solutions Architect Professional", "issuing_organization": "Amazon Web Services", "issue_date": "2021-08-20", "credential_id": "AWS-SAP-77665"},
                {"certification_name": "Google Cloud Architect", "issuing_organization": "Google Cloud", "issue_date": "2022-03-15", "credential_id": "GCP-ARCH-33441"},
                {"certification_name": "TOGAF 9 Certified", "issuing_organization": "The Open Group", "issue_date": "2020-11-10", "credential_id": "TOGAF-99882"},
            ],
        },
        {
            "full_name": "Emma Wilson", "email": "emma.wilson@email.com", "phone": "+1-555-1010",
            "date_of_birth": "1993-10-05", "gender": "Female",
            "current_location": "San Francisco, CA", "city": "San Francisco", "state": "California",
            "current_company": "HR Tech Global", "current_designation": "HR Operations Manager",
            "total_experience": 5.5, "current_salary": 95000, "expected_salary": 115000,
            "notice_period": "45 days", "source": "Agency",
            "linkedin_url": "https://linkedin.com/in/emmawilson",
            "is_active": 1,
            "skills": [
                {"skill": "HR Operations", "proficiency": "Expert"},
                {"skill": "Employee Relations", "proficiency": "Advanced"},
                {"skill": "Recruitment", "proficiency": "Expert"},
                {"skill": "HRIS", "proficiency": "Advanced"},
                {"skill": "Compliance", "proficiency": "Advanced"},
                {"skill": "Data Analysis", "proficiency": "Intermediate"},
            ],
            "education": [
                {"degree": "Master's in HR Management", "institution": "Cornell University", "field_of_study": "Human Resources", "start_date": "2017-08-01", "end_date": "2018-05-31", "grade": "3.8 GPA"},
                {"degree": "B.A. Psychology", "institution": "UC Berkeley", "field_of_study": "Psychology", "start_date": "2011-08-01", "end_date": "2015-05-31", "grade": "3.6 GPA"},
            ],
            "experience": [
                {"company_name": "HR Tech Global", "designation": "HR Operations Manager", "from_date": "2021-06-01", "to_date": "", "is_current": 1, "description": "Managing global HR operations and implementing HR technology solutions."},
                {"company_name": "PeopleFirst Corp", "designation": "HR Generalist", "from_date": add_days(today(), -2900), "to_date": add_days(today(), -1825), "is_current": 0, "description": "Handled full employee lifecycle including onboarding, benefits, and performance management."},
            ],
            "certifications": [
                {"certification_name": "SHRM Certified Professional", "issuing_organization": "SHRM", "issue_date": "2019-06-15", "credential_id": "SHRM-CP-55432"},
                {"certification_name": "PHR Certification", "issuing_organization": "HRCI", "issue_date": "2020-08-20", "credential_id": "PHR-22334"},
            ],
        },
    ]

    for c in candidates_data:
        if not frappe.db.exists("Candidate Profile", c["email"]):
            doc = frappe.get_doc({
                "doctype": "Candidate Profile",
                "naming_series": "CND-.YYYY.-.#####",
                "full_name": c["full_name"],
                "email": c["email"],
                "phone": c.get("phone"),
                "date_of_birth": c.get("date_of_birth"),
                "gender": c.get("gender"),
                "current_location": c.get("current_location"),
                "city": c.get("city"),
                "state": c.get("state"),
                "current_company": c.get("current_company"),
                "current_designation": c.get("current_designation"),
                "total_experience": c.get("total_experience"),
                "current_salary": c.get("current_salary"),
                "expected_salary": c.get("expected_salary"),
                "notice_period": c.get("notice_period"),
                "source": c.get("source"),
                "referred_by": c.get("referred_by"),
                "linkedin_url": c.get("linkedin_url"),
                "portfolio_url": c.get("portfolio_url"),
                "is_active": c.get("is_active", 1),
            })
            for skill in c.get("skills", []):
                doc.append("skills", {"skill": skill["skill"], "proficiency": skill["proficiency"]})
            for edu in c.get("education", []):
                doc.append("education", {
                    "degree": edu["degree"],
                    "institution": edu["institution"],
                    "field_of_study": edu.get("field_of_study"),
                    "start_date": edu.get("start_date"),
                    "end_date": edu.get("end_date"),
                    "grade": edu.get("grade"),
                })
            for exp in c.get("experience", []):
                doc.append("experience", {
                    "company_name": exp["company_name"],
                    "designation": exp["designation"],
                    "from_date": exp["from_date"],
                    "to_date": exp.get("to_date"),
                    "is_current": exp.get("is_current", 0),
                    "description": exp.get("description"),
                })
            for cert in c.get("certifications", []):
                doc.append("certifications", {
                    "certification_name": cert["certification_name"],
                    "issuing_organization": cert.get("issuing_organization"),
                    "issue_date": cert.get("issue_date"),
                    "credential_id": cert.get("credential_id"),
                })
            doc.insert(ignore_permissions=True)
    print("  Created 10 candidates with skills, education, experience & certifications")


def _get_job_posting(title):
    name = frappe.db.get_value("Job Posting", {"job_title": title}, "name")
    return name


def _get_candidate(email):
    name = frappe.db.get_value("Candidate Profile", {"email": email}, "name")
    return name


def _create_job_postings():
    jobs = [
        {
            "job_title": "Senior Python Developer",
            "company": "TechCorp Inc.",
            "department": "Engineering",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "San Francisco, USA",
            "job_description": "<p>We are looking for an experienced Python developer to join our platform engineering team at TechCorp. You will design and build scalable backend services that power our enterprise platform used by thousands of businesses worldwide.</p>",
            "responsibilities": "<ul><li>Design and implement RESTful APIs using Django and FastAPI</li><li>Optimize database queries and application performance</li><li>Mentor junior developers through code reviews and pair programming</li><li>Contribute to architecture decisions and technical roadmap</li><li>Collaborate with product and design teams to deliver features</li><li>Write comprehensive unit and integration tests</li></ul>",
            "requirements": "<ul><li>5+ years of Python development experience</li><li>Strong experience with Django or FastAPI frameworks</li><li>Proficient in SQL and database design (PostgreSQL preferred)</li><li>Experience with cloud services (AWS/GCP)</li><li>Knowledge of Docker and containerization</li><li>Excellent problem-solving and communication skills</li></ul>",
            "benefits": "<ul><li>Competitive salary and equity package</li><li>Comprehensive health, dental, and vision insurance</li><li>Remote-friendly work environment</li><li>401k matching up to 6%</li><li>Annual learning & development budget of $5,000</li><li>Flexible PTO policy</li></ul>",
            "min_experience": 5, "max_experience": 10,
            "min_salary": 140000, "max_salary": 180000,
            "number_of_openings": 2,
            "application_deadline": add_days(today(), 45),
            "status": "Open", "publish_on_website": 1,
            "posted_date": add_days(today(), -15),
        },
        {
            "job_title": "Product Manager",
            "company": "InnovateSoft Solutions",
            "department": "Product",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "New York, USA",
            "job_description": "<p>We're seeking a skilled Product Manager to drive our AI-powered healthcare analytics platform at InnovateSoft Solutions. You'll own the product roadmap and work closely with engineering, design, and clinical stakeholders.</p>",
            "responsibilities": "<ul><li>Define and communicate product roadmap and strategy</li><li>Gather and prioritize product requirements from stakeholders and customers</li><li>Work closely with engineering and design teams to deliver features</li><li>Analyze market trends, competition, and customer feedback</li><li>Define and track key product metrics and OKRs</li><li>Present product updates to leadership and customers</li></ul>",
            "requirements": "<ul><li>3+ years of product management experience in SaaS</li><li>Strong analytical skills and data-driven decision making</li><li>Excellent written and verbal communication skills</li><li>Experience with agile development methodologies</li><li>Healthcare domain experience is a plus</li><li>Technical background or ability to understand complex systems</li></ul>",
            "benefits": "<ul><li>Competitive compensation package</li><li>Stock options with early exercise option</li><li>Flexible work arrangements (hybrid model)</li><li>Learning and development budget</li><li>Health and wellness benefits</li><li>Team retreats and social events</li></ul>",
            "min_experience": 3, "max_experience": 8,
            "min_salary": 120000, "max_salary": 160000,
            "number_of_openings": 1,
            "application_deadline": add_days(today(), 30),
            "status": "Open", "publish_on_website": 1,
            "posted_date": add_days(today(), -10),
        },
        {
            "job_title": "DevOps Engineer",
            "company": "TechCorp Inc.",
            "department": "Infrastructure",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "Remote - Global",
            "job_description": "<p>Join TechCorp's infrastructure team to build and maintain our cloud-native platform used by millions of users worldwide. We're looking for a DevOps Engineer who can help us scale and automate our infrastructure.</p>",
            "responsibilities": "<ul><li>Manage and scale Kubernetes clusters across multiple regions</li><li>Automate deployment pipelines and infrastructure provisioning</li><li>Monitor system health, performance, and cost optimization</li><li>Implement security best practices and compliance requirements</li><li>Participate in on-call rotation for incident response</li><li>Document infrastructure architecture and runbooks</li></ul>",
            "requirements": "<ul><li>3+ years of DevOps/SRE experience</li><li>Strong knowledge of Docker and Kubernetes</li><li>Experience with CI/CD tools (GitLab CI, GitHub Actions, or Jenkins)</li><li>Proficiency in infrastructure as code (Terraform, CloudFormation)</li><li>AWS or GCP certification preferred</li><li>Scripting experience (Python, Bash)</li></ul>",
            "benefits": "<ul><li>Remote-first culture with async communication</li><li>Competitive salary with equity grants</li><li>Home office stipend of $2,000</li><li>Annual performance bonus (10-20%)</li><li>Health insurance coverage</li><li>Co-working space membership</li></ul>",
            "min_experience": 3, "max_experience": 7,
            "min_salary": 110000, "max_salary": 145000,
            "number_of_openings": 1,
            "application_deadline": add_days(today(), 60),
            "status": "Open", "publish_on_website": 1,
            "posted_date": add_days(today(), -5),
        },
        {
            "job_title": "Data Scientist",
            "company": "DataFlow Analytics",
            "department": "Data Science",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "London, UK",
            "job_description": "<p>Help us build the next generation of AI-powered analytics tools at DataFlow Analytics. We're looking for a Data Scientist to develop machine learning models that help businesses make better decisions.</p>",
            "responsibilities": "<ul><li>Develop and deploy machine learning models in production</li><li>Analyze large datasets to extract actionable insights</li><li>Build and maintain data pipelines and ETL processes</li><li>Present findings and recommendations to stakeholders</li><li>Stay current with latest ML research and technologies</li><li>Contribute to internal tools and libraries</li></ul>",
            "requirements": "<ul><li>2+ years of data science experience in a production environment</li><li>Proficiency in Python and SQL</li><li>Experience with ML frameworks (TensorFlow, PyTorch, scikit-learn)</li><li>Strong foundation in statistics and experimental design</li><li>Experience with data visualization tools</li><li>Excellent communication skills</li></ul>",
            "benefits": "<ul><li>Competitive salary with performance bonuses</li><li>Flexible working hours (core hours 10am-3pm)</li><li>Annual training and conference budget of £3,000</li><li>25 days annual leave + public holidays</li><li>Pension scheme with 5% employer contribution</li><li>Team social events and quarterly offsites</li></ul>",
            "min_experience": 2, "max_experience": 6,
            "min_salary": 70000, "max_salary": 95000,
            "number_of_openings": 2,
            "application_deadline": add_days(today(), 30),
            "status": "Open", "publish_on_website": 1,
            "posted_date": add_days(today(), -7),
        },
        {
            "job_title": "Frontend Developer",
            "company": "CloudBase Systems",
            "department": "Engineering",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "Austin, USA",
            "job_description": "<p>CloudBase Systems is looking for a talented Frontend Developer to build intuitive and performant user interfaces for our cloud management platform.</p>",
            "responsibilities": "<ul><li>Build responsive and accessible web applications using React</li><li>Collaborate with UX designers to implement pixel-perfect interfaces</li><li>Optimize application performance and bundle size</li><li>Write comprehensive unit and integration tests</li><li>Contribute to our design system component library</li><li>Participate in code reviews and architecture discussions</li></ul>",
            "requirements": "<ul><li>3+ years of frontend development experience</li><li>Expert knowledge of React, TypeScript, and modern CSS</li><li>Experience with state management (Redux, Zustand)</li><li>Familiarity with testing frameworks (Jest, Cypress)</li><li>Understanding of web performance optimization</li><li>Portfolio demonstrating strong UI/UX sense</li></ul>",
            "benefits": "<ul><li>Competitive salary with equity</li><li>Full health, dental, and vision benefits</li><li>Flexible PTO policy</li><li>Annual device budget of $3,000</li><li>Onsite gym and catered lunches</li><li>Pet-friendly office</li></ul>",
            "min_experience": 3, "max_experience": 7,
            "min_salary": 100000, "max_salary": 135000,
            "number_of_openings": 2,
            "application_deadline": add_days(today(), 45),
            "status": "Open", "publish_on_website": 1,
            "posted_date": add_days(today(), -3),
        },
        {
            "job_title": "Senior Backend Engineer",
            "company": "InnovateSoft Solutions",
            "department": "Engineering",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "New York, USA",
            "job_description": "<p>Join InnovateSoft's engineering team to build the backend infrastructure powering our healthcare AI platform. We're looking for a Senior Backend Engineer who can lead technical initiatives and mentor team members.</p>",
            "responsibilities": "<ul><li>Design and build scalable backend services using Java/Spring Boot</li><li>Lead technical architecture discussions and decisions</li><li>Mentor junior and mid-level engineers</li><li>Ensure high code quality through reviews and testing</li><li>Collaborate with product and infrastructure teams</li></ul>",
            "requirements": "<ul><li>5+ years of backend development experience</li><li>Strong Java/Spring Boot expertise</li><li>Experience with microservices architecture</li><li>Proficiency in SQL and NoSQL databases</li><li>Experience with message queuing systems (Kafka, RabbitMQ)</li><li>Healthcare industry experience preferred</li></ul>",
            "benefits": "<ul><li>Top-tier compensation package with significant equity</li><li>Comprehensive benefits including fertility benefits</li><li>Flexible work arrangements</li><li>Professional development budget</li><li>Employee stock purchase program</li></ul>",
            "min_experience": 5, "max_experience": 10,
            "min_salary": 130000, "max_salary": 170000,
            "number_of_openings": 1,
            "application_deadline": add_days(today(), 45),
            "status": "Open", "publish_on_website": 1,
            "posted_date": add_days(today(), -8),
        },
        {
            "job_title": "Solutions Architect",
            "company": "CloudBase Systems",
            "department": "Solutions Engineering",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "Remote - Global",
            "job_description": "<p>CloudBase Systems is seeking a Solutions Architect to design and implement cloud solutions for our enterprise customers. You'll be the technical authority guiding customers through their cloud transformation journey.</p>",
            "responsibilities": "<ul><li>Design cloud architectures for enterprise customers</li><li>Conduct technical discovery sessions and workshops</li><li>Create detailed architecture documentation and diagrams</li><li>Support sales team with technical expertise during pre-sales</li><li>Stay current with cloud provider services and best practices</li></ul>",
            "requirements": "<ul><li>8+ years in software engineering or cloud architecture</li><li>Deep expertise in AWS or GCP</li><li>Strong understanding of networking, security, and compliance</li><li>Excellent presentation and communication skills</li><li>Cloud architecture certification required</li></ul>",
            "benefits": "<ul><li>Executive-level compensation package</li><li>Unlimited PTO</li><li>Remote-first with travel opportunities</li><li>Annual bonus potential up to 30%</li><li>Car allowance for client visits</li></ul>",
            "min_experience": 8, "max_experience": 15,
            "min_salary": 160000, "max_salary": 200000,
            "number_of_openings": 1,
            "application_deadline": add_days(today(), 60),
            "status": "Open", "publish_on_website": 0,
            "posted_date": add_days(today(), -2),
        },
        {
            "job_title": "Marketing Manager",
            "company": "DataFlow Analytics",
            "department": "Marketing",
            "job_category": "Sales & Marketing",
            "job_type": "Full Time",
            "job_location": "London, UK",
            "job_description": "<p>DataFlow Analytics is looking for a Marketing Manager to drive demand generation and brand awareness for our data analytics platform in the European market.</p>",
            "responsibilities": "<ul><li>Develop and execute marketing strategies to drive pipeline growth</li><li>Manage content marketing, webinars, and events</li><li>Track and report on marketing KPIs and ROI</li><li>Collaborate with sales team on campaign effectiveness</li><li>Manage marketing budget and vendor relationships</li></ul>",
            "requirements": "<ul><li>4+ years of B2B marketing experience</li><li>Strong understanding of demand generation and ABM</li><li>Experience with marketing automation tools (HubSpot, Marketo)</li><li>Excellent copywriting and content creation skills</li><li>Data-driven mindset with analytical capabilities</li></ul>",
            "benefits": "<ul><li>Competitive salary with quarterly bonus</li><li>Hybrid work model (2 days in office)</li><li>25 days holiday + bank holidays</li><li>Company pension scheme</li><li>Health cash plan</li></ul>",
            "min_experience": 4, "max_experience": 8,
            "min_salary": 55000, "max_salary": 75000,
            "number_of_openings": 1,
            "application_deadline": add_days(today(), 30),
            "status": "Open", "publish_on_website": 1,
            "posted_date": add_days(today(), -1),
        },
        {
            "job_title": "HR Operations Specialist",
            "company": "TechCorp Inc.",
            "department": "Human Resources",
            "job_category": "Human Resources",
            "job_type": "Full Time",
            "job_location": "San Francisco, USA",
            "job_description": "<p>TechCorp is seeking an HR Operations Specialist to join our People Operations team. You'll help scale our HR operations as we continue to grow globally.</p>",
            "responsibilities": "<ul><li>Manage employee lifecycle processes from onboarding to offboarding</li><li>Maintain HRIS data accuracy and generate reports</li><li>Support benefits administration and employee inquiries</li><li>Develop and update HR policies and procedures</li><li>Coordinate performance review cycles and promotions</li></ul>",
            "requirements": "<ul><li>3+ years of HR operations experience</li><li>Experience with HRIS systems (Workday, BambooHR)</li><li>Knowledge of employment laws and regulations</li><li>Strong organizational and communication skills</li><li>HR certification (PHR/SHRM-CP) preferred</li></ul>",
            "benefits": "<ul><li>Competitive salary</li><li>Comprehensive benefits package</li><li>Career growth opportunities</li><li>Tuition reimbursement</li><li>Employee wellness program</li></ul>",
            "min_experience": 3, "max_experience": 7,
            "min_salary": 75000, "max_salary": 95000,
            "number_of_openings": 1,
            "application_deadline": add_days(today(), 30),
            "status": "Open", "publish_on_website": 1,
            "posted_date": add_days(today(), -6),
        },
        {
            "job_title": "UX/UI Designer",
            "company": "TechCorp Inc.",
            "department": "Design",
            "job_category": "Design",
            "job_type": "Full Time",
            "job_location": "San Francisco, USA",
            "job_description": "<p>TechCorp is looking for a talented UX/UI Designer to create beautiful and intuitive experiences for our enterprise platform. You'll work closely with product managers and engineers.</p>",
            "responsibilities": "<ul><li>Design user flows, wireframes, and high-fidelity mockups</li><li>Conduct user research and usability testing</li><li>Create and maintain design system components</li><li>Collaborate with engineers during implementation</li><li>Present design solutions to stakeholders</li></ul>",
            "requirements": "<ul><li>3+ years of UX/UI design experience</li><li>Proficiency in Figma and prototyping tools</li><li>Strong portfolio demonstrating UX process</li><li>Understanding of accessibility standards (WCAG)</li><li>Experience with design systems</li></ul>",
            "benefits": "<ul><li>Competitive salary and equity</li><li>Latest MacBook Pro and design tools</li><li>Conference and learning budget</li><li>Health and wellness benefits</li></ul>",
            "min_experience": 3, "max_experience": 7,
            "min_salary": 90000, "max_salary": 120000,
            "number_of_openings": 1,
            "application_deadline": add_days(today(), 30),
            "status": "Open", "publish_on_website": 1,
            "posted_date": add_days(today(), -4),
        },
    ]

    for j in jobs:
        title = j["job_title"]
        if not frappe.db.exists("Job Posting", {"job_title": title}):
            doc = frappe.get_doc({
                "doctype": "Job Posting",
                "naming_series": "JOB-.YYYY.-.#####",
                **j,
                "required_skills": [],
            })
            doc.insert(ignore_permissions=True)
    print("  Created 10 job postings")


def _create_job_applications():
    applications = [
        # TechCorp - Senior Python Developer applications
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("john.doe@email.com"), "company": "TechCorp Inc.", "status": "Interview", "application_date": add_days(today(), -14), "score": 85, "source": "LinkedIn", "interview_rounds": 2, "current_round": 2, "screening_status": "Shortlisted", "cover_letter": "<p>I am very excited about this opportunity at TechCorp. With 7 years of Python experience and a strong background in building scalable backend systems, I believe I would be a great fit for this role. I've been following TechCorp's growth and admire the engineering culture.</p>"},
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("david.brown@email.com"), "company": "TechCorp Inc.", "status": "Applied", "application_date": add_days(today(), -3), "score": 62, "source": "Direct Application", "screening_status": "Pending"},
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("priya.patel@email.com"), "company": "TechCorp Inc.", "status": "Screening", "application_date": add_days(today(), -7), "score": 78, "source": "LinkedIn", "screening_status": "Shortlisted", "cover_letter": "<p>I am excited to apply for the Senior Python Developer position. My experience building high-throughput payment systems has given me deep expertise in Python, system design, and microservices architecture.</p>"},
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("mike.chen@email.com"), "company": "TechCorp Inc.", "status": "Rejected", "application_date": add_days(today(), -20), "score": 55, "source": "Job Portal", "rejection_reason": "Skill set more aligned with DevOps role than backend development", "screening_status": "Rejected"},
        # InnovateSoft - Product Manager applications
        {"job_posting": _get_job_posting("Product Manager"), "candidate": _get_candidate("jane.smith@email.com"), "company": "InnovateSoft Solutions", "status": "Screening", "application_date": add_days(today(), -7), "score": 78, "source": "Referral", "screening_status": "Shortlisted", "cover_letter": "<p>I was referred by Alice Johnson who can vouch for my product management expertise. With 5 years of experience managing SaaS products, I am confident I can drive InnovateSoft's healthcare platform to new heights.</p>"},
        {"job_posting": _get_job_posting("Product Manager"), "candidate": _get_candidate("alex.thompson@email.com"), "company": "InnovateSoft Solutions", "status": "Applied", "application_date": add_days(today(), -5), "score": 65, "source": "LinkedIn", "screening_status": "Pending"},
        # TechCorp - DevOps Engineer applications
        {"job_posting": _get_job_posting("DevOps Engineer"), "candidate": _get_candidate("mike.chen@email.com"), "company": "TechCorp Inc.", "status": "Interview", "application_date": add_days(today(), -10), "score": 88, "source": "Job Portal", "interview_rounds": 1, "current_round": 1, "screening_status": "Shortlisted", "cover_letter": "<p>I have extensive experience managing Kubernetes clusters and building CI/CD pipelines. TechCorp's DevOps role aligns perfectly with my expertise in cloud infrastructure and automation.</p>"},
        {"job_posting": _get_job_posting("DevOps Engineer"), "candidate": _get_candidate("ryan.martinez@email.com"), "company": "TechCorp Inc.", "status": "Interview", "application_date": add_days(today(), -8), "score": 92, "source": "LinkedIn", "interview_rounds": 1, "current_round": 1, "screening_status": "Shortlisted"},
        # DataFlow - Data Scientist applications
        {"job_posting": _get_job_posting("Data Scientist"), "candidate": _get_candidate("sarah.williams@email.com"), "company": "DataFlow Analytics", "status": "Applied", "application_date": add_days(today(), -5), "score": 72, "source": "LinkedIn", "screening_status": "Pending"},
        {"job_posting": _get_job_posting("Data Scientist"), "candidate": _get_candidate("priya.patel@email.com"), "company": "DataFlow Analytics", "status": "Screening", "application_date": add_days(today(), -4), "score": 60, "source": "Direct Application", "screening_status": "Pending"},
        # CloudBase - Frontend Developer applications
        {"job_posting": _get_job_posting("Frontend Developer"), "candidate": _get_candidate("david.brown@email.com"), "company": "CloudBase Systems", "status": "Interview", "application_date": add_days(today(), -6), "score": 82, "source": "Direct Application", "interview_rounds": 1, "current_round": 1, "screening_status": "Shortlisted", "cover_letter": "<p>I've been using CloudBase's platform and I'm impressed by the technology. With my React expertise, I can help build even better user experiences.</p>"},
        {"job_posting": _get_job_posting("Frontend Developer"), "candidate": _get_candidate("lisa.anderson@email.com"), "company": "CloudBase Systems", "status": "Applied", "application_date": add_days(today(), -2), "score": 75, "source": "Direct Application", "screening_status": "Pending"},
        # InnovateSoft - Senior Backend Engineer applications
        {"job_posting": _get_job_posting("Senior Backend Engineer"), "candidate": _get_candidate("priya.patel@email.com"), "company": "InnovateSoft Solutions", "status": "Interview", "application_date": add_days(today(), -9), "score": 86, "source": "LinkedIn", "interview_rounds": 1, "current_round": 1, "screening_status": "Shortlisted"},
        {"job_posting": _get_job_posting("Senior Backend Engineer"), "candidate": _get_candidate("john.doe@email.com"), "company": "InnovateSoft Solutions", "status": "Screening", "application_date": add_days(today(), -6), "score": 74, "source": "Agency", "screening_status": "Shortlisted"},
        # CloudBase - Solutions Architect applications
        {"job_posting": _get_job_posting("Solutions Architect"), "candidate": _get_candidate("ryan.martinez@email.com"), "company": "CloudBase Systems", "status": "Applied", "application_date": add_days(today(), -1), "score": 80, "source": "LinkedIn", "screening_status": "Pending"},
        # DataFlow - Marketing Manager applications
        {"job_posting": _get_job_posting("Marketing Manager"), "candidate": _get_candidate("alex.thompson@email.com"), "company": "DataFlow Analytics", "status": "Screening", "application_date": add_days(today(), -3), "score": 70, "source": "Referral", "screening_status": "Shortlisted"},
        # TechCorp - HR Operations Specialist applications
        {"job_posting": _get_job_posting("HR Operations Specialist"), "candidate": _get_candidate("emma.wilson@email.com"), "company": "TechCorp Inc.", "status": "Interview", "application_date": add_days(today(), -11), "score": 84, "source": "Agency", "interview_rounds": 2, "current_round": 2, "screening_status": "Shortlisted"},
        # TechCorp - UX/UI Designer applications
        {"job_posting": _get_job_posting("UX/UI Designer"), "candidate": _get_candidate("lisa.anderson@email.com"), "company": "TechCorp Inc.", "status": "Applied", "application_date": add_days(today(), -3), "score": 71, "source": "Direct Application", "screening_status": "Pending"},
        {"job_posting": _get_job_posting("UX/UI Designer"), "candidate": _get_candidate("sarah.williams@email.com"), "company": "TechCorp Inc.", "status": "Rejected", "application_date": add_days(today(), -12), "score": 45, "source": "Job Portal", "rejection_reason": "Profile better suited for Data Science roles", "screening_status": "Rejected"},
    ]

    for a in applications:
        if a["candidate"] and a["job_posting"]:
            existing_name = frappe.db.exists("Job Application", {
                "job_posting": a["job_posting"],
                "candidate": a["candidate"]
            })
            if not existing_name:
                doc = frappe.get_doc({
                    "doctype": "Job Application",
                    "naming_series": "APP-.YYYY.MM.-.#####",
                    **a,
                })
                doc.insert(ignore_permissions=True)
    print("  Created 20 job applications")


def _create_interview_schedules():
    schedules = [
        # TechCorp - Senior Python Developer - John Doe - Round 1
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("john.doe@email.com"), "company": "TechCorp Inc.",
         "interview_date": add_days(today(), 2), "interview_time": "10:00:00", "duration": "60 mins", "status": "Scheduled",
         "interview_type": "Technical", "interview_mode": "Video Call", "meeting_link": "https://meet.google.com/abc-defg-hij",
         "interview_round": 1, "feedback_required": 1,
         "interviewers": [
             {"interviewer": "Administrator", "interviewer_name": "James Wilson", "role": "Primary"},
             {"interviewer": "Administrator", "interviewer_name": "Sarah Chen", "role": "Co-Interviewer"},
         ]},
        # TechCorp - Senior Python Developer - John Doe - Round 2 (Completed)
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("john.doe@email.com"), "company": "TechCorp Inc.",
         "interview_date": add_days(today(), -7), "interview_time": "14:00:00", "duration": "45 mins", "status": "Completed",
         "interview_type": "Technical", "interview_mode": "Video Call", "meeting_link": "https://meet.google.com/prev-round-xyz",
         "interview_round": 1, "feedback_required": 1,
         "interviewers": [
             {"interviewer": "Administrator", "interviewer_name": "Sarah Chen", "role": "Primary"},
         ]},
        # TechCorp - DevOps Engineer - Mike Chen
        {"job_posting": _get_job_posting("DevOps Engineer"), "candidate": _get_candidate("mike.chen@email.com"), "company": "TechCorp Inc.",
         "interview_date": add_days(today(), 5), "interview_time": "14:30:00", "duration": "45 mins", "status": "Scheduled",
         "interview_type": "Technical", "interview_mode": "Video Call", "meeting_link": "https://meet.google.com/xyz-uvwx-yz",
         "interview_round": 1, "feedback_required": 1,
         "interviewers": [
             {"interviewer": "Administrator", "interviewer_name": "Emily Watson", "role": "Primary"},
         ]},
        # TechCorp - DevOps Engineer - Ryan Martinez - Completed
        {"job_posting": _get_job_posting("DevOps Engineer"), "candidate": _get_candidate("ryan.martinez@email.com"), "company": "TechCorp Inc.",
         "interview_date": add_days(today(), -2), "interview_time": "11:00:00", "duration": "60 mins", "status": "Completed",
         "interview_type": "Technical", "interview_mode": "Video Call", "meeting_link": "https://zoom.us/j/987654321",
         "interview_round": 1, "feedback_required": 1,
         "interviewers": [
             {"interviewer": "Administrator", "interviewer_name": "James Wilson", "role": "Primary"},
             {"interviewer": "Administrator", "interviewer_name": "Emily Watson", "role": "Co-Interviewer"},
         ]},
        # InnovateSoft - Product Manager - Jane Smith (Completed)
        {"job_posting": _get_job_posting("Product Manager"), "candidate": _get_candidate("jane.smith@email.com"), "company": "InnovateSoft Solutions",
         "interview_date": add_days(today(), -1), "interview_time": "11:00:00", "duration": "60 mins", "status": "Completed",
         "interview_type": "HR", "interview_mode": "Video Call", "meeting_link": "https://zoom.us/j/123456789",
         "interview_round": 1, "feedback_required": 0,
         "interviewers": [
             {"interviewer": "Administrator", "interviewer_name": "Michael Torres", "role": "Primary"},
         ]},
        # CloudBase - Frontend Developer - David Brown
        {"job_posting": _get_job_posting("Frontend Developer"), "candidate": _get_candidate("david.brown@email.com"), "company": "CloudBase Systems",
         "interview_date": add_days(today(), 3), "interview_time": "15:00:00", "duration": "60 mins", "status": "Scheduled",
         "interview_type": "Technical", "interview_mode": "Video Call", "meeting_link": "https://meet.google.com/frontend-abc",
         "interview_round": 1, "feedback_required": 1,
         "interviewers": [
             {"interviewer": "Administrator", "interviewer_name": "Sarah Chen", "role": "Primary"},
         ]},
        # InnovateSoft - Senior Backend Engineer - Priya Patel
        {"job_posting": _get_job_posting("Senior Backend Engineer"), "candidate": _get_candidate("priya.patel@email.com"), "company": "InnovateSoft Solutions",
         "interview_date": add_days(today(), 4), "interview_time": "10:00:00", "duration": "60 mins", "status": "Scheduled",
         "interview_type": "Technical", "interview_mode": "Video Call", "meeting_link": "https://meet.google.com/backend-xyz",
         "interview_round": 1, "feedback_required": 1,
         "interviewers": [
             {"interviewer": "Administrator", "interviewer_name": "James Wilson", "role": "Primary"},
         ]},
        # TechCorp - HR Operations Specialist - Emma Wilson
        {"job_posting": _get_job_posting("HR Operations Specialist"), "candidate": _get_candidate("emma.wilson@email.com"), "company": "TechCorp Inc.",
         "interview_date": add_days(today(), -3), "interview_time": "09:30:00", "duration": "45 mins", "status": "Completed",
         "interview_type": "HR", "interview_mode": "Video Call", "meeting_link": "https://zoom.us/j/hr-round-1",
         "interview_round": 1, "feedback_required": 1,
         "interviewers": [
             {"interviewer": "Administrator", "interviewer_name": "Michael Torres", "role": "Primary"},
         ]},
        # TechCorp - Senior Python Developer - Priya Patel (Screening)
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("priya.patel@email.com"), "company": "TechCorp Inc.",
         "interview_date": add_days(today(), 7), "interview_time": "13:00:00", "duration": "60 mins", "status": "Scheduled",
         "interview_type": "Technical", "interview_mode": "Video Call", "meeting_link": "https://meet.google.com/python-screening",
         "interview_round": 1, "feedback_required": 1,
         "interviewers": [
             {"interviewer": "Administrator", "interviewer_name": "Robert Kim", "role": "Primary"},
         ]},
    ]

    for s in schedules:
        if s["candidate"] and s["job_posting"]:
            existing_name = frappe.db.exists("Interview Schedule", {
                "candidate": s["candidate"],
                "job_posting": s["job_posting"],
                "interview_round": s["interview_round"],
            })
            if not existing_name:
                doc = frappe.get_doc({
                    "doctype": "Interview Schedule",
                    "naming_series": "INT-.YYYY.MM.DD.-.####",
                    "job_posting": s["job_posting"],
                    "candidate": s["candidate"],
                    "company": s["company"],
                    "interview_date": s["interview_date"],
                    "interview_time": s["interview_time"],
                    "duration": s["duration"],
                    "status": s["status"],
                    "interview_type": s["interview_type"],
                    "interview_mode": s["interview_mode"],
                    "meeting_link": s.get("meeting_link"),
                    "interview_round": s["interview_round"],
                    "feedback_required": s["feedback_required"],
                })
                for panelist in s.get("interviewers", []):
                    doc.append("interviewers", panelist)
                doc.insert(ignore_permissions=True)
    print("  Created 9 interview schedules with panelists")


def _create_interview_feedback():
    feedbacks = [
        # John Doe - Senior Python Developer Round 1 (Completed)
        {
            "candidate": _get_candidate("john.doe@email.com"),
            "job_application": None,
            "interviewer": "Administrator",
            "interview_date": add_days(today(), -7),
            "interview_round": "Round 1",
            "status": "Submitted",
            "feedback_rating": 8,
            "strengths": "Strong Python fundamentals and system design knowledge. Excellent communication skills. Good cultural fit.",
            "weaknesses": "Could improve on Kubernetes knowledge. Some gaps in distributed systems experience.",
            "overall_feedback": "<p>John demonstrated strong technical skills and problem-solving abilities. He has good experience building scalable systems and would be a valuable addition to the team.</p>",
            "recommendation": "Hire",
            "decision": "Proceed",
        },
        # Ryan Martinez - DevOps Engineer (Completed)
        {
            "candidate": _get_candidate("ryan.martinez@email.com"),
            "job_application": None,
            "interviewer": "Administrator",
            "interview_date": add_days(today(), -2),
            "interview_round": "Round 1",
            "status": "Submitted",
            "feedback_rating": 9,
            "strengths": "Exceptional cloud architecture knowledge. Very experienced with AWS and Kubernetes. Strong leadership skills.",
            "weaknesses": "May be overqualified for this role given his Solutions Architect background. Should consider for Senior position.",
            "overall_feedback": "<p>Ryan is an outstanding candidate with deep DevOps and cloud expertise. His experience would greatly benefit our infrastructure team.</p>",
            "recommendation": "Strong Hire",
            "decision": "Proceed",
        },
        # Jane Smith - Product Manager (Completed)
        {
            "candidate": _get_candidate("jane.smith@email.com"),
            "job_application": None,
            "interviewer": "Administrator",
            "interview_date": add_days(today(), -1),
            "interview_round": "Round 1",
            "status": "Submitted",
            "feedback_rating": 7,
            "strengths": "Strong product sense and market understanding. Good experience with fintech products. Excellent presentation skills.",
            "weaknesses": "Healthcare domain knowledge is limited. May need ramp-up time to understand the clinical workflow.",
            "overall_feedback": "<p>Jane has strong product management fundamentals and would be a good cultural fit. Her lack of healthcare experience is a concern but her learning ability should compensate.</p>",
            "recommendation": "Hire",
            "decision": "Proceed",
        },
        # Emma Wilson - HR Operations Specialist (Completed)
        {
            "candidate": _get_candidate("emma.wilson@email.com"),
            "job_application": None,
            "interviewer": "Administrator",
            "interview_date": add_days(today(), -3),
            "interview_round": "Round 1",
            "status": "Submitted",
            "feedback_rating": 8,
            "strengths": "Strong HR operations background. Experience with HRIS implementation. Very organized and detail-oriented.",
            "weaknesses": "Limited experience with global HR operations. Need to check familiarity with multi-country compliance.",
            "overall_feedback": "<p>Emma is a well-qualified candidate with strong HR operations experience. Recommended to proceed to next round with a focus on global HR scenarios.</p>",
            "recommendation": "Hire",
            "decision": "Proceed",
        },
    ]

    for f in feedbacks:
        if f["candidate"]:
            # Find the job application for this candidate
            app_name = frappe.db.get_value("Job Application", {"candidate": f["candidate"]}, "name")
            feedback_data = {k: v for k, v in f.items()}
            feedback_data["job_application"] = app_name
            frappe.get_doc({
                "doctype": "Interview Feedback",
                **feedback_data,
            }).insert(ignore_permissions=True)
    print("  Created 4 interview feedback records")


def _create_offer_letters():
    # Find the candidate and job for which we want to create offers
    john_doe = _get_candidate("john.doe@email.com")
    john_app = frappe.db.get_value("Job Application", {"candidate": john_doe}, "name") if john_doe else None

    ryan_martinez = _get_candidate("ryan.martinez@email.com")

    offers = [
        {
            "candidate": john_doe,
            "job_posting": _get_job_posting("Senior Python Developer"),
            "company": "TechCorp Inc.",
            "offer_date": today(),
            "expiry_date": add_days(today(), 7),
            "status": "Draft",
            "position_title": "Senior Python Developer",
            "department": "Engineering",
            "joining_date": add_days(today(), 30),
            "salary_offered": 155000,
            "currency": "USD",
            "reporting_to": "James Wilson",
            "work_location": "San Francisco, USA",
            "benefits": "<ul><li>Health, dental, and vision insurance</li><li>401k matching up to 6%</li><li>Equity grant of 10,000 options</li><li>Annual bonus target of 15%</li></ul>",
            "is_accepted": 0,
            "onboarding_initiated": 0,
        },
        {
            "candidate": ryan_martinez,
            "job_posting": _get_job_posting("DevOps Engineer"),
            "company": "TechCorp Inc.",
            "offer_date": add_days(today(), -3),
            "expiry_date": add_days(today(), 4),
            "status": "Sent",
            "position_title": "DevOps Engineer",
            "department": "Infrastructure",
            "joining_date": add_days(today(), 21),
            "salary_offered": 140000,
            "currency": "USD",
            "reporting_to": "Emily Watson",
            "work_location": "Remote - Global",
            "benefits": "<ul><li>Comprehensive health coverage</li><li>Remote work stipend</li><li>Equity package</li><li>Flexible PTO</li></ul>",
            "is_accepted": 0,
            "onboarding_initiated": 0,
        },
    ]

    for o in offers:
        if o["candidate"] and o["job_posting"]:
            existing_name = frappe.db.exists("Offer Letter", {
                "candidate": o["candidate"],
                "job_posting": o["job_posting"],
            })
            if not existing_name:
                doc = frappe.get_doc({
                    "doctype": "Offer Letter",
                    "naming_series": "OFF-.YYYY.-.#####",
                    **o,
                })
                doc.insert(ignore_permissions=True)
    print("  Created 2 offer letters")


def _create_onboarding():
    john_doe = _get_candidate("john.doe@email.com")
    john_offer = frappe.db.get_value("Offer Letter", {"candidate": john_doe}, "name") if john_doe else None

    if not john_doe or not john_offer:
        print("  Skipping onboarding - required records not found")
        return

    onboarding = [
        {
            "candidate": john_doe,
            "offer_letter": john_offer,
            "company": "TechCorp Inc.",
            "joining_date": add_days(today(), 30),
            "status": "In Progress",
            "department": "Engineering",
            "designation": "Senior Software Engineer",
            "reports_to": "",
            "work_email": "john.doe@techcorp.com",
            "employee_type": "Full Time",
            "documents_verified": 0,
            "completion_status": 35,
            "documents": [
                {"document_type": "Identity Proof", "document_name": "Passport", "verification_status": "Pending"},
                {"document_type": "Address Proof", "document_name": "Utility Bill", "verification_status": "Pending"},
                {"document_type": "Degree Certificate", "document_name": "B.S. Computer Science", "verification_status": "Verified", "verified_by": "Administrator", "verification_date": today()},
                {"document_type": "Previous Employment", "document_name": "Experience Letter", "verification_status": "Pending"},
            ],
            "checklist": [
                {"task": "IT Equipment Setup", "description": "Configure laptop, set up accounts", "assigned_to": "Administrator", "due_date": add_days(today(), 25), "status": "In Progress"},
                {"task": "HR Policy Orientation", "description": "Review employee handbook and sign policies", "due_date": add_days(today(), 28), "status": "Pending"},
                {"task": "Benefits Enrollment", "description": "Complete health insurance and 401k enrollment", "due_date": add_days(today(), 35), "status": "Pending"},
                {"task": "Team Introduction", "description": "Schedule meet-and-greet with team members", "due_date": add_days(today(), 20), "status": "Completed"},
                {"task": "Security Training", "description": "Complete mandatory security awareness training", "due_date": add_days(today(), 14), "status": "Completed"},
                {"task": "Workspace Setup", "description": "Assign desk, building access, parking", "due_date": add_days(today(), 27), "status": "In Progress"},
            ],
        },
    ]

    for o in onboarding:
        existing_name = frappe.db.exists("Employee Onboarding", {
            "candidate": o["candidate"],
            "company": o["company"],
        })
        if not existing_name:
            doc = frappe.get_doc({
                "doctype": "Employee Onboarding",
                "naming_series": "ONB-.YYYY.-.#####",
                "candidate": o["candidate"],
                "offer_letter": o["offer_letter"],
                "company": o["company"],
                "joining_date": o["joining_date"],
                "status": o["status"],
                "department": o["department"],
                "designation": o["designation"],
                "work_email": o.get("work_email"),
                "employee_type": o.get("employee_type"),
                "documents_verified": o.get("documents_verified", 0),
                "completion_status": o.get("completion_status", 0),
            })
            for doc_item in o.get("documents", []):
                doc.append("documents", doc_item)
            for checklist_item in o.get("checklist", []):
                doc.append("checklist", checklist_item)
            doc.insert(ignore_permissions=True)
    print("  Created 1 employee onboarding with documents & checklist")


def _create_subscriptions():
    companies = frappe.get_all("Company Profile", pluck="name")
    plans = frappe.get_all("Subscription Plan", pluck="name")

    if not companies or not plans:
        print("  Skipping subscriptions - required records not found")
        return

    subscriptions = [
        {"company": "TechCorp Inc.", "subscription_plan": "Professional Plan", "start_date": add_days(today(), -180), "end_date": add_days(today(), 185), "status": "Active", "auto_renew": 1, "price": 299, "currency": "USD", "billing_email": "billing@techcorp.com", "payment_status": "Paid"},
        {"company": "InnovateSoft Solutions", "subscription_plan": "Basic Plan", "start_date": add_days(today(), -90), "end_date": add_days(today(), 275), "status": "Active", "auto_renew": 1, "price": 99, "currency": "USD", "billing_email": "accounts@innovatesoft.com", "payment_status": "Paid"},
        {"company": "DataFlow Analytics", "subscription_plan": "Free Plan", "start_date": add_days(today(), -30), "end_date": add_days(today(), 335), "status": "Active", "auto_renew": 0, "price": 0, "currency": "USD", "billing_email": "admin@dataflow.io", "payment_status": "Paid"},
        {"company": "CloudBase Systems", "subscription_plan": "Enterprise Plan", "start_date": add_days(today(), -60), "end_date": add_days(today(), 305), "status": "Active", "auto_renew": 1, "price": 999, "currency": "USD", "billing_email": "finance@cloudbase.io", "payment_status": "Paid"},
    ]

    for s in subscriptions:
        existing_name = frappe.db.exists("Employer Subscription", {
            "company": s["company"],
            "subscription_plan": s["subscription_plan"],
        })
        if not existing_name:
            doc = frappe.get_doc({
                "doctype": "Employer Subscription",
                "naming_series": "SUB-.YYYY.-.#####",
                **s,
            })
            doc.insert(ignore_permissions=True)
    print("  Created 4 employer subscriptions")


def _create_payment_transactions():
    subscriptions = frappe.get_all("Employer Subscription", pluck="name")

    if not subscriptions:
        print("  Skipping payment transactions - subscriptions not found")
        return

    transactions = [
        {"subscription": subscriptions[0], "company": "TechCorp Inc.", "transaction_date": add_days(today(), -180), "amount": 299, "currency": "USD", "payment_method": "Credit Card", "transaction_id": "TXN-1001-ABCD", "status": "Success"},
        {"subscription": subscriptions[0], "company": "TechCorp Inc.", "transaction_date": add_days(today(), -150), "amount": 299, "currency": "USD", "payment_method": "Credit Card", "transaction_id": "TXN-1002-EFGH", "status": "Success"},
        {"subscription": subscriptions[0], "company": "TechCorp Inc.", "transaction_date": add_days(today(), -120), "amount": 299, "currency": "USD", "payment_method": "Credit Card", "transaction_id": "TXN-1003-IJKL", "status": "Success"},
        {"subscription": subscriptions[0], "company": "TechCorp Inc.", "transaction_date": add_days(today(), -90), "amount": 299, "currency": "USD", "payment_method": "Debit Card", "transaction_id": "TXN-1004-MNOP", "status": "Success"},
        {"subscription": subscriptions[0], "company": "TechCorp Inc.", "transaction_date": add_days(today(), -60), "amount": 299, "currency": "USD", "payment_method": "Credit Card", "transaction_id": "TXN-1005-QRST", "status": "Success"},
        {"subscription": subscriptions[1], "company": "InnovateSoft Solutions", "transaction_date": add_days(today(), -90), "amount": 99, "currency": "USD", "payment_method": "Bank Transfer", "transaction_id": "TXN-2001-ABCD", "status": "Success"},
        {"subscription": subscriptions[1], "company": "InnovateSoft Solutions", "transaction_date": add_days(today(), -60), "amount": 99, "currency": "USD", "payment_method": "Bank Transfer", "transaction_id": "TXN-2002-EFGH", "status": "Success"},
        {"subscription": subscriptions[2], "company": "DataFlow Analytics", "transaction_date": add_days(today(), -30), "amount": 0, "currency": "USD", "payment_method": "", "transaction_id": "", "status": "Success"},
        {"subscription": subscriptions[3], "company": "CloudBase Systems", "transaction_date": add_days(today(), -60), "amount": 999, "currency": "USD", "payment_method": "Credit Card", "transaction_id": "TXN-4001-ABCD", "status": "Success"},
        {"subscription": subscriptions[3], "company": "CloudBase Systems", "transaction_date": add_days(today(), -30), "amount": 999, "currency": "USD", "payment_method": "Wire Transfer", "transaction_id": "TXN-4002-EFGH", "status": "Success"},
    ]

    for t in transactions:
        if t["subscription"]:
            frappe.get_doc({
                "doctype": "Payment Transaction",
                "naming_series": "PAY-.YYYY.MM.-.#####",
                **t,
            }).insert(ignore_permissions=True)
    print("  Created 10 payment transactions")


def _create_messages():
    messages = [
        {
            "message_type": "Email",
            "sender": "alice.johnson@techcorp.com",
            "recipients": "john.doe@email.com",
            "subject": "Interview Invitation - Senior Python Developer",
            "send_date": now_datetime(),
            "status": "Sent",
            "message_content": "<p>Dear John,</p><p>We are pleased to invite you for an interview for the Senior Python Developer position at TechCorp Inc.</p><p>Please check your candidate dashboard for details.</p><p>Best regards,<br>Alice Johnson<br>Senior Recruiter, TechCorp Inc.</p>",
            "related_to": _get_candidate("john.doe@email.com"),
            "related_doctype": "Candidate Profile",
        },
        {
            "message_type": "Email",
            "sender": "bob.smith@innovatesoft.com",
            "recipients": "jane.smith@email.com",
            "subject": "Application Received - Product Manager",
            "send_date": now_datetime(),
            "status": "Sent",
            "message_content": "<p>Dear Jane,</p><p>Thank you for applying for the Product Manager position at InnovateSoft Solutions. We have received your application and will review it shortly.</p><p>Best regards,<br>Bob Smith<br>Recruitment Lead, InnovateSoft Solutions</p>",
            "related_to": _get_candidate("jane.smith@email.com"),
            "related_doctype": "Candidate Profile",
        },
        {
            "message_type": "In-App",
            "sender": "diana.lee@cloudbase.io",
            "recipients": "david.brown@email.com",
            "subject": "Interview Update - Frontend Developer",
            "send_date": now_datetime(),
            "status": "Sent",
            "message_content": "<p>Hi David,</p><p>Your interview for the Frontend Developer position has been scheduled. Please check your dashboard for the details.</p><p>Best,<br>Diana Lee<br>Technical Recruiter, CloudBase Systems</p>",
            "related_to": _get_candidate("david.brown@email.com"),
            "related_doctype": "Candidate Profile",
        },
    ]

    for m in messages:
        frappe.get_doc({
            "doctype": "Message Center",
            **m,
        }).insert(ignore_permissions=True)
    print("  Created 3 messages")


def _create_notifications():
    notifications = [
        {"subject": "New application received for Senior Python Developer", "for_user": "Administrator", "type": "Alert", "document_type": "Job Application", "from_user": "Administrator", "email_status": "Not Sent", "sent_on": now_datetime()},
        {"subject": "Interview feedback pending review for John Doe", "for_user": "Administrator", "type": "Assignment", "document_type": "Interview Feedback", "from_user": "Administrator", "email_status": "Not Sent", "sent_on": now_datetime()},
        {"subject": "Offer letter created for John Doe", "for_user": "Administrator", "type": "Alert", "document_type": "Offer Letter", "from_user": "Administrator", "email_status": "Not Sent", "sent_on": now_datetime()},
        {"subject": "Candidate Jane Smith referred by Alice Johnson", "for_user": "Administrator", "type": "Alert", "document_type": "Candidate Profile", "from_user": "Administrator", "email_status": "Not Sent", "sent_on": now_datetime()},
    ]

    for n in notifications:
        frappe.get_doc({
            "doctype": "Notification Log",
            **n,
        }).insert(ignore_permissions=True)
    print("  Created 4 notification logs")
