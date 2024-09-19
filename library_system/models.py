class Book:

    def __init__(self, title : str, author : str, genre : str, is_borrowed : bool = False):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = is_borrowed
        self.due_date = None
    def __str__(self):
        return f"title is {self.title}, author is {self.author}, genre is {self.genre}"

class User:

    def __init__(self, name : str):
        self.name = name
        self.borrowed_books = []
    def __str__(self):
        return f"name is {self.name}, list is {self.borrowed_books}"
