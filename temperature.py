def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a number.")
    if fahrenheit < -459.67:
        raise ValueError("Temperature cannot be below absolute zero (-459.67°F).")

    celsius = (fahrenheit - 32) * 5/9
    return celsius

try:
    user_input = input("Enter temperature in Fahrenheit: ")
    fahrenheit_temp = float(user_input)
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is equal to {celsius_temp}°C")
except ValueError as ve:
    print(f"Error: Invalid input. Please enter a number. {ve}")
except TypeError as te:
    print(f"Error: {te}")
