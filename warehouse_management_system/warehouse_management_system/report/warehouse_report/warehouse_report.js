// Copyright (c) 2024, ali and contributors
// For license information, please see license.txt
/* eslint-disable */
frappe.query_reports["Warehouse Report"] = {
    filters: [
        {
            fieldname: 'warehouse_name',
            label: 'Warehouse Name',
            fieldtype: 'Link',
            options: 'Warehouse'
        },
        {
            fieldname: 'item_name',
            label: 'Item Name',
            fieldtype: 'Link',
            options: 'Item'
        }
    ]
};