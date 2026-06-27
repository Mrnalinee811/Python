#8. Write area(length, width) and call it using keyword arguments 
# in a different order than defined.Logic inside functions

def area(length, width):
    return length * width
result = area(width=4, length=2)
print(result)