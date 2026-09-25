import os

from dotenv import load_dotenv

load_dotenv()


class ModelManager:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model_name = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash",
        )
        self.client = None

        if self.api_key:
            try:
                from google import genai

                self.client = genai.Client(
                    api_key=self.api_key
                )
            except Exception:
                self.client = None

    def generate(self, prompt):
        if not self.client:
            return ""

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )

            return (response.text or "").strip()

        except Exception:
            return ""

    def available(self):
        return self.client is not None
