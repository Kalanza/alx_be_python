FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    temp_celsius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(temp_celsius)

def convert_to_fahrenheit(celsius):
    temp_fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(temp_fahrenheit) 

convert_to_celsius(180)
convert_to_fahrenheit(100)