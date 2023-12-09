from flask import Flask

app = Flask(__name__)

@app.route("/members")
def members():
    return {"mems": ["member 1", "member 2", "member 3"]}

if __name__ == "__main__":
    app.run(debug=True)