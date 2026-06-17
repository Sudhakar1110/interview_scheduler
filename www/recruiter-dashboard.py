# -*- coding: utf-8 -*-
import frappe
from frappe.utils import today, now_datetime


def get_context(context):
    context.no_cache = 1
    
    if frappe.session.user == "Guest":
        frappe.redirect_to_login()
        return
    
    # Get today's interviews
    context.today_interviews = frappe.get_all(
        "Interview Schedule",
        filters={
            "interviewer": frappe.session.user,
            "interview_date": today()
        },
        fields=["name", "candidate", "job_posting", "interview_time", "interview_type", "status"],
        order_by="interview_time asc"
    )
    
    # Get pending applications
    context.pending_applications = frappe.get_all(
        "Job Application",
        filters={"assigned_recruiter": frappe.session.user},
        fields=["name", "candidate", "job_posting", "application_date", "score"],
        order_by="application_date desc",
        limit=20
    )
    
    # Get stats
    context.stats = {
        "pending_screening": frappe.db.count("Job Application", {"assigned_recruiter": frappe.session.user, "status": "Applied"}),
        "interviews_today": len(context.today_interviews),
        "offers_pending": frappe.db.count("Offer Letter", {"recruiter": frappe.session.user, "status": "Sent"}),
        "placements": frappe.db.count("Employee Onboarding", {"recruiter": frappe.session.user, "status": "Completed"})
    }
    
    return context