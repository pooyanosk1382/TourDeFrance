import pycountry
import random

countries = list(pycountry.countries)
random_numbers = [random.randint(0, len(countries)) for _ in range(8)]
speed = [round(random.uniform(0.2, 0.5), 2) for _ in range(8)]

country1 = countries[random_numbers[0]].name
country2 = countries[random_numbers[1]].name
country3 = countries[random_numbers[2]].name
country4 = countries[random_numbers[3]].name
country5 = countries[random_numbers[4]].name
country6 = countries[random_numbers[5]].name
country7 = countries[random_numbers[6]].name
country8 = countries[random_numbers[7]].name

print(country1, speed[0])
print(country2, speed[1])
print(country3, speed[2])
print(country4, speed[3])
print(country5, speed[4])
print(country6, speed[5])
print(country7, speed[6])
print(country8, speed[7])