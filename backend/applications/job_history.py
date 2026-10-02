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
<<<<<<< HEAD
        return list(self.history)
=======
        return list(self.history)
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
