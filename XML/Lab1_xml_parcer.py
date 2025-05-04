"""
Objective:
improving the student's skills in parsing XML documents;
using known methods of the Element object;

Scenario
Have you seen the weather forecast for the coming week? It’ll be an extremely sunny and warm week.
Familiarize yourself with the data in the forecast.xml file and then complete the following tasks:

Create a class named TemperatureConverter and its convert_celsius_to_fahrenheit method.
The convert_celsius_to_fahrenheit method should convert the temperature from Celsius to Fahrenheit.
Use the following formula:

F = 9/5 * C + 32.

Create a class named ForecastXmlParser and its parse method responsible for reading data from forecast.xml.
Use the TemperatureConverter class to convert the temperature from Celsius to Fahrenheit (rounded to one decimal place).
The parse method should print the following results:

Monday: 28 Celsius, 82.4 Fahrenheit
Tuesday: 27 Celsius, 80.6 Fahrenheit
Wednesday: 28 Celsius, 82.4 Fahrenheit
Thursday: 29 Celsius, 84.2 Fahrenheit
Friday: 29 Celsius, 84.2 Fahrenheit
Saturday: 32 Celsius, 89.6 Fahrenheit
Sunday: 33 Celsius, 91.4 Fahrenheit

"""
import xml.etree.ElementTree as ET


class TemperatureConverter:
    @staticmethod
    def convert_celsius_to_fahrenheit(celsius):
        """
        F = 9/5 * C + 32
        """
        fahrenheit = 9/5 * celsius + 32
        return fahrenheit


class ForecastXmlParser:

    convertor = TemperatureConverter()

    tree = ET.parse('forecast.xml')
    root = tree.getroot()

    for item in root:
        print(f'{item[0].text}: {item[1].text} celsius, '
              f'{convertor.convert_celsius_to_fahrenheit(float(item[1].text))} fahrenheit')
        
"""
Monday: 28 celsius, 82.4 fahrenheit
Tuesday: 27 celsius, 80.6 fahrenheit
Wednesday: 28 celsius, 82.4 fahrenheit
Thursday: 29 celsius, 84.2 fahrenheit
Friday: 29 celsius, 84.2 fahrenheit
Saturday: 31 celsius, 87.80000000000001 fahrenheit
Sunday: 32 celsius, 89.6 fahrenheit
"""
