class ElementHandler:
    def element_message(self):
        pass

class BI(ElementHandler):
    def element_message(self):
        return "Big"

class M(ElementHandler):
    def element_message(self):
        return "Men"

class C(ElementHandler):
    def element_message(self):
        return "Cat"

class T(ElementHandler):
    def element_message(self):
        return "Bitter"

class E(ElementHandler):
    def element_message(self):
        return "Women"

class R(ElementHandler):
    def element_message(self):
        return "R"

class N(ElementHandler):
    def element_message(self):
        return "N"

# Використання обробників для класів R і N
r_instance = R()
n_instance = N()

# Виведення повідомлень про елементи
print("Для класу R:", r_instance.element_message())
print("Для класу N:", n_instance.element_message())