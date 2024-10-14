'''
Recursive Approach
'''
def permute(string):
    result = []
    permute_helper(list(string), 0, len(string) - 1, result)
    return result

def permute_helper(s, left, right, result):
    if left == right:        # Checks if left has reached right, meaning a complete permutation has been formed.
        result.append(''.join(s))    
    else:
        for i in range(left, right + 1):
            s[left], s[i] = s[i], s[left]  # Swap
            permute_helper(s, left + 1, right, result)
            s[left], s[i] = s[i], s[left]  # Backtrack

# Example usage
if __name__ == "__main__":
    word = "abc"
    print(f"All permutations of the string are: {permute(word)}")


'''
Using Itertools.permutations
'''

from itertools import permutations

def permute_with_library(string):
    return[''.join(p) for p in permutations(string)]

if __name__ == "__main__":
    word = "pqr"
    print(f"All permutations of the string are: {permute_with_library(word)}")