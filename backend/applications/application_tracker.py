from datetime import datetime
class ApplicationTracker:
    def __init__(self): self.applications=[]
    def add(self,company,role,status="Applied",resume_version="default"):
        x={"id":len(self.applications)+1,"company":company,"role":role,"status":status,"resume_version":resume_version,"created_at":datetime.now().isoformat(timespec="seconds")}; self.applications.append(x); return x
    def all(self): return list(self.applications)
