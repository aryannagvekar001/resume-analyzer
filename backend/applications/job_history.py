class JobHistory:
    def __init__(self): self.history=[]
    def add(self,company,role,outcome): x={"company":company,"role":role,"outcome":outcome}; self.history.append(x); return x
    def all(self): return list(self.history)
