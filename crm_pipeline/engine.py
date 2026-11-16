"""Complete Frappe CRM Engine (Lead se Customer tak - Custom CRM - Koi lead miss nahi hogi, har follow-up yaad rahega)."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class CRMLead:
    lead_id: str
    lead_name: str
    company_name: str
    email: str
    phone: str
    annual_budget_inr: float
    source: str           # Website, WhatsApp, Referral, Cold Call
    status: str = "OPEN"  # OPEN, CONTACTED, QUALIFIED, LOST


@dataclass
class ExotelCallLog:
    call_sid: str
    lead_id: str
    agent_id: str
    duration_seconds: int
    call_status: str      # COMPLETED, MISSED, BUSY


class FrappeCRMPipelineEngine:
    """Lead qualification scoring, Exotel call tracking, and Sales Opportunity Funnel."""

    def score_lead(self, lead: CRMLead) -> float:
        """Derives a predictive lead score (0-100) based on budget, contact details, and source."""
        score = 0.0
        if lead.email and "@" in lead.email:
            score += 20.0
        if lead.phone and len(lead.phone) >= 10:
            score += 20.0
        
        # Budget tiers
        if lead.annual_budget_inr >= 1000000.0:
            score += 40.0
        elif lead.annual_budget_inr >= 250000.0:
            score += 25.0
        else:
            score += 10.0

        if lead.source in ["Referral", "Website"]:
            score += 20.0
        else:
            score += 10.0

        return min(100.0, score)

    def process_exotel_call(self, log: ExotelCallLog, lead: CRMLead) -> str:
        """Transitions lead state upon successful connected phone call."""
        if log.call_status == "COMPLETED" and log.duration_seconds >= 60:
            lead.status = "CONTACTED"
            return "LEAD_ENGAGED"
        return "FOLLOW_UP_REQUIRED"
