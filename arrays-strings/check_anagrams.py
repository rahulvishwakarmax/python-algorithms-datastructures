# Two strings are called anagrams if they contain the same characters in the same frequency, but the order of characters can be different.

# Naive Approach: Sorting

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
print(are_anagrams(str1,str2))



# Optimal Approach: Frequency Counting

from collections import Counter

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    return Counter(str1) == Counter(str2)

str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  



# handling case senstivity and spaces

import re
def are_anagrams(str1, str2):
    # Clean strings by removing non-alphabetic characters and making them lowercase
    str1 = re.sub(r'\W', '', str1).lower()  ## Removes anything that is not a word character (letters, numbers)
    str2 = re.sub(r'\W', '', str2).lower()

    if len(str1) != len(str2):
        return False

        
    
    return Counter(str1) == Counter(str2)

# Example usage:
str1 = "Dormitory"
str2 = "Dirty room"
print(are_anagrams(str1, str2))  # Output: True