dogsFile = "D:\Python\MKPT-7014\Chapter 10\dogs.txt"
catsFile = "D:\Python\MKPT-7014\Chapter 10\cats.txt"
try :
    with open (dogsFile) as dogs :
        print(dogs.read())
except FileNotFoundError :
    print(f"The file {dogsFile} doesn't exist.")
try :
    with open (catsFile) as cats :
        print(cats.read())
except FileNotFoundError :
    print(f"The file {catsFile} doesn't exist.")