from flask import Flask, render_template, request, redirect, session, flash
import re

from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "keep it secret"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def submit():
    is_valid = True
    
    if len(request.form['email']) <1:
        is_valid = False
        flash("Wrong")
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!")
        return redirect('/')

    else:
        flash("SUCCESS NEW EMAIL ACQUIRED HERE")
        query = "INSERT INTO email (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        data = {
            "email": request.form['email'],
        }
        raichu = connectToMySQL("email").query_db(query, data)
        return redirect('/', raichu = raichu)


if __name__=="__main__":
    app.run(debug=True)