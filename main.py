from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        print(title)
        author = request.form["author"]
        print(author)
        rating = request.form["rating"]
        print(rating)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

