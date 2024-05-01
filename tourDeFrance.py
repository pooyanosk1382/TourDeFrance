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
    country1 = multiprocessing.Process(target=tournament, args=(country[0], speed[0]))
    country2 = multiprocessing.Process(target=tournament, args=(country[1], speed[1]))
    country3 = multiprocessing.Process(target=tournament, args=(country[2], speed[2]))
    country4 = multiprocessing.Process(target=tournament, args=(country[3], speed[3]))
    country5 = multiprocessing.Process(target=tournament, args=(country[4], speed[4]))
    country6 = multiprocessing.Process(target=tournament, args=(country[5], speed[5]))
    country7 = multiprocessing.Process(target=tournament, args=(country[6], speed[6]))
    country8 = multiprocessing.Process(target=tournament, args=(country[7], speed[7]))
    country1.start()
    country2.start()
    country3.start()
    country4.start()
    country5.start()
    country6.start()
    country7.start()
    country8.start()
    country1.join()
    country2.join()
    country3.join()
    country4.join()
    country5.join()
    country6.join()
    country7.join()
    country8.join()