from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "keep it secret"


@app.route('/')
def home():
    return render_template("index.html")

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/process', methods=['POST'])
def process():
    is_valid = True

    if len(request.form['first_name']) < 2:
        is_valid = False
        flash("First Name must be longer than 2 characters")
    if not request.form['first_name'].isalpha():
        is_valid = False
        flash("First Name must be letters only")
    if len(request.form['last_name']) < 2:
        is_valid = False
        flash("Last Name must be longer than 2 characters")
    if not request.form['last_name'].isalpha():
        is_valid = False
        flash("Last Name must be letters only")
    if len(request.form['email']) < 1:
        is_valid = False
        flash("Email field is required.")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address!")
    if len(request.form['password']) <8:
        is_valid = False
        flash("password must be at least 8 characters")
    if request.form['password'] != request.form['confirm_password']:
        is_valid = False
        flash("passwords must match")
    
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        query = "INSERT INTO user (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        print(query)
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": pw_hash
        }
        results = connectToMySQL('login_registration').query_db(query,data)
        session['user_id'] = results
        print(results)
        return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    query = "SELECT * FROM user WHERE id = %(id)s"
    data = {
        "id": session['user_id'],
    }
    user = connectToMySQL('login_registration').query_db(query,data)[0]
    return render_template("dashboard.html", user = user)


@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM user WHERE email = %(email)s"
    data = {
        "email": request.form['email']
    }
    results = connectToMySQL('login_registration').query_db(query,data)
    if not results:
        flash("Invalid password/email")
        return redirect('/')
    if bcrypt.check_password_hash(results[0]['password'], request.form['password']):
        session['user_id'] = results[0]['id']
        return redirect('/dashboard')
    flash("Invalid password/email")
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)