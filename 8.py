class SizeAppearanceHandler:
    def size_appearance(self):
        pass

class TwoFour(SizeAppearanceHandler):
    def size_appearance(self):
        return "2/4"

class FourEight(SizeAppearanceHandler):
    def size_appearance(self):
        return "4/8"

class ThreeEight(SizeAppearanceHandler):
    def size_appearance(self):
        return "3/8"

class FourFour(SizeAppearanceHandler):
    def size_appearance(self):
        return "4/4"

class ThreeFour(SizeAppearanceHandler):
    def size_appearance(self):
        return "3/4"

class SixEight(SizeAppearanceHandler):
    def size_appearance(self):
        return "6/8"

class Sonata(SizeAppearanceHandler):
    pass

class Polka(SizeAppearanceHandler):
    pass

# Використання обробників для різних класів
two_four = TwoFour()
four_eight = FourEight()
three_eight = ThreeEight()
four_four = FourFour()
three_four = ThreeFour()
six_eight = SixEight()

sonata = Sonata()
polka = Polka()

# Виведення повідомлень про вигляд розміру
print("Вигляд розміру для 2/4:", two_four.size_appearance())
print("Вигляд розміру для 4/8:", four_eight.size_appearance())
print("Вигляд розміру для 3/8:", three_eight.size_appearance())
print("Вигляд розміру для 4/4:", four_four.size_appearance())
print("Вигляд розміру для 3/4:", three_four.size_appearance())
print("Вигляд розміру для 6/8:", six_eight.size_appearance())

print("Вигляд розміру для Сонати:", sonata.size_appearance())
print("Вигляд розміру для Польки:", polka.size_appearance())