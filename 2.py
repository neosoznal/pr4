class Instrument:
    def message_handler(self):
        return "Musical instrument"


class Drum(Instrument):
    pass


class Brass(Instrument):
    pass


class Keyboard(Instrument):
    pass


# Виклик обробників для класів "Ударні", "Духові", "Клавішні"
drum = Drum()
brass = Brass()
keyboard = Keyboard()

print(drum.message_handler())  # Виведе: Musical instrument
print(brass.message_handler())  # Виведе: Musical instrument
print(keyboard.message_handler())  # Виведе: Musical instrument