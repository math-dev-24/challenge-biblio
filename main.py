from flask import Flask, jsonify, request, redirect, render_template
from Controller.BookController import BookController
from Controller.MovementController import MovementController
from Controller.UserController import UserController

app = Flask(__name__)
controller_book: BookController = BookController()
controller_user: UserController = UserController()
controller_movement: MovementController = MovementController()


@app.route('/', methods=["GET"])
def index():
    data = {
        "nb_books": len(controller_book.get_all_books()),
        "nb_available_books": len(controller_book.get_available_books()),
        "nb_users": len(controller_user.get_all_users())
    }
    return render_template('index.html', data=data)


@app.route("/add-book", methods=["GET"])
def view_add_book():
    error = request.args.get("error")
    book = {
        "title": request.args.get("title", type=str),
        "author": request.args.get("author", type=str),
        "isbn": request.args.get("isbn", type=str),
        "book_type": request.args.get("book_type", type=str)
    }
    return render_template('book/add-book.html', error=error, book=book)


@app.route("/update-book", methods=["GET"])
def view_update_book():
    isbn = request.args.get("isbn", type=str)
    title = request.args.get("title", type=str)
    author = request.args.get("author", type=str)
    book_type = request.args.get("book_type", type=str)
    info = request.args.get("info", type=str) if request.args.get("info", type=str) else ""
    return render_template('book/update-book.html', isbn=isbn, title=title, author=author, book_type=book_type,
                           info=info)


@app.route("/list-book", methods=["GET"])
def list_books():
    page = request.args.get("page", 1, type=int)
    per_page: int = 8
    return render_template('book/list-book.html', data=BookController().get_all_books_page(page, per_page))


@app.route("/list-user", methods=["GET"])
def list_user():
    page = request.args.get("page", 1, type=int)
    per_page: int = 8
    return render_template('user/list-user.html', data=UserController().get_all_users_page(page, per_page))


@app.route("/add-user", methods=["GET"])
def view_add_user():
    return render_template('user/add-user.html')


@app.route("/list-movement", methods=["GET"])
def view_list_movement():
    page = request.args.get("page", 1, type=int)
    per_page: int = 12
    data = controller_movement.get_all_movements_page(page, per_page)
    return render_template('list-movement.html', data=data)


@app.route("/detail-user/<user_id>", methods=["GET"])
def view_detail_user(user_id):
    user = controller_user.get_user_by_id(int(user_id))
    movements = controller_movement.get_movements_by_user_id(user_id)
    return render_template('user/detail-user.html', user=user, movements=movements)


@app.route("/update-user", methods=["GET"])
def view_update_user():
    user_id = request.args.get("user_id", type=str)
    first_name = request.args.get("first_name", type=str)
    last_name = request.args.get("last_name", type=str)
    email = request.args.get("email", type=str)
    info = request.args.get("info", type=str) if request.args.get("info", type=str) else ""
    return render_template('user/update-user.html', user_id=user_id, first_name=first_name, last_name=last_name,
                           email=email, info=info)


@app.route("/reserve-book/<isbn>", methods=["GET"])
def view_reserve_book(isbn):
    if not isbn:
        return redirect("/")
    book = BookController().get_book(isbn)
    users = controller_user.get_all_users()
    return render_template('book/reserve-book.html', book=book, users=users)


@app.route("/detail-book/<isbn>", methods=["GET"])
def view_detail_book(isbn):
    book = BookController().get_book(isbn)
    movements = controller_movement.get_movements_by_isbn(isbn)
    return render_template('book/detail-book.html', book=book, movements=movements)


@app.route("/cancel-movement/<user_id>/<isbn>", methods=["GET"])
def view_cancel_movement(user_id, isbn):
    movement = controller_movement.delete_movements(user_id, isbn)
    return redirect("/list-movement")


@app.route('/api/v1/book', methods=["GET"])
def get_books():
    return jsonify(controller_book.get_all_books())


@app.route('/api/v1/book/update', methods=["GET"])
def update_book():
    isbn = request.args.get("isbn", type=str)
    title = request.args.get("title", type=str)
    author = request.args.get("author", type=str)
    book_type = request.args.get("book_type", type=str)
    is_updated: bool = controller_book.update_book(isbn, title, author, book_type)
    info: str = "Livre mis à jour" if is_updated else "Livre non mis à jour"
    return redirect(
        "/update-book?isbn=" + isbn + "&title=" + title + "&author=" + author + "&book_type=" + book_type + "&info=" + info)


@app.route('/api/v1/user/update/<user_id>', methods=["GET"])
def update_user(user_id):
    firstname = request.args.get("first_name", type=str)
    lastname = request.args.get("last_name", type=str)
    email = request.args.get("email", type=str)
    is_updated: bool = controller_user.update_user(user_id, firstname, lastname, email)
    info: str = "Utilisateur mis à jour" if is_updated else "Utilisateur non mis à jour"
    return redirect(
        "/update-user?user_id=" + user_id + "?first_name=" + firstname + "&last_name=" + lastname + "&email=" + email + "&info=" + info)


@app.route('/api/v1/book', methods=["POST"])
def create_book():
    title = request.form['title']
    author = request.form['author']
    isbn = request.form['isbn']
    book_type = request.form['book_type']

    isbn_exist = controller_book.get_book(isbn)
    if isbn_exist:
        return redirect(
            "/add?error=ISBN déjà utilisé&title=" + title + "&author=" + author + "&isbn=" + isbn + "&book_type=" + book_type)

    if not title or not author or not isbn or not book_type:
        return redirect(
            "/add?error=Données manquantes&title=" + title + "&author=" + author + "&isbn=" + isbn + "&book_type=" + book_type)

    controller_book.create_book(title, author, isbn, book_type)
    return redirect("/list-book")


@app.route("/api/v1/user", methods=["POST"])
def create_user():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password = request.form['password']
    email = request.form['email']
    existing_user = controller_user.get_user_by_email(email)
    if existing_user:
        return redirect(
            "/add?error=Email déjà utilisé&firstname=" + firstname + "&lastname=" + lastname + "&email=" + email)

    if not password or not email or not firstname or not lastname:
        return redirect(
            "/add?error=Données manquantes&firstname=" + firstname + "&lastname=" + lastname + "&email=" + email)

    controller_user.create_user(firstname, lastname, password, email)
    return redirect("/list-user")


@app.route('/api/v1/book/<isbn>/reserve', methods=["POST"])
def reserve_book(isbn):
    data = request.json
    date_start = data.get('reservation_date_start')
    date_end = data.get('reservation_date_end')
    user_id = data.get('user_id')
    result: str = controller_movement.create_movement(user_id, isbn, date_start, date_end)
    return jsonify({"result": result}), 200


@app.route('/api/v1/book/<isbn>', methods=["DELETE"])
def delete_book(isbn):
    is_deleted: bool = controller_book.delete_book(isbn)
    if not is_deleted:
        return jsonify({"error": "Impossible de supprimer le livre"}), 400
    return jsonify({"isbn": isbn}), 200


@app.route('/user/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    is_deleted: bool = controller_user.delete_user(user_id)
    if not is_deleted:
        return jsonify({"error": "Impossible de supprimer l'utilisateur"}), 400
    return jsonify({"id": user_id}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
