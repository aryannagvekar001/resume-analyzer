import tkinter as tk


class InterviewView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="AI Interview Practice",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(pady=30)

        self.question = tk.Label(
            self,
            text="Question 1:\nTell me about yourself.",
            font=("Arial", 16),
            bg="#f5f6fa"
        )
        self.question.pack(pady=30)

        self.answer = tk.Text(
            self,
            height=8,
            width=70
        )
        self.answer.pack()

        tk.Button(
            self,
            text="Submit Answer",
            command=self.submit,
            font=("Arial", 12),
            padx=20,
            pady=8
        ).pack(pady=20)

        self.feedback = tk.Label(
            self,
            text="",
            font=("Arial", 12),
            bg="#f5f6fa"
        )
        self.feedback.pack()

    def submit(self):

        answer = self.answer.get("1.0", "end").strip()

        if answer:
            self.feedback.config(
                text="Good attempt! Try to include your skills, education and career goals."
            )