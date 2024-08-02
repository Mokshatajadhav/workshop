
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre):
        if self._check_duplicate(title, author):
            print("This book already exists in the library.")
        else:
            self.books.append({'title': title, 'author': author, 'genre': genre})
            print(f"Book '{title}' by {author} added to the library.")

    def remove_book(self, title, author):
        self.books = [book for book in self.books if not (book['title'] == title and book['author'] == author)]
        print(f"Book '{title}' by {author} removed from the library.")

    def search_books(self, search_term, search_type='title'):
        return [book for book in self.books if search_term.lower() in book[search_type].lower()]

    def list_books(self):
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
        if not self.books:
            print("The library is empty.")

    def categorize_books(self):
        categorized = {}
        for book in self.books:
            categorized.setdefault(book['genre'], []).append(book)
        return categorized

    def _check_duplicate(self, title, author):
        return any(book for book in self.books if book['title'] == title and book['author'] == author)

# Example usage
library = Library()
library.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction")
library.add_book("1984", "George Orwell", "Dystopian")
library.add_book("Moby Dick", "Herman Melville", "Classic")

library.list_books()
print("Search by title '1984':", library.search_books("1984", "title"))
print("Search by author 'Harper Lee':", library.search_books("Harper Lee", "author"))

library.remove_book("1984", "George Orwell")
library.list_books()

categorized_books = library.categorize_books()
for genre, books in categorized_books.items():
    print(f"\nGenre: {genre}")
    for book in books:
        print(f"  Title: {book['title']}, Author: {book['author']}")

library.add_book("Moby Dick", "Herman Melville", "Classic")


    


