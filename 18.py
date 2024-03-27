class ColorHandler:
    def color_appearance(self):
        pass

class Red(ColorHandler):
    def color_appearance(self):
        return "Червоний"

class Blue(ColorHandler):
    def color_appearance(self):
        return "Синій"

class Green(ColorHandler):
    def color_appearance(self):
        return "Зелений"

class Orange(Red):
    pass

class Violet(Blue):
    pass

# Виклик обробників для класів "Помаранчевий" і "Фіолетовий"
orange_instance = Orange()
violet_instance = Violet()

# Виведення повідомлень про вигляд кольорів
print("Для класу 'Помаранчевий':", orange_instance.color_appearance())
print("Для класу 'Фіолетовий':", violet_instance.color_appearance())