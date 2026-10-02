class ApplicationStatus:
    STATUSES=("Saved","Applied","Screening","Interview","Offer","Rejected","Withdrawn")
    @classmethod
    def valid(cls,status): return status in cls.STATUSES
