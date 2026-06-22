#Q1: Create a dictionary of 3 students and their marks, then print each one.

students = {"Aarav": 85, "Priya": 90, "Rahul": 78}
for name, marks in students.items():
    print(name, marks)
print(students.items)



#Q1: Create a dictionary of 3 fruits and their prices, then print each one.
# fruits={"Apple":1,"mango":2,"pineapple":20}
# for n,m in fruits.items():
#     print(n,m)


#Easy 1: Ek dictionary banao with your favorite food and its price:
# food={"item":"Paneer","Price":200}
# print(food["item"])
# print(food["Price"])

#Easy 2: Ek dictionary mein value change karo:
# person={"name":"Mrnalinee","Age":28}
# person["Age"]=26
# print(person["Age"])

#Easy 3: Check karo ki ek key dictionary mein hai ya nahi:

# person={"name":"Mrnalinee","Age":28}
# print(person["name"])

# person = {"name":"Mrnalinee","Age":28}
# print("name" in person)    # True
# print("city" in person)

# Q1 — Print everything using a loop
# Make a dictionary of 3 students + marks, then use a for loop to print each student:

# students={"neha":300,"sneha":400,"hema":500}
# for name,marks in students.items():
#     print(name,marks)
#print(students.items())    

#Q2 — Add a new pair

# students={"neha":300,"sneha":400,"hema":500}
# students["rekha"]=200
# print(students)

#Q3 — Keys and values separately
# students = {"Aman": 85, "Riya": 90, "Sam": 78}
# print(students.keys())
# print(students.values())

#Update one value
# students = {"Aman": 85, "Riya": 90, "Sam": 78}
# students["Sam"]=34
# print(students)

#Q5 (needs a little thinking) — Highest marks

# students = {"Aman": 85, "Riya": 90, "Sam": 78}
# # who has the highest marks? print it
# print(max(students.values())) 
# topper=max(students,key=students.get)
# print(topper)

#Q6 — Find topper using a loop (no max)
# students={"Neha":38,"rekha":34,"rekha":98}
# highest=0
# topper=""
# count=0
# for name,marks in students.items():
#     if marks>highest :
#         highest=marks
#         topper=name
# print(topper, highest)
        
        
 #Q7 — Sum and average of all marks       
# students={"Neha":38,"rekha":34,"shreya":98}
# total=sum(students.values())
# average=total/len(students)
# print(average)

 #printing names and marks together in a nice format:
# students = {"Aman": 85, "Riya": 90, "Sam": 78}
# # print like:  Aman scored 85
# for name,marks in students.items():
#     print(f"{name} Scored {marks}")



# count how many passed (marks >= 80), then print the count
# students = {"Aman": 85, "Riya": 90, "Sam": 78}
# count=0
# for name,marks in students.items():
#     if (marks>=80):
#         count=count+1
# print(count)


# remove "Sam", then print the dict
students = {"Aman": 85, "Riya": 90, "Sam": 78}
del students["Sam"]
print(students)



