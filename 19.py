class ColorRepresentative:
    def get_color_name(self):
        pass

class Red(ColorRepresentative):
    def get_color_name(self):
        return "Червоний"

class Blue(ColorRepresentative):
    def get_color_name(self):
        return "Синій"

class Green(ColorRepresentative):
    def get_color_name(self):
        return "Зелений"

class Orange(ColorRepresentative):
    def get_color_name(self):
        return "Помаранчевий"

class Violet(ColorRepresentative):
    def get_color_name(self):
        return "Фіолетовий"

# Використання представників для класів "Помаранчевий" і "Фіолетовий"
orange_instance = Orange()
violet_instance = Violet()

# Виведення повідомлень про назву кольору
print("Для класу 'Помаранчевий':", orange_instance.get_color_name())
print("Для класу 'Фіолетовий':", violet_instance.get_color_name())