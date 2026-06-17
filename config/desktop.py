# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "module_name": "HireFlow",
            "category": "Modules",
            "label": _("HireFlow"),
            "color": "#4F46E5",
            "icon": "octicon octicon-briefcase",
            "type": "module",
            "description": _("Interview Scheduling & Recruitment Management Platform")
        }
    ]