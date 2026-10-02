from datetime import datetime


class ApplicationTracker:

    def __init__(self):
        self.applications = []

    def add(
        self,
        company,
        role,
        status="Applied",
        resume_version="default",
    ):
        application = {
            "id": len(self.applications) + 1,
            "company": company,
            "role": role,
            "status": status,
            "resume_version": resume_version,
            "created_at": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.applications.append(application)

        return application

    def all(self):
        return list(self.applications)

    def update_status(self, application_id, status):
        for application in self.applications:
            if application["id"] == application_id:
                application["status"] = status
                return application

        return None

    def remove(self, application_id):
        before = len(self.applications)

        self.applications = [
            item
            for item in self.applications
            if item["id"] != application_id
        ]

<<<<<<< HEAD
        return len(self.applications) < before
=======
        return len(self.applications) < before
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
