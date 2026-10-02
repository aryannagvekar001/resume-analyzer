class ApplicationStatus:

    STATUSES = (
        "Saved",
        "Applied",
        "Screening",
        "Interview",
        "Offer",
        "Rejected",
        "Withdrawn",
    )

    @classmethod
    def valid(cls, status):
        return status in cls.STATUSES

    @classmethod
    def normalize(cls, status):
        if not status:
            return "Saved"

        for item in cls.STATUSES:
            if item.lower() == status.lower():
                return item

<<<<<<< HEAD
        return "Saved"
=======
        return "Saved"
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
