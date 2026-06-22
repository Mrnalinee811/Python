# Search  for a number X in this tuple using loop
list=(1,4,9,16,25,36,49,64,81,100)
i=0
X=49
while i<len(list):
    if(list[i]==X):
        print("found",X)
    else:
        print("Not found")
    i=i+1
    
 
