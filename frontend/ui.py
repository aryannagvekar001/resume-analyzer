import tkinter as tk
from tkinter import ttk

from frontend.dashboard import Dashboard
from frontend.upload_view import UploadView
from frontend.resume_analysis_view import ResumeAnalysisView
from frontend.ats_view import ATSView
from frontend.skills_view import SkillsView
from frontend.job_match_view import JobMatchView
from frontend.suggestions_view import SuggestionsView
from frontend.rewrite_view import RewriteView
from frontend.resume_builder_view import ResumeBuilderView
from frontend.interview_view import InterviewView
from frontend.career_view import CareerView
from frontend.profile_view import ProfileView
from frontend.application_tracker_view import ApplicationTrackerView
from frontend.settings_view import SettingsView


class ResumeAnalyzerApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("AI Resume Analyzer")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        self.configure(bg="#f5f6fa")

        self.create_layout()
        self.show_dashboard()

    def create_layout(self):

        # Sidebar
        self.sidebar = tk.Frame(
            self,
            bg="#20232a",
            width=230
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        title = tk.Label(
            self.sidebar,
            text="AI Resume\nAnalyzer",
            font=("Arial", 20, "bold"),
            bg="#20232a",
            fg="white"
        )
        title.pack(pady=25)

        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Upload Resume", self.show_upload),
            ("Resume Analysis", self.show_analysis),
            ("ATS Score", self.show_ats),
            ("Skills", self.show_skills),
            ("Job Match", self.show_job_match),
            ("Suggestions", self.show_suggestions),
            ("Rewrite Resume", self.show_rewrite),
            ("Resume Builder", self.show_builder),
            ("Interview", self.show_interview),
            ("Career", self.show_career),
            ("Profile", self.show_profile),
            ("Applications", self.show_applications),
            ("Settings", self.show_settings),
        ]

        for text, command in buttons:
            btn = tk.Button(
                self.sidebar,
                text=text,
                command=command,
                font=("Arial", 11),
                bg="#2c3038",
                fg="white",
                activebackground="#4b5260",
                activeforeground="white",
                relief="flat",
                anchor="w",
                padx=20,
                pady=9,
                cursor="hand2"
            )
            btn.pack(fill="x", padx=10, pady=2)

        # Main area
        self.main_area = tk.Frame(
            self,
            bg="#f5f6fa"
        )
        self.main_area.pack(
            side="right",
            fill="both",
            expand=True
        )

    def clear_screen(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

    def show_view(self, view_class):
        self.clear_screen()
        view = view_class(self.main_area)
        view.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.show_view(Dashboard)

    def show_upload(self):
        self.show_view(UploadView)

    def show_analysis(self):
        self.show_view(ResumeAnalysisView)

    def show_ats(self):
        self.show_view(ATSView)

    def show_skills(self):
        self.show_view(SkillsView)

    def show_job_match(self):
        self.show_view(JobMatchView)

    def show_suggestions(self):
        self.show_view(SuggestionsView)

    def show_rewrite(self):
        self.show_view(RewriteView)

    def show_builder(self):
        self.show_view(ResumeBuilderView)

    def show_interview(self):
        self.show_view(InterviewView)

    def show_career(self):
        self.show_view(CareerView)

    def show_profile(self):
        self.show_view(ProfileView)

    def show_applications(self):
        self.show_view(ApplicationTrackerView)

    def show_settings(self):
        self.show_view(SettingsView)