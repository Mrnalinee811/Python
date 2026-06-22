#Section 2 — Accessing values ([] vs .get())
# 2.1 print the name using []
# 2.2 try to get "age" using .get() — see what happens
# 2.3 use .get("age", 0) so it returns 0 instead of None

student = {"name": "Mrnalinee", "city": "Boston"}
print(student["name"])
student["Age"]=28
print(student)
print(student.get("Age"))
print(student.get("Age",0))

#Section 3 — Add, update, delete

# 3.1 add "Sam" with 78
# 3.2 update Aman to 95
# 3.3 delete Riya
# 3.4 print after each step
marks = {"Aman": 85, "Riya": 90}
marks["Sam"]=78
marks["Aman"]=95
del marks["Riya"]
for name,numbers in marks.items():
    print(name,numbers)


#Section 4 — Looping (the 3 ways)

#marks = {"Aman": 85, "Riya": 90, "Sam": 78}
# # 4.1 print only the names
for name in marks:
    print(name)
# 4.2 print only the marks
for value in marks.values():
    print(value)
# 4.3 print "Aman scored 85" style using .items()
for name,value in marks.items():
        print(name,"scored",value)


# #Section 5 — Useful methods
marks = {"Aman": 85, "Riya": 90}
# # 5.1 print number of students with len()
print(len(marks))
# # 5.2 use .update() to add {"Sam": 78, "Neha": 88} in one line
marks.update({"Sam": 78, "Neha": 88})
print(marks)
# # 5.3 use .pop("Aman") and print the value it returns
marks.pop("Aman")
print(marks)


#Section 6 — Membership check (in)
      

# #6.1 check if "Aman" is in the dic
marks = {"Aman": 85, "Riya": 90}
print("Aman" in marks)
    
# #6.2 check if "Sam" is in the dict
marks = {"Sam": 85, "Riya": 90}
print("Sam" in marks)

# #6.3 only print Sam's marks IF Sam exists (if "Sam" in marks:)
marks = {"Aman": 85, "Riya": 90}
if "Sam" in marks:
    print(marks["Sam"])         
else:
    print("Sam not found")
