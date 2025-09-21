SCOPE = 9/5

def celsius_to_fahrenheit(celsius):
    try:
        validation(celsius)
        return celsius * SCOPE + 32

    except ValueError as e:
        print(f'error: {e}')
        return None

def validation(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError(f'celsius value provided: {celsius} Value must be a number')

    if celsius < -273.15:
        raise ValueError('Temperature cannot be below zero')

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-273.15))
print(celsius_to_fahrenheit(-500))
print(celsius_to_fahrenheit("gaku"))
