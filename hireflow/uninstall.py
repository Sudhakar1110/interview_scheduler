# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe


def after_uninstall():
    """
    Called after app uninstallation
    """
    # Clean up custom fields
    frappe.db.sql("""
        DELETE FROM `tabCustom Field`
        WHERE module = 'HireFlow'
    """)
    
    # Clean up workflows
    frappe.db.sql("""
        DELETE FROM `tabWorkflow`
        WHERE module = 'HireFlow'
    """)
    
    # Clean up notifications
    frappe.db.sql("""
        DELETE FROM `tabNotification`
        WHERE module = 'HireFlow'
    """)
    
    frappe.db.commit()
    
    print("\n" + "="*60)
    print("HireFlow Uninstallation Complete!")
    print("="*60 + "\n")