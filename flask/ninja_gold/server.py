from flask import Flask, render_template, request, session, redirect
import random, datetime

app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def home():
    if 'your_gold' not in session:
        session['your_gold'] = 0
        session['result'] = []
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():

    if request.form['building'] == 'casino':
        randint = random.randint(-50, 50)
        result = (f"Earned {randint} golds from the casino! ({datetime.datetime.now().strftime('%c')})")
        session['result'].append(result)
        session['your_gold'] += randint
        return render_template('index.html', result = result, randint = randint)
        # casino process
    elif request.form['building'] == 'farm':
        randint = random.randint(10, 20)
        result = (f"Earned {randint} golds from the farm! ({datetime.datetime.now().strftime('%c')})")
        session['result'].append(result)
        session['your_gold'] += randint
        return render_template('index.html', result = result, randint = randint)
        # farm process
    elif request.form['building'] == 'cave':
        randint = random.randint(5, 10)
        result = (f"Earned {randint} golds from the cave! ({datetime.datetime.now().strftime('%c')})")
        session['result'].append(result)
        session['your_gold'] += randint
        return render_template('index.html', result = result, randint = randint)
        # cave process
    elif request.form['building'] == 'house':
        randint = random.randint(2, 5)
        result = (f"Earned {randint} golds from the house! ({datetime.datetime.now().strftime('%c')})")
        session['result'].append(result)
        session['your_gold'] += randint
        return render_template('index.html', result = result, randint = randint)
        # house process
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)