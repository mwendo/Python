from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "Mr. Nibbles wuz heer."

@app.route("/")
def counter():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)