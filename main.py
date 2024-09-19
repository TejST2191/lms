from library_system.models import Book, User

if __name__ == "__main__":
    book1 = Book(title = "title1", author = "author1", genre = "genre1")
    book2 = Book(title = "title2", author = "author2", genre = "genre2", is_borrowed = True)

    print(book1)
    print(book2)