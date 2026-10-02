class FeedbackGenerator:
    def generate(self,evaluation): return evaluation.get("feedback","") if isinstance(evaluation,dict) else str(evaluation)
