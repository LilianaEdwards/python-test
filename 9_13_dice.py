from random import randint
class Die :
    def __init__(self,sides=6) :
        self.sides = sides
    def roll_die(self) :
        print(randint(1,self.sides))
#for 6-sided die
print("The result for rolling 6-sided die 10 times")
for i in range(1,11) :
    die1 = Die()
    die1.roll_die()
print("The result for rolling 10-sided die 10 times")
#for 10-sided die
for i in range(1,11) :
    die2 = Die(10)
    die2.roll_die()
print("The result for rolling 20-sided die 10 times")
#for 20-sided die
for i in range(1,11) :
    die3 = Die(20)
    die3.roll_die()
