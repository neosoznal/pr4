class ElementHandler:
    def element_message(self):
        pass

class B(ElementHandler):
    def element_message(self):
        return "Bob"

class P(ElementHandler):
    def element_message(self):
        return "Piter"

class C(ElementHandler):
    def element_message(self):
        return "Chloe"

class E(B):
    pass

class D(P):
    pass

# Використання обробників для класів E і D
e_instance = E()
d_instance = D()

# Виведення повідомлень про елементи
print("Для класу E:", e_instance.element_message())
print("Для класу D:", d_instance.element_message())
