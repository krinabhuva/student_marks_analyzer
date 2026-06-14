from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        math = int(request.form["math"])
        science = int(request.form["science"])
        english = int(request.form["english"])

        average = (math + science + english) / 3

        if average >= 40:
            result = "Pass"
        else:
            result = "Fail"

        return render_template(
            "index.html",
            average=round(average, 2),
            result=result
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)