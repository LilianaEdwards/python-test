from random import choice
lottery = [0,1,2,3,4,5,6,7,8,9,'a','e','i','o','u']
ticket =[]
for i in range(4) :
    ticket.append(choice(lottery))
print("The ticket matching the following four numbers or letters wins a prize.")
print(ticket)
