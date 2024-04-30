import pycountry
import random

countries = list(pycountry.countries)
random_numbers = [random.randint(0, len(countries)) for _ in range(8)]
speed = [round(random.uniform(0.2, 0.5), 2) for _ in range(8)]
country = [''] * 8
for i in range(8):
    country[i] = countries[random_numbers[i]].name

for i in range(8):
    print(country[i], speed[i])