class RequirementExtractor:
    def extract(self,text): return {"requirements":[x.strip() for x in (text or "").splitlines() if x.strip()]}
