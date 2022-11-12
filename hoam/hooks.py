from . import __version__ as app_version

app_name = "hoam"
app_title = "Hoam"
app_publisher = "FinByz Tech Pvt Ltd"
app_description = "Custom App"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@finbyz.com"
app_license = "GPL 3.0"




doctype_js = {
	"Issue": "public/js/doctype_js/issue.js",
}
doc_events = {
    "Issue": {
        "validate": "hoam.api.issue_validate"
    }
}

scheduler_events = {
	"cron": {
		"0/1 * * * *": [
			"hoam.api.escalation_email"
		],
	}
	# "all":[
	# 	"jciw.api.make_status_overdue"
	# ]
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hoam/css/hoam.css"
# app_include_js = "/assets/hoam/js/hoam.js"

# include js, css files in header of web template
# web_include_css = "/assets/hoam/css/hoam.css"
# web_include_js = "/assets/hoam/js/hoam.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hoam/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hoam.install.before_install"
# after_install = "hoam.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hoam.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hoam.tasks.all"
# 	],
# 	"daily": [
# 		"hoam.tasks.daily"
# 	],
# 	"hourly": [
# 		"hoam.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hoam.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hoam.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hoam.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hoam.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hoam.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"hoam.auth.validate"
# ]
