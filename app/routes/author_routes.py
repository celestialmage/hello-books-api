# app/routes/author_routes.py
from flask import Blueprint, request, make_response, abort
from .route_utilities import validate_model
from app.models.author import Author
from ..models.book import Book
from ..db import db

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

@authors_bp.post("")
def create_author():
    request_body = request.get_json()

    try:
        new_author = Author.from_dict(request_body)
        
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
    
    db.session.add(new_author)
    db.session.commit()

    return make_response(new_author.to_dict(), 201)

@authors_bp.get("")
def get_all_authors():
    query = db.select(Author)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Author.name.ilike(f"%{name_param}%"))

    authors = db.session.scalars(query.order_by(Author.id))
    # Use list comprehension syntax to create the list `authors_response`
    authors_response = [author.to_dict() for author in authors]

    return authors_response


@authors_bp.get("/<author_id>/books")
def get_books_by_author(author_id):
    author = validate_model(Author, author_id)
    response = [book.to_dict() for book in author.books]
    return response

# app/routes/author_routes.py
@authors_bp.post("/<author_id>/books")
def create_book_with_author(author_id):

    author = validate_model(Author, author_id)

    request_body = request.get_json()
    request_body["author_id"] = author.id

    try:
        new_book = Book.from_dict(request_body)
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    # refer to prior examples or the documentation 
    # and try completing this endpoint yourself

    db.session.add(new_book)
    db.session.commit()

    return make_response(new_book.to_dict(), 201) 