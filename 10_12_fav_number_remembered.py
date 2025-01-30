import json
filename = "fav_number.json"

def get_favorite_number():
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None

def store_favorite_number(number):
    data = number
    with open(filename, 'w') as file:
        json.dump(data, file)

def main():
    favorite_number = get_favorite_number()

    if favorite_number:
        print(f"Your favorite number is {favorite_number}.")
    else:
        favorite_number = input("What's your favorite number?>> ")
        store_favorite_number(favorite_number)
        print(f"Your favorite number {favorite_number} has been stored.")

main()
