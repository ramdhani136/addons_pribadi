# Copyright (c) 2023, Ilham Ramdhani and contributors
# For license information, please see license.txt
import frappe
from frappe import _
from frappe.model.document import Document

class ChildDoc(Document):
    def validate(self):
        self.get_value()
        self.get_document()

    def get_value(self):
        first_name, last_name = frappe.db.get_value(
            "Parent Doc", "ilham", ["first_name", "last_name"]
        )
        frappe.msgprint(
            _("The Parent First Name is {0} and Last Name is {1}").format(
                first_name, last_name
            )
        )
        
    def get_document(self):
        doc = frappe.get_doc("Parent Doc", self.parent_doc_link)
        # frappe.msgprint(_("The Parent Full Name is {0}").format(doc.full_name)) 
        self.parent_full_name = doc.full_name
        self.parent_age = doc.age
        self.parent_present_address = doc.present_address
        # self.save()
        # frappe.db.set_value("Parent Doc", "Ilham", "full_name", "Ilham Ramdhani")

