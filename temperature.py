def celsius_to_fahrenheit(celsius):
    try:
        if not isinstance(celsius, (int, float)):
            raise ValueError('Value must be a number')

        if celsius < -273.15:
            raise ValueError('Temperature cannot be below zero')

        fahrenheit= (celsius * 9/5)+32
        return float(fahrenheit)
    
    except ValueError as e:
        print(f'error: {e}')
        return None

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-273.15))
print(celsius_to_fahrenheit(-500))
print(celsius_to_fahrenheit("gaku"))
