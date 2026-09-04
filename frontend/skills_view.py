import tkinter as tk


class SkillsView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Skills",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(anchor="w", padx=30, pady=30)

        skills = [
            "Python",
            "Machine Learning",
            "Artificial Intelligence",
            "SQL",
            "Java",
            "Git",
            "Data Structures",
            "Pandas",
            "NumPy",
            "Communication"
        ]

        for skill in skills:
            tk.Label(
                self,
                text="✓ " + skill,
                font=("Arial", 13),
                bg="#f5f6fa",
                anchor="w"
            ).pack(anchor="w", padx=50, pady=5)