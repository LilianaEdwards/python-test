#4.1
pizzas = ['Margherita','Marinara','Neapolitan']
for pizza in pizzas :
    print(f"I like {pizza} pizza")
print("I really love pizza")

#4.2
animals = ['dog','cat','parrot','rabbit']
for animal in animals :
    print(f"A {animal} would make a great pet")
print("All of these animals would make a great pet")

#4.3
for value in range(1,21) : 
    print(value)

#4.4
numbers = list(range(1,1000001))
print("Here is the numbers from 1 to 1000000")
for number in numbers :
    print(number)

#4.5
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4.6
odd_numbers = list(range(1,20,2))
print("The odd numbers between 1 and 20 are:")
for value in odd_numbers :
    print(value)

#4.7
multipleOf3 = list(range(3,31,3))
print("The multiples of 3 are:")
for value in multipleOf3 :
    print(value)

#4.8
cubes = []
print("The cubes values for 1 to 10 are:")
for value in range(1,11) :
    cubes.append(value ** 3)
for number in cubes :
    print(number)

#4.9
print("The cube comprehension for 1 to 10 is: ")
cubes = [value**3 for value in range(1,11)]
print(cubes)

#4.10
print("The first three items in the cubes list are: ")
print(cubes[:3])
print("The three items from the middle of the list are: ")
print(cubes[3:6])
print("The last three items in the list are: ")
print(cubes[-3:])

#4.11
friends_pizzas = pizzas[:]
pizzas.append("Sicilian")
friends_pizzas.append("California")
print("My favourite pizzas are: ")
for name in pizzas :
    print(name)
print("My friend\'s favourite pizzas are:")
for name in friends_pizzas :
    print(name)

#4.12
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("My favourite foods are: ")
for name in my_foods :
    print(name)
print("My friend\'s favourite foods are:")
for name in friend_foods :
    print(name)

#4.13
foods = ('Sushi','Octopus','Noddle','Chicken','Rice')
print("The basic foods are: ")
for food in foods:
    print(food)
foods = ('Sushi','Kimchi','Noddle','Juice','Rice')
print("The revised menu is:")
for food in foods:
    print(food)
