from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QFrame,
)


class UploadView(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Title
        title = QLabel("Upload Resume")

        title.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: #172033;
            }
        """)

        layout.addWidget(title)

        # Subtitle
        subtitle = QLabel(
            "Upload your resume in PDF, DOCX or TXT format"
        )

        subtitle.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #64748b;
            }
        """)

        layout.addWidget(subtitle)

        # Upload Card
        card = QFrame()

        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 12px;
            }
        """)

        card_layout = QVBoxLayout(card)

        upload_label = QLabel(
            "📄\n\n"
            "Select your resume\n\n"
            "Supported formats: PDF, DOCX, TXT"
        )

        upload_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        upload_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #64748b;
                padding: 30px;
            }
        """)

        card_layout.addWidget(upload_label)

        upload_button = QPushButton("Choose Resume")

        upload_button.setStyleSheet("""
            QPushButton {
                background-color: #2563eb;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 7px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }
        """)

        upload_button.clicked.connect(
            self.choose_resume
        )

        card_layout.addWidget(upload_button)

        layout.addWidget(card)

        # File name
        self.file_label = QLabel(
            "No resume selected"
        )

        self.file_label.setStyleSheet("""
            color: #64748b;
            font-size: 14px;
        """)

        layout.addWidget(self.file_label)

        # Resume text
        text_title = QLabel("Resume Preview")

        text_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
        """)

        layout.addWidget(text_title)

        self.resume_text = QTextEdit()

        self.resume_text.setPlaceholderText(
            "Extracted resume text will appear here..."
        )

        layout.addWidget(self.resume_text)

        layout.addStretch()

    def choose_resume(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Resume",
            "",
            "Resume Files (*.pdf *.docx *.txt)"
        )

        if file_path:

            self.file_label.setText(
                f"Selected: {file_path}"
            )

            self.resume_text.setText(
                "Resume selected successfully.\n\n"
                "File:\n" + file_path +
                "\n\nResume text extraction will be "
                "connected to the analyzer backend later."
            )