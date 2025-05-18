class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"El libro {self.title} ha sido devuelto")
        else:
            print(f"El libro {self.title} ya está disponible")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"El libro {book.title} ha sido prestado")
        else:
            print(f"El libro {book.title} no está disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"El libro {book.title} ha sido devuelto")
        else:
            print(f"El libro {book.title} no está prestado")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido añadido a la biblioteca")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido añadido a la biblioteca")

    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} por {book.author}")


# Ejemplo de uso
book1 = Book("El Quijote", "Miguel de Cervantes")
book2 = Book("Cien años de soledad", "Gabriel García Márquez")
book3 = Book("El libro de las siete noches", "Miguel de Cervantes")
user1 = User("Alice", 1)
user2 = User("Bob", 2)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_user(user1)
library.register_user(user2)

library.show_available_books()
user1.borrow_book(book1)
user1.borrow_book(book2)
user2.borrow_book(book1)
user1.return_book(book3)
    