class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

    def search(self, keyword):
        return [b for b in self.books if keyword.lower() in b["title"].lower() or keyword.lower() in b["author"].lower()]

# Test
lib = Library()
lib.add_book("Python Basics", "John")
lib.add_book("Data Science", "Alice")
print(lib.search("Python"))
