# ==========================================
# 8. LISTS
# ==========================================


# ------------------------------------------
# Create a list of 5 numbers and print the largest and smallest
# ------------------------------------------
list=[11,2,33,4,55]
print(max(list))
print(min(list))

numbers = [11, 2, 33, 4, 55]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# ------------------------------------------
# Add and remove an item from a list
# ------------------------------------------
numbers = [11, 2, 33, 4, 55]
numbers.pop(2)
print(numbers)


# ------------------------------------------
# Count how many times a value appears in a list
# ------------------------------------------
list=[2,2,2,2,11,22,22,11,23,1]
seen=[]
for num in list: 
    if num not in seen: 
        print(num,"appears",list.count(num),"times")
    seen.append(num)


# ------------------------------------------
# Print only the count of even numbers from a list
# ------------------------------------------
nums = [3, 8, 5, 12, 7, 4, 10]
count=0
for num in nums:
    if(num%2==0):
        count=count+1
print(count)


# ------------------------------------------
# Print only the count of even numbers from a list (second version)
# ------------------------------------------
nums = [3, 8, 5, 12, 7, 4, 10]
count=0
for num in nums:
    if(num%2==0):
        count=count+1
print(count)


# ------------------------------------------
# Add 60 to the list, print the list, remove 20 from the list
# ------------------------------------------
nums = [10, 20, 30, 40, 50]
nums.append(60)
nums.remove(20)
print(nums)