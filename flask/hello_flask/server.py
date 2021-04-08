from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("users.html")


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


@app.route("/users")
def users():
    db_users = [
        {"first_name":"Micah", "last_name":"Wendorf", "email":"wendorfmicah0@gmail.com"},
        {"first_name":"Chris", "last_name":"Juarex", "email":"cjuarez@codingdojo.com"},
        {"first_name":"Benny Bob", "last_name":"McBob", "email":"bob@mcbob.com"},
        {"first_name":"Mr. Nibbles", "last_name":"Pancakes", "email":"nibs@pancakes.com"}
    ]
    return render_template("users.html", users=db_users)

@app.route("/others")
def others():
    db_others = [
        {"first_name":"Anne", "last_name":"Jurack", "email":"ajurack@gmail.com"},
        {"first_name":"Marisa", "last_name":"Goode", "email":"mgoode@codingdojo.com"}
    ]
    return render_template("users.html", users=db_users)


@app.route("/add/user")
def add_user():
    return render_template("add_user.html")

@app.route("/create/user", methods=['POST'])
def create_user():
    print(request.form['first_name'])
    print(request.form['last_name'])
    print(request.form['email'])



if __name__ == "__main__":
    app.run(debug=True)