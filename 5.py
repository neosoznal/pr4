class TransportTypeHandler:
    def transport_type(self):
        pass

class Land(TransportTypeHandler):
    def transport_type(self):
        return "Лідер"

class Water(TransportTypeHandler):
    def transport_type(self):
        return "Морський"

class Boat(TransportTypeHandler):
    pass

class Gibrid(TransportTypeHandler):
    pass

# Використання обробників для різних класів
land = Land()
water = Water()

boat = Boat()
gibrid = Gibrid()

# Виведення повідомлень про вид транспорту
print("Вид транспорту для Land:", land.transport_type())
print("Вид транспорту для Water:", water.transport_type())

print("Вид транспорту для Boat:", boat.transport_type())
print("Вид транспорту для Gibrid:", gibrid.transport_type())