# analysis/ats/ats_analyzer.py
from .ats_score import ATSScore
from .ats_risk_detector import ATSRiskDetector
from .ats_compatibility import ATSCompatibility


class ATSAnalyzer:
    def __init__(self):
        self.score_calculator = ATSScore()
        self.risk_detector = ATSRiskDetector()
        self.compatibility_checker = ATSCompatibility()

    def analyze(self, resume_text, job_description=""):
        ats_score = self.score_calculator.calculate(
            resume_text,
            job_description,
        )
        risks = self.risk_detector.detect(resume_text)
        compatibility = self.compatibility_checker.evaluate(
            ats_score,
            risks,
        )

        return {
            "ats_score": ats_score,
            "risks": risks,
            "compatibility": compatibility,
        }