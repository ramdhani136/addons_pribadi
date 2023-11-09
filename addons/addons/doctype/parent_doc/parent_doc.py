# Copyright (c) 2023, Ilham Ramdhani and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ParentDoc(Document):
	
	def validate(self):
		frappe.msgprint("Halo dari server script")
