class LinkValidator:
    def validate(self,links): return {"linkedin":any("linkedin.com/" in x.lower() for x in links or []),"github":any("github.com/" in x.lower() for x in links or [])}
