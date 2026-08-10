# ============================================================
# JOB KEYWORDS
# ============================================================

COMMON_JOB_KEYWORDS = [

    # Programming
    "python",
    "java",
    "javascript",
    "typescript",
    "c",
    "c++",
    "c#",
    "sql",

    # Web
    "html",
    "css",
    "react",
    "angular",
    "node.js",
    "fastapi",
    "flask",
    "django",

    # Data / AI
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "generative ai",
    "data analysis",
    "data science",
    "pandas",
    "numpy",
    "scikit-learn",
    "nlp",
    "llm",

    # Database
    "mysql",
    "postgresql",
    "mongodb",
    "oracle",

    # Cloud
    "aws",
    "azure",
    "gcp",
    "google cloud",
    "cloud run",

    # DevOps
    "docker",
    "kubernetes",
    "git",
    "github",
    "ci/cd",

    # Development
    "rest api",
    "api",
    "oop",
    "data structures",
    "algorithms",

    # Soft skills
    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "problem-solving",

    # Work methods
    "agile",
    "scrum",
    "project management"
]


# ============================================================
# EXTRACT JOB KEYWORDS
# ============================================================

def extract_job_keywords(job_description):

    text = job_description.lower()

    found = []

    for keyword in COMMON_JOB_KEYWORDS:

        if keyword.lower() in text:
            found.append(keyword)

    return sorted(set(found))


# ============================================================
# SKILL MATCH
# ============================================================

def calculate_skill_match(
    resume_skills,
    job_keywords
):

    resume_skills_lower = {
        skill.lower()
        for skill in resume_skills
    }

    matched = []
    missing = []

    for keyword in job_keywords:

        if keyword.lower() in resume_skills_lower:
            matched.append(keyword)

        else:
            missing.append(keyword)

    if job_keywords:

        score = round(
            len(matched)
            / len(job_keywords)
            * 100
        )

    else:

        score = 0

    return {

        "score": score,

        "matched": matched,

        "missing": missing

    }


# ============================================================
# KEYWORD MATCH
# ============================================================

def calculate_keyword_match(
    resume_text,
    job_description
):

    resume_text_lower = resume_text.lower()

    job_keywords = extract_job_keywords(
        job_description
    )

    matched = []
    missing = []

    for keyword in job_keywords:

        if keyword.lower() in resume_text_lower:
            matched.append(keyword)

        else:
            missing.append(keyword)

    if job_keywords:

        score = round(
            len(matched)
            / len(job_keywords)
            * 100
        )

    else:

        score = 0

    return {

        "score": score,

        "matched": matched,

        "missing": missing

    }


# ============================================================
# REQUIRED SECTIONS
# ============================================================

REQUIRED_SECTIONS = [

    "Education",
    "Experience",
    "Projects",
    "Skills"

]


# ============================================================
# SECTION SCORE
# ============================================================

def calculate_section_score(sections):

    sections_lower = {
        section.lower()
        for section in sections
    }

    present = []
    missing = []

    for section in REQUIRED_SECTIONS:

        if section.lower() in sections_lower:
            present.append(section)

        else:
            missing.append(section)

    score = round(
        len(present)
        / len(REQUIRED_SECTIONS)
        * 100
    )

    return {

        "score": score,

        "present": present,

        "missing": missing

    }


# ============================================================
# FORMAT SCORE
# ============================================================

def calculate_format_score(resume_data):

    score = 100

    text = resume_data["raw_text"]

    if len(text) < 500:
        score -= 30

    if not resume_data["email"]:
        score -= 15

    if not resume_data["phone"]:
        score -= 15

    if not resume_data["skills"]:
        score -= 20

    return max(score, 0)


# ============================================================
# SUGGESTIONS
# ============================================================

def generate_suggestions(
    resume_data,
    skill_match,
    keyword_match,
    section_analysis
):

    suggestions = []

    if skill_match["missing"]:

        missing = ", ".join(
            skill_match["missing"][:8]
        )

        suggestions.append(
            "Consider adding relevant skills such as "
            f"{missing}, but only if you genuinely "
            "have those skills."
        )

    if keyword_match["missing"]:

        missing = ", ".join(
            keyword_match["missing"][:8]
        )

        suggestions.append(
            "Important job keywords missing from "
            f"your resume: {missing}."
        )

    if section_analysis["missing"]:

        missing = ", ".join(
            section_analysis["missing"]
        )

        suggestions.append(
            "Consider adding these sections: "
            f"{missing}."
        )

    if resume_data["text_length"] < 800:

        suggestions.append(
            "Your resume appears short. Consider "
            "adding relevant projects, achievements, "
            "technical details, or measurable results."
        )

    if not resume_data["email"]:

        suggestions.append(
            "Add a professional email address."
        )

    if not resume_data["phone"]:

        suggestions.append(
            "Add a professional phone number."
        )

    suggestions.append(
        "Use measurable achievements where possible, "
        "such as percentages, time saved, users supported, "
        "or performance improvements."
    )

    return suggestions


# ============================================================
# MAIN RESUME ANALYSIS
# ============================================================

def analyze_resume(
    resume_data,
    job_description
):

    resume_text = resume_data["raw_text"]

    resume_skills = resume_data["skills"]

    sections = resume_data["sections"]


    # Job keywords
    job_keywords = extract_job_keywords(
        job_description
    )


    # Skill match
    skill_match = calculate_skill_match(
        resume_skills,
        job_keywords
    )


    # Keyword match
    keyword_match = calculate_keyword_match(
        resume_text,
        job_description
    )


    # Sections
    section_analysis = calculate_section_score(
        sections
    )


    # Formatting
    format_score = calculate_format_score(
        resume_data
    )


    # ========================================================
    # ATS SCORE
    # ========================================================

    ats_score = round(

        (
            skill_match["score"]
            * 0.40
        )

        +

        (
            keyword_match["score"]
            * 0.30
        )

        +

        (
            section_analysis["score"]
            * 0.20
        )

        +

        (
            format_score
            * 0.10
        )

    )


    # Suggestions
    suggestions = generate_suggestions(

        resume_data,

        skill_match,

        keyword_match,

        section_analysis

    )


    return {

        "ats_score": ats_score,

        "skill_match": skill_match,

        "keyword_match": keyword_match,

        "section_score": section_analysis["score"],

        "format_score": format_score,

        "sections": section_analysis,

        "suggestions": suggestions

    }