from flask import Flask, render_template
app = Flask(__name__)

# @app.route ('/')
# def hello_world():
#     return render_template("index.html", phrase="hello", times=5)

@app.route ('/play/<x>/<color>')
def playground(x, color):
    return render_template("playground.html", repeat=int(x),  color_template=color) 

@app.route ('/')
def play():
    return render_template("playground.html", repeat=64)

@app.route ('/dojo')
def dojo():
    return 'Dojo!'

@app.route ('/hello/<name>')
def hello(name):
    return "Hello, " + name

@app.route ('/repeat/<number>/<word>')
def repeat(number, word):
    return word * int(number)

if __name__ == "__main__":
    app.run(debug=True)