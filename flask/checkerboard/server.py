from flask import Flask, render_template
app = Flask(__name__)


@app.route("/<int:num1>/<int:num2>")
def index(num1, num2):
    return render_template("index.html", num1=num1, num2=num2)


if __name__ == "__main__":
    app.run(debug=True)
