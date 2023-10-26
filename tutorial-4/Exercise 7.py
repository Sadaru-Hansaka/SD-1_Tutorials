import random

count=0
double_count=0

for i in range(100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    count+=1
    print(f"{count}) Dice 1 = {dice1} and Dice 2 = {dice2}")

    if (dice1==dice2):
        double_count+=1
    else:
        continue
print("\nNumber of time dice :",count)
print(f"Out of 100 you rolled {double_count} doubles\n")
