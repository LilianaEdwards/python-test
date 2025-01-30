#3.1
friends = ["Khin Thanthar","Wai Wai Myint","Poe Ei Kae"]
print("The names of my friends are: ")
print(friends[0])
print(friends[1])
print(friends[2])

#3.2
message = "Nice to meet you, "
print(message,friends[0])
print(message,friends[1])
print(message,friends[2])

#3.3
cars = ['Lambo','Ferrari','Lexus','BMW']
print(f"I would like to own a {cars[0]} car.")
print(f"I would like to own a {cars[1]} car.")
print(f"I would like to own a {cars[2]} car.")
print(f"I would like to own a {cars[3]} car.")

#3.4
guests = ["Khin Thanthar","Wai Wai Myint","Poe Ei Kae"]
print(f"Hello {guests[0]}, I would like to invite you to the dinner party.")
print(f"Hello {guests[1]}, I would like to invite you to the dinner party.")
print(f"Hello {guests[2]}, I would like to invite you to the dinner party.")

#3.5
print("The first three people are:")
print(guests[0]+", "+guests[1]+" and "+guests[2])
guests[-1] = 'Htet Ohnmar Win'
print(f"Hey {guests[0]}, would you like to come to the party?")
print(f"Hey {guests[1]}, would you like to come to the party?")
print(f"Hey {guests[2]}, would you like to come to the party?")

#3.6
guests.insert(0,'Min Khant')
guests.insert(2,'T T Kyaw')
guests.append('Depar')
print(f"Hi {guests[0]}, I want you to come to my party next Friday")
print(f"Hi {guests[1]}, I want you to come to my party next Friday")
print(f"Hi {guests[2]}, I want you to come to my party next Friday")
print(f"Hi {guests[3]}, I want you to come to my party next Friday")
print(f"Hi {guests[4]}, I want you to come to my party next Friday")
print(f"Hi {guests[5]}, I want you to come to my party next Friday")
print("The invited people are: ")
print(guests)

#3.7
print("Sorry I can invite only two people")
print(f"Sorry for cancelling my invitation, {guests.pop()}")
print(f"Sorry for cancelling my invitation, {guests.pop()}")
print(f"Sorry for cancelling my invitation, {guests.pop()}")
print(f"Sorry for cancelling my invitation, {guests.pop()}")
print(f"Hey! you are still on my list, {guests[0]}")
print(f"Hey! you are still on my list, {guests[1]}")
del guests[1]
del guests[0]
print("Finally! My list is empty!!")
print(guests)

#3.8
places = ['Dubai','Paris','Hawaii','Switzerland','Bagan']
print("The places I wanna visit are: ")
print(places)
print("The sorted result is")
print(sorted(places))
print("The original list is")
print(places)
places.reverse()
print("The list has been reversed")
print(places)
places.reverse()
print("The reversed list has been changed to its original")
print(places)
places.sort()
print("The original list has been sorted")
print(places)
places.sort(reverse=True)
print("The reversed alphabetical order is")
print(places)

#3.9
guests = ["Khin Thanthar","Min Khant","Wai Wai Myint","Poe Ei Kae"]
print("The number of people I am inviting to dinner is ", len(guests))

#3.10
mountains = ['Everest','Popa','Fuji']
rivers = ['Nine','Chindwin','Ayeyarwaddy','Sittaung']
countries = ['Japan','Korea','US','UK']
cities = ['Mandalay','Yangon','Magway']
languages = ['English','Burmese','Thai']
items_list = [mountains,rivers,countries,cities,languages]
print("The number of items in the list is", len(items_list))
print("The sorted list is")
items_list.sort()
print(items_list)
print("The reversed list is")
items_list.reverse()
print(items_list)
