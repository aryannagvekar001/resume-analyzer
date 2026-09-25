from .resume_routes import analyze_resume
from .job_routes import match_job
from .analysis_routes import analyze_resume_details
from .interview_routes import generate_interview
from .career_routes import recommend_career

def create_routes():
    return {"resume": analyze_resume, "job": match_job, "analysis": analyze_resume_details, "interview": generate_interview, "career": recommend_career}
