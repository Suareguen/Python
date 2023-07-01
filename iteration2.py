def get_drink(age):
    if age < 14:
        return "Water"
    elif age < 18:
        return "Strawberry Clipper"
    elif age < 21:
        return "Tropical"
    else:
        return "Whisky"

age = int(input("Enter your age: "))

drink = get_drink(age)

print("You are allowed to drink " + drink)

