class Error:
    def message_handler(self):
        return "Error"

class Success:
    def message_handler(self):
        return "Success"

class Begin:
    def __init__(self):
        self.error_handler = Error()
        self.success_handler = Success()

    def handle_message(self):
        # Приклад логіки, що викликає обробник повідомлень
        return self.error_handler.message_handler()  # Можна також викликати success_handler

class B:
    def __init__(self):
        self.error_handler = Error()
        self.success_handler = Success()

    def handle_message(self):
        # Приклад логіки, що викликає обробник повідомлень
        return self.success_handler.message_handler()  # Можна також викликати error_handler

# Створення екземплярів класів і виклик обробників повідомлень
begin_instance = Begin()
b_instance = B()

begin_message = begin_instance.handle_message()
b_message = b_instance.handle_message()

print("Message from Begin:", begin_message)
print("Message from B:", b_message)