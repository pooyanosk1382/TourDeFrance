import pycountry
import random
import time
import multiprocessing

countries = list(pycountry.countries)
random_numbers = [random.randint(0, len(countries)) for _ in range(8)]
speed = [round(random.uniform(0.2, 0.5), 2) for _ in range(8)]
country = [''] * 8
for i in range(8):
    country[i] = countries[random_numbers[i]].name

for i in range(8):
    print(country[i], speed[i])


def tournament(countryName, countrySpeed, day):
    startTime = time.time()
    distance = 0
    for i in range(100):
        distance += 1
        time.sleep(countrySpeed)
    endTime = time.time()
    print(str(countryName) + ' covered distance in ' + str(endTime - startTime) + ' seconds in day ' + str(day))


tournament(country[0], speed[0], 5)