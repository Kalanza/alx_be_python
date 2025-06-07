FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    temp_celsius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_celsius

def convert_to_fahrenheit(celsius):
    temp_fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return temp_fahrenheit 

x = float(input('Enter the temperature to convert: '))
y = input('Is this temperature in Celsius or Fahrenheit? (C/F) ')
if y == 'C':
    a = convert_to_fahrenheit(x)
    print(a,'°C is',x,'°F')
else:
    a = convert_to_celsius(x)
    print(x,'°F is',a,'°C')
