#8.1
def display_message() :
    print("I am learning about function.")
display_message()

#8.2
def favorite_book(title) :
    print(f"One of my favorite book is {title}")
favorite_book('Alice in Wonderland')

#8.3
def make_shirt(size,message) :
    print(f"The size is {size}\nThe message is {message}")
make_shirt(size='medium',message='UCSM Third Year')
make_shirt(message='UCSM Welcome',size='small')

#8.4
def make_shirt(size='large',message='I love Python') :
    print(f"The size is {size}\nThe message is {message}")
make_shirt(size='large')
make_shirt(size='medium')
make_shirt(size='medium',message='UCSM')

#8.5
def describe_city(city,country='myanmar') :
    print(f"{city.title()} is in {country.title()}")
describe_city('mandalay','myanmar')
describe_city('yangon','myanmar')
describe_city('chinmai','thailand')

#8.6
def city_country(city,country) :
    pair = f'{city.title()}, {country.title()}'
    return pair
print(city_country('mandalay','myanmar'))
print(city_country('chinmai','thailand'))
print(city_country('dubai','india'))

#8.7
def make_album(name,title) :
    album = {name : title}
    return album
album1 = make_album('Taylor','Lover')
album2 = make_album('Olivia','Sour') 
album3 = make_album('Ed Sheeran','The Orange Room')
print("The artists and the album titles are: ")
print(album1) 
print(album2)  
print(album3)

#8.8
while True :
    name = input("Enter an artist name>> ")
    title = input("Enter the album title>> ")
    print(make_album(name,title))
    quit = input("Enter 'q' to quit the program>> ")
    if quit == 'q' :
        break

#8.9
def show_messages(messages) :
    for message in messages :
        print(message)
messages = ['Hello','Nice to meet you','Good bye']
show_messages(messages)

#8.10
def show_messages(messages) :
    for message in messages :
        print(message)

def send_messages(messages,sent_messages) :
    while messages :
        msg = messages.pop()
        print(msg)
        sent_messages.append(msg)

messages = ['Hello','Nice to meet you','Good bye']
sent_messages = []
show_messages(messages)
send_messages(messages,sent_messages)
print("The original list: ")
print(messages)
print("The copied list:")
print(sent_messages)

#8.11
messages = ['Hello','Nice to meet you','Good bye']
send_messages(messages[:],sent_messages)

#8.12
def sandwiches (*items) :
    print("The items that are on the sandwiches are :")
    for item in items :
        print(item)
sandwiches('bread','meat')
sandwiches('bread','meat','cheese')
sandwiches('bread','meat','vegeetable','cheese')

#8.13
def build_profile(first, last, **user_info) :
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Lilliana', 'Edward',
                             location='Mandalay',
                             age='20',
                             field='CS',
                             uni='UCSM')
print(user_profile)

#8.14
def make_car(manufacturer,m_name,**others):
    others['maker'] = manufacturer
    others['name'] = m_name
    return others
car = make_car('subaru','outback',
                color = 'blue',
                tow_package = True)
print(car)

#8.15
import printing_models
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_models.print_models(unprinted_designs, completed_models)
printing_models.show_completed_models(completed_models)

#8.16
from user_profile import build_profile
build_profile('Lilliana', 'Edward',location='Mandalay',age='20',field='CS',uni='UCSM')

from user_profile import build_profile as bp
bp('Lilliana', 'Edward',location='Mandalay',age='20',field='CS',uni='UCSM')

import user_profile as p
p.build_profile('Lilliana', 'Edward',location='Mandalay',age='20',field='CS',uni='UCSM')

from user_profile import *
build_profile('Lilliana', 'Edward',location='Mandalay',age='20',field='CS',uni='UCSM')
