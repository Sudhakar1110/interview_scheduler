# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document


class EmployeeOnboarding(Document):
    def validate(self):
        self.calculate_completion()
    
    def calculate_completion(self):
        if self.checklist:
            completed = sum(1 for item in self.checklist if item.status == "Completed")
            total = len(self.checklist)
            self.completion_status = (completed / total * 100) if total > 0 else 0
    
    def on_submit(self):
        self.create_employee()
        self.update_application()
    
    def create_employee(self):
        if not self.employee_created:
            employee = frappe.get_doc({
                "doctype": "Employee",
                "first_name": self.candidate,
                "company": self.company,
                "department": self.department,
                "designation": self.designation,
                "reports_to": self.reports_to,
                "date_of_joining": self.joining_date,
                "employment_type": self.employee_type,
                "email": self.work_email,
                "hireflow_onboarding": self.name
            })
            employee.insert()
            self.employee_created = employee.name
            self.save(ignore_permissions=True)
    
    def update_application(self):
        if self.job_application:
            frappe.db.set_value("Job Application", self.job_application, "status", "Hired")
            frappe.db.set_value("Job Application", self.job_application, "hired_on", frappe.utils.today())
        
        if self.offer_letter:
            frappe.db.set_value("Offer Letter", self.offer_letter, "is_accepted", 1)
            frappe.db.set_value("Offer Letter", self.offer_letter, "status", "Accepted")