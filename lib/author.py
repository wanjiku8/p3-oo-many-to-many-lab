class Author:
    def __init__(self, name):
        self.name = name

class Contract:
    def __init__(self, book, author, date, royalties):
        self.book = book
        self.author = author
        self.date = date
        self.royalties = royalties
