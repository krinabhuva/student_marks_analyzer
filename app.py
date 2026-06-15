from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)