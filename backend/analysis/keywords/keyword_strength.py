class KeywordStrength:
    def calculate(self,keywords): return "strong" if len(keywords or [])>=15 else "moderate" if len(keywords or [])>=8 else "weak"
