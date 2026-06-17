# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe


def execute():
    """Create default subscription plans"""
    plans = [
        {
            "plan_name": "Free Plan",
            "price": 0,
            "billing_cycle": "Monthly",
            "max_jobs": 5,
            "max_applications": 50,
            "features": "Basic job posting\nCandidate database\nEmail support",
            "is_active": 1
        },
        {
            "plan_name": "Basic Plan",
            "price": 99,
            "billing_cycle": "Monthly",
            "max_jobs": 20,
            "max_applications": 200,
            "features": "Advanced job posting\nATS tracking\nInterview scheduling\nPriority support",
            "is_active": 1
        },
        {
            "plan_name": "Professional Plan",
            "price": 299,
            "billing_cycle": "Monthly",
            "max_jobs": 100,
            "max_applications": 1000,
            "features": "Unlimited job posting\nAdvanced ATS\nMulti-round interviews\nOffer management\nAnalytics & reports\n24/7 support",
            "is_active": 1
        },
        {
            "plan_name": "Enterprise Plan",
            "price": 999,
            "billing_cycle": "Monthly",
            "max_jobs": -1,
            "max_applications": -1,
            "features": "All Professional features\nCustom branding\nAPI access\nDedicated account manager\nCustom integrations",
            "is_active": 1
        }
    ]
    
    for plan_data in plans:
        if not frappe.db.exists("Subscription Plan", plan_data["plan_name"]):
            plan = frappe.get_doc({
                "doctype": "Subscription Plan",
                **plan_data
            })
            plan.insert(ignore_permissions=True)
            frappe.db.commit()
            print("Created subscription plan: {0}".format(plan_data["plan_name"]))