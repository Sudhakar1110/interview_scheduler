# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document
from hireflow.utils.validators import validate_offer_letter
from hireflow.utils.notifications import send_offer_letter_email


class OfferLetter(Document):
    def validate(self):
        validate_offer_letter(self)
    
    def on_submit(self):
        self.send_offer_email()
        self.update_application()
    
    def send_offer_email(self):
        try:
            send_offer_letter_email(self)
        except:
            pass
    
    def update_application(self):
        if self.job_application:
            frappe.db.set_value("Job Application", self.job_application, "status", "Offer")
            frappe.db.set_value("Job Application", self.job_application, "offer_letter", self.name)
    
    def check_expiry(self):
        if self.status == "Sent":
            if frappe.utils.getdate(self.expiry_date) < frappe.utils.getdate():
                self.status = "Expired"
                self.save()