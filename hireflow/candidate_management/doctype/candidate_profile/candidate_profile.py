# -*- coding: utf-8 -*-
import frappe


class CandidateProfile(frappe.Document):
    def validate(self):
        self.validate_email()
        self.calculate_total_experience()
    
    def validate_email(self):
        if self.email:
            if not frappe.db.exists("Candidate Profile", {"email": self.email, "name": ["!=", self.name]}):
                pass
            else:
                frappe.throw("Candidate with this email already exists")
    
    def calculate_total_experience(self):
        total = 0
        for exp in self.experience or []:
            if exp.from_date and exp.to_date:
                from_date = frappe.utils.getdate(exp.from_date)
                to_date = frappe.utils.getdate(exp.to_date) if exp.to_date else frappe.utils.today()
                years = (to_date - from_date).days / 365
                total += years
        self.total_experience = total