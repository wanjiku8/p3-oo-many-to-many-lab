from lib.author import Author
from lib.book import Book

class Contract:
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):  # ✅ Fix: Use the Author class
            raise TypeError("author must be an instance of Author")
        
        if not isinstance(book, Book):  # ✅ Fix: Use the Book class
            raise TypeError("book must be an instance of Book")

        if not isinstance(date, str):
            raise TypeError("date must be a string")

        if not isinstance(royalties, (int, float)):
            raise TypeError("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

