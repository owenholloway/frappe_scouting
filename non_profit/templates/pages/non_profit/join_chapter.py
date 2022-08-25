import frappe


def get_context(context):
	context.no_cache = True
	scout_group = frappe.get_doc('Scout Group', frappe.form_dict.name)
	if frappe.session.user!='Guest':
		if frappe.session.user in [d.user for d in scout_group.members if d.enabled == 1]:
			context.already_member = True
		else:
			if frappe.request.method=='GET':
				pass
			elif frappe.request.method=='POST':
				scout_group.append('members', dict(
					user=frappe.session.user,
					introduction=frappe.form_dict.introduction,
					website_url=frappe.form_dict.website_url,
					enabled=1
				))
				scout_group.save(ignore_permissions=1)
				frappe.db.commit()

	context.scout_group = scout_group
