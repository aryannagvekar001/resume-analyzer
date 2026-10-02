import re


class ResumeScore:
    REQUIRED_SECTIONS = (
        "experience",
        "education",
        "skills",
        "summary",
    )

    ACTION_VERBS = {
        "achieved",
        "built",
        "created",
        "delivered",
        "designed",
        "developed",
        "improved",
        "increased",
        "led",
        "managed",
        "optimized",
        "reduced",
    }

    def calculate(self, resume_text, skills=None):
        text = (resume_text or "").strip()
        normalized = text.lower()

        words = re.findall(
            r"\b[\w+#.-]+\b",
            normalized,
        )

        skills = skills or []

        breakdown = {}

        breakdown["length"] = (
            25
            if 300 <= len(words) <= 900
            else 15
            if len(words) >= 150
            else 5
        )

        found_sections = sum(
            section in normalized
            for section in self.REQUIRED_SECTIONS
        )

        breakdown["sections"] = round(
            found_sections
            / len(self.REQUIRED_SECTIONS)
            * 25
        )

        has_email = bool(
            re.search(
                r"[\w.+-]+@[\w-]+\.[\w.-]+",
                text,
            )
        )

        has_phone = bool(
            re.search(
                r"\+?\d[\d\s().-]{7,}\d",
                text,
            )
        )

        breakdown["contact"] = (
            15
            if has_email and has_phone
            else 8
            if has_email or has_phone
            else 0
        )

        breakdown["skills"] = min(
            20,
            len(skills) * 2,
        )

        action_count = sum(
            word in self.ACTION_VERBS
            for word in words
        )

        breakdown["impact"] = (
            15
            if action_count >= 5
            else 8
            if action_count >= 2
            else 2
        )

        suggestions = []

        if len(words) < 300:
            suggestions.append(
                "Add more detail about experience and projects."
            )

        if found_sections < 4:
            suggestions.append(
                "Add clear resume section headings."
            )

        if not has_email:
            suggestions.append(
                "Add a professional email address."
            )

        if not has_phone:
            suggestions.append(
                "Add a phone number."
            )

        if len(skills) < 5:
            suggestions.append(
                "Include more relevant technical skills."
            )

        if action_count < 5:
            suggestions.append(
                "Use stronger action verbs for achievements."
            )

        return {
            "score": min(
                100,
                sum(breakdown.values()),
            ),
            "breakdown": breakdown,
            "suggestions": suggestions,
            "word_count": len(words),
        }