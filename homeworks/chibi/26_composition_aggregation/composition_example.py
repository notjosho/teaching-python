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
        return (
            f"{self.brand} {self.model} - "
            f"Processor: {self.processor.model} ({self.processor.speed}GHz) - "
            f"Battery: {self.battery.capacity}mAh ({self.battery.charge_level}% charged)"
        )

    def use_phone(self, minutes):
        reduction = minutes // 10
        self.battery.charge_level -= reduction
        if self.battery.charge_level < 0:
            self.battery.charge_level = 0

        return self.battery.charge_level

    def get_battery_status(self):
        level = self.battery.charge_level
        if level > 50:
            return "High"
        elif level > 20:
            return "Normal"
        else:
            return "Low"
