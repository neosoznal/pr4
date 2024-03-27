class BookAppearanceHandler:
    def book_appearance(self):
        pass

class Native(BookAppearanceHandler):
    def book_appearance(self):
        return "Рідна книга"

class Foreign(BookAppearanceHandler):
    def book_appearance(self):
        return "Іноземна книга"

class Science(BookAppearanceHandler):
    def book_appearance(self):
        return "Наукова книга"

class Art(BookAppearanceHandler):
    def book_appearance(self):
        return "Художня книга"

class ForeignScienceFiction(BookAppearanceHandler):
    pass

class NativeScience(BookAppearanceHandler):
    pass

# Використання обробників для різних класів
native = Native()
foreign = Foreign()
science = Science()
art = Art()

foreign_science_fiction = ForeignScienceFiction()
native_science = NativeScience()

# Виведення повідомлень про вигляд книги
print("Вигляд книги для рідних:", native.book_appearance())
print("Вигляд книги для іноземних:", foreign.book_appearance())
print("Вигляд книги для наукових:", science.book_appearance())
print("Вигляд книги для художніх:", art.book_appearance())

print("Вигляд книги для іноземних наукових фантастики:", foreign_science_fiction.book_appearance())
print("Вигляд книги для рідних наукових:", native_science.book_appearance())