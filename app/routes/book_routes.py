from flask import Blueprint, abort, make_response
# from app.models.book import books

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")


# vvvvvvvvvvvvvv old code vvvvvvvvvvvvvv

# @books_bp.get("")
# def get_all_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     return books_response

# # No new import statements...
# # No modifications to the other route...

# # Surround url parameter with arrow brackets to designate it as a passed variable


# @books_bp.get("/<book_id>")
# # Enter the url parameter in the function arguments
# def get_one_book(book_id):

#     found_book = validate_book(book_id)

#     book = {
#         "id": found_book.id,
#         "title": found_book.title,
#         "description": found_book.description
#     }

#     return book

# # vvvvvvvvvvvvvvvvv HELPER FUNCTIONS vvvvvvvvvvvvvvvvv


# def validate_book(book_id):

#     # Parameters are read as strings, so try to convert to int
#     try:
#         book_id = int(book_id)
#     except:
#         # If the string can't be converted, returns a status 400 message
#         response = {"message": f"book {book_id} invalid"}
#         abort(make_response(response, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     # If no matching book is found, return 404 error
#     response = {"message": f"book {book_id} not found"}
#     abort(make_response(response, 404))
