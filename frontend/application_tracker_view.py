import tkinter as tk


class ApplicationTrackerView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Application Tracker",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(pady=30)

        columns = ("Company", "Job", "Status")

        self.table = tk.Frame(self, bg="white")
        self.table.pack(fill="x", padx=30)

        for i, column in enumerate(columns):

            tk.Label(
                self.table,
                text=column,
                font=("Arial", 12, "bold"),
                bg="white",
                width=25
            ).grid(row=0, column=i, padx=5, pady=10)

        data = [
            ("Google", "Python Intern", "Applied"),
            ("Microsoft", "AI Intern", "Interview"),
            ("TCS", "Software Engineer", "Applied"),
            ("Infosys", "Data Analyst", "Selected")
        ]

        for row, item in enumerate(data, start=1):

            for col, value in enumerate(item):

                tk.Label(
                    self.table,
                    text=value,
                    bg="white",
                    width=25
                ).grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=8
                )