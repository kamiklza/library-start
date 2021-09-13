from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my-books-collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


db.create_all()

all_books = []


@app.route('/')
def home():
    global all_books
    all_books = db.session.query(Book).all()
    print(all_books)
    if not all_books:
        return render_template('index.html', empty=True)
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global all_books
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]

        book = Book(title=title, author=author, rating=rating)
        db.session.add(book)
        db.session.commit()

        book_detail = {
            "id": book.id,
            "title": title,
            "author": author,
            "rating": rating
        }
        all_books.append(book_detail)
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit/<int:book_id>')
def edit(book_id):
    for book in all_books:
        if book.id == book_id:
            selected_book = book
    return render_template('edit.html', selected_book=selected_book)




if __name__ == "__main__":
    app.run(debug=True)

