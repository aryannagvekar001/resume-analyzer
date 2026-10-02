class BulletAnalyzer:
    def analyze(self,text): return {"count":sum(x.strip().startswith(("-","*","•")) for x in (text or "").splitlines())}
