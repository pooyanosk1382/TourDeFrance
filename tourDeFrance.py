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


def tournament(countryName, countrySpeed, competitionTime):
    for i in range(2):
        competitionTime.value += race(countryName, countrySpeed, i)
    print(str(countryName) + ' covered all distance in ' + str(competitionTime.value) + 'seconds.')
    return competitionTime


if __name__ == '__main__':
    countries = list(pycountry.countries)
    random_numbers = [random.randint(0, len(countries) - 1) for _ in range(8)]
    speed = [round(random.uniform(0.4, 0.5), 2) for _ in range(8)]
    country = [''] * 8
    cyclist = [None] * 8
    competitionTimes = [None] * 8
    for i in range(8):
        competitionTimes[i] = multiprocessing.Value('d', 0.0)
    for i in range(8):  # names of countries in the competition
        country[i] = countries[random_numbers[i]].name
    for i in range(8):  # print countries and their speed
        print(country[i], speed[i])
    for i in range(8):  # creating processes with target function of tournament
        cyclist[i] = multiprocessing.Process(target=tournament, args=(country[i], speed[i], competitionTimes[i]))
    for i in range(8):  # start processes
        cyclist[i].start()
    for i in range(8):  # join processes
        cyclist[i].join()
