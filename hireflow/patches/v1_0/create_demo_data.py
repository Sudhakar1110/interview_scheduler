# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.utils import today, add_days


def execute():
    """Create comprehensive demo data for all HireFlow modules"""
    _create_job_locations()
    _create_companies()
    _create_recruiters()
    _create_candidates()
    _create_job_postings()
    _create_job_applications()
    _create_interview_schedules()
    _create_offer_letters()
    _create_onboarding()
    frappe.db.commit()
    print("Demo data created successfully.")


def _create_job_locations():
    locations = [
        {"location_name": "Remote - Global", "city": "", "state": "", "country": ""},
        {"location_name": "New York, USA", "city": "New York", "state": "New York", "country": "United States"},
        {"location_name": "San Francisco, USA", "city": "San Francisco", "state": "California", "country": "United States"},
        {"location_name": "London, UK", "city": "London", "state": "England", "country": "United Kingdom"},
        {"location_name": "Bangalore, India", "city": "Bangalore", "state": "Karnataka", "country": "India"},
    ]
    for loc in locations:
        if not frappe.db.exists("Job Location", loc["location_name"]):
            frappe.get_doc({"doctype": "Job Location", **loc}).insert(ignore_permissions=True)
    print("  Created job locations")


def _create_companies():
    companies = [
        {
            "company_name": "TechCorp Inc.",
            "website": "https://techcorp.com",
            "industry": "Technology",
            "company_size": "201-500",
            "description": "<p>TechCorp is a leading technology company specializing in enterprise software solutions. We build products that help businesses streamline their operations and grow.</p>",
            "founded_year": 2015,
            "headquarters": "San Francisco, USA",
            "contact_email": "hr@techcorp.com",
            "contact_phone": "+1-555-0100",
            "city": "San Francisco",
            "state": "California",
            "country": "United States",
            "is_active": 1,
        },
        {
            "company_name": "InnovateSoft Solutions",
            "website": "https://innovatesoft.com",
            "industry": "Information Technology",
            "company_size": "51-200",
            "description": "<p>InnovateSoft is a fast-growing software company building next-generation AI-powered tools for the healthcare industry.</p>",
            "founded_year": 2018,
            "headquarters": "New York, USA",
            "contact_email": "careers@innovatesoft.com",
            "contact_phone": "+1-555-0200",
            "city": "New York",
            "state": "New York",
            "country": "United States",
            "is_active": 1,
        },
        {
            "company_name": "DataFlow Analytics",
            "website": "https://dataflow.io",
            "industry": "Analytics",
            "company_size": "11-50",
            "description": "<p>DataFlow Analytics provides cutting-edge data visualization and business intelligence platforms for mid-market enterprises.</p>",
            "founded_year": 2020,
            "headquarters": "London, UK",
            "contact_email": "jobs@dataflow.io",
            "contact_phone": "+44-20-5555-0100",
            "city": "London",
            "state": "England",
            "country": "United Kingdom",
            "is_active": 1,
        },
    ]
    for c in companies:
        if not frappe.db.exists("Company Profile", c["company_name"]):
            frappe.get_doc({"doctype": "Company Profile", **c}).insert(ignore_permissions=True)
    print("  Created companies")


def _create_recruiters():
    recruiters = [
        {"recruiter_name": "Alice Johnson", "company": "TechCorp Inc.", "email": "alice@techcorp.com", "phone": "+1-555-0101", "designation": "Senior Recruiter", "department": "Human Resources", "skills": "Technical Recruitment, Interviewing, HR Operations", "is_active": 1},
        {"recruiter_name": "Bob Smith", "company": "InnovateSoft Solutions", "email": "bob@innovatesoft.com", "phone": "+1-555-0201", "designation": "Recruitment Lead", "department": "Talent Acquisition", "skills": "Executive Search, Campus Recruitment, Employer Branding", "is_active": 1},
        {"recruiter_name": "Carol Davis", "company": "TechCorp Inc.", "email": "carol@techcorp.com", "phone": "+1-555-0102", "designation": "Recruiter", "department": "Human Resources", "skills": "Screening, Interview Coordination, Offer Management", "is_active": 1},
    ]
    for r in recruiters:
        if not frappe.db.exists("Recruiter Profile", r["recruiter_name"]):
            frappe.get_doc({"doctype": "Recruiter Profile", **r}).insert(ignore_permissions=True)
    print("  Created recruiters")


def _create_candidates():
    candidates = [
        {"full_name": "John Doe", "email": "john.doe@email.com", "phone": "+1-555-1001", "current_location": "San Francisco, CA", "city": "San Francisco", "state": "California", "country": "United States", "current_company": "WebDev Studios", "current_designation": "Senior Software Engineer", "total_experience": 7, "current_salary": 135000, "expected_salary": 160000, "notice_period": "30 days", "source": "LinkedIn", "is_active": 1},
        {"full_name": "Jane Smith", "email": "jane.smith@email.com", "phone": "+1-555-1002", "current_location": "New York, NY", "city": "New York", "state": "New York", "country": "United States", "current_company": "FinanceHub Inc.", "current_designation": "Product Manager", "total_experience": 5, "current_salary": 120000, "expected_salary": 145000, "notice_period": "60 days", "source": "Referral", "referred_by": "Alice Johnson", "is_active": 1},
        {"full_name": "Mike Chen", "email": "mike.chen@email.com", "phone": "+1-555-1003", "current_location": "Bangalore, India", "city": "Bangalore", "state": "Karnataka", "country": "India", "current_company": "GlobalTech Systems", "current_designation": "DevOps Engineer", "total_experience": 4, "current_salary": 30000, "expected_salary": 45000, "notice_period": "45 days", "source": "Job Portal", "is_active": 1},
        {"full_name": "Sarah Williams", "email": "sarah.w@email.com", "phone": "+1-555-1004", "current_location": "London, UK", "city": "London", "state": "England", "country": "United Kingdom", "current_company": "DataDriven Ltd", "current_designation": "Data Scientist", "total_experience": 3, "current_salary": 65000, "expected_salary": 85000, "notice_period": "30 days", "source": "LinkedIn", "is_active": 1},
        {"full_name": "David Brown", "email": "david.brown@email.com", "phone": "+1-555-1005", "current_location": "Austin, TX", "city": "Austin", "state": "Texas", "country": "United States", "current_company": "StartupXYZ", "current_designation": "Frontend Developer", "total_experience": 2, "current_salary": 85000, "expected_salary": 110000, "notice_period": "15 days", "source": "Direct Application", "is_active": 1},
    ]
    for c in candidates:
        if not frappe.db.exists("Candidate Profile", c["email"]):
            frappe.get_doc({"doctype": "Candidate Profile", **c}).insert(ignore_permissions=True)
    print("  Created candidates")


def _create_job_postings():
    jobs = [
        {
            "job_title": "Senior Python Developer",
            "company": "TechCorp Inc.",
            "department": "Engineering",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "San Francisco, USA",
            "job_description": "<p>We are looking for an experienced Python developer to join our platform engineering team. You will design and build scalable backend services.</p>",
            "responsibilities": "<ul><li>Design and implement RESTful APIs</li><li>Optimize database queries and application performance</li><li>Mentor junior developers</li><li>Participate in code reviews</li></ul>",
            "requirements": "<ul><li>5+ years of Python experience</li><li>Experience with Django or FastAPI</li><li>Strong SQL skills</li><li>Experience with cloud services (AWS/GCP)</li></ul>",
            "benefits": "<ul><li>Competitive salary and equity</li><li>Health, dental, and vision insurance</li><li>Remote-friendly</li><li>401k matching</li></ul>",
            "min_experience": 5, "max_experience": 10,
            "min_salary": 140000, "max_salary": 180000,
            "number_of_openings": 2,
            "application_deadline": add_days(today(), 45),
            "status": "Open", "publish_on_website": 1,
        },
        {
            "job_title": "Product Manager",
            "company": "InnovateSoft Solutions",
            "department": "Product",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "New York, USA",
            "job_description": "<p>We're seeking a skilled Product Manager to drive our AI-powered healthcare analytics platform.</p>",
            "responsibilities": "<ul><li>Define product roadmap and strategy</li><li>Gather and prioritize product requirements</li><li>Work closely with engineering and design teams</li><li>Analyze market trends and competition</li></ul>",
            "requirements": "<ul><li>3+ years of product management experience</li><li>Experience with SaaS products</li><li>Strong analytical and communication skills</li><li>Healthcare domain experience is a plus</li></ul>",
            "benefits": "<ul><li>Competitive compensation</li><li>Stock options</li><li>Flexible work arrangements</li><li>Learning and development budget</li></ul>",
            "min_experience": 3, "max_experience": 8,
            "min_salary": 120000, "max_salary": 160000,
            "number_of_openings": 1,
            "application_deadline": add_days(today(), 30),
            "status": "Open", "publish_on_website": 1,
        },
        {
            "job_title": "DevOps Engineer",
            "company": "TechCorp Inc.",
            "department": "Infrastructure",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "Remote - Global",
            "job_description": "<p>Join our infrastructure team to build and maintain our cloud-native platform used by millions.</p>",
            "responsibilities": "<ul><li>Manage Kubernetes clusters</li><li>Automate deployment pipelines</li><li>Monitor system health and performance</li><li>Implement security best practices</li></ul>",
            "requirements": "<ul><li>3+ years of DevOps experience</li><li>Strong knowledge of Docker and Kubernetes</li><li>Experience with CI/CD tools</li><li>AWS or GCP certification preferred</li></ul>",
            "benefits": "<ul><li>Remote-first culture</li><li>Competitive salary</li><li>Home office stipend</li><li>Annual bonus</li></ul>",
            "min_experience": 3, "max_experience": 7,
            "min_salary": 110000, "max_salary": 145000,
            "number_of_openings": 1,
            "application_deadline": add_days(today(), 60),
            "status": "Open", "publish_on_website": 1,
        },
        {
            "job_title": "Data Scientist",
            "company": "DataFlow Analytics",
            "department": "Data Science",
            "job_category": "Information Technology",
            "job_type": "Full Time",
            "job_location": "London, UK",
            "job_description": "<p>Help us build the next generation of AI-powered analytics tools for businesses worldwide.</p>",
            "responsibilities": "<ul><li>Develop machine learning models</li><li>Analyze large datasets to extract insights</li><li>Build data pipelines</li><li>Present findings to stakeholders</li></ul>",
            "requirements": "<ul><li>2+ years of data science experience</li><li>Proficiency in Python and SQL</li><li>Experience with ML frameworks (TensorFlow, PyTorch)</li><li>Strong statistical analysis skills</li></ul>",
            "benefits": "<ul><li>Competitive salary</li><li>Flexible working hours</li><li>Training budget</li><li>Team social events</li></ul>",
            "min_experience": 2, "max_experience": 6,
            "min_salary": 70000, "max_salary": 95000,
            "number_of_openings": 2,
            "application_deadline": add_days(today(), 30),
            "status": "Open", "publish_on_website": 1,
        },
    ]
    for j in jobs:
        title = j["job_title"]
        if not frappe.db.exists("Job Posting", {"job_title": title}):
            frappe.get_doc({"doctype": "Job Posting", **j}).insert(ignore_permissions=True)
    print("  Created job postings")


def _get_job_posting(title):
    return frappe.db.get_value("Job Posting", {"job_title": title}, "name")


def _get_candidate(email):
    return frappe.db.get_value("Candidate Profile", {"email": email}, "name")


def _create_job_applications():
    applications = [
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("john.doe@email.com"), "company": "TechCorp Inc.", "status": "Interview", "application_date": add_days(today(), -14), "score": 85, "source": "LinkedIn", "cover_letter": "<p>I am very excited about this opportunity at TechCorp. With 7 years of Python experience, I believe I would be a great fit for this role.</p>"},
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("david.brown@email.com"), "company": "TechCorp Inc.", "status": "Applied", "application_date": add_days(today(), -3), "score": 62, "source": "Direct Application"},
        {"job_posting": _get_job_posting("Product Manager"), "candidate": _get_candidate("jane.smith@email.com"), "company": "InnovateSoft Solutions", "status": "Screening", "application_date": add_days(today(), -7), "score": 78, "source": "Referral", "cover_letter": "<p>I was referred by Alice Johnson who I believe would vouch for my product management expertise.</p>"},
        {"job_posting": _get_job_posting("DevOps Engineer"), "candidate": _get_candidate("mike.chen@email.com"), "company": "TechCorp Inc.", "status": "Interview", "application_date": add_days(today(), -10), "score": 88, "source": "Job Portal"},
        {"job_posting": _get_job_posting("Data Scientist"), "candidate": _get_candidate("sarah.williams@email.com"), "company": "DataFlow Analytics", "status": "Applied", "application_date": add_days(today(), -5), "score": 72, "source": "LinkedIn"},
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("mike.chen@email.com"), "company": "TechCorp Inc.", "status": "Rejected", "application_date": add_days(today(), -20), "score": 55, "source": "Job Portal", "rejection_reason": "Skill set not aligned with requirements"},
    ]
    for a in applications:
        if a["candidate"] and a["job_posting"]:
            if not frappe.db.exists("Job Application", {"job_posting": a["job_posting"], "candidate": a["candidate"]}):
                frappe.get_doc({"doctype": "Job Application", **a}).insert(ignore_permissions=True)
    print("  Created job applications")


def _create_interview_schedules():
    schedules = [
        {"job_posting": _get_job_posting("Senior Python Developer"), "candidate": _get_candidate("john.doe@email.com"), "company": "TechCorp Inc.", "interview_date": add_days(today(), 2), "interview_time": "10:00:00", "duration": "60 mins", "status": "Scheduled", "interview_type": "Technical", "interview_mode": "Video Call", "meeting_link": "https://meet.google.com/abc-defg-hij", "interview_round": 1, "feedback_required": 1},
        {"job_posting": _get_job_posting("DevOps Engineer"), "candidate": _get_candidate("mike.chen@email.com"), "company": "TechCorp Inc.", "interview_date": add_days(today(), 5), "interview_time": "14:30:00", "duration": "45 mins", "status": "Scheduled", "interview_type": "Technical", "interview_mode": "Video Call", "meeting_link": "https://meet.google.com/xyz-uvwx-yz", "interview_round": 1, "feedback_required": 1},
        {"job_posting": _get_job_posting("Product Manager"), "candidate": _get_candidate("jane.smith@email.com"), "company": "InnovateSoft Solutions", "interview_date": add_days(today(), -1), "interview_time": "11:00:00", "duration": "60 mins", "status": "Completed", "interview_type": "HR", "interview_mode": "Video Call", "meeting_link": "https://zoom.us/j/123456789", "interview_round": 1, "feedback_required": 0},
    ]
    for s in schedules:
        if s["candidate"] and s["job_posting"]:
            if not frappe.db.exists("Interview Schedule", {"candidate": s["candidate"], "job_posting": s["job_posting"], "interview_date": s["interview_date"]}):
                frappe.get_doc({"doctype": "Interview Schedule", **s}).insert(ignore_permissions=True)
    print("  Created interview schedules")


def _create_offer_letters():
    offers = [
        {"candidate_name": "John Doe", "candidate_email": "john.doe@email.com", "job_title": "Senior Python Developer", "company": "TechCorp Inc.", "offer_date": today(), "expiry_date": add_days(today(), 7), "status": "Draft", "salary": 155000, "currency": "USD", "annual_bonus": 15000, "stock_options": 5000, "start_date": add_days(today(), 30), "notes": "Standard offer package for senior engineering role."},
    ]
    for o in offers:
        if not frappe.db.exists("Offer Letter", {"candidate_email": o["candidate_email"], "job_title": o["job_title"]}):
            frappe.get_doc({"doctype": "Offer Letter", **o}).insert(ignore_permissions=True)
    print("  Created offer letters")


def _create_onboarding():
    onboarding = [
        {"candidate_name": "John Doe", "job_title": "Senior Python Developer", "company": "TechCorp Inc.", "offer_date": today(), "start_date": add_days(today(), 30), "department": "Engineering", "designation": "Senior Software Engineer", "status": "Pending", "onboarding_type": "Technical"},
    ]
    for o in onboarding:
        if not frappe.db.exists("Employee Onboarding", {"candidate_name": o["candidate_name"], "job_title": o["job_title"]}):
            frappe.get_doc({"doctype": "Employee Onboarding", **o}).insert(ignore_permissions=True)
    print("  Created onboarding records")
