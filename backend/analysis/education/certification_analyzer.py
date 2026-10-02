class CertificationAnalyzer:

    def analyze(self, text):
        lines = [
            line.strip()
            for line in (text or "").splitlines()
            if line.strip()
        ]

        keywords = (
            "certification",
            "certified",
            "certificate",
            "aws",
            "azure",
            "google cloud",
            "nism",
        )

        matches = [
            line
            for line in lines
            if any(
                word in line.lower()
                for word in keywords
            )
        ]

        return {
            "count": len(matches),
            "certifications": matches,
<<<<<<< HEAD
        }
=======
        }
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
