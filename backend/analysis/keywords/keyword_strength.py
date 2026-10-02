class KeywordStrength:

    def calculate(self, keywords):
        count = len(keywords or [])

        if count >= 15:
            return "strong"
        if count >= 8:
            return "moderate"

        return "weak"