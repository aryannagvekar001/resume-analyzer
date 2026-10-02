from collections import Counter


class ApplicationAnalytics:

    def summarize(self, applications):
        applications = applications or []

        statuses = Counter(
            item.get("status", "Unknown")
            for item in applications
        )

        total = len(applications)

        interviews = sum(
            statuses.get(status, 0)
            for status in (
                "Interview",
                "Offer",
            )
        )

        offers = statuses.get("Offer", 0)

        return {
            "total": total,
            "by_status": dict(statuses),
            "interview_rate": round(
                interviews / total * 100,
                2,
            ) if total else 0,
            "offer_rate": round(
                offers / total * 100,
                2,
            ) if total else 0,
        }