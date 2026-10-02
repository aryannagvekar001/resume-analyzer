from collections import Counter
class ApplicationAnalytics:
    def summarize(self,applications):
        c=Counter(x.get("status","Unknown") for x in applications or []); return {"total":sum(c.values()),"by_status":dict(c)}
