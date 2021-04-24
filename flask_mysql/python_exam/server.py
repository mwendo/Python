from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "keep it secret"

@app.route('/')
def home():
    return render_template("register_login.html")

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Registration
@app.route('/process', methods=['POST'])
def process():
    is_valid = True
    print (len(request.form['password']))
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
    if len(request.form['password']) >15:
        is_valid = False
        flash("Must create a password")
    if request.form['password'] != request.form['confirm_password']:
        is_valid = False
        flash("passwords must match")
    if is_valid == True:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": pw_hash
        }
        results = connectToMySQL('magazines').query_db(query,data)
        session['user_id'] = results
        return redirect('/dashboard')
    return redirect("/")

# Login
@app.route('/login', methods=['POST'])
def login():
    is_valid = True

    if len(request.form['email']) < 1:
        is_valid = False
        flash("Email field is required.")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address!")
    if len(request.form['password']) <8:
        is_valid = False
        flash("password must be at least 8 characters")
    if is_valid == True:
        query = "SELECT * FROM users WHERE email = %(email)s"
        data = {
            "email": request.form['email']
        }
        results = connectToMySQL('magazines').query_db(query,data)
        if not results:
            flash("Invalid password/email")
            return redirect('/')
        if bcrypt.check_password_hash(results[0]['password'], request.form['password']):
            session['user_id'] = results[0]['id']
            return redirect('/dashboard')
        flash("Invalid password/email")
        return redirect('/dashboard')
    return redirect("/")

# Dashboard Home Page
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    query = "SELECT * FROM users JOIN magazines ON users.id = user_id WHERE users.id = %(id)s"
    query_user = "SELECT * FROM users WHERE id = %(id)s"
    data = {
        "id": session['user_id'],
    }
    results = connectToMySQL('magazines').query_db(query,data)
    user = connectToMySQL('magazines').query_db(query_user,data)
    return render_template("dashboard.html", magazines = results, user = user[0])

# Add New Magazine Page
@app.route('/new')
def new_magazine_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("add_magazine.html")

# Add New Magazine Route
@app.route('/add_magazine', methods=['POST'])
def add_new_magazine():
    if 'user_id' not in session:
        return redirect('/')

    is_valid = True

    if len(request.form['title']) < 2:
        is_valid = False
        flash("Title must be at least 2 characters long.")
    if len(request.form['description']) < 10:
        is_valid = False
        flash("Description must be at least 2 chracters long.")
    if is_valid == True:
        query = "INSERT INTO magazines (name, description, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, NOW(), NOW(), %(user_id)s);"
        data = {
            "name": request.form['title'],
            "description": request.form['description'],
            "user_id": session['user_id']
        }
        result = connectToMySQL('magazines').query_db(query, data)
        return redirect('/dashboard')
    return redirect('/new')

@app.route('/show/<int:magazine_id>')
def show_details_of_magazine(magazine_id):
    if 'user_id' not in session:
        return redirect('/')
    query = "SELECT * FROM users JOIN magazines ON users.id = user_id WHERE users.id = %(id)s;"
    data = {
        "id": session['user_id'],
    }
    results = connectToMySQL('magazines').query_db(query, data)
    return render_template("show_magazine_details.html", magazine=results[0])

@app.route('/account/<int:user_id>')
def user_details_page(user_id):
    if 'user_id' not in session:
        return redirect('/')
    query = "SELECT * FROM users WHERE id = %(id)s;"
    query_user = "SELECT * FROM users JOIN magazines ON users.id = user_id WHERE users.id = %(id)s"
    data = {
        "id": user_id
    }
    results = connectToMySQL('magazines').query_db(query,data)
    result = connectToMySQL('magazines').query_db(query_user,data)
    return render_template("user_details_page.html", user = results[0], magazines=result)

@app.route('/edit/user/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    if 'user_id' not in session:
        return redirect('/')

    is_valid = True

    if len(request.form['first_name']) < 2:
        is_valid = False
        flash("First Name must be longer than 2 characters")
        return redirect('/dashboard')
    if not request.form['first_name'].isalpha():
        is_valid = False
        flash("First Name must be letters only")
        return redirect('/dashboard')
    if len(request.form['last_name']) < 2:
        is_valid = False
        flash("Last Name must be longer than 2 characters")
        return redirect('/dashboard')
    if not request.form['last_name'].isalpha():
        is_valid = False
        flash("Last Name must be letters only")
        return redirect('/dashboard')
    if len(request.form['email']) < 1:
        is_valid = False
        flash("Email field is required.")
        return redirect('/dashboard')
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address!")
        return redirect('/dashboard')

    query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE users.id = %(id)s"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": user_id
    }
    result = connectToMySQL('magazines').query_db(query,data)
    return redirect('/dashboard')


@app.route('/delete/<int:magazine_id>')
def delete(magazine_id):
    if 'user_id' not in session:
        return redirect('/')
    query = "DELETE FROM magazines WHERE id = %(id)s"
    data = {
        "id": magazine_id
    }
    result = connectToMySQL('magazines').query_db(query,data)
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)