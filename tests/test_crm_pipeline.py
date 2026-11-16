import unittest
from crm_pipeline.engine import FrappeCRMPipelineEngine, CRMLead, ExotelCallLog

class TestCRMPipeline(unittest.TestCase):
    def test_lead_qualification_scoring(self):
        engine = FrappeCRMPipelineEngine()
        lead = CRMLead("LEAD-01", "Vikram Singh", "Apex Infotech", "vikram@apex.com", "9876543210", 1500000.0, "Referral")
        score = engine.score_lead(lead)
        self.assertEqual(score, 100.0)

    def test_exotel_call_transition(self):
        engine = FrappeCRMPipelineEngine()
        lead = CRMLead("LEAD-02", "Sunita Rao", "Rao Consulting", "sunita@rao.com", "9876543211", 300000.0, "Website")
        call = ExotelCallLog("EXO-CALL-991", "LEAD-02", "AGENT-01", 120, "COMPLETED")
        status = engine.process_exotel_call(call, lead)
        self.assertEqual(status, "LEAD_ENGAGED")
        self.assertEqual(lead.status, "CONTACTED")

if __name__ == "__main__":
    unittest.main()
