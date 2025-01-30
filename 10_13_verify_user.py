import json
filename = 'username.json'
def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
        is_correct = input(f"Is {username} the correct username? (yes/no) ").strip().lower()
        if is_correct != 'yes':
            username = get_new_username()
            store_username(username)
            print(f"Your username has been updated to {username}.")
        else:
            print(f"Great! Continuing as {username}.")
    else:
        username = get_new_username()
        store_username(username)
        print(f"Your username has been set to {username}.")

def get_stored_username():
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None

def store_username(username):
    data = username
    with open(filename, 'w') as file:
        json.dump(data, file)

def get_new_username():
    return input("Please enter your username: ").strip()

greet_user()
