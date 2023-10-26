num_1=input("Enter first integer :")
operator = input("Enter your operator(+,/,- or *) :")
num_2 = input("Enter your second integer :")

num_1=int(num_1)
num_2=int(num_2)
try:
    if (operator=="+"):
        print(f"{num_1} {operator} {num_2} =",num_1+num_2)
    elif (operator=="-"):
        print(f"{num_1} {operator} {num_2} =",num_1-num_2)
    elif (operator=="/"):
        print(f"{num_1} {operator} {num_2} =",num_1/num_2)
    elif (operator=="*"):
        print(f"{num_1} {operator} {num_2} =",num_1*num_2)
    else:
        print("Invalid operator")
except ZeroDivisionError:
    print("Error")