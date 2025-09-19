def validate_temperature_input(temp):
    if not isinstance(temp, (int, float)):
        raise TypeError("Input must be a number.")
    if temp < -459.67:
        raise ValueError("Temperature cannot be below absolute zero (-459.67°F).")
    return temp

def fahrenheit_to_celsius(fahrenheit):
    try:
        validate_temperature_input(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

# Test cases
print("\n--- Test Cases ---")
print(f"32°F = {fahrenheit_to_celsius(32)}°C")
print(f"100°F = {fahrenheit_to_celsius(100)}°C")
print(f"-459.67°F = {fahrenheit_to_celsius(-459.67)}°C")
print(f"-500°F = {fahrenheit_to_celsius(-500)}")
print(f"'gaku'°F = {fahrenheit_to_celsius('gaku')}")
