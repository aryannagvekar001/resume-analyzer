from backend.career.career_recommender import CareerRecommender

def recommend_career(resume_text):
    return CareerRecommender().recommend(resume_text)
