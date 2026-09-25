from .model_manager import ModelManager
from .prompt_manager import PromptManager
from .response_parser import ResponseParser
class AIAnalyzer:
    def __init__(self): self.model=ModelManager(); self.prompts=PromptManager(); self.parser=ResponseParser()
    def improve_resume(self,text): return self.parser.clean(self.model.generate(self.prompts.improve_resume(text)))
    def summarize(self,text): return self.parser.clean(self.model.generate(self.prompts.summarize(text)))
    def tailor(self,text,job): return self.parser.clean(self.model.generate(self.prompts.tailor(text,job)))
    def recommendations(self,text): return self.parser.bullets(self.model.generate(self.prompts.recommendations(text)))
