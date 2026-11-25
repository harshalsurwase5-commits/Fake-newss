from flask import Flask, render_template, request

app = Flask(__name__)


def analyze_news(news):
    # Simple prototype logic
    fake_words = [
        "shocking", "100% true", "secret", "miracle",
        "you won't believe", "breaking", "guaranteed",
        "click here", "exposed"
    ]

    score = 0
    found_words = []

    text = news.lower()

    for word in fake_words:
        if word in text:
            score += 10
            found_words.append(word)

    if score >= 30:
        result = "Potentially Fake"
        confidence = min(70 + score, 98)
        explanation = (
            "The content contains several sensational or "
            "emotionally charged expressions commonly associated "
            "with misleading news."
        )

    elif score >= 10:
        result = "Potentially Misleading"
        confidence = 60 + score
        explanation = (
            "Some characteristics of the content may require "
            "further verification from reliable sources."
        )

    else:
        result = "Likely Reliable"
        confidence = 75
        explanation = (
            "No major suspicious patterns were detected. "
            "However, the information should still be verified "
            "using trustworthy news sources."
        )

    return result, confidence, explanation, found_words


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    confidence = None
    explanation = None
    suspicious = []

    if request.method == "POST":

        news = request.form["news"]

        if news.strip():

            result, confidence, explanation, suspicious = analyze_news(news)

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        explanation=explanation,
        suspicious=suspicious
    )


if __name__ == "__main__":
    app.run(debug=True)