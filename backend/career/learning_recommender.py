class LearningRecommender:
    def recommend(self,skills): return [{"skill":s,"topic":"Learn "+s} for s in skills or []]
