# -*- coding: utf-8 -*-
import frappe


def get_context(context):
    context.no_cache = 1
    
    if frappe.session.user == "Guest":
        frappe.redirect_to_login()
        return
    
    # Get employer company
    company = frappe.db.get_value("Company Profile", {"user": frappe.session.user}, "name")
    
    if not company:
        context.show_onboarding = True
        return context
    
    context.company = frappe.get_doc("Company Profile", company)
    
    # Get jobs
    context.jobs = frappe.get_all(
        "Job Posting",
        filters={"company": company},
        fields=["name", "job_title", "posted_date", "status"],
        order_by="posted_date desc"
    )
    
    # Get applications
    context.applications = frappe.get_all(
        "Job Application",
        filters={"company": company},
        fields=["name", "candidate", "job_posting", "application_date", "status"],
        order_by="application_date desc",
        limit=20
    )
    
    # Get stats
    context.stats = {
        "open_jobs": frappe.db.count("Job Posting", {"company": company, "status": "Open"}),
        "total_applications": len(context.applications),
        "interviews_scheduled": frappe.db.count("Interview Schedule", {"company": company}),
        "hired": frappe.db.count("Employee Onboarding", {"company": company, "status": "Completed"})
    }
    
    return context