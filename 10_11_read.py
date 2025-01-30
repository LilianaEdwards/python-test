import json
fileName = "fav_number.json"
with open (fileName) as file :
    num = json.load(file)
print(f"I know your favorite number! It's {num}")