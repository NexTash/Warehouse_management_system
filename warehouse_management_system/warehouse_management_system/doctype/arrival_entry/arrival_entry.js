// Copyright (c) 2024, ali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Arrival Entry', {
	onload: function(frm) {
        frm.set_query("item_location",'warehouse_location', () => {
            return {
                filters: {
                    warehouse: frm.doc.warehouse_name
                }
            };
        });
    }
});

