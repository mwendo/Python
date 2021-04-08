from flask import Flask
app = Flask(__name__)

@app.route ('/')
def hello_world():
    return 'Hello World!'

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