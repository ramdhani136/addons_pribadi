# Copyright (c) 2023, Ilham Ramdhani and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ParentDoc(Document):	
	
	def validate(self):
		self.check_data()
                
				
	def check_data(self):
		if self.enable:
			if self.workflow_state=="Waiting SPV":
				# for data in self.date_and_value:
				# 	frappe.throw(_("Gagal update"))
				# for data in self.date_and_value:
				# 	print(data)
				frappe.throw("dd")
			
		
