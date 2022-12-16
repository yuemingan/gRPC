from concurrent import futures

import grpc


import inventory_pb2
import inventory_pb2_grpc



class InventoryService(inventory_pb2_grpc.InventoryServiceServicer):
# I used a dictionary in class InventoryService to store the books, the key is the isbn number, and other information 
# of the book is store in the value, so that in GetBook function, I can retrieve book according to isbn number
    def __init__(self):
        self.books = books = {
    "12345678": {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": Genre.FICTION,
        "publishing_year": 1954
    },
    "23456789": {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": Genre.FICTION,
        "publishing_year": 1965
    },
    "34567890": {
        "title": "The Hound of the Baskervilles",
        "author": "Arthur Conan Doyle",
        "genre": Genre.FICTION,
        "publishing_year": 1902
    },
    "45678901": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": Genre.FICTION,
        "publishing_year": 1813
    }
}

    def CreateBook(self, request, context):
        try: 
            self.books[request.book.isbn] = request.book
            # Return a message indicating success
            return CreateBookResponse(success=True, message="Book created successfully.")
        except RpcError as error:
            # Return a message indicating failure
            return CreateBookResponse(success=False, message=str(error))

    def GetBook(self, request, context):
        # Get the book with the specified ISBN
        book = self.books.get(request.isbn, None)

        if book:
         # Return the book if it exists
            return self.books.get(request.isbn)
        else:
        # Raise an error if the book does not exist
            raise grpc.RpcError('Book not found')

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  inventory_pb2_grpc.add_InventoryServiceServicer_to_server(
      InventoryService(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()


if __name__ == '__main__':

    serve()

class CreateBookResponse(Servicer):
  def __init__(self, success=None, message=None):
    self.success = success
    self.message = message