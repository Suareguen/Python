name = input("Enter a word: ")

length = len(name)

if length % 2 == 0:
    idx2 =( length // 2)  
    idx = (length // 2) - 1
    result = name[idx] + ' ' + name[idx2]
else: 
    idx = (length // 2)
    result = name[idx]

print(result)

