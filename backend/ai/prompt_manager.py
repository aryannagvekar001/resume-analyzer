class PromptManager:
    @staticmethod
    def improve_resume(text): return f"Improve this resume without inventing facts:\n{text}"
    @staticmethod
    def summarize(text): return f"Write a concise professional resume summary without inventing facts:\n{text}"
    @staticmethod
    def tailor(text,job): return f"Tailor this resume to the job. Keep facts truthful.\nRESUME:\n{text}\nJOB:\n{job}"
    @staticmethod
    def recommendations(text): return f"Give practical resume improvement recommendations. Do not invent facts.\n{text}"
