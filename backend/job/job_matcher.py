class JobMatcher:
    def match(self,resume_text,job_description):
        a=set((resume_text or "").lower().split()); b=set((job_description or "").lower().split()); m=a&b
        return {"score":round(len(m)/len(b)*100) if b else 0,"matched_keywords":sorted(m),"missing_keywords":sorted(b-a)}
