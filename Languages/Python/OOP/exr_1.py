class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_available(self):
        return self.available

    def display_info(self):
        print(
            f"{self.title} - {self.author} ({self.year}) - {"Available" if self.available == True else "Borrowed"}")

    def borrow(self):
        if (self.available == True):
            self.available = False
            print("Muon thanh cong!!!")
        else:
            print("Khong thanh cong!! Sach da duoc muon")

    def return_book(self):
        self.available = True
        print("Tra thanh cong")


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        # title = input()
        # author = input()
        # year = int(input())

        # book.set_title(title)
        # book.set_author(author)
        # book.set_year(year)

        return self.book_list.append(book)

    def show_all_books(self):
        print("--- Danh sách sách trong thư viện ---")
        for book in self.book_list:
            book.display_info()

    def search_by_author(self, author_name):
        found = False
        print(f"\n📚 Sách của tác giả '{author_name}':")
        for book in self.book_list:
            if book.author.lower() == author_name.lower():
                book.display_info()
                found = True
        if not found:
            print("Không tìm thấy tác giả này.")


# Tạo đối tượng Book
b1 = Book("Harry Potter", "J.K. Rowling", 1997)
b2 = Book("Clean Code", "Robert C. Martin", 2008)
b3 = Book("Effective Java", "Joshua Bloch", 2018)

# Tạo thư viện và thêm sách
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

# Hiển thị và tìm kiếm
lib.show_all_books()
lib.search_by_author("Robert C. Martin")
