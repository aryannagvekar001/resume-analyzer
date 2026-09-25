class PromptManager:

    @staticmethod
    def improve_resume(text):
        return f"""
Improve the following resume content.

Rules:
- Keep facts unchanged.
- Do not invent experience.
- Use clear professional language.
- Make achievements measurable when the original text provides numbers.
- Keep it concise.

Resume:
{text}
""".strip()

    @staticmethod
    def summarize(text):
        return f"""
Create a concise professional resume summary from the following content.

Do not invent information.

Resume:
{text}
""".strip()

    @staticmethod
    def tailor(text, job_description):
        return f"""
Tailor the resume to the job description.

Keep all facts truthful.
Use relevant keywords naturally.
Do not invent skills or experience.

RESUME:
{text}

JOB DESCRIPTION:
{job_description}
""".strip()

    @staticmethod
    def recommendations(text):
        return f"""
Review this resume and provide practical improvement suggestions.

Focus on:
- skills
- achievements
- clarity
- ATS compatibility
- missing information

Do not invent facts.

Resume:
{text}
""".strip()