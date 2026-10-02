class ReadabilityAnalyzer:
    def analyze(self,text): return {"word_count":len((text or "").split())}
