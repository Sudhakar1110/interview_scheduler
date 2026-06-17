# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe


def execute():
    """Create default email templates"""
    templates = [
        {
            "template_name": "Interview Invitation",
            "subject": "Interview Invitation - {job_title}",
            "message": """Dear {candidate_name},

We are pleased to invite you for an interview for the position of {job_title} at {company_name}.

Interview Details:
- Date: {interview_date}
- Time: {interview_time}
- Duration: {duration}
- Type: {interview_type}
- Panel: {interviewer_names}

{meeting_link}

Please confirm your availability.

Best regards,
{company_name} HR Team"""
        },
        {
            "template_name": "Application Received",
            "subject": "Application Received - {job_title}",
            "message": """Dear {candidate_name},

Thank you for applying for the position of {job_title} at {company_name}.

We have received your application and our recruitment team will review it shortly. You will hear from us within 5-7 business days.

Best regards,
{company_name} HR Team"""
        },
        {
            "template_name": "Offer Letter Template",
            "subject": "Job Offer - {job_title}",
            "message": """Dear {candidate_name},

Congratulations! We are pleased to offer you the position of {job_title} at {company_name}.

Offer Details:
- Position: {job_title}
- Department: {department}
- Salary: {salary}
- Start Date: {start_date}

Please review the attached offer letter and respond by {expiry_date}.

Best regards,
{company_name} HR Team"""
        },
        {
            "template_name": "Interview Reminder",
            "subject": "Interview Reminder - Tomorrow",
            "message": """Dear {candidate_name},

This is a reminder about your interview scheduled for tomorrow.

Interview Details:
- Date: {interview_date}
- Time: {interview_time}
- Position: {job_title}
- Company: {company_name}

{meeting_link}

We look forward to meeting you!

Best regards,
{company_name} HR Team"""
        }
    ]
    
    for template_data in templates:
        if not frappe.db.exists("Email Template", template_data["template_name"]):
            template = frappe.get_doc({
                "doctype": "Email Template",
                **template_data
            })
            template.insert(ignore_permissions=True)
            frappe.db.commit()
            print("Created email template: {0}".format(template_data["template_name"]))