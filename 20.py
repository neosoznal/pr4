class Person:
    def breakfast(self):
        return "Fruit"

class Man(Person):
    def breakfast(self):
        return "Donut"

class Worker(Person):
    def breakfast(self):
        return "Bacon"

class Woman(Person):
    def breakfast(self):
        return "Croissant"

class Parent(Person):
    pass

class Father(Parent):
    pass

class Mother(Parent):
    def breakfast(self):
        return "Fruit"

class WkgMan(Man, Worker):
    pass

class WkgWoman(Worker, Woman):
    pass

class WkgFather(WkgMan, Father):
    pass

class WkgMother(Mother, WkgWoman):
    pass

joan = WkgMother()
jim = WkgMan()

print("Відповідь Joan на повідомлення 'breakfast':", joan.breakfast())
print("Відповідь Jim на повідомлення 'breakfast':", jim.breakfast())