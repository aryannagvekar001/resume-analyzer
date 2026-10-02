class BulletAnalyzer:

    def analyze(self, text):
        lines = [
            line.strip()
            for line in (text or "").splitlines()
            if line.strip()
        ]

        bullets = [
            line
            for line in lines
            if line.startswith(("-", "*", "•"))
        ]

        return {
            "count": len(bullets),
            "bullets": bullets,
<<<<<<< HEAD
        }
=======
        }
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
