from flask import Flask, request, jsonify
import json

app = Flask(__name__)


books = [
    {
        "id": 1,
        "title": "Advance Java",
        "author": "Proticent",
        "price": 230,
        "year_published": 2023,
    },
    {
        "id": 2,
        "title": "Python for Data Analysis",
        "author": "Wrox Press Inc.",
        "price": 456.78,
        "year_published": 2019,
    },
    {
        "id": 3,
        "title": "The Elements of Computing Systems",
        "author": "Noah S. Sprague",
        "price": 567.99,
        "year_published": 2009,
    },
]
book_id_counter = 1


# Create Routes for CRUD Operations


# Read (GET): Retrieve all books
@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify(list(books))


# Read (GET): Retrieve a specific book by id
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book_by_id(book_id):
    # book = books.get(book_id)
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
        pass
    return jsonify({"message": "Book not found"}), 404


# Create (POST): Add a new book
@app.route("/books", methods=["POST"])
def add_book():
    new_title = request.form["title"]
    new_author = request.form["author"]
    new_price = request.form["price"]
    new_year_published = request.form["year_published"]
    iD = books[-1]["id"] + 1

    new_obj = {
        "id": iD,
        "title": new_title,
        "author": new_author,
        "price": new_price,
        "year_published": new_year_published,
    }
    books.append(new_obj)
    return jsonify(books), 201


# Update (PUT/PATCH): Update details of a specific book by id
@app.route("/books/<int:book_id>", methods=["PUT", "PATCH"])
def update_book(book_id):
    if request.method == "PUT":
        for book in books:
            if book["id"] == book_id:
                book["author"] = request.form["author"]
                book["price"] = request.form["price"]
                book["title"] = request.form["title"]
                book["year_published"] = request.form["year_published"]
                updated_book = {
                    "author": book["author"],
                    "price": book["price"],
                    "title": book["title"],
                    "year_published": book["year_published"],
                }
                return jsonify(updated_book)
        return {"message": "Books Not Found.. In List"}


# Delete (DELETE): Remove a book by id
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(index)
            return jsonify(books)


if __name__ == "__main__":
    app.run(debug=True)
