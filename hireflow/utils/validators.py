# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, today


def validate_interview_schedule(doc, method=None):
    """Validate interview schedule"""
    # Check if interview date is in future
    if getdate(doc.interview_date) < getdate(today()):
        frappe.throw(_("Interview date cannot be in the past"))
    
    # Check interviewer availability
    check_interviewer_availability(doc)
    
    # Check candidate availability
    check_candidate_availability(doc)


def check_interviewer_availability(interview):
    """Check if interviewers are available (checks child table interviewers)"""
    if not interview.interviewers:
        return
    
    # Collect interviewer names from child table
    interviewer_names = [row.interviewer for row in interview.interviewers if row.interviewer]
    if not interviewer_names:
        return
    
    # Find other Interview Schedules at the same date/time
    other_schedules = frappe.get_all("Interview Schedule",
        filters={
            "interview_date": interview.interview_date,
            "interview_time": interview.interview_time,
            "status": ["in", ["Scheduled", "Confirmed"]],
            "name": ["!=", interview.name]
        },
        pluck="name"
    )
    
    if not other_schedules:
        return
    
    # Check if any of those schedules have the same interviewers
    conflicting = frappe.db.get_all("Interview Panel",
        filters={
            "parent": ["in", other_schedules],
            "interviewer": ["in", interviewer_names]
        },
        pluck="interviewer",
        distinct=1
    )
    
    if conflicting:
        frappe.throw(_("Interviewer(s) {0} are not available at the selected time").format(
            ", ".join(set(conflicting))
        ))


def check_candidate_availability(interview):
    """Check if candidate has another interview at the same time"""
    conflicts = frappe.db.count("Interview Schedule", {
        "candidate": interview.candidate,
        "interview_date": interview.interview_date,
        "interview_time": interview.interview_time,
        "status": ["in", ["Scheduled", "Confirmed"]],
        "name": ["!=", interview.name]
    })
    
    if conflicts > 0:
        frappe.throw(_("Candidate has another interview at the selected time"))


def validate_offer_letter(doc):
    """Validate offer letter"""
    # Check if candidate already has an active offer
    existing_offers = frappe.db.count("Offer Letter", {
        "candidate": doc.candidate,
        "status": ["in", ["Sent", "Accepted"]],
        "name": ["!=", doc.name]
    })
    
    if existing_offers > 0:
        frappe.throw(_("Candidate already has an active offer"))
    
    # Check if expiry date is valid
    if getdate(doc.expiry_date) <= getdate(today()):
        frappe.throw(_("Expiry date must be in the future"))


def validate_subscription_limits(company, doctype):
    """Validate if company has reached subscription limits"""
    subscription = frappe.db.get_value("Employer Subscription", 
        {"company": company, "status": "Active"}, 
        ["subscription_plan"], as_dict=1)
    
    if not subscription:
        frappe.throw(_("No active subscription found for this company"))
    
    plan = frappe.get_doc("Subscription Plan", subscription.subscription_plan)
    
    if doctype == "Job Posting":
        current_jobs = frappe.db.count("Job Posting", {
            "company": company,
            "status": "Open"
        })
        
        if plan.max_jobs != -1 and current_jobs >= plan.max_jobs:
            frappe.throw(_("You have reached the maximum number of job postings for your plan"))
    
    elif doctype == "Job Application":
        current_month_apps = frappe.db.count("Job Application", {
            "company": company,
            "creation": [">=", frappe.utils.get_first_day()]
        })
        
        if plan.max_applications != -1 and current_month_apps >= plan.max_applications:
            frappe.throw(_("You have reached the maximum number of applications for this month"))


def validate_job_posting(doc):
    """Validate job posting"""
    # Check subscription limits
    if doc.is_new():
        validate_subscription_limits(doc.company, "Job Posting")
    
    # Validate application deadline
    if getdate(doc.application_deadline) < getdate(today()):
        frappe.throw(_("Application deadline cannot be in the past"))
    
    # Validate salary range
    if doc.min_salary and doc.max_salary:
        if doc.min_salary > doc.max_salary:
            frappe.throw(_("Minimum salary cannot be greater than maximum salary"))