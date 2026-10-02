class PriorityEngine:

    def prioritize(self, recommendations):
        if not recommendations:
            return []

        high_words = (
            "missing",
            "remove",
            "add",
            "ats",
            "contact",
        )

        high = []
        normal = []

        for recommendation in recommendations:
            item = recommendation.strip()

            if any(
                word in item.lower()
                for word in high_words
            ):
                high.append(item)
            else:
                normal.append(item)

        return high + normal