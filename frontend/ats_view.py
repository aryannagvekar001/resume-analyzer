import tkinter as tk


class ATSView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="ATS Score",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(pady=40)

        tk.Label(
            self,
            text="78 / 100",
            font=("Arial", 50, "bold"),
            bg="#f5f6fa"
        ).pack(pady=20)

        tk.Label(
            self,
            text="Your resume is compatible with most ATS systems.",
            font=("Arial", 13),
            bg="#f5f6fa"
        ).pack()