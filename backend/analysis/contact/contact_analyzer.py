import re
class ContactAnalyzer:
    def analyze(self,text): return {"email":bool(re.search(r"[\\w.+-]+@[\\w-]+\\.[\\w.-]+",text or "")),"phone":bool(re.search(r"\\+?\\d[\\d\\s().-]{7,}\\d",text or ""))}
