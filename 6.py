class City:
    def city_name(self):
        pass

class Strasbourg(City):
    def city_name(self):
        return "Страсбург"

class Toulouse(City):
    def city_name(self):
        return "Тулуза"

class Marseille(City):
    def city_name(self):
        return "Марсель"

class Birmingham(City):
    def city_name(self):
        return "Бірмінгем"

class Manchester(City):
    def city_name(self):
        return "Манчестер"

class Canberra(City):
    def city_name(self):
        return "Канберра"

class Sydney(City):
    def city_name(self):
        return "Сідней"

class Melbourne(City):
    def city_name(self):
        return "Мельбурн"

class Europe:
    pass

class Australia:
    pass

# Використання обробників для різних класів
strasbourg = Strasbourg()
toulouse = Toulouse()
marseille = Marseille()
birmingham = Birmingham()
manchester = Manchester()

canberra = Canberra()
sydney = Sydney()
melbourne = Melbourne()

europe = Europe()
australia = Australia()

# Виведення назв міст
print("Назва міста в Європі:", strasbourg.city_name())
print("Назва міста в Європі:", toulouse.city_name())
print("Назва міста в Європі:", marseille.city_name())
print("Назва міста в Європі:", birmingham.city_name())
print("Назва міста в Європі:", manchester.city_name())

print("Назва міста в Австралії:", canberra.city_name())
print("Назва міста в Австралії:", sydney.city_name())
print("Назва міста в Австралії:", melbourne.city_name())