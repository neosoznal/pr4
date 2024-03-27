class FruitHandler:
    def fruit_name(self):
        pass

class Grapefruit(FruitHandler):
    def fruit_name(self):
        return "Грейпфрут"

class Mandarin(FruitHandler):
    def fruit_name(self):
        return "Мандарин"

class Orange(FruitHandler):
    def fruit_name(self):
        return "Апельсин"

class Lime(FruitHandler):
    def fruit_name(self):
        return "Лайм"

class Orlando(FruitHandler):
    def fruit_name(self):
        return "Орландо"

class Rangpur(FruitHandler):
    def fruit_name(self):
        return "Рангпур"

# Використання обробників для класів "Орландо" і "Рангпур"
orlando_instance = Orlando()
rangpur_instance = Rangpur()

# Виведення повідомлень про назву фруктів
print("Для класу 'Орландо':", orlando_instance.fruit_name())
print("Для класу 'Рангпур':", rangpur_instance.fruit_name())