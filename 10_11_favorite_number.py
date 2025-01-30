import json
fav_number = int(input("What is your favorite number?>> "))
fileName = "fav_number.json"
with open (fileName,'w') as file :
    json.dump(fav_number, file)