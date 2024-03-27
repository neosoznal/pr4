class ForestAppearanceHandler:
    def forest_appearance(self):
        pass

class OnSand(ForestAppearanceHandler):
    def forest_appearance(self):
        return "Ліс на піску"

class OnSwamp(ForestAppearanceHandler):
    def forest_appearance(self):
        return "Ліс на болоті"

class Pine(ForestAppearanceHandler):
    def forest_appearance(self):
        return "Хвойний ліс"

class Leafed(ForestAppearanceHandler):
    def forest_appearance(self):
        return "Листяний ліс"

class Taiga(ForestAppearanceHandler):
    pass

class Shifted(ForestAppearanceHandler):
    pass

# Використання обробників для різних класів
on_sand = OnSand()
on_swamp = OnSwamp()
pine = Pine()
leafed = Leafed()

taiga = Taiga()
shifted = Shifted()

# Виведення повідомлень про вигляд лісу
print("Вигляд лісу на піску:", on_sand.forest_appearance())
print("Вигляд лісу на болоті:", on_swamp.forest_appearance())
print("Вигляд хвойного лісу:", pine.forest_appearance())
print("Вигляд листяного лісу:", leafed.forest_appearance())

print("Вигляд тайги:", taiga.forest_appearance())
print("Вигляд зміненого лісу:", shifted.forest_appearance())