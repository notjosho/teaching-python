class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
        self.charge_level = 100


class Processor:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed


class Smartphone:
    def __init__(
        self, brand, model, battery_capacity, processor_model, processor_speed
    ):
        self.brand = brand
        self.model = model
        self.battery = Battery(battery_capacity)
        self.processor = Processor(processor_model, processor_speed)

    def get_specs(self):
        return f"{self.brand} {self.model} - Processor: {self.processor.model} ({self.processor.speed}GHz) - Battery: {self.battery.capacity}mAh ({self.battery.charge_level}% charged)"

    def use_phone(self, minutes):
        self.battery.charge_level -= minutes // 10
        if self.battery.charge_level <= 0:
            self.battery.charge_level = 0
        return self.battery.charge_level

    def get_battery_status(self):
        if self.battery.charge_level > 50:
            return "High"
        elif 50 >= self.battery.charge_level > 20:
            return "Normal"
        else:
            return "Low"


phone = Smartphone("Apple", "iPhone 14", 3279, "A15 Bionic", 3.2)

print(phone.use_phone(0))
print(phone.get_battery_status())
