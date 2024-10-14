# Check if one string is a rotation of another

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    concatenated = s1 + s1
    return s2 in concatenated

if __name__ == "__main__":
    str1 = "abcde"
    str2 = "deabc"

    if is_rotation(str1, str2):
        print(f"{str2} is a rotation of {str1}")
    else:
        print(f"{str2} is not a rotation of {str1}")