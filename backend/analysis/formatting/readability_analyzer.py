import re


class ReadabilityAnalyzer:

    def analyze(self, text):
        words = re.findall(
            r"\b\w+\b",
            text or "",
        )

        sentences = re.split(
            r"[.!?]+",
            text or "",
        )

        sentences = [
            sentence
            for sentence in sentences
            if sentence.strip()
        ]

        average = (
            len(words) / len(sentences)
            if sentences
            else 0
        )

        return {
            "word_count": len(words),
            "sentence_count": len(sentences),
            "average_words_per_sentence": round(
                average,
                2,
            ),
<<<<<<< HEAD
        }
=======
        }
>>>>>>> ea09b18b8e005edee83c588e73dec1f896c9f6bf
