from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "Mr. Nibbles wuz heer."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

# ALWAYS REDIRECT ON A POST ROUTE
@app.route("/process", methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['bun'] = request.form['bun']
    session['meat'] = request.form['meat']
    session['calories'] = request.form['calories']
    session['topping_one'] = request.form['topping_one']
    session['topping_two'] = request.form['topping_two']
    return redirect('/burger')

@app.route('/burger')
def burger():
    if "name" not in session: 
        return redirect ("/")
    lunch = {
        'name': session['name'],
        'bun' : session['bun'],
        'meat': session['meat'],
        'calories': session['calories'],
        'topping_one': session['topping_one'],
        'topping_two': session['topping_two']
    }
    return render_template("burger.html", burger = lunch)






if __name__=="__main__":
    app.run(debug=True)