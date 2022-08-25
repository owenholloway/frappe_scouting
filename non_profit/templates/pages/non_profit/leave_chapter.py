import frappe


def get_context(context):
	context.no_cache = True
	scout_group = frappe.get_doc('Scout Group', frappe.form_dict.name)
	context.member_deleted = True
	context.scout_group = scout_group
