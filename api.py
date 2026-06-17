# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _


@frappe.whitelist(allow_guest=False)
def get_dashboard_stats():
    """Get dashboard statistics for HireFlow workspace"""
    stats = {
        "open_jobs": frappe.db.count("Job Posting", {"status": "Open"}),
        "total_candidates": frappe.db.count("Candidate Profile", {"is_active": 1}),
        "upcoming_interviews": frappe.db.count("Interview Schedule", {"status": ["in", ["Scheduled", "Confirmed"]]}),
        "hired_this_month": frappe.db.count("Employee Onboarding", {"status": "Completed"})
    }
    return stats


@frappe.whitelist()
def get_candidate_interviews(candidate):
    """Get interviews for a candidate"""
    if not candidate:
        return []
    
    interviews = frappe.get_all(
        "Interview Schedule",
        filters={"candidate": candidate},
        fields=["name", "interview_date", "interview_time", "status", "job_posting"],
        order_by="interview_date desc"
    )
    return interviews


@frappe.whitelist()
def calculate_match_score(job_posting, candidate):
    """Calculate match score between a job posting and candidate"""
    if not job_posting or not candidate:
        return 0
    
    from hireflow.utils.calculations import calculate_application_score
    
    # Create a temporary application-like dict for calculation
    class TempApplication:
        def __init__(self, job_posting, candidate):
            self.job_posting = job_posting
            self.candidate = candidate
    
    temp_app = TempApplication(job_posting, candidate)
    score = calculate_application_score(temp_app)
    return score
