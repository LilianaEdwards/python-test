def count_the_in_text(fileName):
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            count = text.count('the ') 
            return count
    except FileNotFoundError:
        print(f"The file {fileName} was not found.")
        return None

fileName = "D:\Python\MKPT-7014\Chapter 10\\text_file.txt"
count = count_the_in_text(fileName)

if count is not None:
    print(f"The word 'the' appears {count} times in the text.")
