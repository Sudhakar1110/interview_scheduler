# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _


def get_notification_config():
    """Return notification configuration"""
    return {
        "for_doctype": {
            "Job Application": {
                "status": "Open"
            },
            "Interview Schedule": {
                "status": ["Scheduled", "Confirmed"]
            },
            "Offer Letter": {
                "status": "Sent"
            }
        }
    }