# analysis/ats/ats_compatibility.py
class ATSCompatibility:
    def evaluate(self, ats_score, risks):
        score = int(ats_score.get("score", 0))
        high_risks = sum(risk["level"] == "high" for risk in risks)
        medium_risks = sum(risk["level"] == "medium" for risk in risks)

        adjusted_score = max(0, score - high_risks * 20 - medium_risks * 8)

        if adjusted_score >= 80:
            label = "High compatibility"
        elif adjusted_score >= 60:
            label = "Moderate compatibility"
        else:
            label = "Low compatibility"

        return {
            "score": adjusted_score,
            "label": label,
            "risk_count": len(risks),
            "recommendation": (
                "Use missing job keywords naturally in your experience."
                if ats_score.get("missing_keywords")
                else "Use clear headings and a simple resume layout."
            ),
        }