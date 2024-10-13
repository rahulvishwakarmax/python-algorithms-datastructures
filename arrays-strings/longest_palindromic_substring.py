def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""
    
    def expand_around_center(left, right):
        # Expand as long as the characters on both sides are equal
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring
        return s[left + 1:right]

    longest = ""
    
    for i in range(len(s)):
        # Odd length palindromes (center at one character)
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Even length palindromes (center between two characters)
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest

if __name__ == "__main__":
    string = "babad"
    result = longest_palindromic_substring(string)
    print("The Longest Palindromic Substring is:", result)
