from lib.book import Book
from lib.author import Author
from lib.contract import Contract   

class ManyToMany:
    def __init__(self):
        self.authors = []
        self.books = []
        self.contracts = []

    def add_author(self, name):
        author = Author(name)
        self.authors.append(author)
        return author
    
    def add_book(self, title):  
        book = Book(title)
        self.books.append(book)
        return book
    


    def add_contract(self, author, book, date, royalties):
        contract = Contract(author, book, date, royalties)
        self.contracts.append(contract)
        return contract
    def contracts_by_date(self, date):
        return [contract for contract in self.contracts if contract.date == date]
    
    def contracts_by_author(self, author):
        return [contract for contract in self.contracts if contract.author == author]
    
    def contracts_by_book(self, book):
        return [contract for contract in self.contracts if contract.book == book]
    
    def royalties_by_author(self, author):
        return sum([contract.royalties for contract in self.contracts_by_author(author)])
    
    def royalties_by_book(self, book):
        return sum([contract.royalties for contract in self.contracts_by_book(book)])
    
    def royalties_by_date(self, date):
        return sum([contract.royalties for contract in self.contracts_by_date(date)])
    
    def royalties_by_author_and_date(self, author, date):
        return sum([contract.royalties for contract in self.contracts_by_author(author) if contract.date == date])
    
    def royalties_by_book_and_date(self, book, date):
        return sum([contract.royalties for contract in self.contracts_by_book(book) if contract.date == date])
    
    def royalties_by_author_and_book(self, author, book):
        return sum([contract.royalties for contract in self.contracts_by_author(author) if contract.book == book])
    
    def royalties_by_author_book_and_date(self, author, book, date):
        return sum([contract.royalties for contract in self.contracts_by_author(author) if contract.book == book and contract.date == date])
    
    def royalties_by_author_and_book(self, author, book):
        return sum([contract.royalties for contract in self.contracts_by_author(author) if contract.book == book])
    
    