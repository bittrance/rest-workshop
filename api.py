#!/usr/bin/env python3

import json, uuid
from bottle import Bottle, HTTPResponse, request, response

# Some Bottle how-tos:
# request.query['foo']
# request.headers['some-header']
# response.headers['some-header'] = 'some-value'
# return HTTPResponse(
#     status=400,
#     body=json.dumps({'some': 'value'}),
#     headers={'Content-type': 'application/json'},
# )

Book = {
    'name': str,
    'author': str,
    'pages': int,
}

def validate(type, item):
    if item.keys() != type.keys():
        return False
    for field, dtype in type.items():
        try:
            dtype(item[field])
        except:
            return False
    return True

app = Bottle()

books = {}

@app.get('/books')
def get_books():
    # TODO: introduce pagination - next page in Link header
    return books

@app.post('/books')
def post_books():
    # TODO: Create a new book - reply with Location header
    # TODO: Introduce validation - what are the status codes?
    book_id = str(uuid.uuid4())
    book = request.json
    books[book_id] = book
    book['id'] = book_id
    return book

@app.get('/books/:id') # Magically handles HEAD requests too
def get_book(id):
    # TODO: Implement ETag, If-Modified
    # TODO: Implement 404
    etag = str(hash(json.dumps(books[id])))
    if etag == request.headers.get('if-modified'):
        return HTTPResponse(status=304)
    response.headers['ETag'] = etag
    return books[id]

@app.put('/books/:book_id')
def put_book(book_id):
    # TODO: Update existing book - refuse to create new
    pass

@app.delete('/books/:book_id')
def delete_book(book_id):
    # TODO: Delete an existing book
    pass

@app.post('/books/:id/borrow')
def borrow_book(id):
    pass

@app.post('/books/:id/loans')
@app.get('/books/:id/loans')
# TODO: Implement borrowing books
# TODO: Implement a search interface

if __name__ == '__main__':
    app.run(reloader=True, debug=True)
