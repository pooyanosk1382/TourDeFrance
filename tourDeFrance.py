import pycountry
import random
import time
import multiprocessing


def race(countryName, countrySpeed, day):
    startTime = time.time()
    distance = 0
    for i in range(10):
        distance += 1
        time.sleep(countrySpeed)
    endTime = time.time()
    period = endTime - startTime
    print(str(countryName) + ' covered distance in ' + str(period) + ' seconds in day ' + str(day+1))
    return period


def tournament(countryName, countrySpeed):
    competitionTime = 0
    for i in range(10):
        competitionTime += race(countryName, countrySpeed, i)
    print(str(countryName) + ' covered all distance in ' + str(competitionTime) + 'seconds.')


if __name__ == '__main__':
    countries = list(pycountry.countries)
    random_numbers = [random.randint(0, len(countries) - 1) for _ in range(8)]
    speed = [round(random.uniform(0.4, 0.5), 2) for _ in range(8)]
    country = [''] * 8
    for i in range(8):
        country[i] = countries[random_numbers[i]].name
    for i in range(8):
        print(country[i], speed[i])
    cyclist = [None] * 8
    for i in range(8):
        cyclist[i] = multiprocessing.Process(target=tournament, args=(country[i], speed[i]))
    for i in range(8):
        cyclist[i].start()
    for i in range(8):
        cyclist[i].join()
