string = input("Enter a word: ")

count = 0

for word in string:
    if word == 'a':
        count = count + 1

print(count)