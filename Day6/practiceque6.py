# 6. Loops (for, while)

# Print numbers from 1 to 10

# i=1
# while(i<=10):
#     print(i)
#     i=i+1
 


# Print the multiplication table of a number

# n=int(input("Enter the number: "))
# i=1
# while(i<=10):
#     print(str(n) + "*" + str(i) + "=" +str(n*i))
#     i=i+1

# Print the sum of numbers from 1 to n

# n=int(input("Enter the number: "))
# i=1
# total=0
# while(i<=n):
#     total=total+i
#     i=i+1
# print(total)


# Print all even numbers between 1 and 20


# i=1
# while(i<=20):
#     if(i%2==0):
#       print(str(i)+" even number")
#     else:
#         print(str(i)+" odd number")
#     i=i+1 

    

# Calculate the factorial of a number

num=int(input("Enter the number: "))
i=1
count=1
while(i<=num):
    count=count*i
    i=i+1
print(count)
    