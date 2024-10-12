def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0] # Take the first string as the initial prefix

    for s in strs[1:]: # Compare with all other strings
        # While the current string doesn't start with the current prefix
        while not s.startswith(prefix):
            prefix = prefix[:-1] # Reduce the prefix by one character
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    strings = ["flower", "flow", "flight"]
    common_prefix = longest_common_prefix(strings)
    print("The Longest common prefix is:", common_prefix)