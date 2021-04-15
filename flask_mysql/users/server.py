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

@app.route('/show_page/<int:people_id>')
def show(people_id):
    query = "SELECT * FROM people WHERE id = %(id)s;"
    data = {
        "id": people_id
    }
    people = connectToMySQL('people').query_db(query, data)
    print(people)
    return render_template("read(one).html", people = people[0])

@app.route('/edit_page/<int:people_id>')
def edit(people_id):
    query = "SELECT * FROM people WHERE id = %(id)s;"
    data = {
        "id": people_id
    }
    people = connectToMySQL('people').query_db(query, data)
    print(people)
    return render_template("edit_page.html", people = people[0])

@app.route('/update/<int:people_id>', methods=['POST'])
def update(people_id):
    query = "UPDATE people SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": people_id,
    }
    people = connectToMySQL('people').query_db(query, data)
    print(people)
    return redirect(f"/show_page/{people_id}")

@app.route('/delete/<int:people_id>')
def delete(people_id):
    query = "DELETE FROM people WHERE id = %(id)s;"
    data = {
        "id": people_id
    }
    people = connectToMySQL('people').query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)