# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import now_datetime, add_days, getdate, today


def send_interview_reminders():
    """Send interview reminders 24 hours before scheduled time"""
    tomorrow = add_days(today(), 1)
    
    interviews = frappe.get_all(
        "Interview Schedule",
        filters={
            "interview_date": tomorrow,
            "status": ["in", ["Scheduled", "Confirmed"]],
            "reminder_sent": 0
        },
        fields=["name", "candidate", "interviewer", "job_posting", "interview_time"]
    )
    
    for interview in interviews:
        try:
            send_interview_reminder_email(interview)
            frappe.db.set_value("Interview Schedule", interview.name, "reminder_sent", 1)
        except Exception as e:
            frappe.log_error("Failed to send interview reminder: {0}".format(str(e)))
    
    frappe.db.commit()


def send_interview_reminder_email(interview):
    """Send interview reminder email"""
    from hireflow.utils.notifications import send_email_from_template
    
    candidate = frappe.get_doc("Candidate Profile", interview.candidate)
    job = frappe.get_doc("Job Posting", interview.job_posting)
    
    context = {
        "candidate_name": candidate.full_name,
        "job_title": job.job_title,
        "company_name": job.company,
        "interview_date": interview.interview_date,
        "interview_time": interview.interview_time
    }
    
    send_email_from_template(
        template_name="Interview Reminder",
        recipients=[candidate.email],
        context=context
    )


def check_offer_expiry():
    """Check and mark expired offers"""
    today_date = getdate()
    
    expired_offers = frappe.get_all(
        "Offer Letter",
        filters={
            "expiry_date": ["<", today_date],
            "status": "Sent"
        },
        fields=["name"]
    )
    
    for offer in expired_offers:
        frappe.db.set_value("Offer Letter", offer.name, "status", "Expired")
        
        offer_doc = frappe.get_doc("Offer Letter", offer.name)
        send_offer_expiry_notification(offer_doc)
    
    frappe.db.commit()


def send_offer_expiry_notification(offer):
    """Send offer expiry notification to employer"""
    frappe.publish_realtime(
        event="offer_expired",
        message={
            "offer": offer.name,
            "candidate": offer.candidate,
            "job": offer.job_posting
        },
        user=offer.owner
    )


def update_job_status():
    """Update job status based on application deadline"""
    today_date = getdate()
    
    expired_jobs = frappe.get_all(
        "Job Posting",
        filters={
            "application_deadline": ["<", today_date],
            "status": "Open"
        },
        fields=["name"]
    )
    
    for job in expired_jobs:
        frappe.db.set_value("Job Posting", job.name, "status", "Closed")
    
    frappe.db.commit()


def send_application_status_updates():
    """Send daily application status updates to candidates"""
    yesterday = add_days(today(), -1)
    
    applications = frappe.get_all(
        "Job Application",
        filters={
            "modified": [">=", yesterday],
            "status_update_sent": 0
        },
        fields=["name", "candidate", "job_posting", "status"]
    )
    
    for app in applications:
        try:
            send_status_update_email(app)
            frappe.db.set_value("Job Application", app.name, "status_update_sent", 1)
        except Exception as e:
            frappe.log_error("Failed to send status update: {0}".format(str(e)))
    
    frappe.db.commit()


def send_status_update_email(application):
    """Send application status update email"""
    from hireflow.utils.notifications import send_email_from_template
    
    candidate = frappe.get_doc("Candidate Profile", application.candidate)
    job = frappe.get_doc("Job Posting", application.job_posting)
    
    context = {
        "candidate_name": candidate.full_name,
        "job_title": job.job_title,
        "company_name": job.company,
        "status": application.status
    }
    
    send_email_from_template(
        template_name="Application Received",
        recipients=[candidate.email],
        context=context
    )


def send_weekly_report():
    """Send weekly hiring report to employers"""
    employers = frappe.get_all(
        "Company Profile",
        filters={"is_active": 1},
        fields=["name", "contact_email"]
    )
    
    for employer in employers:
        try:
            generate_and_send_weekly_report(employer)
        except Exception as e:
            frappe.log_error("Failed to send weekly report: {0}".format(str(e)))


def generate_and_send_weekly_report(employer):
    """Generate and send weekly report"""
    last_week = add_days(today(), -7)
    
    stats = {
        "applications": frappe.db.count("Job Application", {
            "company": employer.name,
            "creation": [">=", last_week]
        }),
        "interviews": frappe.db.count("Interview Schedule", {
            "company": employer.name,
            "creation": [">=", last_week]
        }),
        "offers": frappe.db.count("Offer Letter", {
            "company": employer.name,
            "creation": [">=", last_week]
        }),
        "hires": frappe.db.count("Employee Onboarding", {
            "company": employer.name,
            "creation": [">=", last_week]
        })
    }
    return stats


def cleanup_old_notifications():
    """Cleanup notifications older than 30 days"""
    thirty_days_ago = add_days(today(), -30)
    
    frappe.db.sql("""
        DELETE FROM `tabNotification Log`
        WHERE creation < %s
    """, (thirty_days_ago,))
    
    frappe.db.commit()


def generate_monthly_analytics():
    """Generate monthly analytics and insights"""
    pass


def process_subscription_renewals():
    """Process monthly subscription renewals"""
    today_date = getdate()
    
    expiring_subscriptions = frappe.get_all(
        "Employer Subscription",
        filters={
            "end_date": today_date,
            "auto_renew": 1,
            "status": "Active"
        },
        fields=["name", "company", "subscription_plan"]
    )
    
    for sub in expiring_subscriptions:
        try:
            renew_subscription(sub)
        except Exception as e:
            frappe.log_error("Failed to renew subscription: {0}".format(str(e)))


def renew_subscription(subscription):
    """Renew subscription"""
    pass