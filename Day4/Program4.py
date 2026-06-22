# WAP  to enter marks of 3 subjects from the user and store them in a 
# dictionary .start with an empty dictionary and add one by one .
# use  subject name  as key and marks as value

marks={}

x =int(input("Emter the marks of physics: "))
marks.update({"physics" : x})

x =int(input("Emter the marks of chem: "))
marks.update({"chem" : x})

x =int(input("Emter the marks of math: "))
marks.update({"math" : x})

print(marks)