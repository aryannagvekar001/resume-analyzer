```python
import re
from pathlib import Path

import PyPDF2
from docx import Document


# ============================================================
# TEXT EXTRACTION
# ============================================================

def extract_text_from_pdf(file_path):
    """Extract text from a PDF resume."""

    text = ""

    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        raise ValueError(f"Could not read PDF file: {e}")

    return clean_text(text)


def extract_text_from_docx(file_path):
    """Extract text from a DOCX resume."""

    try:
        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text)

        return clean_text("\n".join(paragraphs))

    except Exception as e:
        raise ValueError(f"Could not read DOCX file: {e}")


def extract_text(file_path):
    """
    Automatically detect the file type and extract resume text.

    Supported:
    - PDF
    - DOCX
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = file_path.suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    else:
        raise ValueError(
            "Unsupported file format. Please upload a PDF or DOCX file."
        )


# ============================================================
# TEXT CLEANING
# ============================================================

def clean_text(text):
    """Clean and normalize extracted resume text."""

    if not text:
        return ""

    # Remove excessive spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove spaces around new lines
    text = re.sub(r" *\n *", "\n", text)

    # Normalize common bullet characters
    text = text.replace("•", "-")
    text = text.replace("●", "-")
    text = text.replace("▪", "-")
    text = text.replace("◦", "-")

    return text.strip()


# ============================================================
# SECTION DETECTION
# ============================================================

SECTION_NAMES = {
    "summary": [
        "summary",
        "professional summary",
        "profile",
        "career objective",
        "objective",
    ],
    "skills": [
        "skills",
        "technical skills",
        "core skills",
        "key skills",
        "technologies",
    ],
    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
    ],
    "education": [
        "education",
        "academic background",
        "educational background",
        "qualifications",
    ],
    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "key projects",
    ],
    "certifications": [
        "certifications",
        "certificates",
        "licenses",
    ],
    "achievements": [
        "achievements",
        "accomplishments",
        "awards",
    ],
    "internships": [
        "internship",
        "internships",
    ],
}


def normalize_heading(text):
    """Normalize a possible section heading."""

    text = text.lower().strip()

    # Remove common punctuation
    text = re.sub(r"[:|]", "", text)

    return text


def detect_section_heading(line):
    """Return the standardized section name if a line is a heading."""

    normalized = normalize_heading(line)

    for section, headings in SECTION_NAMES.items():
        if normalized in headings:
            return section

    return None


def extract_sections(text):
    """
    Split resume text into logical sections.

    Returns a dictionary such as:

    {
        "summary": "...",
        "skills": "...",
        "experience": "...",
        "education": "..."
    }
    """

    sections = {}
    current_section = "general"

    sections[current_section] = []

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        detected_section = detect_section_heading(line)

        if detected_section:
            current_section = detected_section

            if current_section not in sections:
                sections[current_section] = []

            continue

        sections[current_section].append(line)

    # Convert lists to strings
    for section in sections:
        sections[section] = "\n".join(sections[section]).strip()

    return sections


# ============================================================
# BASIC INFORMATION EXTRACTION
# ============================================================

def extract_email(text):
    """Find an email address."""

    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    match = re.search(pattern, text)

    return match.group(0) if match else None


def extract_phone(text):
    """Find an Indian-style phone number."""

    patterns = [
        r"\+91[\s-]?[6-9]\d{9}",
        r"\b[6-9]\d{9}\b",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            return match.group(0)

    return None


def extract_linkedin(text):
    """Find a LinkedIn profile URL."""

    pattern = r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

    match = re.search(pattern, text, re.IGNORECASE)

    return match.group(0) if match else None


def extract_github(text):
    """Find a GitHub profile URL."""

    pattern = r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+"

    match = re.search(pattern, text, re.IGNORECASE)

    return match.group(0) if match else None


# ============================================================
# SKILL EXTRACTION
# ============================================================

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
    "tableau",
]


def extract_skills(text):
    """Find known technical skills in resume text."""

    text_lower = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:

        # Escape special characters such as C++
        escaped_skill = re.escape(skill.lower())

        pattern = rf"(?<!\w){escaped_skill}(?!\w)"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return sorted(set(found_skills))


# ============================================================
# EXPERIENCE EXTRACTION
# ============================================================

def extract_years_of_experience(text):
    """
    Estimate years of experience from phrases such as:

    2 years experience
    3+ years of experience
    1 year experience
    """

    patterns = [
        r"(\d+)\+?\s*years?\s+(?:of\s+)?experience",
        r"experience\s*[:\-]?\s*(\d+)\+?\s*years?",
    ]

    for pattern in patterns:

        matches = re.findall(pattern, text.lower())

        if matches:
            try:
                return max(int(value) for value in matches)
            except ValueError:
                pass

    return 0


# ============================================================
# COMPLETE RESUME PARSER
# ============================================================

def parse_resume(file_path):
    """
    Complete resume parsing function.

    Returns structured resume information.
    """

    text = extract_text(file_path)

    sections = extract_sections(text)

    resume_data = {
        "file_name": Path(file_path).name,
        "raw_text": text,
        "email": extract_email(text),
        "phone": extract_phone(text),
        "linkedin": extract_linkedin(text),
        "github": extract_github(text),
        "skills": extract_skills(text),
        "years_of_experience": extract_years_of_experience(text),
        "sections": sections,
    }

    return resume_data


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("ADVANCED RESUME PARSER")
    print("=" * 60)

    file_path = input("\nEnter resume file path: ").strip()

    try:

        resume = parse_resume(file_path)

        print("\nResume parsed successfully!\n")

        print("File:", resume["file_name"])
        print("Email:", resume["email"])
        print("Phone:", resume["phone"])
        print("LinkedIn:", resume["linkedin"])
        print("GitHub:", resume["github"])
        print("Experience:", resume["years_of_experience"], "years")

        print("\nDetected Skills:")
        for skill in resume["skills"]:
            print(" -", skill)

        print("\nDetected Sections:")

        for section, content in resume["sections"].items():

            if content:
                print(f"\n[{section.upper()}]")
                print(content[:500])

    except Exception as error:

        print("\nError:", error)
