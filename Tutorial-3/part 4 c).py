marks=input("Enter mark :")
marks = float(marks)

if(0<=marks<=100):
    if(marks>=70):
        print("Exceptional result!")
    elif (marks >= 40):
        print("Satisfactory result!")
    else:
        print("You have failed.")
else:
    print("Mark is invalid")