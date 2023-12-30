class Book():
    def __init__(self, title, author, price, pages) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

    def __str__(self) -> str:
        return "Title: {}, Author: {}, Price: {}, Pages: {}".format(self.title, self.author, self.price, self.pages)
    
    def __len__(self) -> int:
        return self.pages
    
    def __del__(self) -> None:
        print("A book was destroyed")
    
x = Book("Book One", "Author One", 200000, 500)
# print(x)
# print(len(x))
del x