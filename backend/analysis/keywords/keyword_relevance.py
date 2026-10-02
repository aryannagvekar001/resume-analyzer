class KeywordRelevance:

    def calculate(self, matched, job_words):
        total = len(set(job_words or []))

        if not total:
            return 0

        return round(
            len(set(matched or [])) / total * 100
        )