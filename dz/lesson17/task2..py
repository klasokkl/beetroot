class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return f"{self.name} ({self.country}, born {self.birthday})"


class Book:
    total_books = 0  # class variable for counting all books

    def __init__(self, name: str, year: int, author: Author):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author class")
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1
        author.books.append(self)

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={repr(self.author)})"

    def __str__(self):
        return f"'{self.name}' by {self.author.name}, {self.year}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author) -> Book:
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}')"

    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books and {len(self.authors)} authors"


tolkien = Author("J.R.R. Tolkien", "UK", "1892-01-03")
rowling = Author("J.K. Rowling", "UK", "1965-07-31")

lib = Library("City Library")

lib.new_book("The Hobbit", 1937, tolkien)
lib.new_book("Harry Potter and the Philosopher's Stone", 1997, rowling)
lib.new_book("The Lord of the Rings", 1954, tolkien)

print(lib.group_by_author(tolkien))  
print(lib.group_by_year(1997))       

print("Total books:", Book.total_books)
