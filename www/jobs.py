# -*- coding: utf-8 -*-
import frappe


def get_context(context):
    context.no_cache = 1
    
    # Get filter parameters
    category = frappe.form_dict.get("category")
    job_type = frappe.form_dict.get("type")
    location = frappe.form_dict.get("location")
    search = frappe.form_dict.get("q")
    
    # Build filters
    filters = {
        "status": "Open",
        "publish_on_website": 1
    }
    
    if category:
        filters["job_category"] = category
    if job_type:
        filters["job_type"] = job_type
    if location:
        filters["job_location"] = ["like", "%{0}%".format(location)]
    
    # Get jobs
    jobs = frappe.get_all(
        "Job Posting",
        filters=filters,
        fields=["name", "job_title", "company", "job_location", "job_type", "job_category", "posted_date", "job_description"],
        order_by="posted_date desc"
    )
    
    # Filter by search query
    if search:
        jobs = [j for j in jobs if search.lower() in j.job_title.lower() or search.lower() in j.company.lower()]
    
    context.jobs = jobs
    
    # Get categories for filter
    context.categories = frappe.get_all(
        "Job Category",
        fields=["name", "category_name"],
        order_by="category_name"
    )
    
    # Get job types for filter
    context.job_types = frappe.get_all(
        "Job Type",
        fields=["name", "type_name"],
        order_by="type_name"
    )
    
    return context