from .ats_score import ATSScore
from .ats_risk_detector import ATSRiskDetector
from .ats_compatibility import ATSCompatibility


class ATSAnalyzer:
    def __init__(self):
        self.score = ATSScore()
        self.risks = ATSRiskDetector()
        self.compatibility = ATSCompatibility()

    def analyze(self, resume_text, job_description=""):
        score = self.score.calculate(
            resume_text,
            job_description,
        )

        risks = self.risks.detect(resume_text)

        compatibility = self.compatibility.evaluate(
            score,
            risks,
        )

        return {
            "ats_score": score,
            "risks": risks,
            "compatibility": compatibility,
        }