# -*- coding: utf-8 -*-
import frappe
import json


def get_context(context):
    context.no_cache = 1
    
    # Get featured jobs
    context.featured_jobs = frappe.get_all(
        "Job Posting",
        filters={
            "status": "Open",
            "publish_on_website": 1
        },
        fields=["name", "job_title", "company", "job_location", "job_type", "posted_date"],
        order_by="posted_date desc",
        limit=6
    )
    
    # Get job statistics
    context.stats = {
        "total_jobs": frappe.db.count("Job Posting", {"status": "Open"}),
        "total_companies": frappe.db.count("Company Profile", {"is_active": 1}),
        "total_candidates": frappe.db.count("Candidate Profile"),
        "total_hires": frappe.db.count("Employee Onboarding", {"status": "Completed"})
    }
    
    return context