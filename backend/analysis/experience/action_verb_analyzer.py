class ActionVerbAnalyzer:

    VERBS = {
        "built", "created", "designed", "developed",
        "implemented", "improved", "led", "managed",
        "optimized", "reduced", "increased",
        "automated", "delivered", "created",
    }

    def analyze(self, text):
        words = (text or "").lower().split()

        found = sorted(
            verb
            for verb in self.VERBS
            if verb in words
        )

        return {
            "count": len(found),
            "verbs": found,
        }
