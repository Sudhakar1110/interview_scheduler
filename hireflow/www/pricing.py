# -*- coding: utf-8 -*-
import frappe


def get_context(context):
    context.no_cache = 1
    
    # Get subscription plans
    context.plans = frappe.get_all(
        "Subscription Plan",
        filters={"is_active": 1},
        fields=["name", "plan_name", "price", "billing_cycle", "max_jobs", "max_applications", "features", "is_featured"],
        order_by="price asc"
    )
    
    return context