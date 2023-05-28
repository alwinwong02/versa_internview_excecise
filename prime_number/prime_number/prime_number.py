import json

result = []

for number in range (1,100):
    if number % 3 == 0 and number % 5 == 0:
        result.append("BIG BANG")
    elif number % 3 == 0:
        result.append("BIG")
    elif number % 5 == 0:
        result.append("BANG")
    else: 
        result.append(str(number))

    with open ('output.json','w') as file:
        json.dump(result,file)

