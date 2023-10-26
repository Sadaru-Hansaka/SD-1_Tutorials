import random

hidden_number=random.randint(1,20)

for count in range (1,6):
    user_guess=input(f"{count}) Enter your guess :")
    user_guess=int(user_guess)
    if (hidden_number==user_guess):
        print(f"Random number is :{hidden_number}")
        print(f"Nice guess")
        break
    else:
        if(hidden_number>user_guess):
            print("Your guess is less than the hidden number.")
        elif(hidden_number<user_guess):
            print("Your guess is greater than the hidden number.")
    print("")
    
print(f"Bad luck, You didn't guess the hidden number.\nHidden number is {hidden_number}")
