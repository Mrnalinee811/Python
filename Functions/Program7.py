 #Write make_profile(**details) that prints each key-value pair as key: value.
 
def make_profile(**details):
    
    for key,value in details.items():
        print(f"{key}: {value}")
        
make_profile(name="neha", age=24)

        
    