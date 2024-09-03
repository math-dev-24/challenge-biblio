from flask import Flask, jsonify, request, redirect, render_template
from Controller.BookController import BookController

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    controller_book: BookController = BookController()
    data = {
        "nb_books": len(controller_book.get_all_books()),
        "nb_available_books": len(controller_book.available_books())
    }
    return render_template('index.html', data=data)


@app.route("/add", methods=["GET"])
def add_book():
    data = {
        "error": request.args.get("error"),
        "book": {
            "title": request.args.get("title"),
            "author": request.args.get("author"),
            "isbn": request.args.get("isbn"),
            "book_type": request.args.get("book_type")
        }
    }
    return render_template('add.html', data=data)


@app.route("/list", methods=["GET"])
def list_books():
    return render_template('list.html', list_books=BookController().get_all_books())


@app.route("/reserve", methods=["GET"])
def reserve_book():
    return render_template('reserve.html')


@app.route('/api/v1/books', methods=["GET"])
def get_books():
    controller_book: BookController = BookController()
    return jsonify(controller_book.get_all_books())


@app.route('/api/v1/books', methods=["POST"])
def create_book():
    controller_book: BookController = BookController()
    title = request.form['title']
    author = request.form['author']
    isbn = request.form['isbn']
    book_type = request.form['book_type']

    if not title or not author or not isbn or not book_type:
        return redirect("/add?error=Données manquantes&title=" + title + "&author=" + author + "&isbn=" + isbn + "&book_type=" + book_type)

    controller_book.create_book(request.form['title'], request.form['author'], request.form['isbn'],
                                request.form['book_type'])
    return redirect("/list")


@app.route('/api/v1/books/<isbn>', methods=["DELETE"])
def delete_book(isbn):
    controller_book: BookController = BookController()
    controller_book.delete_book(isbn)
    return jsonify({"isbn": isbn}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
