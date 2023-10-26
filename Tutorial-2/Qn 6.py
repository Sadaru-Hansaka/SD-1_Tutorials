num_1 = input("Enter first number :")
num_2 = input("Enter second number :")
try:
    num_1=int(num_1)
    num_2=int(num_2)
    print(num_1/num_2)
except:
    print("Can't divide by zero")