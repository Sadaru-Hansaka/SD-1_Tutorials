age = input('Enter your age: ')

try:
    age = int(age)
    if age >= 18:
        print("You can vote")
except ValueError:
    print("Entered value is not an integer")