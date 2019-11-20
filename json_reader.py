import json

with open('data.json') as data_file:
    data = json.load(data_file)

# print(data)

s_f = input("please enter your ingredient! ")

for name in data['recipes']:
    if s_f in name["ingred 1"] or s_f in name["ingred 2"]:
        print(f'{name["name"]} at {name["link"]},')
        # print(name["ingred 1"])
        # print(name["ingred 2"])