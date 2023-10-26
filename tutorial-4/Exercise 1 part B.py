import random
hidden_number=random.randint(1,20)

while True:
    user_guess= input("Guess a number between 1 and 20 :")
    user_guess=int(user_guess)

    if(user_guess==hidden_number):
        print(f"{user_guess} was corect")
        break
    else:
        print(f"{user_guess} is not correct")