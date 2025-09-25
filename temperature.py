SLOPE = 9/5
MAGIC_NUMBER= -273.15
Y_INTERCEPT= 32

def celsius_to_fahrenheit(celsius):
    try:
        validated= validation(celsius)
        return celsius * SLOPE + Y_INTERCEPT

    except ValueError as e:
        print(f'error: {e}')
        return None

def validation(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError(f'celsius value provided: {celsius} Value must be a number')

    if celsius < MAGIC_NUMBER:
        raise ValueError('Temperature cannot be below zero')
    return celsius

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-273.15))
print(celsius_to_fahrenheit(-500))
print(celsius_to_fahrenheit("gaku"))
