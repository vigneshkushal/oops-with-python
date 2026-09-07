class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author      
        self.pages = pages        

    def describe(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

my_book = Book("The Hobbit", "J.R.R. Tolkien", 310)

print(my_book.title)
print(my_book.describe())