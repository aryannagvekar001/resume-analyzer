import tkinter as tk


class JobMatchView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Job Match",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(anchor="w", padx=30, pady=30)

        jobs = [
            ("Python Developer", "92%"),
            ("Machine Learning Intern", "88%"),
            ("AI Engineer Intern", "82%"),
            ("Data Analyst", "76%"),
            ("Software Developer", "71%")
        ]

        for job, score in jobs:

            frame = tk.Frame(
                self,
                bg="white",
                bd=1,
                relief="solid"
            )
            frame.pack(fill="x", padx=30, pady=7)

            tk.Label(
                frame,
                text=job,
                font=("Arial", 13, "bold"),
                bg="white"
            ).pack(side="left", padx=15, pady=15)

            tk.Label(
                frame,
                text=f"Match: {score}",
                font=("Arial", 12),
                bg="white"
            ).pack(side="right", padx=15)