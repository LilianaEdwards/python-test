#7.1
rental_car = input("What kind of rental car you would like to rent?  ")
print(f"Let me see if I can find you a {rental_car}.")

#7.2
number = int(input("How many people are in your dinner group?  "))
if (number > 8) :
    print("You have to wait for a table.")
else :
    print("Your table is ready.")

#7.3
number = int(input("Enter a number>> "))
if (number % 10 == 0) :
    print(f"{number} is a multiple of 10.")
else :
    print(f"{number} is not a multiple of 10.")

#7.4
while True :
    topping = input("Enter a topping name or \'quit\' to exit>> ").lower()
    if (topping == 'quit'):
        break
    print(f"I will add {topping} topping to your pizza.")

#7.5
action = True
while action :
    age = int(input("Enter your age or 0 to exit>> "))
    if (age == 0) :
        action = False
    elif (age < 3) :
        print("You are free")
    elif (age < 12 and age >=3) :
        print("The ticket is $10")
    elif (age >= 12) :
        print("The ticket is $15")

#7.8
sandwich_orders = ['pastrami','chicken','pastrami','tuna','egg','pastrami']
finished_sandwiches = []
while sandwich_orders :
    sandwiches = sandwich_orders.pop()
    print(f"I made your {sandwiches} sandwich")
    finished_sandwiches.append(sandwiches)
print("The finished sandwiches I have made are :")
for sandwich in finished_sandwiches :
    print(f"{sandwich} sandwich")

#7.9
sandwich_orders = ['pastrami','chicken','pastrami','tuna','egg','pastrami']
print("Sorry! the deli has run out of pastrami")
while 'pastrami' in sandwich_orders :
    sandwich_orders.remove('pastrami')
print("Here is the sandwich order")
print(sandwich_orders)
print("The finished sandwiches I have made are :")
for sandwich in finished_sandwiches :
    print(f"{sandwich} sandwich")

#7.10
places = []
action = True
while action :
    place = input("\nIf you could visit one place in the world, where would you go? >>")
    places.append(place)
    
    repeat = input("Would you like to let another person respond? (yes/no) >> ").lower()
    if repeat == 'no' :
        action = False
print("\n--- Poll results ---")
for place in places :
    print(place)
        

    