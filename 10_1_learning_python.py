fileName = 'D:\Python\MKPT-7014\Chapter 10\learning_python.txt'
for i in range(3):
    i = open(fileName).read()
    print(i)

with open(fileName, 'r') as file:
    for lines in file:
        print(lines)

with open(fileName,'r') as file:
    output_text = file.readlines()

text = []

for data in output_text:
    text.append(data.rstrip("\n"))
print(text)

    