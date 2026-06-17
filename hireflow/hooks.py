# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version


app_name = "hireflow"
app_title = "HireFlow"
app_publisher = "Antigravity"
app_description = "Interview Scheduling & Recruitment Management Platform"
app_icon = "octicon octicon-briefcase"
app_color = "#4F46E5"
app_email = "info@antigravity.com"
app_license = "MIT"


# Includes in <head>
app_include_css = "/assets/hireflow/css/hireflow.css"
app_include_js = "/assets/hireflow/js/hireflow.js"


# include js, css files in header of web template
web_include_css = "/assets/hireflow/css/hireflow.css"
web_include_js = "/assets/hireflow/js/hireflow.js"


# Installation
after_install = "hireflow.install.after_install"


# After Migration
# NOTE: This points to hireflow.install.after_migrate, which was not provided
# for review. Confirm it calls frappe.utils.fixtures.sync_fixtures() (or that
# core Frappe's default fixture-import step is not being skipped/overridden)
# so that fixtures actually sync into the DB on every `bench migrate`, not
# just on `bench export-fixtures`. Also confirm it does not catch/swallow
# exceptions silently - a failure here can abort migrate before Workspace
# fixtures are synced, which looks identical to "workspace renders empty".
after_migrate = "hireflow.install.after_migrate"


# Uninstallation
after_uninstall = "hireflow.uninstall.after_uninstall"


# Desk Notifications
notification_config = "hireflow.notifications.get_notification_config"


# Document Events
# NOTE: Module paths below were not verified against actual files in this
# review (e.g. hireflow/ats_management/doctype/job_application/job_application.py).
# If any path/function is missing, Frappe raises an ImportError while loading
# hooks at the start of `bench migrate`, which aborts migration before
# fixtures (including Workspace) ever sync - producing the same symptom
# ("workspace looks empty") for an unrelated reason. Run a full migrate and
# read the traceback end-to-end rather than assuming hook registration succeeded.
doc_events = {
    "Job Application": {
        "on_submit": "hireflow.ats_management.doctype.job_application.job_application.on_submit",
        "on_update": "hireflow.ats_management.doctype.job_application.job_application.on_update"
    },
    "Interview Schedule": {
        "on_submit": "hireflow.interview_management.doctype.interview_schedule.interview_schedule.send_reminder",
        "validate": "hireflow.interview_management.doctype.interview_schedule.interview_schedule.validate_schedule"
    },
    "Offer Letter": {
        "on_submit": "hireflow.offer_management.doctype.offer_letter.offer_letter.send_offer_email",
        "on_update": "hireflow.offer_management.doctype.offer_letter.offer_letter.check_expiry"
    },
    "Employee Onboarding": {
        "on_submit": "hireflow.hiring_management.doctype.employee_onboarding.employee_onboarding.create_employee"
    }
}


# Scheduled Tasks
scheduler_events = {
    "daily": [
        "hireflow.tasks.send_interview_reminders",
        "hireflow.tasks.check_offer_expiry",
        "hireflow.tasks.update_job_status",
        "hireflow.tasks.send_application_status_updates"
    ],
    "weekly": [
        "hireflow.tasks.send_weekly_report",
        "hireflow.tasks.cleanup_old_notifications"
    ],
    "monthly": [
        "hireflow.tasks.generate_monthly_analytics",
        "hireflow.tasks.process_subscription_renewals"
    ]
}


# Fixtures
fixtures = [
    {
        "doctype": "Role",
        "filters": [
            [
                "name",
                "in",
                [
                    "HireFlow Admin",
                    "Employer",
                    "Recruiter",
                    "Interviewer",
                    "Candidate"
                ]
            ]
        ]
    },
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "module",
                "=",
                "HireFlow"
            ]
        ]
    },
    {
        "doctype": "Workflow"
    },
    {
        "doctype": "Notification"
    },
    {
        "doctype": "Workspace",
        "filters": [
            [
                "module",
                "=",
                "Hireflow"
            ]
        ]
    },
    {
        "doctype": "Report",
        "filters": [
            [
                "module",
                "=",
                "Hireflow"
            ]
        ]
    },
    {
        "doctype": "Dashboard Chart",
        "filters": [
            [
                "chart_name",
                "in",
                [
                    "Applications by Status",
                    "Interviews by Month",
                    "Hiring Funnel",
                    "Open Jobs by Department",
                    "Candidate Pipeline"
                ]
            ]
        ]
    },
    {
        "doctype": "Number Card",
        "filters": [
            [
                "label",
                "in",
                [
                    "Open Jobs",
                    "Active Candidates",
                    "Scheduled Interviews",
                    "Offers Released",
                    "Hires Completed"
                ]
            ]
        ]
    }
]


# Website Route Rules
website_route_rules = [
    {"from_route": "/jobs/<path:job_id>", "to_route": "job"},
    {"from_route": "/company/<path:company_name>", "to_route": "company"},
]


# Portal Pages
has_website_permission = {
    "Job Posting": "hireflow.job_management.doctype.job_posting.job_posting.has_website_permission"
}


# Website Context
website_context = {
    "favicon": "/assets/hireflow/images/favicon.ico",
    "splash_image": "/assets/hireflow/images/logo.png"
}


# Home Pages
role_home_page = {
    "Candidate": "candidate-dashboard",
    "Employer": "employer-dashboard",
    "Recruiter": "recruiter-dashboard"
}


# Permissions
permission_query_conditions = {
    "Job Posting": "hireflow.job_management.doctype.job_posting.job_posting.get_permission_query_conditions"
}


# Override DocType Dashboards
# (none - removed broken reference to non-existent dashboard file)
