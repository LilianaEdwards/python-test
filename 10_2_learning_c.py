fileName = 'D:\Python\MKPT-7014\Chapter 10\learning_python.txt'
with open (fileName) as f:
    for line in f :
        replace_c = line.replace("Python","C")
        print(replace_c)
