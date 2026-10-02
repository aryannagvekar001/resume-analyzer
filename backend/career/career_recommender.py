from .role_recommender import RoleRecommender
class CareerRecommender:
    def __init__(self): self.roles=RoleRecommender()
    def recommend(self,text): return {"recommended_roles":self.roles.recommend([])}
