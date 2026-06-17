# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
import json


def after_install():
    """
    Called after app installation
    """
    frappe.clear_cache()
    
    # Create default roles
    create_roles()
    
    # Create default subscription plans
    create_subscription_plans()
    
    # Create email templates
    create_email_templates()
    
    # Create default job categories
    create_job_categories()
    
    # Create default job types
    create_job_types()
    
    # Setup permissions
    setup_permissions()
    
    sync_module_workspaces()
    if frappe.conf.get("developer_mode"):
        create_demo_data()
    frappe.db.commit()
    
    print("\n" + "="*60)
    print("HireFlow Installation Complete!")
    print("="*60)
    print("Next Steps:")
    print("1. Access HireFlow workspace from desk")
    print("2. Configure your company profile")
    print("3. Start posting jobs")
    print("="*60 + "\n")


def create_roles():
    """Create custom roles for HireFlow"""
    roles = [
        {"role_name": "HireFlow Admin", "desk_access": 1},
        {"role_name": "Employer", "desk_access": 1},
        {"role_name": "Recruiter", "desk_access": 1},
        {"role_name": "Interviewer", "desk_access": 1},
        {"role_name": "Candidate", "desk_access": 0}
    ]
    
    for role_data in roles:
        if not frappe.db.exists("Role", role_data["role_name"]):
            role = frappe.get_doc({
                "doctype": "Role",
                "role_name": role_data["role_name"],
                "desk_access": role_data["desk_access"]
            })
            role.insert(ignore_permissions=True)
            print("Created role: {0}".format(role_data["role_name"]))


def create_subscription_plans():
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
            print("Created subscription plan: {0}".format(plan_data["plan_name"]))


def create_email_templates():
    """Create default email templates"""
    templates = [
        {
            "template_name": "Interview Invitation",
            "subject": "Interview Invitation - {job_title}",
            "message": """Dear {candidate_name},

We are pleased to invite you for an interview for the position of {job_title} at {company_name}.

Interview Details:
- Date: {interview_date}
- Time: {interview_time}
- Duration: {duration}
- Type: {interview_type}
- Panel: {interviewer_names}

{meeting_link}

Please confirm your availability.

Best regards,
{company_name} HR Team"""
        },
        {
            "template_name": "Application Received",
            "subject": "Application Received - {job_title}",
            "message": """Dear {candidate_name},

Thank you for applying for the position of {job_title} at {company_name}.

We have received your application and our recruitment team will review it shortly.

Best regards,
{company_name} HR Team"""
        },
        {
            "template_name": "Offer Letter Template",
            "subject": "Job Offer - {job_title}",
            "message": """Dear {candidate_name},

Congratulations! We are pleased to offer you the position of {job_title} at {company_name}.

Offer Details:
- Position: {job_title}
- Department: {department}
- Salary: {salary}
- Start Date: {start_date}

Please review the attached offer letter and respond by {expiry_date}.

Best regards,
{company_name} HR Team"""
        },
        {
            "template_name": "Interview Reminder",
            "subject": "Interview Reminder - Tomorrow",
            "message": """Dear {candidate_name},

This is a reminder about your interview scheduled for tomorrow.

Interview Details:
- Date: {interview_date}
- Time: {interview_time}
- Position: {job_title}
- Company: {company_name}

{meeting_link}

We look forward to meeting you!

Best regards,
{company_name} HR Team"""
        }
    ]
    
    for template_data in templates:
        if not frappe.db.exists("Email Template", template_data["template_name"]):
            template = frappe.get_doc({
                "doctype": "Email Template",
                **template_data
            })
            template.insert(ignore_permissions=True)
            print("Created email template: {0}".format(template_data["template_name"]))


def create_job_categories():
    """Create default job categories"""
    categories = [
        "Information Technology",
        "Sales & Marketing",
        "Finance & Accounting",
        "Human Resources",
        "Operations",
        "Customer Service",
        "Engineering",
        "Design",
        "Healthcare",
        "Education",
        "Legal",
        "Manufacturing",
        "Other"
    ]
    
    for category in categories:
        if not frappe.db.exists("Job Category", category):
            doc = frappe.get_doc({
                "doctype": "Job Category",
                "category_name": category
            })
            doc.insert(ignore_permissions=True)


def create_job_types():
    """Create default job types"""
    job_types = [
        "Full Time",
        "Part Time",
        "Contract",
        "Internship",
        "Temporary",
        "Remote",
        "Hybrid"
    ]
    
    for job_type in job_types:
        if not frappe.db.exists("Job Type", job_type):
            doc = frappe.get_doc({
                "doctype": "Job Type",
                "type_name": job_type
            })
            doc.insert(ignore_permissions=True)



def setup_permissions():
    """Setup role-based permissions for HireFlow DocTypes"""
    # Role permissions are already configured in each DocType's JSON file
    # and synced via fixtures. This hook ensures any additional custom
    # permission rules are applied post-install.
    
    # Ensure HireFlow Admin has full access to all HireFlow DocTypes
    hireflow_doctypes = [
        "Job Posting", "Job Category", "Job Type", "Job Location", "Job Skill",
        "Company Profile", "Recruiter Profile",
        "Candidate Profile", "Candidate Skill", "Candidate Education", "Candidate Experience", "Candidate Certification",
        "Job Application", "Interview Feedback",
        "Interview Schedule", "Interview Panel",
        "Panel Member", "Panel Availability", "Panel Skill",
        "Offer Letter",
        "Employee Onboarding", "Document Verification", "Joining Checklist",
        "Subscription Plan", "Employer Subscription", "Payment Transaction",
        "Email Template", "Message Center", "Notification Log"
    ]
    
    for doctype in hireflow_doctypes:
        if frappe.db.exists("DocType", doctype):
            try:
                doc = frappe.get_doc("DocType", doctype)
                # Ensure basic permissions exist
                if not any(p.role == "HireFlow Admin" for p in doc.permissions):
                    doc.append("permissions", {
                        "role": "HireFlow Admin",
                        "read": 1,
                        "write": 1,
                        "create": 1,
                        "delete": 1
                    })
                    doc.save(ignore_permissions=True)
            except Exception:
                pass
    
    frappe.db.commit()


def create_demo_data():
    """Create demo data for testing"""
    try:
        from hireflow.patches.v1_0.create_demo_data import execute
        execute()
    except Exception as e:
        print("Demo data creation skipped: {0}".format(str(e)))


def _make_workspace(title, module, icon, indicator_color, sequence_id,
                    parent_page=None, shortcuts=None, links=None, extra_content_items=None):
    # Build content JSON from links using Frappe v15 format
    # Card: {"type": "card", "label": "...", "links": [{"type": "doctype", "name": "...", "label": "..."}]}
    content_items = []
    if extra_content_items:
        content_items.extend(extra_content_items)
    if links:
        current_card_links = None
        current_card_label = None
        for lnk in links:
            if lnk["type"] == "Card Break":
                if current_card_links:
                    content_items.append({
                        "type": "card",
                        "label": current_card_label,
                        "links": current_card_links
                    })
                current_card_label = lnk["label"]
                current_card_links = []
            elif lnk["type"] == "Link" and current_card_links is not None:
                link_type = lnk.get("link_type", "DocType")
                if link_type == "DocType":
                    current_card_links.append({
                        "type": "doctype",
                        "name": lnk["link_to"],
                        "label": lnk["label"]
                    })
        if current_card_links:
            content_items.append({
                "type": "card",
                "label": current_card_label,
                "links": current_card_links
            })

    content_json = json.dumps(content_items)

    if frappe.db.exists("Workspace", title):
        doc = frappe.get_doc("Workspace", title)
        doc.module = module
        doc.icon = icon
        doc.indicator_color = indicator_color
        doc.sequence_id = sequence_id
        doc.is_standard = 1
        doc.public = 1
        doc.is_hidden = 0
        doc.content = content_json
        doc.parent_page = parent_page if parent_page else ""
        doc.shortcuts = []
        doc.links = []
        doc.number_cards = []
        doc.charts = []
        doc.quick_lists = []
        if shortcuts:
            for sc in shortcuts:
                doc.append("shortcuts", sc)
        if links:
            for lnk in links:
                doc.append("links", lnk)
        doc.flags.ignore_permissions = True
        doc.flags.ignore_validate = True
        doc.save(ignore_permissions=True)
        print("  Updated workspace: {0}".format(title))
    else:
        doc_data = {
            "doctype": "Workspace",
            "title": title, "label": title, "module": module,
            "icon": icon, "indicator_color": indicator_color,
            "is_standard": 1, "public": 1, "is_hidden": 0,
            "sequence_id": sequence_id, "content": content_json,
        }
        if parent_page:
            doc_data["parent_page"] = parent_page
        doc = frappe.get_doc(doc_data)
        if shortcuts:
            for sc in shortcuts:
                doc.append("shortcuts", sc)
        if links:
            for lnk in links:
                doc.append("links", lnk)
        doc.insert(ignore_permissions=True, ignore_mandatory=True)
        print("  Created workspace: {0}".format(title))
    return doc


def _cleanup_stale_workspace_refs():
    """Delete stale Number Cards and Dashboard Charts from previous iterations."""
    # Only delete truly orphaned references from other apps, not our own
    stale_cards = ["Total Open Jobs", "Total Candidates"]
    for name in stale_cards:
        if frappe.db.exists("Number Card", name):
            try:
                frappe.delete_doc("Number Card", name, ignore_permissions=True)
                print("  Deleted stale Number Card: {0}".format(name))
            except Exception:
                pass

    stale_charts = ["Candidates by Status", "Hiring Funnel Analytics", "Applications By Status",
                    "Applications By Month", "Interview Status Summary"]
    for name in stale_charts:
        if frappe.db.exists("Dashboard Chart", name):
            try:
                frappe.delete_doc("Dashboard Chart", name, ignore_permissions=True)
                print("  Deleted stale Dashboard Chart: {0}".format(name))
            except Exception:
                pass
    frappe.db.commit()


def create_number_cards():
    """Create Number Card records for the HireFlow workspace"""
    cards = [
        {
            "label": "Open Jobs",
            "document_type": "Job Posting",
            "function": "Count",
            "filters_json": '[["status", "=", "Open"]]',
            "color": "#2490ef",
            "is_public": 1,
        },
        {
            "label": "Active Candidates",
            "document_type": "Candidate Profile",
            "function": "Count",
            "filters_json": '[["is_active", "=", 1]]',
            "color": "#39b446",
            "is_public": 1,
        },
        {
            "label": "Scheduled Interviews",
            "document_type": "Interview Schedule",
            "function": "Count",
            "filters_json": '[["status", "=", "Scheduled"]]',
            "color": "#e0732e",
            "is_public": 1,
        },
        {
            "label": "Offers Released",
            "document_type": "Offer Letter",
            "function": "Count",
            "filters_json": '[["status", "in", ["Sent", "Accepted"]]]',
            "color": "#b7443f",
            "is_public": 1,
        },
        {
            "label": "Hires Completed",
            "document_type": "Employee Onboarding",
            "function": "Count",
            "filters_json": '[["status", "=", "Completed"]]',
            "color": "#8b5cf6",
            "is_public": 1,
        },
    ]
    for card_data in cards:
        label = card_data["label"]
        if frappe.db.exists("Number Card", label):
            # Update existing card
            doc = frappe.get_doc("Number Card", label)
            for key, value in card_data.items():
                doc.set(key, value)
            doc.flags.ignore_permissions = True
            doc.save(ignore_permissions=True)
            print("  Updated Number Card: {0}".format(label))
        else:
            doc = frappe.get_doc({
                "doctype": "Number Card",
                "type": "Document Type",
                **card_data,
            })
            doc.insert(ignore_permissions=True)
            print("  Created Number Card: {0}".format(label))
    print("  All 5 Number Cards synced.")


def create_dashboard_charts():
    """Create Dashboard Chart records for the HireFlow workspace"""
    charts = [
        {
            "chart_name": "Applications by Status",
            "chart_type": "Group By",
            "document_type": "Job Application",
            "type": "Pie",
            "group_by_based_on": "status",
            "group_by_type": "Count",
            "filters_json": "[]",
            "is_public": 1,
        },
        {
            "chart_name": "Interviews by Month",
            "chart_type": "Count",
            "document_type": "Interview Schedule",
            "type": "Bar",
            "based_on": "interview_date",
            "timespan": "Last Year",
            "time_interval": "Monthly",
            "filters_json": "[]",
            "is_public": 1,
        },
        {
            "chart_name": "Hiring Funnel",
            "chart_type": "Group By",
            "document_type": "Job Application",
            "type": "Donut",
            "group_by_based_on": "status",
            "group_by_type": "Count",
            "filters_json": "[]",
            "is_public": 1,
        },
        {
            "chart_name": "Open Jobs by Department",
            "chart_type": "Group By",
            "document_type": "Job Posting",
            "type": "Bar",
            "group_by_based_on": "department",
            "group_by_type": "Count",
            "filters_json": '[["status", "=", "Open"]]',
            "is_public": 1,
        },
        {
            "chart_name": "Candidate Pipeline",
            "chart_type": "Group By",
            "document_type": "Job Application",
            "type": "Donut",
            "group_by_based_on": "status",
            "group_by_type": "Count",
            "filters_json": "[]",
            "is_public": 1,
        },
    ]
    for chart_data in charts:
        name = chart_data["chart_name"]
        if frappe.db.exists("Dashboard Chart", name):
            doc = frappe.get_doc("Dashboard Chart", name)
            # Only update existing, don't change references that might be in use elsewhere
            doc.flags.ignore_permissions = True
            doc.save(ignore_permissions=True)
            print("  Updated Dashboard Chart: {0}".format(name))
        else:
            doc = frappe.get_doc({
                "doctype": "Dashboard Chart",
                **chart_data,
            })
            doc.insert(ignore_permissions=True)
            print("  Created Dashboard Chart: {0}".format(name))
    print("  All 5 Dashboard Charts synced.")


def sync_module_workspaces():
    print("=" * 50)
    print("Syncing HireFlow Module Workspaces...")
    _cleanup_stale_workspace_refs()
    # Create Number Card and Dashboard Chart records
    create_number_cards()
    create_dashboard_charts()
    # Build HireFlow workspace with number cards, charts, quick lists and card sections
    hireflow_extra_content = [
        # Number Cards
        {"type": "number_card", "data": {"card_name": "Open Jobs"}},
        {"type": "number_card", "data": {"card_name": "Active Candidates"}},
        {"type": "number_card", "data": {"card_name": "Scheduled Interviews"}},
        {"type": "number_card", "data": {"card_name": "Offers Released"}},
        {"type": "number_card", "data": {"card_name": "Hires Completed"}},
        # Dashboard Charts
        {"type": "chart", "data": {"chart_name": "Applications by Status"}},
        {"type": "chart", "data": {"chart_name": "Interviews by Month"}},
        {"type": "chart", "data": {"chart_name": "Hiring Funnel"}},
        {"type": "chart", "data": {"chart_name": "Open Jobs by Department"}},
        {"type": "chart", "data": {"chart_name": "Candidate Pipeline"}},
        # Quick Lists
        {"type": "quick_list", "data": {"doctype": "Job Posting", "label": "Job Openings"}},
        {"type": "quick_list", "data": {"doctype": "Job Application", "label": "Job Applications"}},
        {"type": "quick_list", "data": {"doctype": "Candidate Profile", "label": "Candidates"}},
        {"type": "quick_list", "data": {"doctype": "Interview Schedule", "label": "Interview Schedules"}},
        {"type": "quick_list", "data": {"doctype": "Offer Letter", "label": "Offer Letters"}},
    ]
    _make_workspace(title="Hireflow", module="HireFlow", icon="briefcase", indicator_color="green", sequence_id=1,
        extra_content_items=hireflow_extra_content,
        shortcuts=[
            {"label": "New Job Posting", "type": "DocType", "link_to": "Job Posting", "onboard": 1},
            {"label": "New Candidate", "type": "DocType", "link_to": "Candidate Profile", "onboard": 1},
            {"label": "New Application", "type": "DocType", "link_to": "Job Application", "onboard": 1},
            {"label": "Schedule Interview", "type": "DocType", "link_to": "Interview Schedule", "onboard": 1},
            {"label": "New Offer", "type": "DocType", "link_to": "Offer Letter", "onboard": 0},
            {"label": "New Company", "type": "DocType", "link_to": "Company Profile", "onboard": 0}
        ],
        links=[
            {"type": "Card Break", "label": "Job Management", "icon": "briefcase"},
            {"type": "Link", "label": "Job Postings", "link_type": "DocType", "link_to": "Job Posting"},
            {"type": "Link", "label": "Job Categories", "link_type": "DocType", "link_to": "Job Category"},
            {"type": "Link", "label": "Job Types", "link_type": "DocType", "link_to": "Job Type"},
            {"type": "Link", "label": "Job Locations", "link_type": "DocType", "link_to": "Job Location"},
            {"type": "Card Break", "label": "Employer Management", "icon": "building"},
            {"type": "Link", "label": "Company Profiles", "link_type": "DocType", "link_to": "Company Profile"},
            {"type": "Link", "label": "Recruiter Profiles", "link_type": "DocType", "link_to": "Recruiter Profile"},
            {"type": "Card Break", "label": "Candidate Management", "icon": "people"},
            {"type": "Link", "label": "Candidate Profiles", "link_type": "DocType", "link_to": "Candidate Profile"},
            {"type": "Card Break", "label": "ATS Management", "icon": "check"},
            {"type": "Link", "label": "Job Applications", "link_type": "DocType", "link_to": "Job Application"},
            {"type": "Link", "label": "Interview Feedback", "link_type": "DocType", "link_to": "Interview Feedback"},
            {"type": "Card Break", "label": "Interview Management", "icon": "calendar"},
            {"type": "Link", "label": "Interview Schedules", "link_type": "DocType", "link_to": "Interview Schedule"},
            {"type": "Card Break", "label": "Panel Management", "icon": "group"},
            {"type": "Link", "label": "Panel Members", "link_type": "DocType", "link_to": "Panel Member"},
            {"type": "Card Break", "label": "Offer Management", "icon": "mail"},
            {"type": "Link", "label": "Offer Letters", "link_type": "DocType", "link_to": "Offer Letter"},
            {"type": "Card Break", "label": "Hiring Management", "icon": "user"},
            {"type": "Link", "label": "Employee Onboardings", "link_type": "DocType", "link_to": "Employee Onboarding"},
            {"type": "Card Break", "label": "Subscription Management", "icon": "credit-card"},
            {"type": "Link", "label": "Subscription Plans", "link_type": "DocType", "link_to": "Subscription Plan"},
            {"type": "Link", "label": "Employer Subscriptions", "link_type": "DocType", "link_to": "Employer Subscription"},
            {"type": "Link", "label": "Payment Transactions", "link_type": "DocType", "link_to": "Payment Transaction"},
            {"type": "Card Break", "label": "Communication Management", "icon": "message-square"},
            {"type": "Link", "label": "Email Templates", "link_type": "DocType", "link_to": "Email Template"},
            {"type": "Link", "label": "Message Center", "link_type": "DocType", "link_to": "Message Center"},
            {"type": "Link", "label": "Notification Log", "link_type": "DocType", "link_to": "Notification Log"},
            {"type": "Card Break", "label": "Reports & Analytics", "icon": "folder"},
            {"type": "Card Break", "label": "Configuration", "icon": "setting"},
            {"type": "Link", "label": "Company Settings", "link_type": "DocType", "link_to": "Company Profile"},
        ])
    _make_workspace(title="Job Management", module="HireFlow", icon="briefcase", indicator_color="blue", sequence_id=2, parent_page="Hireflow",
        shortcuts=[{"label": "New Job Posting", "type": "DocType", "link_to": "Job Posting", "onboard": 1},
            {"label": "New Category", "type": "DocType", "link_to": "Job Category", "onboard": 0},
            {"label": "New Type", "type": "DocType", "link_to": "Job Type", "onboard": 0},
            {"label": "New Location", "type": "DocType", "link_to": "Job Location", "onboard": 0},
            {"label": "New Skill", "type": "DocType", "link_to": "Job Skill", "onboard": 0}],
        links=[{"type": "Card Break", "label": "Job Openings", "icon": "briefcase"},
            {"type": "Link", "label": "Job Postings", "link_type": "DocType", "link_to": "Job Posting"},
            {"type": "Card Break", "label": "Masters", "icon": "setting"},
            {"type": "Link", "label": "Job Categories", "link_type": "DocType", "link_to": "Job Category"},
            {"type": "Link", "label": "Job Types", "link_type": "DocType", "link_to": "Job Type"},
            {"type": "Link", "label": "Job Locations", "link_type": "DocType", "link_to": "Job Location"},
            {"type": "Link", "label": "Job Skills", "link_type": "DocType", "link_to": "Job Skill"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    _make_workspace(title="Employer Management", module="HireFlow", icon="building", indicator_color="green", sequence_id=3, parent_page="Hireflow",
        shortcuts=[{"label": "New Company", "type": "DocType", "link_to": "Company Profile", "onboard": 1},
            {"label": "New Recruiter", "type": "DocType", "link_to": "Recruiter Profile", "onboard": 1}],
        links=[{"type": "Card Break", "label": "Employers", "icon": "building"},
            {"type": "Link", "label": "Company Profiles", "link_type": "DocType", "link_to": "Company Profile"},
            {"type": "Link", "label": "Recruiter Profiles", "link_type": "DocType", "link_to": "Recruiter Profile"},
            {"type": "Card Break", "label": "Subscriptions", "icon": "credit-card"},
            {"type": "Link", "label": "Employer Subscriptions", "link_type": "DocType", "link_to": "Employer Subscription"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    _make_workspace(title="Candidate Management", module="HireFlow", icon="people", indicator_color="purple", sequence_id=4, parent_page="Hireflow",
        shortcuts=[{"label": "New Candidate", "type": "DocType", "link_to": "Candidate Profile", "onboard": 1}],
        links=[{"type": "Card Break", "label": "Candidates", "icon": "people"},
            {"type": "Link", "label": "Candidate Profiles", "link_type": "DocType", "link_to": "Candidate Profile"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    _make_workspace(title="ATS Management", module="HireFlow", icon="check", indicator_color="orange", sequence_id=5, parent_page="Hireflow",
        shortcuts=[{"label": "New Application", "type": "DocType", "link_to": "Job Application", "onboard": 1},
            {"label": "New Feedback", "type": "DocType", "link_to": "Interview Feedback", "onboard": 0}],
        links=[{"type": "Card Break", "label": "Applications", "icon": "file-text"},
            {"type": "Link", "label": "Job Applications", "link_type": "DocType", "link_to": "Job Application"},
            {"type": "Link", "label": "Interview Feedback", "link_type": "DocType", "link_to": "Interview Feedback"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    _make_workspace(title="Interview Management", module="HireFlow", icon="people", indicator_color="cyan", sequence_id=6, parent_page="Hireflow",
        shortcuts=[{"label": "Schedule Interview", "type": "DocType", "link_to": "Interview Schedule", "onboard": 1},
            {"label": "New Feedback", "type": "DocType", "link_to": "Interview Feedback", "onboard": 0}],
        links=[{"type": "Card Break", "label": "Schedules", "icon": "calendar"},
            {"type": "Link", "label": "Interview Schedules", "link_type": "DocType", "link_to": "Interview Schedule"},
            {"type": "Card Break", "label": "Feedback", "icon": "comment"},
            {"type": "Link", "label": "Interview Feedback", "link_type": "DocType", "link_to": "Interview Feedback"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    _make_workspace(title="Panel Management", module="HireFlow", icon="group", indicator_color="darkgrey", sequence_id=7, parent_page="Hireflow",
        shortcuts=[{"label": "New Panel Member", "type": "DocType", "link_to": "Panel Member", "onboard": 1}],
        links=[{"type": "Card Break", "label": "Panel Members", "icon": "people"},
            {"type": "Link", "label": "All Panel Members", "link_type": "DocType", "link_to": "Panel Member"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    _make_workspace(title="Offer Management", module="HireFlow", icon="mail", indicator_color="pink", sequence_id=8, parent_page="Hireflow",
        shortcuts=[{"label": "New Offer Letter", "type": "DocType", "link_to": "Offer Letter", "onboard": 1}],
        links=[{"type": "Card Break", "label": "Offers", "icon": "mail"},
            {"type": "Link", "label": "Offer Letters", "link_type": "DocType", "link_to": "Offer Letter"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    _make_workspace(title="Hiring Management", module="HireFlow", icon="user", indicator_color="red", sequence_id=9, parent_page="Hireflow",
        shortcuts=[{"label": "New Onboarding", "type": "DocType", "link_to": "Employee Onboarding", "onboard": 1}],
        links=[{"type": "Card Break", "label": "Onboarding", "icon": "user"},
            {"type": "Link", "label": "Employee Onboardings", "link_type": "DocType", "link_to": "Employee Onboarding"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    _make_workspace(title="Subscription Management", module="HireFlow", icon="credit-card", indicator_color="yellow", sequence_id=10, parent_page="Hireflow",
        shortcuts=[{"label": "New Plan", "type": "DocType", "link_to": "Subscription Plan", "onboard": 1},
            {"label": "New Subscription", "type": "DocType", "link_to": "Employer Subscription", "onboard": 0}],
        links=[{"type": "Card Break", "label": "Plans", "icon": "tag"},
            {"type": "Link", "label": "Subscription Plans", "link_type": "DocType", "link_to": "Subscription Plan"},
            {"type": "Card Break", "label": "Subscriptions", "icon": "shopping-cart"},
            {"type": "Link", "label": "Employer Subscriptions", "link_type": "DocType", "link_to": "Employer Subscription"},
            {"type": "Card Break", "label": "Payments", "icon": "dollar"},
            {"type": "Link", "label": "Payment Transactions", "link_type": "DocType", "link_to": "Payment Transaction"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    _make_workspace(title="Communication Management", module="HireFlow", icon="message-square", indicator_color="blue", sequence_id=11, parent_page="Hireflow",
        shortcuts=[{"label": "New Template", "type": "DocType", "link_to": "Email Template", "onboard": 1},
            {"label": "New Message", "type": "DocType", "link_to": "Message Center", "onboard": 0}],
        links=[{"type": "Card Break", "label": "Templates", "icon": "mail"},
            {"type": "Link", "label": "Email Templates", "link_type": "DocType", "link_to": "Email Template"},
            {"type": "Card Break", "label": "Messages", "icon": "message-circle"},
            {"type": "Link", "label": "Message Center", "link_type": "DocType", "link_to": "Message Center"},
            {"type": "Link", "label": "Notification Log", "link_type": "DocType", "link_to": "Notification Log"},
            {"type": "Card Break", "label": "Reports", "icon": "folder"}])
    frappe.db.commit()
    print("=" * 50)
    print("HireFlow Workspace Verification")
    print("=" * 50)
    workspace_titles = [
        "Hireflow", "Job Management", "Employer Management", "Candidate Management",
        "ATS Management", "Interview Management", "Panel Management", "Offer Management",
        "Hiring Management", "Subscription Management", "Communication Management"
    ]
    all_ok = True
    for wt in workspace_titles:
        if frappe.db.exists("Workspace", wt):
            doc = frappe.get_doc("Workspace", wt)
            content = doc.content
            has_content = bool(content and content != "[]" and content != "" and content != "null")
            has_shortcuts = bool(doc.shortcuts)
            status = "\u2713" if (has_content and doc.public) else "\u2717"
            print("  {0} {1}".format(status, wt))
            if has_content:
                import json
                try:
                    blocks = json.loads(content)
                    print("    Content Length: {0} chars, Blocks: {1}".format(len(content), len(blocks)))
                except Exception:
                    print("    Content Length: {0} chars (invalid JSON)".format(len(content)))
            print("    Shortcuts: {0}, Charts: {1}, Number Cards: {2}, Quick Lists: {3}".format(
                len(doc.shortcuts), len(doc.charts), len(doc.number_cards), len(doc.quick_lists)))
            if not has_content:
                print("    WARNING: content is empty")
                all_ok = False
        else:
            print("  \u2717 {0} Workspace NOT FOUND".format(wt))
            all_ok = False
    chart_count = len(frappe.get_all("Dashboard Chart", filters={"chart_name": ["in", ["Applications by Status", "Interviews by Month", "Hiring Funnel", "Open Jobs by Department", "Candidate Pipeline"]]}))
    print("Dashboard Charts: {0}/5 verified".format(chart_count))
    card_count = len(frappe.get_all("Number Card", filters={"label": ["in", ["Open Jobs", "Active Candidates", "Scheduled Interviews", "Offers Released", "Hires Completed"]]}))
    print("Number Cards: {0}/5 verified".format(card_count))
    print("\u2713 Workspace content rebuilt successfully" if all_ok else "\u26a0 Some workspaces have issues")
    print("=" * 50)


def after_migrate():
    frappe.clear_cache()
    sync_module_workspaces()
    # NOTE: create_demo_data() is intentionally NOT called here.
    # Demo data insertion on every migrate causes LinkValidationError
    # when referenced doctypes are not yet fully synced in the DB.
    # Demo data is only created on fresh install (after_install) in developer mode.
    print("Clear browser cache and refresh Desk to see changes.")
    frappe.db.commit()