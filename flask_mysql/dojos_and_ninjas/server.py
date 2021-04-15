from flask import Flask, render_template, request, redirect

from mysqlconnection import connectToMySQL

app = Flask(__name__)


@app.route("/dojos")
def home():
    dojos = connectToMySQL('dojos_and_ninjas').query_db("SELECT * FROM dojos;")
    return render_template("dojos.html", dojos = dojos)

@app.route("/new_dojos", methods=['POST'])
def new_dojo():
    mysql = connectToMySQL('dojos_and_ninjas')
    query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
    data = {
        "name": request.form['dojo_name']
    }
    mysql.query_db(query,data)
    return redirect("/dojos")

@app.route("/dojos/<int:dojos_id>")
def show_dojo(dojos_id):
    query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = dojo_id WHERE dojos.id = %(id)s;"
    data = {
        "id": dojos_id
    }
    ninjas = connectToMySQL('dojos_and_ninjas').query_db(query,data)
    return render_template("dojo_details.html", ninjas = ninjas)

@app.route("/dojos/ninjas")
def add_ninja():
    dojos = connectToMySQL('dojos_and_ninjas').query_db("SELECT * FROM dojos")
    return render_template("ninjas.html", dojos = dojos)

@app.route("/create_ninja", methods=['POST'])
def create_ninja():
    query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo'],
    }
    create = connectToMySQL("dojos_and_ninjas").query_db(query,data)
    return redirect("/dojos") # redirect route is gonnna give you trouble check it later

if __name__ == "__main__":
    app.run(debug=True)