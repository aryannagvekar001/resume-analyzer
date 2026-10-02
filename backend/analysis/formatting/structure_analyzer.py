class StructureAnalyzer:

    SECTIONS = (
        "summary",
        "experience",
        "education",
        "skills",
        "projects",
        "certifications",
    )

    def analyze(self, text):
        normalized = (text or "").lower()

        found = [
            section
            for section in self.SECTIONS
            if section in normalized
        ]

        return {
            "sections_found": found,
            "section_count": len(found),
        }