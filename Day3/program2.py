# WAP to check if the list contains a panlindrome element 
# (hint: use copy method)
# [1,2,3,2,1] [1,"abc","abc",1]

list1 = [1,2,3,2,1]
list2 =[1,"abc","abc",1]
P = list2.copy()

P.reverse()
print(P)
if list2 == P:        # compare original with the reversed copy
    print("It is a palindrome")
else:
    print("It is not a palindrome")
