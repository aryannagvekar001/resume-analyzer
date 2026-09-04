import tkinter as tk
from tkinter import messagebox


class SettingsView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f5f6fa")

        tk.Label(
            self,
            text="Settings",
            font=("Arial", 28, "bold"),
            bg="#f5f6fa"
        ).pack(anchor="w", padx=30, pady=30)

        self.dark_mode = tk.BooleanVar(value=False)

        tk.Checkbutton(
            self,
            text="Dark Mode",
            variable=self.dark_mode,
            command=self.toggle_dark_mode,
            font=("Arial", 13),
            bg="#f5f6fa"
        ).pack(anchor="w", padx=50, pady=10)

        tk.Button(
            self,
            text="Save Settings",
            command=self.save_settings,
            font=("Arial", 12),
            padx=20,
            pady=8
        ).pack(pady=30)

    def toggle_dark_mode(self):

        if self.dark_mode.get():
            self.configure(bg="#20232a")
        else:
            self.configure(bg="#f5f6fa")

    def save_settings(self):

        messagebox.showinfo(
            "Settings",
            "Settings saved successfully!"
        )