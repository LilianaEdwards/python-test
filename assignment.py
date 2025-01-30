fileName = 'D:\Python\MKPT-7014\Chapter 10\\assignment.txt'
try :
    input_num = int(input("Enter a number to see its multiply table>> "))
except :
    print('Enter only number!!')
else :
    for i in range(1,13) :
        result = input_num * i
        output =  f"{input_num} * {i} = {result}"
        try:
            with open(fileName,'a') as file_object :
                file_object.write( f"{input_num} * {i} = {result}\n")

        except FileNotFoundError :
            print("Your file isn't in location.")

        print(output)
            