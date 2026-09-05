# analysis/ats/ats_risk_detector.py
import re


class ATSRiskDetector:
    def detect(self, resume_text):
        text = (resume_text or "").strip()
        word_count = len(re.findall(r"\b\w+\b", text))
        risks = []

        if word_count < 150:
            risks.append({
                "level": "high",
                "message": "Resume content is too short.",
            })

        if not re.search(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", text):
            risks.append({
                "level": "medium",
                "message": "No email address detected.",
            })

        if not re.search(r"\+?\d[\d\s().-]{7,}\d", text):
            risks.append({
                "level": "medium",
                "message": "No phone number detected.",
            })

        if not re.search(r"\b(experience|employment|work history)\b", text, re.I):
            risks.append({
                "level": "medium",
                "message": "No experience section heading detected.",
            })

        if not re.search(r"\b(education|qualification)\b", text, re.I):
            risks.append({
                "level": "low",
                "message": "No education section heading detected.",
            })

        return risks