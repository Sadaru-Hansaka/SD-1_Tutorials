question=input("Do you like Python?(yes/no) :")

question=question.lower()

if (question == "yes") or (question == "y") :
    print("you are on the right course")
elif (question == "no") or (question == "n"):
    print("you might change your mind")
else:
    print("I don't understand")
