# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "crm_pipeline"
app_title = "Frappe Crm Lead Opportunity Pipeline"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Crm Lead Opportunity Pipeline for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/crm_pipeline/css/crm_pipeline.bundle.css"
app_include_js = "/assets/crm_pipeline/js/crm_pipeline.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "crm_pipeline.engine.on_document_submit",
        "on_cancel": "crm_pipeline.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "crm_pipeline.engine.daily_scheduled_sync"
    ]
}
