name = input("Enter a name: ")

result = name + ' : ' + name[0] + '.'

for word in name:
    if word == ' ':
        idx = name.find(word) + 1
        result = name + ' : ' + name[0].upper() + '.' + name[idx].upper()

print(result)