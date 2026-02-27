from flask import Flask, render_template, request
from analyzer import analyze_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        score, strength, entropy, feedback = analyze_password(password)

        result = {
            "score": score,
            "strength": strength,
            "entropy": entropy,
            "feedback": feedback
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)