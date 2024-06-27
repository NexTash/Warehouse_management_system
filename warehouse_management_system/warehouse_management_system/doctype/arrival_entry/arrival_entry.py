# Copyright (c) 2024, ali and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ArrivalEntry(Document):
	def validate(self):
		for row in self.warehouse_location:
			docs = frappe.get_list("Warehouse Bin", {"warehouse": self.warehouse_name, "item" : row.item_name, "location": row.item_location})
			if len(docs) > 0:
				frappe.msgprint(f"{docs}")
				doc = frappe.get_doc("Warehouse Bin", docs[0].name)
				doc.qty = doc.qty + row.qty
				doc.save()
			else:
				new_doc = frappe.new_doc("Warehouse Bin")
				new_doc.warehouse = self.warehouse_name
				new_doc.item = row.item_name
				new_doc.location = row.item_location
				new_doc.qty = row.qty
				new_doc.save()
			frappe.db.commit()

























# @frappe.whitelist()
# def update_qty(warehouse, item_code, qty, operation):

#     arrival_entry = frappe.get_doc('Arrival Entry', {'warehouse_location': warehouse, 'item_name': item_code})
#     if not arrival_entry:
#         frappe.throw(('Arrival Entry not found for the given warehouse and item.'))
    
#     current_qty = arrival_entry.qty or 0


#     if operation == 'add':
#         new_qty = current_qty + qty
#     elif operation == 'subtract':
#         new_qty = current_qty - qty


#     arrival_entry.qty = new_qty
#     arrival_entry.save()
#     frappe.db.commit()