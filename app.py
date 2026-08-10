import customtkinter as ctk

from tkinter import filedialog, messagebox

from backhand.resume_parser import parse_resume

from backhand.analyzer import analyze_resume

from backhand.ai_analyzer import analyze_with_gemini


# ============================================================
# APPLICATION SETTINGS
# ============================================================

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")


# ============================================================
# MAIN APPLICATION
# ============================================================

class ResumeAnalyzerApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        # Window
        self.title(
            "ResumeAI - AI Resume Analyzer"
        )

        self.geometry(
            "1250x850"
        )

        self.minsize(
            1000,
            700
        )


        # Variables
        self.resume_path = None

        self.resume_data = None

        self.analysis = None


        # Build UI
        self.create_sidebar()

        self.create_main_area()


    # ========================================================
    # SIDEBAR
    # ========================================================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=230,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # Logo
        logo = ctk.CTkLabel(

            self.sidebar,

            text="📄 ResumeAI",

            font=ctk.CTkFont(
                size=25,
                weight="bold"
            )

        )

        logo.pack(
            pady=(35, 5)
        )


        subtitle = ctk.CTkLabel(

            self.sidebar,

            text="AI Resume Analyzer",

            text_color="gray"

        )

        subtitle.pack(
            pady=(0, 35)
        )


        # Navigation buttons
        buttons = [

            "🏠 Dashboard",

            "📊 Analysis",

            "🧠 Skills",

            "🔑 Keywords",

            "🤖 AI Feedback"

        ]


        for text in buttons:

            button = ctk.CTkButton(

                self.sidebar,

                text=text,

                height=42,

                anchor="w",

                fg_color="transparent",

                hover_color="#1f2937",

                command=lambda value=text:
                    self.navigation_click(value)

            )

            button.pack(
                padx=15,
                pady=5,
                fill="x"
            )


        # Bottom information
        info = ctk.CTkLabel(

            self.sidebar,

            text=(
                "ResumeAI\n\n"
                "PDF • DOCX\n"
                "ATS Analysis\n"
                "Gemini AI"
            ),

            text_color="gray",

            justify="left"

        )

        info.pack(
            side="bottom",
            padx=20,
            pady=30
        )


    # ========================================================
    # MAIN AREA
    # ========================================================

    def create_main_area(self):

        self.main = ctk.CTkFrame(

            self,

            corner_radius=0,

            fg_color="#111827"

        )

        self.main.pack(

            side="left",

            fill="both",

            expand=True

        )


        # Header
        header = ctk.CTkFrame(

            self.main,

            fg_color="transparent"

        )

        header.pack(

            fill="x",

            padx=35,

            pady=(30, 10)

        )


        title = ctk.CTkLabel(

            header,

            text="Resume Analyzer",

            font=ctk.CTkFont(

                size=32,

                weight="bold"

            )

        )

        title.pack(
            anchor="w"
        )


        self.status_label = ctk.CTkLabel(

            header,

            text="Upload your resume to begin.",

            text_color="gray"

        )

        self.status_label.pack(
            anchor="w",
            pady=(5, 0)
        )


        # Scrollable area
        self.content = ctk.CTkScrollableFrame(

            self.main

        )

        self.content.pack(

            fill="both",

            expand=True,

            padx=30,

            pady=20

        )


        self.create_upload_section()

        self.create_job_section()

        self.create_analyze_button()

        self.create_results_section()


    # ========================================================
    # UPLOAD SECTION
    # ========================================================

    def create_upload_section(self):

        card = ctk.CTkFrame(
            self.content
        )

        card.pack(
            fill="x",
            pady=10
        )


        title = ctk.CTkLabel(

            card,

            text="📎 Resume",

            font=ctk.CTkFont(

                size=20,

                weight="bold"

            )

        )

        title.pack(

            anchor="w",

            padx=25,

            pady=(20, 5)

        )


        self.file_label = ctk.CTkLabel(

            card,

            text="No resume selected",

            text_color="gray"

        )

        self.file_label.pack(

            anchor="w",

            padx=25,

            pady=10

        )


        browse_button = ctk.CTkButton(

            card,

            text="Choose Resume",

            command=self.select_resume

        )

        browse_button.pack(

            anchor="w",

            padx=25,

            pady=(5, 20)

        )


    # ========================================================
    # JOB DESCRIPTION
    # ========================================================

    def create_job_section(self):

        card = ctk.CTkFrame(

            self.content

        )

        card.pack(

            fill="x",

            pady=10

        )


        title = ctk.CTkLabel(

            card,

            text="💼 Job Description",

            font=ctk.CTkFont(

                size=20,

                weight="bold"

            )

        )

        title.pack(

            anchor="w",

            padx=25,

            pady=(20, 10)

        )


        self.job_text = ctk.CTkTextbox(

            card,

            height=180

        )

        self.job_text.pack(

            fill="x",

            padx=25,

            pady=(0, 20)

        )


    # ========================================================
    # ANALYZE BUTTON
    # ========================================================

    def create_analyze_button(self):

        self.analyze_button = ctk.CTkButton(

            self.content,

            text="🚀 ANALYZE RESUME",

            height=55,

            font=ctk.CTkFont(

                size=17,

                weight="bold"

            ),

            command=self.run_analysis

        )

        self.analyze_button.pack(

            fill="x",

            pady=20

        )


    # ========================================================
    # RESULTS SECTION
    # ========================================================

    def create_results_section(self):

        self.results_frame = ctk.CTkFrame(

            self.content

        )

        self.results_frame.pack(

            fill="both",

            expand=True,

            pady=10

        )


        title = ctk.CTkLabel(

            self.results_frame,

            text="📊 Analysis Results",

            font=ctk.CTkFont(

                size=22,

                weight="bold"

            )

        )

        title.pack(

            anchor="w",

            padx=25,

            pady=20

        )


        # Score
        self.score_label = ctk.CTkLabel(

            self.results_frame,

            text="--",

            font=ctk.CTkFont(

                size=50,

                weight="bold"

            )

        )

        self.score_label.pack(
            pady=10
        )


        # Progress bar
        self.score_progress = ctk.CTkProgressBar(

            self.results_frame,

            width=500

        )

        self.score_progress.pack(
            pady=10
        )

        self.score_progress.set(0)


        # Score details
        self.score_details = ctk.CTkLabel(

            self.results_frame,

            text="Run analysis to see results.",

            justify="left",

            font=ctk.CTkFont(
                size=15
            )

        )

        self.score_details.pack(

            anchor="w",

            padx=25,

            pady=20

        )


        # Tabs
        self.tabview = ctk.CTkTabview(

            self.results_frame

        )

        self.tabview.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20

        )


        self.tabview.add("🧠 Skills")

        self.tabview.add("🔑 Keywords")

        self.tabview.add("📋 Sections")

        self.tabview.add("💡 Suggestions")

        self.tabview.add("🤖 AI Feedback")


        # Text widgets
        self.skills_text = self.create_result_textbox(
            "🧠 Skills"
        )

        self.keywords_text = self.create_result_textbox(
            "🔑 Keywords"
        )

        self.sections_text = self.create_result_textbox(
            "📋 Sections"
        )

        self.suggestions_text = self.create_result_textbox(
            "💡 Suggestions"
        )

        self.ai_text = self.create_result_textbox(
            "🤖 AI Feedback"
        )


    # ========================================================
    # RESULT TEXTBOX
    # ========================================================

    def create_result_textbox(self, tab_name):

        textbox = ctk.CTkTextbox(

            self.tabview.tab(tab_name)

        )

        textbox.pack(

            fill="both",

            expand=True,

            padx=10,

            pady=10

        )

        return textbox


    # ========================================================
    # SELECT RESUME
    # ========================================================

    def select_resume(self):

        file_path = filedialog.askopenfilename(

            title="Select Resume",

            filetypes=[

                (
                    "Resume Files",
                    "*.pdf *.docx"
                ),

                (
                    "PDF Files",
                    "*.pdf"
                ),

                (
                    "Word Documents",
                    "*.docx"
                )

            ]

        )


        if file_path:

            self.resume_path = file_path

            self.file_label.configure(

                text=file_path

            )

            self.status_label.configure(

                text="Resume selected. "
                "Paste the job description."

            )


    # ========================================================
    # RUN ANALYSIS
    # ========================================================

    def run_analysis(self):

        # Check resume
        if not self.resume_path:

            messagebox.showwarning(

                "Resume Required",

                "Please select a PDF or DOCX resume."

            )

            return


        # Get job description
        job_description = (

            self.job_text
            .get(
                "1.0",
                "end"
            )
            .strip()

        )


        if not job_description:

            messagebox.showwarning(

                "Job Description Required",

                "Please paste the job description."

            )

            return


        try:

            self.analyze_button.configure(

                state="disabled",

                text="⏳ ANALYZING..."

            )


            self.status_label.configure(

                text="Extracting resume..."

            )

            self.update()


            # =================================================
            # PARSE
            # =================================================

            self.resume_data = parse_resume(

                self.resume_path

            )


            self.status_label.configure(

                text="Calculating ATS score..."

            )

            self.update()


            # =================================================
            # ATS ANALYSIS
            # =================================================

            self.analysis = analyze_resume(

                self.resume_data,

                job_description

            )


            self.status_label.configure(

                text="Sending resume to Gemini..."

            )

            self.update()


            # =================================================
            # GEMINI
            # =================================================

            ai_feedback = analyze_with_gemini(

                self.resume_data["raw_text"],

                job_description

            )


            # =================================================
            # DISPLAY
            # =================================================

            self.display_results(

                ai_feedback

            )


            self.status_label.configure(

                text="✅ Analysis completed."

            )


        except Exception as error:

            messagebox.showerror(

                "Analysis Error",

                str(error)

            )

            self.status_label.configure(

                text="❌ Analysis failed."

            )


        finally:

            self.analyze_button.configure(

                state="normal",

                text="🚀 ANALYZE RESUME"

            )


    # ========================================================
    # DISPLAY RESULTS
    # ========================================================

    def display_results(self, ai_feedback):

        analysis = self.analysis


        # ----------------------------------------------------
        # SCORE
        # ----------------------------------------------------

        score = analysis["ats_score"]


        self.score_label.configure(

            text=f"{score}/100"

        )


        self.score_progress.set(

            score / 100

        )


        # ----------------------------------------------------
        # SCORE DETAILS
        # ----------------------------------------------------

        details = (

            f"🎯 Skill Match: "
            f"{analysis['skill_match']['score']}%\n\n"

            f"🔑 Keyword Match: "
            f"{analysis['keyword_match']['score']}%\n\n"

            f"📋 Section Score: "
            f"{analysis['section_score']}%\n\n"

            f"📐 Format Score: "
            f"{analysis['format_score']}%"

        )


        self.score_details.configure(

            text=details

        )


        # ----------------------------------------------------
        # SKILLS
        # ----------------------------------------------------

        self.skills_text.delete(
            "1.0",
            "end"
        )


        matched = analysis[
            "skill_match"
        ]["matched"]


        missing = analysis[
            "skill_match"
        ]["missing"]


        self.skills_text.insert(

            "end",

            "✅ MATCHED SKILLS\n\n"

        )


        for skill in matched:

            self.skills_text.insert(

                "end",

                f"• {skill.title()}\n"

            )


        self.skills_text.insert(

            "end",

            "\n\n❌ MISSING SKILLS\n\n"

        )


        for skill in missing:

            self.skills_text.insert(

                "end",

                f"• {skill.title()}\n"

            )


        # ----------------------------------------------------
        # KEYWORDS
        # ----------------------------------------------------

        self.keywords_text.delete(
            "1.0",
            "end"
        )


        keyword_match = analysis[
            "keyword_match"
        ]


        self.keywords_text.insert(

            "end",

            "✅ MATCHED KEYWORDS\n\n"

        )


        for keyword in keyword_match[
            "matched"
        ]:

            self.keywords_text.insert(

                "end",

                f"• {keyword}\n"

            )


        self.keywords_text.insert(

            "end",

            "\n\n❌ MISSING KEYWORDS\n\n"

        )


        for keyword in keyword_match[
            "missing"
        ]:

            self.keywords_text.insert(

                "end",

                f"• {keyword}\n"

            )


        # ----------------------------------------------------
        # SECTIONS
        # ----------------------------------------------------

        self.sections_text.delete(
            "1.0",
            "end"
        )


        sections = analysis[
            "sections"
        ]


        self.sections_text.insert(

            "end",

            "✅ PRESENT SECTIONS\n\n"

        )


        for section in sections[
            "present"
        ]:

            self.sections_text.insert(

                "end",

                f"• {section}\n"

            )


        self.sections_text.insert(

            "end",

            "\n\n❌ MISSING SECTIONS\n\n"

        )


        for section in sections[
            "missing"
        ]:

            self.sections_text.insert(

                "end",

                f"• {section}\n"

            )


        # ----------------------------------------------------
        # SUGGESTIONS
        # ----------------------------------------------------

        self.suggestions_text.delete(
            "1.0",
            "end"
        )


        for suggestion in analysis[
            "suggestions"
        ]:

            self.suggestions_text.insert(

                "end",

                f"💡 {suggestion}\n\n"

            )


        # ----------------------------------------------------
        # AI FEEDBACK
        # ----------------------------------------------------

        self.ai_text.delete(
            "1.0",
            "end"
        )


        self.ai_text.insert(

            "end",

            ai_feedback

        )


    # ========================================================
    # NAVIGATION
    # ========================================================

    def navigation_click(self, text):

        if text == "🏠 Dashboard":

            self.content.yview_moveto(0)


        elif text == "📊 Analysis":

            self.content.yview_moveto(0.5)


        elif text == "🧠 Skills":

            self.tabview.set(
                "🧠 Skills"
            )

            self.content.yview_moveto(1)


        elif text == "🔑 Keywords":

            self.tabview.set(
                "🔑 Keywords"
            )

            self.content.yview_moveto(1)


        elif text == "🤖 AI Feedback":

            self.tabview.set(
                "🤖 AI Feedback"
            )

            self.content.yview_moveto(1)


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    app = ResumeAnalyzerApp()

    app.mainloop()