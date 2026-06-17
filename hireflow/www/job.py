# -*- coding: utf-8 -*-
import frappe


def get_context(context):
    context.no_cache = 1
    
    job_id = frappe.form_dict.get("job_id")
    
    if not job_id:
        frappe.redirect_to_message("Job Not Found", "/jobs")
        return
    
    job = frappe.get_doc("Job Posting", job_id)
    context.job = job
    
    # Get company info
    context.company = frappe.get_doc("Company Profile", job.company)
    
    # Get similar jobs
    context.similar_jobs = frappe.get_all(
        "Job Posting",
        filters={
            "job_category": job.job_category,
            "status": "Open",
            "name": ["!=", job.name]
        },
        fields=["name", "job_title", "company", "job_location", "posted_date"],
        limit=5
    )
    
    return context