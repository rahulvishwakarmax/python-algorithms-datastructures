# Check if the String is Palindrome (Using reversed and join)
mystr = "BoB"

# Convert to lower case to ignore case sensitivity
reversed_str = ''.join(reversed(mystr.lower()))

if mystr.lower() == reversed_str:
    print("string is palindrome")
else:
    print("string is not palindrome")

# slicing method
reversed_str2 = mystr.lower()[::-1]

if mystr.lower() == reversed_str2:
    print("string is palindrome")
else:
    print("string is not palindrome")


# Using two pointers
mystr.lower()
left = 0  # starting index
right = len(mystr) - 1  # last index

is_palindrome = True  # assume it's a palindrome

while left < right:
    if mystr[left] != mystr[right]:
        is_palindrome = False
        break
    left += 1  # move left pointer forward 
    right -= 1  # move right pointer backward

if is_palindrome:
    print("string is palindrome")
else:
    print("string is not palindrome")