import tkinter as tk


class ProfileView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="My Profile",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(pady=30)

        fields = ["Name", "Email", "Phone", "Career Goal"]

        self.entries = {}

        for field in fields:

            row = tk.Frame(self, bg="#f5f6fa")
            row.pack(pady=8)

            tk.Label(
                row,
                text=field,
                width=15,
                anchor="w",
                font=("Arial", 12),
                bg="#f5f6fa"
            ).pack(side="left")

            entry = tk.Entry(
                row,
                width=40,
                font=("Arial", 12)
            )
            entry.pack(side="left")

            self.entries[field] = entry

        tk.Button(
            self,
            text="Save Profile",
            command=self.save_profile,
            font=("Arial", 12),
            padx=20,
            pady=8
        ).pack(pady=20)

    def save_profile(self):

        print("Profile saved.")

        for field, entry in self.entries.items():
            print(field, ":", entry.get())