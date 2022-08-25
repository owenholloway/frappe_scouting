# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe.website.website_generator import WebsiteGenerator


class Scout Group(WebsiteGenerator):
	_website = frappe._dict(
		condition_field = "published",
	)

	def get_context(self, context):
		context.no_cache = True
		context.show_sidebar = True
		context.parents = [dict(label='View All Scout Groups',
			route='scout_groups', title='View Scout Groups')]

	def validate(self):
		if not self.route:		#pylint: disable=E0203
			self.route = 'scout_groups/' + self.scrub(self.name)

	def enable(self):
		scout_group = frappe.get_doc('Scout Group', frappe.form_dict.name)
		scout_group.append('members', dict(enable=self.value))
		scout_group.save(ignore_permissions=1)
		frappe.db.commit()


def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.show_sidebar = True
	context.title = 'All Scout Groups'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'


@frappe.whitelist()
def leave(title, user_id, leave_reason):
	scout_group = frappe.get_doc("Scout Group", title)
	for member in scout_group.members:
		if member.user == user_id:
			member.enabled = 0
			member.leave_reason = leave_reason
	scout_group.save(ignore_permissions=1)
	frappe.db.commit()
	return "Thank you for Feedback"
