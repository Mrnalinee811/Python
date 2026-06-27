#Write add_all(*numbers) that returns the sum of
# any number of arguments passed in.

def add_all(*numbers):
    sum=0
    for num in numbers:
        sum= sum + num
    return sum
    
print(add_all(34, 34, 2))