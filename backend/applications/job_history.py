class JobHistory:

    def __init__(self):
        self.history = []

    def add(self, company, role, outcome):
        item = {
            "company": company,
            "role": role,
            "outcome": outcome,
        }

        self.history.append(item)

        return item

    def all(self):
        return list(self.history)
