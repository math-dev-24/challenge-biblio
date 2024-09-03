from flask import Flask, jsonify, request, redirect, render_template
from Controller.BookController import BookController
from Controller.MovementController import MovementController

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
    error = request.args.get("error")
    book = {
        "title": request.args.get("title"),
        "author": request.args.get("author"),
        "isbn": request.args.get("isbn"),
        "book_type": request.args.get("book_type")
    }
    return render_template('add.html', error=error, book=book)


@app.route("/list", methods=["GET"])
def list_books():
    return render_template('list.html', list_books=BookController().get_all_books())


@app.route("/reserve", methods=["GET"])
def view_reserve_book():
    isbn = request.args.get("isbn")
    if not isbn:
        return redirect("/")

    book = BookController().get_book(isbn)
    return render_template('reserve.html', book=book)


@app.route("/detail/<isbn>", methods=["GET"])
def view_detail_book(isbn):
    book = BookController().get_book(isbn)
    controller_movement: MovementController = MovementController()
    movements = controller_movement.get_movement_by_isbn(isbn)
    return render_template('detail.html', book=book, movements=movements)


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
        return redirect(
            "/add?error=Données manquantes&title=" + title + "&author=" + author + "&isbn=" + isbn + "&book_type=" + book_type)

    controller_book.create_book(request.form['title'], request.form['author'], request.form['isbn'],
                                request.form['book_type'])
    return redirect("/list")


@app.route('/api/v1/books/<isbn>/reserve', methods=["POST"])
def reserve_book(isbn):
    data = request.json
    movement_controller: MovementController = MovementController()
    date_start = data.get('reservation_date_start')
    date_end = data.get('reservation_date_end')
    result: str = movement_controller.create_movement(isbn, date_start, date_end)
    return jsonify({"result": result}), 200


@app.route('/api/v1/books/<isbn>', methods=["DELETE"])
def delete_book(isbn):
    controller_book: BookController = BookController()
    controller_book.delete_book(isbn)
    return jsonify({"isbn": isbn}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
