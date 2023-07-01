enter = input("Enter a operation: ")
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
operation = enter.lower()
print(operation)
if operation == 'substract':
    result = number1 - number2
elif operation == 'add':
    result = number1 + number2
elif operation == 'divide':
    result = number1 / number2
elif operation == 'multiply':
    result = number1 * number2
else:
    result = 'Enter a valid operation or numbers'

print(result)
