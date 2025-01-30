file_name = "D:\Python\MKPT-7014\Chapter 10\guest.txt"
name = input("Enter your name>> ")
with open(file_name,'w') as file :
    file.write(name)