from flask import Flask, render_template, request, redirect

from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('people')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM people;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("read.html", all_friends = friends)

@app.route('/create_page')
def create_page():
    return render_template("create.html")

@app.route('/create', methods=['POST'])
def create():
    query = "INSERT INTO people (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())"
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
    }
    mysql = connectToMySQL('people')
    mysql.query_db(query,data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)