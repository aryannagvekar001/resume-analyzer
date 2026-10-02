class ProjectRelevance:

    def calculate(self, project_text, job_description):
        project_words = set(
            (project_text or "").lower().split()
        )

        job_words = set(
            (job_description or "").lower().split()
        )

        if not job_words:
            return 0

        return round(
            len(project_words & job_words)
            / len(job_words)
            * 100
        )