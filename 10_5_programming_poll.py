fileName = "D:\Python\MKPT-7014\Chapter 10\poll.txt"
while True :
    reason = input("Why do you like programming? Enter 'q' to exit>> ")
    if reason == 'q' :
        break
    with open (fileName,'a') as file :
        file.write(reason+'\n')
