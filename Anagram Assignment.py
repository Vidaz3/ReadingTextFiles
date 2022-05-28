# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
print ("Welcome to the anagram Detector \n Enter the words you would like to check here. \n If they are anagrams, it will return a true response. \n If they are not anagrams, it will return a false response ")

r1 = input("Enter your first word here: ")
r2 = input("Enter your second word here: ")

def find_anagram(r1, r2):    
    if (sorted (r1)== sorted (r2)):
        return True
    else:
        return False
print(find_anagram(r1, r2))
