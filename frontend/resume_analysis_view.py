import tkinter as tk


class ResumeAnalysisView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Resume Analysis",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(anchor="w", padx=30, pady=30)

        analysis = tk.Text(
            self,
            font=("Arial", 12),
            height=20,
            width=80
        )
        analysis.pack(padx=30, pady=10)

        analysis.insert(
            "1.0",
            "Resume Analysis\n\n"
            "Overall Resume Score: 85/100\n\n"
            "Strengths:\n"
            "• Good technical skills\n"
            "• Clear education section\n"
            "• Good project experience\n\n"
            "Areas to improve:\n"
            "• Add measurable achievements\n"
            "• Improve summary section\n"
            "• Add more keywords"
        )

        analysis.config(state="disabled")