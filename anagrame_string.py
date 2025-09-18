# function to check if two strings are
# anagram or not 
def check(s1, s2):
     
    # the sorted strings are checked 
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.") 
    else:
        print("The strings aren't anagrams.")         
         
# driver code  
s1 ="listen"
s2 ="silent"
check(s1, s2)


'''Question:

Given two strings s1 and s2, check if both the strings are anagrams of each other.

Examples: 

Input : s1 = "listen"
        s2 = "silent"
Output : The strings are anagrams.


Input : s1 = "dad"
        s2 = "bad"
Output : The strings aren't anagrams.'''
