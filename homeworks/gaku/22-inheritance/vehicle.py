class Vehicle:
    def __init__(self, name, color, speed):
        self._name = name
        self._color = color
        self._max_speed = speed

    def start(self):
        print(f"{self._name} is starting")

    def stop(self):
        print(f"{self._name} is stopping")

    def show_info(self):
        print(f"{self._name} - Color: {self._color}, Max Speed: {self._max_speed} km/h")


class LandVehicle(Vehicle):
    def drive(self):
        print(f"{self._name} is driving on land")


class WaterVehicle(Vehicle):
    def sail(self):
        print(f"{self._name} is sailing on water")


class Car(LandVehicle):
    def honk(self):
        print(f"{self._name} says beep beep!")


class AmphibiousCar(Car, WaterVehicle):
    def switch_mode(self):
        print(f"{self._name} is switching between land and water mode")


vehicle = Vehicle("Generic Vehicle", "Gray", 100)
vehicle.start()  # Expected Output: Generic Vehicle is starting
vehicle.show_info()  # Expected Output: Generic Vehicle - Color: Gray, Max Speed: 100 km/h
vehicle.stop()  # Expected Output: Generic Vehicle is stopping

land_vehicle = LandVehicle("Truck", "Red", 120)
land_vehicle.start()  # Expected Output: Truck is starting
land_vehicle.drive()  # Expected Output: Truck is driving on land
land_vehicle.show_info()  # Expected Output: Truck - Color: Red, Max Speed: 120 km/h
land_vehicle.stop()  # Expected Output: Truck is stopping

water_vehicle = WaterVehicle("Boat", "White", 80)
water_vehicle.start()  # Expected Output: Boat is starting
water_vehicle.sail()  # Expected Output: Boat is sailing on water
water_vehicle.show_info()  # Expected Output: Boat - Color: White, Max Speed: 80 km/h
water_vehicle.stop()  # Expected Output: Boat is stopping

car = Car("Toyota", "Blue", 180)
car.start()  # Expected Output: Toyota is starting
car.drive()  # Expected Output: Toyota is driving on land
car.honk()  # Expected Output: Toyota says beep beep!
car.show_info()  # Expected Output: Toyota - Color: Blue, Max Speed: 180 km/h
car.stop()  # Expected Output: Toyota is stopping

amphibious = AmphibiousCar("AquaCar", "Green", 90)
amphibious.start()  # Expected Output: AquaCar is starting
amphibious.drive()  # Expected Output: AquaCar is driving on land
amphibious.honk()  # Expected Output: AquaCar says beep beep!
amphibious.switch_mode()  # Expected Output: AquaCar is switching between land and water mode
amphibious.sail()  # Expected Output: AquaCar is sailing on water
amphibious.show_info()  # Expected Output: AquaCar - Color: Green, Max Speed: 90 km/h
amphibious.stop()  # Expected Output: AquaCar is stopping
