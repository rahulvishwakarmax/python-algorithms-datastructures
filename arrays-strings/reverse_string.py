#  Reverse a String

mystr = "I love Machine Learning"
result = ""
for str in mystr:
    result = str + result

print(result)

# we can also use slicing

reversed_str = mystr[::-1]  # mystr[start:stop:step] 
print(reversed_str)

# We can also use built in function

reversed_str2 = ''.join(reversed(mystr)) # Use the reversed() function to reverse the string and ''.join() to combine the characters back into a single string

print(reversed_str2)
