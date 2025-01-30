#5.1
car = 'subaru'
print("Is car == 'subaru' ? I predict True.")
print(car == 'subaru')
print("Is car == 'audi' ? I predict False.")
print(car == 'audi')

print('Mg Mg' == 'Mg Mg')
print(18 >10)
print('HELLO'.lower() == 'hello')
print(24 == 24)
print('oh'.title() == 'Oh')
print(18 == 20)
print(40 != 40)
print('Olivia' == 'olivia')
print(30 < 15)
print(20 == 19)

#5.2
name = 'Olivia'
if(name == 'Olivia'):
    print(f"You are {name}")
if(name != 'Olivia'):
    print(f"You are not {name}")
if(name.lower() == 'olivia'):
    print(name.lower()=='olivia')
if(name.lower() == 'Olivia'):
    print(name.lower()=='olivia')
print(18 == 20)
print(18!= 20)
print(18>20)
print(18<20)
print(18>=20)
print(18<=20)
lists = [1,2,3,4,5]
if(1 in lists) :
    print("1 is in list")
if(9 not in lists) :
    print("9 is not in list")

#5.3
alien_color = 'green'
if('green' in alien_color):
    print("You just earned 5 points")

#5.4
alien_color = 'yellow'
if('green' in alien_color):
    print("You just earned 5 points")
else:
    print("You just earned 10 points")

#5.5
alien_color = 'red'
if('green' in alien_color):
    print("You just earned 5 points")
elif('yellow' in alien_color):
    print("You just earned 10 points")
else:
    print("You just earned 15 points")

#5.6
age = 20
if(age < 2):
    print("The person is a baby")
elif(age >=2 and age < 4):
    print("The person is a toddler")
elif(age >=4 and age < 13):
    print("The person is a kid")
elif(age >=13 and age < 20):
    print("The person is a teenager")
elif(age >=20 and age < 65):
    print("The person is an adult")
else:
    print("The person is an elder")

#5.7
favorite_fruits = ['apple','orange','strawberry']
if('apple' in favorite_fruits):
    print("You really like apple")
if('banana' in favorite_fruits):
    print("You really like banana")
if('orange' in favorite_fruits):
    print("You really like orange")
if('strawberry' in favorite_fruits):
    print("You really like strawberry")
if('grape' in favorite_fruits):
    print("You really like grape")

#5.8
names = ['admin','Olivia','Elisa','Bambi','Daniel']
for name in names:
    if(name == 'admin'):
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again")

#5.9
if names:
    names = []
    print(f"The list is empty")
    print(names)
else :
    print("We need to find some users")

#5.10
current_users = ['Kyi Sin Thant','Khin Thanthar','Wai Wai Myint','Poe Ei Kae','Htet Htet']
new_users = ['Min Khant','Kyi Sin Thant','T T Kyaw','Khin Thanthar','Kaung Myat']
current_users_copy = current_users[:]
for i in current_users:
    current_users_copy.append(i.lower())
for user in new_users :
    if (user.lower() in current_users_copy) :
        print("You will need to enter a new username")
    else :
        print("The username is available")