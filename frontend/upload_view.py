import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox


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

        self.resume_text = tk.Text(self, font=("Arial", 11), height=16, wrap="word")
        self.resume_text.pack(fill="both", expand=True, padx=30, pady=(0, 30))

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

        path = Path(file_path)
        self.file_label.config(text=f"Selected: {path.name}")
        self.resume_text.delete("1.0", tk.END)

        if path.suffix.lower() == ".txt":
            try:
                self.resume_text.insert("1.0", path.read_text(encoding="utf-8"))
                return
            except UnicodeDecodeError:
                self.resume_text.insert(
                    "1.0",
                    path.read_text(encoding="latin-1"),
                )
                return
            except OSError as error:
                messagebox.showerror("Unable to read resume", str(error))
                return

        self.resume_text.insert(
            "1.0",
            f"Resume selected successfully.\n\nFile: {path}\n\n"
            "PDF and DOCX text extraction will be connected to the analyzer backend.",
        )
