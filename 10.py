class RadiationAppearanceHandler:
    def radiation_appearance(self):
        pass

class Radio(RadiationAppearanceHandler):
    def radiation_appearance(self):
        return "Радіо"

class Sound(RadiationAppearanceHandler):
    def radiation_appearance(self):
        return "Звук"

class VisibleLight(RadiationAppearanceHandler):
    def radiation_appearance(self):
        return "Видимі світло"

class Infrared(RadiationAppearanceHandler):
    def radiation_appearance(self):
        return "Інфрачервоне випромінювання"

class Ultraviolet(RadiationAppearanceHandler):
    def radiation_appearance(self):
        return "Ультрафіолетове випромінювання"

class Gamma(RadiationAppearanceHandler):
    def radiation_appearance(self):
        return "Гамма-випромінювання"

class XRay(RadiationAppearanceHandler):
    def radiation_appearance(self):
        return "Рентгенівське випромінювання"

class LightBulb(RadiationAppearanceHandler):
    pass

class Radio(RadiationAppearanceHandler):
    pass

# Використання обробників для різних класів
radio = Radio()
sound = Sound()
visible_light = VisibleLight()
infrared = Infrared()
ultraviolet = Ultraviolet()
gamma = Gamma()
x_ray = XRay()

light_bulb = LightBulb()
radio = Radio()

# Виведення повідомлень про вигляд випромінювання
print("Вигляд випромінювання для Радіо:", radio.radiation_appearance())
print("Вигляд випромінювання для Звуку:", sound.radiation_appearance())
print("Вигляд випромінювання для Видимого світла:", visible_light.radiation_appearance())
print("Вигляд випромінювання для Інфрачервоного випромінювання:", infrared.radiation_appearance())
print("Вигляд випромінювання для Ультрафіолетового випромінювання:", ultraviolet.radiation_appearance())
print("Вигляд випромінювання для Гамма-випромінювання:", gamma.radiation_appearance())
print("Вигляд випромінювання для Рентгенівського випромінювання:", x_ray.radiation_appearance())

print("Вигляд випромінювання для Лампочки:", light_bulb.radiation_appearance())
print("Вигляд випромінювання для Рації:", radio.radiation_appearance())