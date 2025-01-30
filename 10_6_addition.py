try : 
    int1 = int(input("Enter one number>> "))
    int2 = int(input("Enter another number to add>> "))
except ValueError :
    print("Please enter only numbers!!")
else :
    print(int1+int2)
