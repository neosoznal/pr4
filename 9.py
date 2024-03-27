class HouseAppearanceHandler:
    def house_appearance(self):
        pass

class WithLand(HouseAppearanceHandler):
    def house_appearance(self):
        return "З земельною ділянкою"

class WithoutLand(HouseAppearanceHandler):
    def house_appearance(self):
        return "Без земельної ділянки"

class ForManyFamilies(HouseAppearanceHandler):
    def house_appearance(self):
        return "Для багатьох сімей"

class ForOneFamily(HouseAppearanceHandler):
    def house_appearance(self):
        return "Для однієї сім'ї"

class Villets(HouseAppearanceHandler):
    pass

class Apartments(HouseAppearanceHandler):
    pass

# Використання обробників для різних класів
with_land = WithLand()
without_land = WithoutLand()
for_many_families = ForManyFamilies()
for_one_family = ForOneFamily()

villets = Villets()
apartments = Apartments()

# Виведення повідомлень про вигляд будинку
print("Вигляд будинку для земельною ділянкою:", with_land.house_appearance())
print("Вигляд будинку без земельною ділянкою:", without_land.house_appearance())
print("Вигляд будинку для багатьох сімей:", for_many_families.house_appearance())
print("Вигляд будинку для однієї сім'ї:", for_one_family.house_appearance())

print("Вигляд будинку для вілл:", villets.house_appearance())
print("Вигляд будинку для квартир:", apartments.house_appearance())