import tkinter as tk


class Dashboard(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Dashboard",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(anchor="w", padx=30, pady=(30, 5))

        tk.Label(
            self,
            text="Welcome to AI Resume Analyzer",
            font=("Arial", 14),
            bg="#f5f6fa"
        ).pack(anchor="w", padx=30)

        cards = tk.Frame(self, bg="#f5f6fa")
        cards.pack(fill="x", padx=30, pady=40)

        self.create_card(cards, "Resume Score", "85%", 0)
        self.create_card(cards, "ATS Score", "78%", 1)
        self.create_card(cards, "Skills Found", "24", 2)
        self.create_card(cards, "Job Matches", "12", 3)

    def create_card(self, parent, title, value, column):

        card = tk.Frame(
            parent,
            bg="white",
            width=190,
            height=130,
            bd=1,
            relief="solid"
        )

        card.grid(
            row=0,
            column=column,
            padx=10,
            sticky="nsew"
        )

        parent.grid_columnconfigure(column, weight=1)

        tk.Label(
            card,
            text=title,
            font=("Arial", 12),
            bg="white"
        ).pack(pady=(25, 5))

        tk.Label(
            card,
            text=value,
            font=("Arial", 25, "bold"),
            bg="white"
        ).pack()