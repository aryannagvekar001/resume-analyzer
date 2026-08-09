import os
import re

import PyPDF2
from docx import Document


# ============================================================
# PDF TEXT EXTRACTION
# ============================================================

def extract_pdf_text(file_path):
    """Extract text from a PDF file."""

    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()


# ============================================================
# DOCX TEXT EXTRACTION
# ============================================================

def extract_docx_text(file_path):
    """Extract text from a DOCX file."""

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)


# ============================================================
# GENERAL RESUME EXTRACTION
# ============================================================

def extract_resume_text(file_path):
    """Extract text from PDF or DOCX."""

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    if extension == ".docx":
        return extract_docx_text(file_path)

    raise ValueError(
        "Unsupported file type. Please upload a PDF or DOCX file."
    )


# ============================================================
# EMAIL EXTRACTION
# ============================================================

def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return ""


# ============================================================
# PHONE EXTRACTION
# ============================================================

def extract_phone(text):
    patterns = [
        r"\+91[\s-]?[6-9]\d{9}",
        r"\b[6-9]\d{9}\b",
        r"\+?\d[\d\s().-]{8,}\d"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            return match.group(0).strip()

    return ""


# ============================================================
# SKILLS DATABASE
# ============================================================

SKILLS_DATABASE = [

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

    # Data
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "data analysis",
    "data science",

    # AI
    "artificial intelligence",
    "generative ai",
    "genai",
    "llm",
    "nlp",
    "gemini",
    "openai",

    # Databases
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "oracle",

    # Cloud
    "aws",
    "azure",
    "google cloud",
    "gcp",
    "cloud run",

    # DevOps
    "docker",
    "kubernetes",
    "git",
    "github",
    "ci/cd",

    # Tools
    "linux",
    "power bi",
    "excel",
    "tableau",

    # Other
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
    "time management"
]


# ============================================================
# SKILL EXTRACTION
# ============================================================

def extract_skills(text):
    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS_DATABASE:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return sorted(set(found_skills))


# ============================================================
# SECTION DETECTION
# ============================================================

SECTION_KEYWORDS = {

    "Summary": [
        "summary",
        "professional summary",
        "profile",
        "objective"
    ],

    "Education": [
        "education",
        "academic background",
        "academic qualification"
    ],

    "Experience": [
        "experience",
        "work experience",
        "employment",
        "professional experience"
    ],

    "Projects": [
        "projects",
        "personal projects",
        "academic projects"
    ],

    "Skills": [
        "skills",
        "technical skills",
        "technical expertise"
    ],

    "Certifications": [
        "certification",
        "certifications"
    ],

    "Achievements": [
        "achievements",
        "awards",
        "accomplishments"
    ],

    "Languages": [
        "languages",
        "language"
    ]
}


def detect_sections(text):
    text_lower = text.lower()

    detected = []

    for section, keywords in SECTION_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text_lower:
                detected.append(section)
                break

    return detected


# ============================================================
# RESUME PARSER
# ============================================================

def parse_resume(file_path):

    text = extract_resume_text(file_path)

    if not text.strip():
        raise ValueError(
            "No readable text was found in the resume."
        )

    email = extract_email(text)

    phone = extract_phone(text)

    skills = extract_skills(text)

    sections = detect_sections(text)

    return {

        "file_name": os.path.basename(file_path),

        "raw_text": text,

        "email": email,

        "phone": phone,

        "skills": skills,

        "sections": sections,

        "text_length": len(text)

    }