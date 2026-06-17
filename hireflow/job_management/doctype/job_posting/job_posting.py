# -*- coding: utf-8 -*-
# Copyright (c) 2026, Antigravity and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, today
from frappe.website.website_generator import WebsiteGenerator
from hireflow.utils.validators import validate_job_posting


class JobPosting(WebsiteGenerator):
    website = frappe._dict(
        condition_field="publish_on_website",
        page_title_field="job_title",
    )

    def validate(self):
        validate_job_posting(self)
        self.set_created_by()
        self.set_modified_by()
    
    def set_created_by(self):
        if self.is_new():
            self.created_by = frappe.session.user
    
    def set_modified_by(self):
        self.modified_by = frappe.session.user
    
    def on_update(self):
        if self.publish_on_website and self.status == "Open":
            self.publish_to_website()
    
    def publish_to_website(self):
        """Publish job to website"""
        pass
    
    def get_context(self, context):
        """Context for web view"""
        context.no_cache = 1
        context.company_details = frappe.get_doc("Company Profile", self.company)
        context.similar_jobs = frappe.get_all(
            "Job Posting",
            filters={
                "job_category": self.job_category,
                "status": "Open",
                "name": ["!=", self.name]
            },
            fields=["name", "job_title", "company", "job_location", "posted_date"],
            limit=5
        )
        return context


def has_website_permission(doc, ptype, user, verbose=False):
    """Check if user has permission to view job"""
    if doc.status == "Open" and doc.publish_on_website:
        return True
    return False


def get_permission_query_conditions(user):
    """Permission query conditions"""
    if not user:
        user = frappe.session.user
    
    if "HireFlow Admin" in frappe.get_roles(user):
        return ""
    
    if "Employer" in frappe.get_roles(user):
        companies = frappe.get_all(
            "Company Profile",
            filters={"user": user},
            pluck="name"
        )
        if companies:
            return "`tabJob Posting`.company in {0}".format(tuple(companies))
        return "1=0"
    
    if "Recruiter" in frappe.get_roles(user):
        return "`tabJob Posting`.recruiter = '{0}'".format(user)
    
    return "`tabJob Posting`.publish_on_website = 1 and `tabJob Posting`.status = 'Open'"


@frappe.whitelist()
def get_job_applications(job_posting):
    """Get all applications for a job"""
    return frappe.get_all(
        "Job Application",
        filters={"job_posting": job_posting},
        fields=["name", "candidate", "status", "application_date", "score"],
        order_by="score desc"
    )


@frappe.whitelist()
def close_job(job_posting):
    """Close job posting"""
    doc = frappe.get_doc("Job Posting", job_posting)
    doc.status = "Closed"
    doc.save()
    return {"message": "Job closed successfully"}