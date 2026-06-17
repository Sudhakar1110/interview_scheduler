# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document
from hireflow.utils.validators import validate_interview_schedule
from hireflow.utils.notifications import send_interview_invitation


class InterviewSchedule(Document):
    def validate(self):
        validate_interview_schedule(self)
        self.set_company()
    
    def set_company(self):
        if self.job_posting and not self.company:
            job = frappe.get_doc("Job Posting", self.job_posting)
            self.company = job.company
    
    def on_submit(self):
        self.send_invitation()
        self.update_application_status()
        self.send_reminder()
    
    def send_invitation(self):
        try:
            send_interview_invitation(self)
        except:
            pass
    
    def send_reminder(self):
        try:
            from hireflow.tasks import send_interview_reminder_email
            send_interview_reminder_email(self)
            self.reminder_sent = 1
            # No self.save() here — called from on_submit() where the
            # document is already being saved as part of the submit process.
        except:
            pass
    
    def update_application_status(self):
        if self.job_application:
            frappe.db.set_value("Job Application", self.job_application, "status", "Interview")
            frappe.db.set_value("Job Application", self.job_application, "current_round", self.interview_round or 1)