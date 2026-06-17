// HireFlow Custom JavaScript

// Job Application Form Utilities
frappe.ui.form.on('Job Application', {
    refresh: function(frm) {
        if (frm.doc.__islocal) {
            frm.add_custom_button(__('From Job Portal'), function() {
                frappe.route_options = {
                    "job_posting": cur_frm.doc.job_posting
                };
                frappe.set_route("jobs");
            });
        }
    },

    validate: function(frm) {
        if (!frm.doc.candidate) {
            frappe.msgprint(__('Please select a candidate'));
            frappe.validated = false;
        }

        if (!frm.doc.job_posting) {
            frappe.msgprint(__('Please select a job posting'));
            frappe.validated = false;
        }
    }
});

// Interview Schedule Auto-fill & Validation
frappe.ui.form.on('Interview Schedule', {
    candidate: function(frm) {
        if (frm.doc.candidate) {
            frappe.call({
                method: 'hireflow.api.get_candidate_interviews',
                args: {
                    candidate: frm.doc.candidate
                },
                callback: function(r) {
                    // Handle response
                }
            });
        }
    },

    interview_date: function(frm) {
        if (frm.doc.interview_date) {
            var today = frappe.datetime.get_today();
            if (frm.doc.interview_date < today) {
                frappe.msgprint(__('Interview date cannot be in the past'));
                frm.set_value('interview_date', '');
            }
        }
    }
});

// Calculate Match Score for Job Application
frappe.ui.form.on('Job Application', {
    onload: function(frm) {
        if (frm.doc.job_posting && frm.doc.candidate) {
            calculate_match_score(frm);
        }
    },

    job_posting: function(frm) {
        if (frm.doc.candidate) {
            calculate_match_score(frm);
        }
    },

    candidate: function(frm) {
        if (frm.doc.job_posting) {
            calculate_match_score(frm);
        }
    }
});

function calculate_match_score(frm) {
    frappe.call({
        method: 'hireflow.api.calculate_match_score',
        args: {
            job_posting: frm.doc.job_posting,
            candidate: frm.doc.candidate
        },
        callback: function(r) {
            if (r.message) {
                frm.set_value('score', r.message);
            }
        }
    });
}

// Notification Toast Helper
function show_notification(title, message, type) {
    frappe.show_alert({
        message: message,
        title: title,
        indicator: type || 'blue'
    });
}
