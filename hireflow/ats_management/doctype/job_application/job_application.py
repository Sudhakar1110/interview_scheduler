# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document
from hireflow.utils.notifications import send_application_received_email


class JobApplication(Document):
    def validate(self):
        self.set_company()
        self.calculate_score()
    
    def set_company(self):
        if self.job_posting and not self.company:
            job = frappe.get_doc("Job Posting", self.job_posting)
            self.company = job.company
    
    def calculate_score(self):
        if self.job_posting and self.candidate:
            try:
                from hireflow.utils.calculations import calculate_application_score
                self.score = calculate_application_score(self)
            except:
                self.score = 0
    
    def on_submit(self):
        self.send_application_notification()
    
    def on_update(self):
        if self.status == "Interview" and self.status != self._doc_before_save.status:
            frappe.publish_realtime("application_status_changed", {
                "application": self.name,
                "status": self.status
            })
    
    def send_application_notification(self):
        try:
            send_application_received_email(self)
        except:
            pass


def get_permission_query_conditions(user):
    if "HireFlow Admin" in frappe.get_roles(user):
        return ""
    
    if "Employer" in frappe.get_roles(user):
        companies = frappe.get_all("Company Profile", filters={"user": user}, pluck="name")
        if companies:
            return "`tabJob Application`.company in {0}".format(tuple(companies))
    
    if "Recruiter" in frappe.get_roles(user):
        return "`tabJob Application`.assigned_recruiter = '{0}'".format(user)
    
    return "1=0"