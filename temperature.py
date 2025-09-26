FREEZING_OFFSET = 32
SCALE_FACTOR = 5/9
SLOPE = 9/5
ABSOLUTE_ZERO_FAHRENHEIT = -459.67
ABSOLUTE_ZERO_CELSIUS= -273.15


def validate_fahrenheit(temp):
    if not isinstance(temp, (int, float)):
        raise TypeError(f"Input '{temp}' must be a number.")
    if temp < ABSOLUTE_ZERO_FAHRENHEIT:
        raise ValueError(f"Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_FAHRENHEIT}°F) your input was {temp}.")
    return temp

def fahrenheit_to_celsius(fahrenheit):
    try:
        validated_fahrenheit= validate_fahrenheit(fahrenheit)
        celsius = (validated_fahrenheit - FREEZING_OFFSET) * SCALE_FACTOR
        return celsius
    except (ValueError, TypeError) as e:
        return f"Error: {e}"
  
def celsius_to_fahrenheit(celsius):
    try:
        validated_celsius= validation_celsius(celsius)
        return validated_celsius * SLOPE + FREEZING_OFFSET

    except ValueError as e:
        print(f'error: {e}')
        return None

def validation_celsius(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError(f'celsius value provided: {celsius} Value must be a number')

    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError('Temperature cannot be below zero')
    return celsius


# Test cases
print("\n--- Test Fahrenheit Cases ---")
print(f"32°F = {fahrenheit_to_celsius(32)}°C")
print(f"100°F = {fahrenheit_to_celsius(100)}°C")
print(f"-459.67°F = {fahrenheit_to_celsius(-459.67)}°C")
print(f"-500°F = {fahrenheit_to_celsius(-500)}")
print(f"'gaku'°F = {fahrenheit_to_celsius('gaku')}")

print("\n--- Test Celsius Cases ---")
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-273.15))
print(celsius_to_fahrenheit(-500))
print(celsius_to_fahrenheit("gaku"))
