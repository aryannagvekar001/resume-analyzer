import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

from praser import ParserError, parse_resume


class UploadView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")
        self._build_ui()

    def _build_ui(self):
        tk.Label(
            self,
            text="Upload Resume",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa",
            fg="#172033",
        ).pack(anchor="w", padx=30, pady=(30, 8))

        tk.Label(
            self,
            text="Upload your resume in PDF, DOCX, or TXT format.",
            font=("Arial", 12),
            bg="#f5f6fa",
            fg="#64748b",
        ).pack(anchor="w", padx=30, pady=(0, 20))

        card = tk.Frame(self, bg="white", bd=1, relief="solid")
        card.pack(fill="x", padx=30, pady=5)

        tk.Label(
            card,
            text="Select your resume\nSupported formats: PDF, DOCX, TXT",
            font=("Arial", 14),
            bg="white",
            fg="#64748b",
            justify="center",
        ).pack(pady=(30, 16))

        tk.Button(
            card,
            text="Choose Resume",
            command=self.choose_resume,
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            padx=18,
            pady=10,
            cursor="hand2",
        ).pack(pady=(0, 30))

        self.file_label = tk.Label(
            self,
            text="No resume selected",
            font=("Arial", 11),
            bg="#f5f6fa",
            fg="#64748b",
        )
        self.file_label.pack(anchor="w", padx=30, pady=(12, 8))

        tk.Label(
            self,
            text="Resume Preview",
            font=("Arial", 18, "bold"),
            bg="#f5f6fa",
            fg="#172033",
        ).pack(anchor="w", padx=30, pady=(10, 6))

        self.resume_text = tk.Text(
            self,
            font=("Arial", 11),
            height=16,
            wrap="word",
        )
        self.resume_text.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 30),
        )
        self.file_label.pack(anchor="w", padx=30, pady=(12, 8))

    def choose_resume(self):
        file_path = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=[
                ("Resume files", "*.pdf *.docx *.txt"),
                ("PDF files", "*.pdf"),
                ("Word documents", "*.docx"),
                ("Text files", "*.txt"),
            ],
        )

        if not file_path:
            return

        try:
            resume = parse_resume(file_path)
        except ParserError as error:
            messagebox.showerror(
                "Unable to parse resume",
                str(error),
                parent=self.winfo_toplevel(),
            )
            return

        path = Path(file_path)

        self.file_label.config(text=f"Selected: {path.name}")
        self.resume_text.delete("1.0", tk.END)
        self.resume_text.insert("1.0", resume["text"])

        # Stored for future analysis, ATS, skills, and suggestions views.
        self.winfo_toplevel().current_resume = resume
