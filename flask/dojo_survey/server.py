from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    is_valid = True
    if len(request.form['user_name']) <1:
        is_valid = False
        flash("Please enter a first name")
    if len(request.form['dojo_location']) <4:
        is_valid = False
        flash("Please enter a last name")
    if len(request.form['favorite_language']) <2:
        is_valid = False
        flash("Please enter a favorite language")
    if len(request.form['comment']) < 10:
        is_valid = False
        flash("Please enter a valid comment")

    if not is_valid:
        return redirect('/')
    else:
        flash("Friend successfully added!")
        query = "INSERT INTO user (user_name, dojo_location, favorite_language, comment, created_at, updated_at) VALUES (%(user_name)s, %(dojo_location)s, %(favorite_language)s, %(comment)s, NOW(), NOW());"
        print(query)
        data = {
            "user_name": request.form['user_name'],
            "dojo_location": request.form['dojo_location'],
            "favorite_language": request.form['favorite_language'],
            "comment": request.form['comment']
        }
        pikachu = connectToMySQL("dojo_survey").query_db(query, data)
        return redirect ('/show_page')


@app.route('/show_page')
def show():
    mysql = connectToMySQL("dojo_survey").query_db("SELECT * FROM user;")
    return render_template("show.html", mysql = mysql)

if __name__=="__main__":
    app.run(debug=True)