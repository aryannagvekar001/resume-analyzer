# analysis/resume_score.py
import re


class ResumeScore:
    REQUIRED_SECTIONS = ("experience", "education", "skills", "summary")
    ACTION_VERBS = {
        "achieved", "built", "created", "delivered", "designed",
        "developed", "improved", "increased", "led", "managed",
        "optimized", "reduced",
    }

    def calculate(self, resume_text, skills=None):
        text = (resume_text or "").strip()
        normalized = text.lower()
        words = re.findall(r"\b[\w+#.-]+\b", normalized)
        skills = skills or []

        breakdown = {}
        suggestions = []

        breakdown["length"] = 25 if 300 <= len(words) <= 900 else 15 if len(words) >= 150 else 5
        if len(words) < 300:
            suggestions.append("Add more detail about your experience and projects.")

        found_sections = sum(section in normalized for section in self.REQUIRED_SECTIONS)
        breakdown["sections"] = round(found_sections / len(self.REQUIRED_SECTIONS) * 25)

        missing = [
            section.title()
            for section in self.REQUIRED_SECTIONS
            if section not in normalized
        ]
        if missing:
            suggestions.append("Add sections for: " + ", ".join(missing) + ".")

        has_email = bool(re.search(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", text))
        has_phone = bool(re.search(r"\+?\d[\d\s().-]{7,}\d", text))
        breakdown["contact"] = 15 if has_email and has_phone else 8 if has_email or has_phone else 0

        if not has_email:
            suggestions.append("Add a professional email address.")
        if not has_phone:
            suggestions.append("Add a phone number.")

        breakdown["skills"] = min(20, len(skills) * 2)
        if len(skills) < 5:
            suggestions.append("Include more relevant technical skills.")

        action_count = sum(word in self.ACTION_VERBS for word in words)
        breakdown["impact"] = 15 if action_count >= 5 else 8 if action_count >= 2 else 2
        if action_count < 5:
            suggestions.append("Use action verbs to describe achievements.")

        return {
            "score": min(100, sum(breakdown.values())),
            "breakdown": breakdown,
            "suggestions": suggestions,
            "word_count": len(words),
        }