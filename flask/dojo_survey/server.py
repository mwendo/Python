from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "Christian is gay"

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
        # add user to database
        flash("Friend successfully added!")
        return redirect('/')

    query = "INSERT INTO user (user_name, dojo_location, favorite_language, comment, created_at, updated_at) VALUES (%(user_name)s, %(dojo_location)s, %(favorite_language)s, %(comment)s, NOW(), NOW());"
    data = {
        "user_name": request.form['user_name'],
        "dojo_location": request.form['dojo_location'],
        "comment": request.form['comment']
    }
    pussy = connectToMySQL("dojo_survey").query_db(query, data)
    return redirect ('/', pussy = pussy)


if __name__=="__main__":
    app.run(debug=True)