# Copyright (c) 2024, ali and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns, data = [], []
    
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data

def get_columns():
    return [
        {
            "label": "Warehouse Name", 
            "fieldname": "warehouse", 
            "fieldtype": "Link", 
            "options": "Warehouse", 
            "width": 200
        },
        {
            "label": "Item Name", 
            "fieldname": "item", 
            "fieldtype": "Data", 
            "width": 250
        },
        {
            "label": "Item Location", 
            "fieldname": "location", 
            "fieldtype": "Data", 
            "width": 250
        },
        {
            "label": "QTY", 
            "fieldname": "qty", 
            "fieldtype": "Int", 
            "width": 200
        }
    ]

def get_data(filters):
    data = []
    conditions = {"docstatus": ("<", 2)}

    if filters.get("warehouse_name"):
        conditions["warehouse"] = filters.get("warehouse_name")
    if filters.get("item_name"):
        conditions["item"] = filters.get("item_name")
   
    entries = frappe.get_all('Warehouse Bin', filters=conditions, fields=['*'])
    for ent in entries:
        data.append({
            "warehouse": ent.warehouse,
            "item": ent.item,
            "location": ent.location,
            "qty": ent.qty
        })
    
    return data