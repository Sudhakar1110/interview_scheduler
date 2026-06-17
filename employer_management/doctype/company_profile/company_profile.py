# -*- coding: utf-8 -*-
import frappe


class CompanyProfile(frappe.Document):
    def validate(self):
        if self.is_new() and self.user:
            self.assign_employer_role()
    
    def assign_employer_role(self):
        if not frappe.db.exists("Has Role", {"parent": self.user, "role": "Employer"}):
            doc = frappe.get_doc({
                "doctype": "Has Role",
                "parent": self.user,
                "parentfield": "roles",
                "parenttype": "User",
                "role": "Employer"
            })
            doc.insert(ignore_permissions=True)