file_name = "D:\Python\MKPT-7014\Chapter 10\guest_book.txt"
while True :
    name = input("Enter your name or 'q' to quit>> ")
    if name == 'q' :
        break
    print(f"Hello {name}")
    with open(file_name,'a') as file :
        file.write(f"{name} just visited.\n")