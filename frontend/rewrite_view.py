import tkinter as tk


class RewriteView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Rewrite Resume",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(pady=30)

        tk.Label(
            self,
            text="Enter text you want to improve:",
            font=("Arial", 13),
            bg="#f5f6fa"
        ).pack()

        self.input_box = tk.Text(
            self,
            height=8,
            width=80
        )
        self.input_box.pack(pady=15)

        tk.Button(
            self,
            text="Improve Text",
            command=self.rewrite,
            font=("Arial", 12),
            padx=20,
            pady=8
        ).pack()

        self.output_box = tk.Text(
            self,
            height=8,
            width=80
        )
        self.output_box.pack(pady=20)

    def rewrite(self):

        text = self.input_box.get("1.0", "end").strip()

        if not text:
            return

        improved = (
            "Improved Version:\n\n"
            + text
            + "\n\n"
            "Tip: Add measurable results and strong action verbs."
        )

        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", improved)