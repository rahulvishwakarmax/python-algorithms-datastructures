def remove_duplicates(arr):
    if not arr:
        return 0
    
    # Initialize the first pointer
    i = 0

    # Traverse the array with the second pointer
    for j in range(1, len(arr)):
        # When a new unique element is found
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    # returns the length of the array without duplicates
    return i + 1

# Example usage

arr = [1,1,2,2,3,4,4,5]
new_length  = remove_duplicates(arr)
print(f"Length of array without duplicates: {new_length}")
print(f"Modified array: {arr[:new_length]}")