import tkinter as tk
from tkinter import messagebox

from backend.analysis.ats.ats_analyzer import ATSAnalyzer


class ATSView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")
        self.analyzer = ATSAnalyzer()
        self._build_ui()

    def _build_ui(self):
        tk.Label(
            self,
            text="ATS Score",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa",
            fg="#172033",
        ).pack(anchor="w", padx=30, pady=(30, 8))

        tk.Label(
            self,
            text="Upload a resume, paste a job description, then run the ATS check.",
            font=("Arial", 12),
            bg="#f5f6fa",
            fg="#64748b",
        ).pack(anchor="w", padx=30, pady=(0, 15))

        tk.Label(
            self,
            text="Job Description",
            font=("Arial", 14, "bold"),
            bg="#f5f6fa",
            fg="#172033",
        ).pack(anchor="w", padx=30)

        self.job_description = tk.Text(
            self,
            height=8,
            font=("Arial", 11),
            wrap="word",
        )
        self.job_description.pack(fill="x", padx=30, pady=(6, 14))

        tk.Button(
            self,
            text="Analyze ATS Compatibility",
            command=self.analyze_ats,
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            padx=18,
            pady=10,
            cursor="hand2",
        ).pack(anchor="w", padx=30, pady=(0, 18))

        self.score_label = tk.Label(
            self,
            text="Upload a resume to begin",
            font=("Arial", 24, "bold"),
            bg="#f5f6fa",
            fg="#172033",
        )
        self.score_label.pack(anchor="w", padx=30, pady=(0, 8))

        self.compatibility_label = tk.Label(
            self,
            text="",
            font=("Arial", 13),
            bg="#f5f6fa",
            fg="#475569",
        )
        self.compatibility_label.pack(anchor="w", padx=30)

        self.results = tk.Text(
            self,
            height=14,
            font=("Arial", 11),
            wrap="word",
            state="disabled",
        )
        self.results.pack(fill="both", expand=True, padx=30, pady=(15, 30))

    def analyze_ats(self):
        app = self.winfo_toplevel()
        resume = getattr(app, "current_resume", None)

        if not resume or not resume.get("text", "").strip():
            messagebox.showwarning(
                "Resume required",
                "Please upload a resume before running the ATS check.",
                parent=app,
            )
            return

        job_description = self.job_description.get("1.0", tk.END).strip()

        if not job_description:
            messagebox.showwarning(
                "Job description required",
                "Paste the job description to calculate an ATS match score.",
                parent=app,
            )
            return

        result = self.analyzer.analyze(resume["text"], job_description)

        ats_score = result["ats_score"]
        compatibility = result["compatibility"]
        risks = result["risks"]

        self.score_label.config(
            text=f'{compatibility["score"]} / 100'
        )
        self.compatibility_label.config(
            text=compatibility["label"]
        )

        risks_text = "\n".join(
            f'- [{risk["level"].upper()}] {risk["message"]}'
            for risk in risks
        ) or "- No ATS risks detected."

        matched_keywords = ", ".join(
            ats_score["matched_keywords"]
        ) or "None"

        missing_keywords = ", ".join(
            ats_score["missing_keywords"]
        ) or "None"

        output = (
            f"Matched keywords:\n{matched_keywords}\n\n"
            f"Missing keywords:\n{missing_keywords}\n\n"
            f"ATS risks:\n{risks_text}\n\n"
            f"Recommendation:\n{compatibility['recommendation']}"
        )

        self.results.config(state="normal")
        self.results.delete("1.0", tk.END)
        self.results.insert("1.0", output)
        self.results.config(state="disabled")