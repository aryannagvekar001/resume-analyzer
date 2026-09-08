# analysis/ats/ats_score.py
import re


class ATSScore:
    def calculate(self, resume_text, job_description=""):
        resume_words = self._extract_words(resume_text)
        job_words = self._extract_words(job_description)

        if not job_words:
            return {
                "score": 0,
                "matched_keywords": [],
                "missing_keywords": [],
                "message": "Add a job description to calculate ATS matching.",
            }

        ignored = {
            "and", "are", "for", "from", "have", "into", "job",
            "our", "that", "the", "this", "with", "will", "you",
        }

        keywords = {
            word for word in job_words
            if len(word) > 2 and word not in ignored
        }

        matched = sorted(keywords.intersection(resume_words))
        missing = sorted(keywords.difference(resume_words))
        score = round((len(matched) / len(keywords)) * 100) if keywords else 0

        return {
            "score": score,
            "matched_keywords": matched,
            "missing_keywords": missing,
            "message": "ATS keyword comparison completed.",
        }

    @staticmethod
    def _extract_words(text):
        return set(re.findall(r"[a-zA-Z][a-zA-Z0-9+#.-]*", (text or "").lower()))