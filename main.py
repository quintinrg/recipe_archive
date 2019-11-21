import json

rec_name = input("What is the name of the recipe?  ")

web_adr = input("Please input the url of the recipe.  ")

ing_one = input("What is the most prominent ingredient?  ")

ing_two = input("Secondary noteworthy ingredient?  ")

complexity = input("Is it high, medium, or low complexity?  ")

fanciness = input("Is it high, medium, or low fanciness?  ")

data = {}
data['recipes'] = []
data['recipes'].append(
    {
        'name': rec_name,
        'link': web_adr,
        'ingred 1': ing_one,
        'ingred 2': ing_two,
        'complex': complexity,
        'fancy': fanciness
    }
)

with open('data.json', 'a') as data_file:
  json.dump(data, data_file)