#6.1
person1 = {'first_name' : 'john' , 'last_name' : 'smith', 'age' : 18, 'city' : 'new york'}
for value in person1.values():
    print(value)

#6.2
favourite_numbers = {'John' : 1,
                     'Ethan' : 2,
                     'Smith' : 3,
                     'Emily' : 4,
                     'Adam' : 5}
for name in favourite_numbers :
    print(f"\n{name} \'s favourite number is {favourite_numbers[name]}")

#6.3
glossary = {'String' : 'A series of characters.',
            'Comment' : 'A note in the program that the Python interpreter ignores.',
            'List' : 'A collection of items in a particular order.',
            'Loop' : 'Work through a collection of items one at a time.',
            'Dictionary' : 'A collection of key-value pairs.'}
for defination in glossary :
    print(f"{defination}: {glossary[defination]}")

#6.4
glossary['Key'] = 'The first item in a key-value pair in a dictionary.'
glossary['Value'] = 'An item associated with a key in a dictionary.'
glossary['Conditional Test'] = 'A comparison between two values.'
glossary['Float'] = 'A numerical value with a decimal component.'
glossary['Boolean Expression'] = 'An expression that evaluates to True or False.'
for name,defination in glossary.items() :
    print(f"{name}: {defination}\n")

#6.5
dictionary = {'nile' : 'egypt','fraser' : 'canada', 'yangtze' : 'china'}
for river,country in dictionary.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in the dictionary:")
for river in dictionary.keys():
    print(river.title())

print("\nCountry included in the dictionary:")
for country in dictionary.values():
    print(country.title())
print('\n')
#6.6
favorite_languages = {'jen' : 'python','sarah' : 'c','edward' : 'ruby', 'phil' : 'python'}
friends = ['jen','smith','sarah','ethan']
for name in friends:
    if name in favorite_languages.keys():
        print(f"Hi {name.title()}, thank you for your response.")
    else:
        print(f"Hi {name.title()}, I would like to invite you to take a poll.")

#6.7
person2 = {'first_name' : 'ella' , 'last_name' : 'mon', 'age' : 20, 'city' : 'bangkok'}
person3 = {'first_name' : 'eric' , 'last_name' : 'matthes', 'age' : 15, 'city' : 'sitka'}

people = [person1,person2,person3]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"Fullname: {full_name.title()}")
    print(f"Age: {age}")
    print(f"City : {city.title()}\n")

#6.8
pet1 = {'animal type' : 'dog', 'name' : 'john', 'owner' : 'tiffany'}
pet2 = {'animal type' : 'cat', 'name' : 'peso', 'owner' : 'eric'}
pets = [pet1,pet2]
for pet in pets:
    for key,value in pet.items():
        print(f"{key.title()} : {value.title()}")

#6.9
favorite_places = {'emily' : ['chinmai','iceland'],
'john' : ['cafe','museum'],
'amy' : ['valley','hawaii']}
for name,places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"{place.title()}")

#6.10
favourite_numbers = {'John' : [1,2,8],
                     'Ethan' : [2,6,9],
                     'Smith' : [3,1,0],
                     'Emily' : [4,2,7],
                     'Adam' : [5,4,7]}
for name,numbers in favourite_numbers.items():
    print(f"{name.title()}\'s favourite numbers are:")
    for number in numbers:
        print(number)

#6.11
cities = {'santiago' : {'country':'chile','population':'6157800','nearby mountains':'andes'},
'chinmai' : {'country':'bangkok','population':'8527130','nearby mountains':'alaska range'},
'kathmandu' : {'country':'nepal','population':'60478000','nearby mountains':'himilaya'}}
for city,info in cities.items():
    print(f"\n{city.title()}\'s information:")
    for key,value in info.items():
        print(f"{key.title()}: {value.title()}")