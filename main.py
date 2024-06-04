from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main_page.html")


@app.route("/vankuse")
def pillows():
    return render_template("vankuse.html")


if __name__ == "__main__":
    app.run(debug=True)
