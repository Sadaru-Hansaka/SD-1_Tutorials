while True:
    try:
        user_inut=input("Enter your menu option :")
        user_inut=int(user_inut)
        if(user_inut==1):
            print("1 selected")
        elif(user_inut==2):
            print("'2 selected")
        elif(user_inut==3):
            print("3 selected")
        elif(user_inut==5):
            break
        else:
            print("Option not recognize")
    except ValueError:
        print("Enter a integer")