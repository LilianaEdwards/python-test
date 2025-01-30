from random import choices
my_ticket = "i71u"
lottery = [0,1,2,3,4,5,6,7,8,9,'a','e','i','o','u']
ticket =""
count = 0
selection = choices(lottery,k=4)
ticket = "".join(map(str, selection))
while True:
    count += 1
    if ticket == my_ticket:
        print(f"\nYou've won with tkt no. {ticket}")
        print(f"It took {count} tries to win.\n")
        break
    else:
        print(f"Trying to win:tkt no. {ticket}, attempt no. {count}")
        ticket = ""
        selection = choices(lottery,k=4)
        ticket = "".join(map(str, selection))

