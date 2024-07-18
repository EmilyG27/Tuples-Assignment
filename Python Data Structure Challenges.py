def add_book(books):
    title = input("What is the book title? ")
    author = input("Who is the author? ")
    book = (title, author)

    if book in books:
        print("That book is already in the library.")
    else:   
        books.append(book)
        print(books)

def main():
    books = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

    while True:
        choice = input("Do you want to add a book?(yes/no): ")
        if choice == "yes":
            add_book(books)
        else:
            break

if __name__ == "__main__":
    main()
        