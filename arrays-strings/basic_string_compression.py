def compress_string(s):
    # Edge case: If the string is empty, return it
    if not s:
        return ""
    
    compressed = []
    count = 1
    
    # Iterate through the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            # Append the character and its count to the compressed list
            compressed.append(s[i - 1] + str(count))
            count = 1
    
    # Don't forget to append the last set of characters
    compressed.append(s[-1] + str(count))
    
    # Join the list into a compressed string
    compressed_str = ''.join(compressed)
    
    # Return the original string if the compressed version is longer
    return compressed_str if len(compressed_str) < len(s) else s

# Example usage:
if __name__ == "__main__":
    string = "aaabbcccc"
    result = compress_string(string)
    print("Compressed string:", result)
