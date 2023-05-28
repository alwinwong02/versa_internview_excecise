import json

data = []

for number in range (1,101):
    if number % 3 == 0 and number % 5 == 0:
        data.append("BIG BANG")
    elif number % 3 == 0:
        data.append("BIG")
    elif number % 5 == 0:
        data.append("BANG")
    else: 
        data.append(str(number))

    with open ('BIGBANG.json','w') as file:
        json.dump(data,file)

    with open ('BIGBANG.json','r') as file:
        result = json.load(file)

print(result)