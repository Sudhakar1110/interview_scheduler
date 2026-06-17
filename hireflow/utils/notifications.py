# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import get_url


def send_email_from_template(template_name, recipients, context):
    """Send email using email template"""
    template = frappe.get_doc("Email Template", template_name)
    
    subject = frappe.render_template(template.subject, context)
    message = frappe.render_template(template.message, context)
    
    frappe.sendmail(
        recipients=recipients,
        subject=subject,
        message=message,
        delayed=False
    )


def send_interview_invitation(interview):
    """Send interview invitation to candidate"""
    candidate = frappe.get_doc("Candidate Profile", interview.candidate)
    job = frappe.get_doc("Job Posting", interview.job_posting)
    
    interviewer_names = ", ".join([
        frappe.db.get_value("Panel Member", i.interviewer, "full_name") 
        for i in interview.interviewers
    ])
    
    context = {
        "candidate_name": candidate.full_name,
        "job_title": job.job_title,
        "company_name": job.company,
        "interview_date": interview.interview_date,
        "interview_time": interview.interview_time,
        "duration": interview.duration,
        "interview_type": interview.interview_type,
        "interviewer_names": interviewer_names,
        "meeting_link": interview.meeting_link or "N/A"
    }
    
    send_email_from_template(
        template_name="Interview Invitation",
        recipients=[candidate.email],
        context=context
    )


def send_application_received_email(application):
    """Send application received confirmation"""
    candidate = frappe.get_doc("Candidate Profile", application.candidate)
    job = frappe.get_doc("Job Posting", application.job_posting)
    
    context = {
        "candidate_name": candidate.full_name,
        "job_title": job.job_title,
        "company_name": job.company
    }
    
    send_email_from_template(
        template_name="Application Received",
        recipients=[candidate.email],
        context=context
    )


def send_offer_letter_email(offer):
    """Send offer letter to candidate"""
    candidate = frappe.get_doc("Candidate Profile", offer.candidate)
    job = frappe.get_doc("Job Posting", offer.job_posting)
    
    context = {
        "candidate_name": candidate.full_name,
        "job_title": job.job_title,
        "company_name": job.company,
        "department": job.department,
        "salary": offer.salary_offered,
        "start_date": offer.joining_date,
        "expiry_date": offer.expiry_date
    }
    
    send_email_from_template(
        template_name="Offer Letter Template",
        recipients=[candidate.email],
        context=context
    )


def create_notification(doctype, document_name, message, users):
    """Create notification for users"""
    for user in users:
        notification = frappe.get_doc({
            "doctype": "Notification Log",
            "for_user": user,
            "type": "Alert",
            "document_type": doctype,
            "document_name": document_name,
            "subject": message
        })
        notification.insert(ignore_permissions=True)


def notify_recruiter_new_application(application):
    """Notify recruiter about new application"""
    job = frappe.get_doc("Job Posting", application.job_posting)
    
    if job.recruiter:
        message = "New application received for {0}".format(job.job_title)
        create_notification("Job Application", application.name, message, [job.recruiter])