class ResumeVersions:
    def __init__(self): self.versions=[]
    def add(self,name,text): x={"id":len(self.versions)+1,"name":name,"text":text}; self.versions.append(x); return x
    def all(self): return list(self.versions)
