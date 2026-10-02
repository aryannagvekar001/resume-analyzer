class ResumeVersions:

    def __init__(self):
        self.versions = []

    def add(self, name, resume_text):
        version = {
            "id": len(self.versions) + 1,
            "name": name,
            "text": resume_text,
        }

        self.versions.append(version)

        return version

    def all(self):
        return list(self.versions)

    def get(self, version_id):
        for version in self.versions:
            if version["id"] == version_id:
                return version

        return None
