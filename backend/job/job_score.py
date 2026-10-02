class JobScore:
    def calculate(self,matched,total): return round(matched/total*100) if total else 0
