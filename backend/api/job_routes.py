from backend.job.job_description_analyzer import JobDescriptionAnalyzer
from backend.job.job_matcher import JobMatcher


def match_job(resume_text, job_description):
    job_data = JobDescriptionAnalyzer().analyze(job_description)

    result = JobMatcher().match(
        resume_text,
        job_description,
    )

    result["job_analysis"] = job_data

    return result