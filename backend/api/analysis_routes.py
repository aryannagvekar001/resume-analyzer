from backend.analysis.resume_analyzer import ResumeAnalyzer


def analyze_resume_details(resume_text, job_description=""):
    analyzer = ResumeAnalyzer()

    return analyzer.analyze(
        resume_text,
        job_description,
    )