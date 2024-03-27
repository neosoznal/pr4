class NatureElementHandler:
    def element_message(self):
        pass

class AI(NatureElementHandler):
    def element_message(self):
        return "Air"

class GR(NatureElementHandler):
    def element_message(self):
        return "Ground"

class FI(NatureElementHandler):
    def element_message(self):
        return "Fire"

class WA(NatureElementHandler):
    def element_message(self):
        return "Water"

class SG(NatureElementHandler):
    pass

class NO(NatureElementHandler):
    pass

# Використання обробників для класів SG і NO
sg_element = SG()
no_element = NO()

# Виведення повідомлень про елемент природи
print("Для класу SG:", sg_element.element_message())
print("Для класу NO:", no_element.element_message())