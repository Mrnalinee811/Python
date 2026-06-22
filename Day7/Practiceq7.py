#Accessing — chain the brackets left to right:

# students = {
#     "Aman": {"math": 85, "science": 90},
#     "Riya": {"math": 78, "science": 88}
# }

# 7.1 print Aman's full inner dictionary
#print (students["Aman"])

# 7.2 print Riya's science marks (chain two brackets)
#print(students["Riya"]["science"])

# 7.3 loop and print each student's math marks
# students = {
#     "Aman": {"math": 85, "science": 90},
#     "Riya": {"math": 78, "science": 88}
# }

# for name, subject in students.items():
#     print(name,subject["math"])
    
   

# students = {
#     "Aman": {"math": 85, "science": 90},
#     "Riya": {"math": 78, "science": 88},
#     "Sam":  {"math": 92, "science": 80}
# }

# print Sam's science marks
# print(students["Sam"]["science"])
# # print Aman's math marks
# print(students["Aman"]["math"])

# print like:  Aman science 90
# for name, subjects in students.items():
#     print(name,"scored",subjects["science"])

# print like:  Aman - math: 85, science: 90
for name, subjects in students.items():
    print(name,"- math:",subjects["math"],"science:",subjects["science"])
    
# N4 — add "english": 75 to Riya, then print Riya's full dict

students = {
    "Aman": {"math": 85, "science": 90},
    "Riya": {"math": 78, "science": 88},
    "Sam":  {"math": 92, "science": 80}
}
# students["Riya"]["english"]= 75
# print(students)

# N5 — print like:  Aman total: 175
for name,subjects in students.items():
    total=subjects["math"]+subjects["science"]
    print(name,"total:",total)
    
# N6 — print every student with each subject on its own line:
# Aman
#   math: 85
#   science: 90
# Riya
#   math: 78
#   ...  

for name,subjects in students.items():
    print(name)
    for marks in subjects:
        print(" ",marks,":",subjects[marks])