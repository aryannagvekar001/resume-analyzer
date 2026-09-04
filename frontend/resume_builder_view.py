import tkinter as tk


class ResumeBuilderView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Resume Builder",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(pady=30)

        form = tk.Frame(self, bg="#f5f6fa")
        form.pack(pady=10)

        fields = [
            "Full Name",
            "Email",
            "Phone",
            "Education",
            "Skills",
            "Projects"
        ]

        self.entries = {}

        for i, field in enumerate(fields):

            tk.Label(
                form,
                text=field,
                font=("Arial", 12),
                bg="#f5f6fa"
            ).grid(row=i, column=0, padx=10, pady=8, sticky="w")

            entry = tk.Entry(
                form,
                width=50,
                font=("Arial", 12)
            )
            entry.grid(row=i, column=1, padx=10, pady=8)

            self.entries[field] = entry

        tk.Button(
            self,
            text="Create Resume",
            command=self.create_resume,
            font=("Arial", 12),
            padx=20,
            pady=8
        ).pack(pady=20)

    def create_resume(self):

        print("Resume created successfully.")

        for field, entry in self.entries.items():
            print(field + ":", entry.get())