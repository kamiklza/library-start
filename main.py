from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    if not all_books:
        return render_template('index.html', empty=True)
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        detail = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(detail)
        return redirect(url_for('home', all_books=all_books))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

