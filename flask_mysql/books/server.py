from flask import Flask, render_template, request, redirect

from mysqlconnection import connectToMySQL

app = Flask(__name__)

# Displays authors
@app.route("/authors")
def authors_home():
    authors = connectToMySQL("favorite_books").query_db("SELECT * FROM authors")
    return render_template("home.html", authors = authors)

# Adds new authors to authors table
@app.route("/new_authors", methods=['POST'])
def authors():
    mysql = connectToMySQL('favorite_books')
    query = "INSERT INTO authors (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
    }
    mysql.query_db(query,data)
    return redirect("/authors")

# Displays specific authors favorite books
@app.route("/authors/<int:authors_id>")
def authors_favorite_books(authors_id):
    query = "SELECT * FROM books JOIN favorites ON books.id = favorites.book_id JOIN authors ON favorites.author_id = %(id)s WHERE authors.id = %(id)s;"
    book_q = connectToMySQL("favorite_books").query_db("SELECT * FROM books;")
    data = {
        "id": authors_id,
    }
    books = connectToMySQL('favorite_books').query_db(query, data)
    author_q = connectToMySQL("favorite_books").query_db("SELECT * FROM authors WHERE id = %(id)s;", data)
    print(books)
    return render_template("authors_favorite_books.html", books = books, book_q = book_q, author_q = author_q[0])

# add's a book to that specific author's favorite books list
@app.route("/add_book", methods=['POST'])
def add_book():
    query = "INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s);"
    data = {
        "book_id": request.form['add_book'],
        "author_id": request.form['author_id'] 
    }
    id = request.form['author_id']
    results = connectToMySQL('favorite_books').query_db(query, data)
    return redirect(f"/authors/{id}")

# creates a new book to the overall book dictionary
@app.route("/create_new_books", methods=['POST'])
def create_new_book():
    mysql = connectToMySQL("favorite_books")
    query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages'],
    }
    results = mysql.query_db(query,data)
    print(results)
    return redirect("/books")

# displays the library of current books
@app.route("/books")
def books_home():
    books = connectToMySQL("favorite_books").query_db("SELECT * FROM books")
    return render_template("books.html", books = books)


@app.route("/books/<int:books_id>")
def books_details(books_id):
    query = "SELECT * FROM books JOIN favorites ON books.id = favorites.book_id JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
    data = {
        "id": books_id,
    }
    books = connectToMySQL('favorite_books').query_db(query, data)
    
    return render_template("books_details.html", books = books)


if __name__ == "__main__":
    app.run(debug=True)