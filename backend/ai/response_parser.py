import re
class ResponseParser:
    @staticmethod
    def clean(text): return re.sub(r"```$","",re.sub(r"^```(?:text|markdown)?","",(text or "").strip(),flags=re.I)).strip()
    @staticmethod
    def bullets(text): return [re.sub(r"^[-*•]\s*","",x.strip()) for x in (text or "").splitlines() if x.strip()]
