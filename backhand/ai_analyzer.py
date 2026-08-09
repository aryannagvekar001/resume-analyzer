import os

from dotenv import load_dotenv
from google import genai


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


if not api_key:

    raise ValueError(
        "GOOGLE_API_KEY was not found.\n\n"
        "Create a .env file in the project folder "
        "and add:\n\n"
        "GOOGLE_API_KEY=YOUR_API_KEY"
    )


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=api_key
)


# ============================================================
# GEMINI ANALYSIS
# ============================================================

def analyze_with_gemini(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert ATS resume analyzer,
technical recruiter, and career advisor.

Analyze the candidate's resume against the
provided job description.

========================
RESUME
========================

{resume_text}


========================
JOB DESCRIPTION
========================

{job_description}


========================
ANALYSIS REQUIRED
========================

Provide the following:

1. Overall Resume-Job Fit

Give a realistic assessment.

2. Resume Strengths

Identify the strongest parts of the resume.

3. Resume Weaknesses

Identify areas that should be improved.

4. Matching Skills

List technical and professional skills
that match the job.

5. Missing Skills

List important skills mentioned in the job
description that are not clearly demonstrated
in the resume.

6. Matching Keywords

Identify important keywords already present.

7. Missing Keywords

Identify useful job-specific keywords missing
from the resume.

8. Experience Relevance

Explain how relevant the candidate's experience
is to the position.

9. Project Relevance

Explain which projects are relevant and how
they could be presented better.

10. ATS Optimization

Give practical ATS recommendations.

11. Professional Summary

Suggest how the professional summary could
be improved.

12. Bullet Point Improvements

Give examples of how existing resume bullets
could be made stronger.

13. Final Recommendation

Give a concise recommendation.

IMPORTANT RULES:

- Do not invent experience.
- Do not invent projects.
- Do not invent certifications.
- Do not invent skills.
- Do not claim the candidate has experience
  that is not present.
- Clearly separate existing skills from
  recommended skills.
- Be realistic.
- Do not encourage the candidate to lie.
- Use headings and bullet points.
- Keep the response professional and useful.
"""

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        return response.text


    except Exception as error:

        return (
            "Gemini analysis could not be completed.\n\n"
            f"Error: {str(error)}"
        )