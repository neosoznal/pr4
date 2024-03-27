class DeviceTypeHandler:
    def device_type(self):
        pass

class RadioModule(DeviceTypeHandler):
    def device_type(self):
        return "Радіомодуль"

class Buttons(DeviceTypeHandler):
    def device_type(self):
        return "Кнопки"

class Battery(DeviceTypeHandler):
    def device_type(self):
        return "Батарея"

class Screen(DeviceTypeHandler):
    def device_type(self):
        return "Екран"

class Processor(DeviceTypeHandler):
    def device_type(self):
        return "Процесор"

class Sensor(DeviceTypeHandler):
    def device_type(self):
        return "Сенсор"

class Radio(DeviceTypeHandler):
    pass

class Phone(DeviceTypeHandler):
    pass

class Tablet(DeviceTypeHandler):
    pass

# Використання обробників для різних класів
radio_module = RadioModule()
buttons = Buttons()
battery = Battery()
screen = Screen()
processor = Processor()
sensor = Sensor()

radio = Radio()
phone = Phone()
tablet = Tablet()

# Виведення повідомлень про тип пристрою
print("Тип пристрою для Радіо:", radio_module.device_type())
print("Тип пристрою для Кнопок:", buttons.device_type())
print("Тип пристрою для Батареї:", battery.device_type())
print("Тип пристрою для Екрану:", screen.device_type())
print("Тип пристрою для Процесору:", processor.device_type())
print("Тип пристрою для Сенсору:", sensor.device_type())

print("Тип пристрою для Радіо:", radio.device_type())
print("Тип пристрою для Телефону:", phone.device_type())
print("Тип пристрою для Планшету:", tablet.device_type())