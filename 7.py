class AnimalAppearanceHandler:
    def appearance(self):
        pass

class Herbivores(AnimalAppearanceHandler):
    def appearance(self):
        return "Травоїдні"

class Carnivores(AnimalAppearanceHandler):
    def appearance(self):
        return "Хижаки"

class WarmBlooded(AnimalAppearanceHandler):
    def appearance(self):
        return "Теплокровні"

class CoolBlooded(AnimalAppearanceHandler):
    def appearance(self):
        return "Холоднокровні"

class Cobra(AnimalAppearanceHandler):
    pass

class BrownBear(AnimalAppearanceHandler):
    pass

# Використання обробників для різних класів
herbivores = Herbivores()
carnivores = Carnivores()
warm_blooded = WarmBlooded()
cool_blooded = CoolBlooded()

cobra = Cobra()
brown_bear = BrownBear()

# Виведення повідомлень про вигляд тварини
print("Вигляд тварини для травоїдних:", herbivores.appearance())
print("Вигляд тварини для хижаків:", carnivores.appearance())
print("Вигляд тварини для теплокровних:", warm_blooded.appearance())
print("Вигляд тварини для холоднокровних:", cool_blooded.appearance())

print("Вигляд тварини для кобри:", cobra.appearance())
print("Вигляд тварини для бурого ведмедя:", brown_bear.appearance())