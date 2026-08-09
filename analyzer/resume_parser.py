import re
from pathlib import Path

import PyPDF2
from docx import Document


def clean_text(text):
    if not text:
        return ""

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    text = re.sub(r" *\n *", "\n", text)

    text = text.replace("•", "-")
    text = text.replace("●", "-")
    text = text.replace("▪", "-")
    text = text.replace("◦", "-")

    return text.strip()


def extract_pdf_text(file_path):
    text = ""

    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        raise ValueError(f"Unable to read PDF: {e}")

    return clean_text(text)


def extract_docx_text(file_path):
    try:
        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text)

        return clean_text("\n".join(paragraphs))

    except Exception as e:
        raise ValueError(f"Unable to read DOCX: {e}")


def extract_resume_text(file_path):
    """
    Extract text from PDF or DOCX resume.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    extension = file_path.suffix.lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    else:
        raise ValueError(
            "Only PDF and DOCX files are supported."
        )


def extract_email(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return None


def extract_phone(text):
    patterns = [
        r"\+91[\s-]?[6-9]\d{9}",
        r"\b[6-9]\d{9}\b"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            return match.group(0)

    return None


COMMON_SKILLS = [
    "python",
    "java",
    "javascript",
    "typescript",
    "c",
    "c++",
    "c#",
    "html",
    "css",
    "react",
    "angular",
    "node.js",
    "nodejs",
    "fastapi",
    "flask",
    "django",
    "streamlit",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "google cloud",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "power bi",
    "excel",
    "tableau"
]


def extract_skills(text):
    text_lower = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:

        pattern = rf"(?<!\w){re.escape(skill.lower())}(?!\w)"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return sorted(set(found_skills))


def extract_years_of_experience(text):
    patterns = [
        r"(\d+)\+?\s*years?\s+(?:of\s+)?experience",
        r"experience\s*[:\-]?\s*(\d+)\+?\s*years?"
    ]

    years = []

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text.lower()
        )

        for value in matches:

            try:
                years.append(int(value))

            except ValueError:
                pass

    if years:
        return max(years)

    return 0


def parse_resume(file_path):
    text = extract_resume_text(file_path)

    return {
        "file_name": Path(file_path).name,
        "raw_text": text,
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "years_of_experience": extract_years_of_experience(text)
    }