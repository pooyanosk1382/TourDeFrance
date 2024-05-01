import pycountry
import random
import time
import multiprocessing
import numpy as np


def race(countryName, countrySpeed, day, period):
    startTime = time.time()
    distance = 0
    for i in range(100):
        distance += 1
        time.sleep(countrySpeed)
    endTime = time.time()
    period = endTime - startTime
    print(str(countryName) + ' covered distance in ' + str(period) + ' seconds in day ' + str(day+1))
    return period


if __name__ == '__main__':
    countries = list(pycountry.countries)
    randomNumbers = [random.randint(0, len(countries) - 1) for _ in range(8)]
    speed = [round(random.uniform(0.1, 0.2), 4) for _ in range(8)]
    country = [''] * 8
    cyclist = [None] * 8
    competitionTimes = [None] * 8
    competition = [0] * 8

    for i in range(8):  # names of countries in the competition
        country[i] = countries[randomNumbers[i]].name

    for i in range(8):  # print countries and their speed
        print(country[i], speed[i])

    for day in range(21):

        for i in range(8):  # creating some shared data that help us find the winner
            competitionTimes[i] = multiprocessing.Value('d', 0.0)

        for i in range(8):  # creating processes with target function of tournament
            cyclist[i] = multiprocessing.Process(target=race, args=(country[i], speed[i], day, competitionTimes[i]))

        for i in range(8):  # start processes
            cyclist[i].start()

        for i in range(8):  # join processes
            cyclist[i].join()

        for i in range(8):
            competition[i] += competitionTimes[i].value

    topThreeIndices = np.argsort(competition)[:3]
    topThreeCountries = [country[i] for i in topThreeIndices]
    print(topThreeCountries)
