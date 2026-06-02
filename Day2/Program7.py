#WAP to find the greatest of 3 numbers entered by the user.
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=int(input("Enter a number"))

if(num1>num2 and num1>num3):
    print("num1 is greater")
elif(num2>num3 and num2>num1):
    print("num2 is greater")
else:
    print("num3 is greater")
    
