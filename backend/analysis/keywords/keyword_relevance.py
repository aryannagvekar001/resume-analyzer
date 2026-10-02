class KeywordRelevance:
    def calculate(self,matched,job_words): return round(len(set(matched or []))/len(set(job_words or []))*100) if job_words else 0
