from flask import Flask, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = "I love coding"

@app.route('/')
def home():
    session['randint'] = random.randint(1, 100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) == session['randint']:
        result = "You got it!"
        return render_template("index.html", result = result)
    elif int(request.form['guess']) < session['randint']:
        result = "Too low! Try again."
        return render_template("index.html", result = result)
    elif int(request.form['guess']) > session['randint']:
        result = ("Too high! Try again.")
        return render_template("index.html", result = result)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)