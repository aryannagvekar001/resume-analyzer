import tkinter as tk


class CareerView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Career Suggestions",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(pady=30)

        careers = [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Python Developer",
            "Data Analyst",
            "Software Engineer"
        ]

        for career in careers:
            tk.Label(
                self,
                text="→ " + career,
                font=("Arial", 14),
                bg="#f5f6fa"
            ).pack(anchor="w", padx=60, pady=8)