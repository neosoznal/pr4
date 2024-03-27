class BookTitleHandler:
    def book_title(self):
        pass

class ChroniclesOfNarnia(BookTitleHandler):
    def book_title(self):
        return "Хроніки Нарнії"

class AmphibianMan(BookTitleHandler):
    def book_title(self):
        return "Людина-амфібія"

class GulliversTravels(BookTitleHandler):
    def book_title(self):
        return "Подорож Гуллівера"

class IslandsInTheStream(BookTitleHandler):
    def book_title(self):
        return "Острови в океані"

class CrimeAndPunishment(BookTitleHandler):
    def book_title(self):
        return "Злочин і кара"

class TheManInBrownSuit(BookTitleHandler):
    def book_title(self):
        return "Людина в коричневому костюмі"

class MurderOnTheMorgueStreet(BookTitleHandler):
    def book_title(self):
        return "Вбивство на вулиці Морг"

class SciFi(BookTitleHandler):
    pass

class Detective(BookTitleHandler):
    pass

# Використання обробників для різних класів
narnia = ChroniclesOfNarnia()
amphibian_man = AmphibianMan()
gullivers_travels = GulliversTravels()
islands = IslandsInTheStream()
crime_and_punishment = CrimeAndPunishment()
man_in_brown_suit = TheManInBrownSuit()
murder_on_morgue_street = MurderOnTheMorgueStreet()

sci_fi = SciFi()
detective = Detective()

# Виведення повідомлень про назву книги
print("Назва книги фантастики:", narnia.book_title())
print("Назва книги фантастики:", amphibian_man.book_title())
print("Назва книги фантастики:", gullivers_travels.book_title())
print("Назва книги фантастики:", islands.book_title())

print("Назва книги детективу:", crime_and_punishment.book_title())
print("Назва книги детективу:", man_in_brown_suit.book_title())
print("Назва книги детективу:", murder_on_morgue_street.book_title())