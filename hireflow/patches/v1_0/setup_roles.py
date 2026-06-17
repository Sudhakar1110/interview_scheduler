# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe


def execute():
    """Create custom roles for HireFlow"""
    roles = [
        {
            "role_name": "HireFlow Admin",
            "desk_access": 1,
            "home_page": "/app/hireflow-dashboard"
        },
        {
            "role_name": "Employer",
            "desk_access": 1,
            "home_page": "/app/employer-dashboard"
        },
        {
            "role_name": "Recruiter",
            "desk_access": 1,
            "home_page": "/app/recruiter-dashboard"
        },
        {
            "role_name": "Interviewer",
            "desk_access": 1,
            "home_page": "/app/interview-feedback"
        },
        {
            "role_name": "Candidate",
            "desk_access": 0,
            "home_page": "/candidate-dashboard"
        }
    ]
    
    for role_data in roles:
        if not frappe.db.exists("Role", role_data["role_name"]):
            role = frappe.get_doc({
                "doctype": "Role",
                **role_data
            })
            role.insert(ignore_permissions=True)
            frappe.db.commit()
            print("Created role: {0}".format(role_data["role_name"]))