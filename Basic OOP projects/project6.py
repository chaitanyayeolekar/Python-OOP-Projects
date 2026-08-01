class Book:
    def __init__(self, book_id,name, author):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.available = True


class Library:
    
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)# b1, b2, b3
        print(book.name,"added successfully")

    def issue_book(self, book_id):

        for book in self.books:
            if book.book_id == book_id:

                if book.available:
                    book.available = False
                    print(book.name,"issued successfully")
                else:
                    print(book.name, "is already issued")
                return
        print("book not found")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print(book.name,"returneed successfully")
                return 

        print("Book not found")

    def display_book(self):
        print("\nLibrary Books\n")

        for book in self.books:

            print("Book Id:", book.book_id)
            print("Book Name:", book.name)
            print("Author",book.author)

            if book.available:
                print("status : Available")
            else:
                print("Status : Issued")

            print("------------------------")
        

library = Library()

b1 = Book(101, "python", "Guido")
b2 = Book(102, "Java", "james Gosling")
b3 = Book(103, "C++", "jarne stroustrup")


library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.display_book()

library.issue_book(102)

library.display_book()

library.issue_book(102)

library.display_book()




#***************************************Library Management********************************

class Book:
    def __init__(self,book_id, name, author):
        self.book_id = book_id
        self.name= name
        self.author = author
        self.available = "Yes"

    def display(self):
        print("Book Id : ",self.book_id)
        print("Book Name : ",self.name)
        print("Author : ",self.author)
        print("Available : ",self.available)

    def issue_book(self):
        self.available = "No"
        print("Book issued")

    def return_book(self):
        self.available = "Yes"
        print("Book returned")

b1 = Book(101,"Python","Guido")

b2 = Book(102,"Jave","James")

b1.display()

b1.issue_book()
b1.return_book()
b1.display()