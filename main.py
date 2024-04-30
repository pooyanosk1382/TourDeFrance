import pycountry
countries = list(pycountry.countries)
for country in countries:
    print(country.name)