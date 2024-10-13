def longest_substring_without_repeating_characters(s):
    char_index_map = {}
    start = 0
    longest = ""
    
    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1  # Move start to the right of the last occurrence of char
        char_index_map[char] = i  # Update the last seen index of the character
        
        # Update longest substring if the current length is greater
        if i - start + 1 > len(longest):
            longest = s[start:i + 1]
    
    return longest

if __name__ == "__main__":
    string = "abcabcbb"
    longest_substring = longest_substring_without_repeating_characters(string)
    print("The Longest substring without repeating characters is:", longest_substring)
