cost=input("Enter the cost of the bill :Rs.")
satisfaction_level=input("Satisfaction leve (1=totally satisfied , 2=satisfied , 3=dissatisfied) :")

cost=float(cost)
satisfaction_level=int(satisfaction_level)

if (satisfaction_level==1):
    tip=cost*20/100
    print("Suggested tip Rs.",tip)
elif (satisfaction_level==2):
    tip=cost*15/100
    print("Suggested tip Rs.",tip)
elif (satisfaction_level==3):
    tip=cost*10/100
    print("Suggested tip Rs.",tip)
else:
    print("You should pay a tip!")