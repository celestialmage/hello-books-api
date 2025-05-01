from flask import Blueprint, abort, make_response, request
from app.models.book import Book
from ..db import db

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")


@books_bp.post("")
def create_book():
    request_body = request.get_json()

    new_book = validate_create_book(request_body)
    db.session.add(new_book)
    db.session.commit()

    response = new_book.to_dict()
    return response, 201


@books_bp.get("")
def get_all_books():
    query = db.select(Book)

    title_param = request.args.get("title")
    if title_param:
        query = query.where(Book.title.ilike(f"%{title_param}"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Book.description.ilike(f"%{description_param}%"))

    books = db.session.scalars(query.order_by(Book.id))

    books_response = []
    for book in books:
        books_response.append(book.to_dict())
    return books_response


@books_bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_book(book_id)

    return book.to_dict()


def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        response = {"message": f"Book {book_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Book).where(Book.id == book_id)
    book = db.session.scalar(query)

    if not book:
        response = {"message": f"Book {book_id} not found"}
        abort(make_response(response, 404))

    return book


def validate_create_book(request):

    try:
        new_book = Book.from_dict(request)
    except KeyError as error:
        message = {
            "message": f"New book missing '{error.args[0]}' attribute."
        }
        abort(make_response(message, 400))

    return new_book
