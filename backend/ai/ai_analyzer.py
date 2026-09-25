from .model_manager import ModelManager
from .prompt_manager import PromptManager
from .response_parser import ResponseParser


class AIAnalyzer:
    def __init__(self):
        self.model = ModelManager()
        self.prompts = PromptManager()
        self.parser = ResponseParser()

    def improve_resume(self, text):
        response = self.model.generate(
            self.prompts.improve_resume(text)
        )

        return self.parser.clean(response)

    def summarize(self, text):
        response = self.model.generate(
            self.prompts.summarize(text)
        )

        return self.parser.clean(response)

    def tailor(self, text, job_description):
        response = self.model.generate(
            self.prompts.tailor(
                text,
                job_description,
            )
        )

        return self.parser.clean(response)

    def recommendations(self, text):
        response = self.model.generate(
            self.prompts.recommendations(text)
        )

        return self.parser.bullets(response)