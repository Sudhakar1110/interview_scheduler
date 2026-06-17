# -*- coding: utf-8 -*-
import frappe


def get_context(context):
    context.no_cache = 1
    
    if frappe.session.user == "Guest":
        frappe.redirect_to_login()
        return
    
    # Get current user
    user = frappe.get_doc("User", frappe.session.user)
    context.user = user
    
    # Get user applications
    context.applications = frappe.get_all(
        "Job Application",
        filters={"candidate": frappe.session.user},
        fields=["name", "job_posting", "application_date", "status"],
        order_by="application_date desc"
    )
    
    # Get user interviews
    context.interviews = frappe.get_all(
        "Interview Schedule",
        filters={"candidate": frappe.session.user},
        fields=["name", "job_posting", "interview_date", "interview_time", "interview_type", "status"],
        order_by="interview_date asc"
    )
    
    # Get stats
    context.stats = {
        "applications": len(context.applications),
        "interviews": len(context.interviews),
        "offers": frappe.db.count("Job Application", {"candidate": frappe.session.user, "status": "Offer"})
    }
    
    return context