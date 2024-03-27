class Error:
    def message(self):
        return "Error"

class Success:
    def message(self):
        return "Success"

class Begin:
    def __init__(self):
        self.handler = Error()  # Встановлюємо обробник помилок для класу Begin

    def handle(self):
        return self.handler.message()

class ThiFive:
    def __init__(self):
        self.handler = Success()  # Встановлюємо обробник успіху для класу ThiFive

    def handle(self):
        return self.handler.message()

# Створення об'єктів і виклик обробників
begin_instance = Begin()
thi_five_instance = ThiFive()

# Виведення повідомлень
print("Повідомлення для класу Begin:", begin_instance.handle())
print("Повідомлення для класу ThiFive:", thi_five_instance.handle())
