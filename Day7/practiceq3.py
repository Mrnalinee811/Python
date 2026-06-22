#Question 1: Create a tuple of your favorite colors and print the second one.
# color=("red","yellow","green")
# print(color[1])
# print(len(color))

#1. Access different items
# Print the first fruit and the last fruit. 
# pythonfruits = ("apple", "banana", "mango", "orange")
# print(pythonfruits[0])    # first
# print(pythonfruits[-1])   # last

# 2. Loop through a tuple
# Print each color on its own line using a for loop.
# pythoncolors = ("red", "green", "blue")
# for num in pythoncolors:
#     print(num)


# 3. Length and a calculation
# Print how many marks there are (len),
# and then try printing their sum using sum(marks).
# marks = (80, 75, 90, 85)

# print(len(marks))
# print(sum(marks))

#4: Check if an item exists

# check if "tomato" is in the tuple, print True or False
# veggies = ("potato", "tomato", "onion")
# search = "tomato"          

# if search in veggies:
#     print(search, "True")
# else:
#     print(search, "False")


#5: Count occurrences in a tuple.

tuple=(2,2,2,2,2,6,6,11,11,1,5,8,9,6)
seen=()
for num in tuple:
    if num not in seen:
        print(num ,"seen" , tuple.count(num),"appears in list")
    seen=seen+(num,)