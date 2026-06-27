#9. Write count_vowels(word) that returns how many vowels are in a string.
def count_vowels(word):    
    count=0
    for letter in word.lower():
        if letter in "aeiou":
            count=count+1
    print(count)
   
    
count_vowels("Apple")