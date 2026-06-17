# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint


def calculate_application_score(application):
    """Calculate application match score based on skills and experience"""
    score = 0
    
    # Get job requirements
    job = frappe.get_doc("Job Posting", application.job_posting)
    candidate = frappe.get_doc("Candidate Profile", application.candidate)
    
    # Skill match (40%)
    skill_match = calculate_skill_match(job, candidate)
    score += skill_match * 0.4
    
    # Experience match (30%)
    experience_match = calculate_experience_match(job, candidate)
    score += experience_match * 0.3
    
    # Education match (20%)
    education_match = calculate_education_match(job, candidate)
    score += education_match * 0.2
    
    # Location match (10%)
    location_match = calculate_location_match(job, candidate)
    score += location_match * 0.1
    
    return min(score, 100)


def calculate_skill_match(job, candidate):
    """Calculate skill match percentage"""
    if not job.required_skills:
        return 100
    
    required_skills = set([skill.skill for skill in job.required_skills])
    candidate_skills = set([skill.skill for skill in candidate.skills])
    
    if not required_skills:
        return 100
    
    matched_skills = required_skills.intersection(candidate_skills)
    return (len(matched_skills) / len(required_skills)) * 100


def calculate_experience_match(job, candidate):
    """Calculate experience match percentage"""
    required_exp = flt(job.min_experience)
    candidate_exp = flt(candidate.total_experience)
    
    if candidate_exp >= required_exp:
        return 100
    elif candidate_exp >= required_exp * 0.7:
        return 70
    elif candidate_exp >= required_exp * 0.5:
        return 50
    else:
        return 30


def calculate_education_match(job, candidate):
    """Calculate education match percentage"""
    return 80


def calculate_location_match(job, candidate):
    """Calculate location match percentage"""
    if job.location == candidate.current_location:
        return 100
    else:
        return 50


def calculate_hiring_conversion_rate(company, from_date, to_date):
    """Calculate hiring conversion rate"""
    total_applications = frappe.db.count("Job Application", {
        "company": company,
        "creation": ["between", [from_date, to_date]]
    })
    
    total_hires = frappe.db.count("Employee Onboarding", {
        "company": company,
        "creation": ["between", [from_date, to_date]]
    })
    
    if total_applications == 0:
        return 0
    
    return (total_hires / total_applications) * 100


def calculate_time_to_hire(company, from_date, to_date):
    """Calculate average time to hire"""
    applications = frappe.db.sql("""
        SELECT 
            ja.creation as application_date,
            eo.creation as hire_date
        FROM `tabJob Application` ja
        INNER JOIN `tabEmployee Onboarding` eo ON ja.candidate = eo.candidate
        WHERE ja.company = %s
        AND ja.creation BETWEEN %s AND %s
    """, (company, from_date, to_date), as_dict=1)
    
    if not applications:
        return 0
    
    total_days = 0
    for app in applications:
        days = (app.hire_date - app.application_date).days
        total_days += days
    
    return total_days / len(applications)


def calculate_offer_acceptance_rate(company, from_date, to_date):
    """Calculate offer acceptance rate"""
    total_offers = frappe.db.count("Offer Letter", {
        "company": company,
        "creation": ["between", [from_date, to_date]]
    })
    
    accepted_offers = frappe.db.count("Offer Letter", {
        "company": company,
        "status": "Accepted",
        "creation": ["between", [from_date, to_date]]
    })
    
    if total_offers == 0:
        return 0
    
    return (accepted_offers / total_offers) * 100