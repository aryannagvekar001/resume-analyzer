class StructureAnalyzer:
    def analyze(self,text): return {"sections_found":[x for x in ("summary","experience","education","skills","projects") if x in (text or "").lower()]}
