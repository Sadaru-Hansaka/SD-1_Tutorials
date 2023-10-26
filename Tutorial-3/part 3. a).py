choice=input("Choose what's your converter.\nTo convert celcius to fahrenheit enter 1 or convert fahrenheit to celcius enter 2 :")
temperature=input("Enter a temperature in the correct unit :")

choice=float(choice)
temperature=float(temperature)

if(choice==1):
    temp=(temperature*1.8)+32
    print(temp)
elif(choice==2):
    temp=(temperature-32)/1.8
    print(temp)
else:
    print("Invalid option entered!")