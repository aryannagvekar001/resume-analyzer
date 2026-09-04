import tkinter as tk


class SuggestionsView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Resume Suggestions",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(anchor="w", padx=30, pady=30)

        suggestions = [
            "Add more measurable achievements.",
            "Improve your professional summary.",
            "Add relevant technical keywords.",
            "Include links to your GitHub projects.",
            "Use action verbs in your experience section.",
            "Keep your resume between 1–2 pages."
        ]

        for suggestion in suggestions:
            tk.Label(
                self,
                text="• " + suggestion,
                font=("Arial", 13),
                bg="#f5f6fa"
            ).pack(anchor="w", padx=50, pady=8) 