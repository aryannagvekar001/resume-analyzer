from backend.analysis.resume_analyzer import ResumeAnalyzer
from backend.parser import parse_resume


def analyze_resume(file_path, job_description=""):
    resume = parse_resume(file_path)

    analyzer = ResumeAnalyzer()

    result = analyzer.analyze(
        resume["text"],
        job_description,
    )

    result["source"] = resume["source"]
    result["contact"] = resume["contact"]
    result["sections"] = resume["sections"]

    return result