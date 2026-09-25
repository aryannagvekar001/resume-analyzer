from backend.interview.question_generator import QuestionGenerator


def generate_interview(resume_text, job_description=""):
    generator = QuestionGenerator()

    return generator.generate(
        resume_text,
        job_description,
    )