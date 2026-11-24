# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "crm_pipeline"
app_title = "Frappe Crm Lead Opportunity Pipeline"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Crm Lead Opportunity Pipeline - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/crm_pipeline/css/crm_pipeline.bundle.css"
app_include_js = "/assets/crm_pipeline/js/crm_pipeline.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Crm Lead Opportunity Pipeline Entry": {
        "validate": "crm_pipeline.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "crm_pipeline.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "crm_pipeline.tasks.hourly_sync"
    ],
    "daily": [
        "crm_pipeline.tasks.daily_reconciliation"
    ],
    "weekly": [
        "crm_pipeline.tasks.weekly_digest"
    ]
}
