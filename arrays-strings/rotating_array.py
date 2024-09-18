# Rotating an array by K Elements (Method 1: Using slicing)

def rotate_array(arr, k1):
    # In case k1 is larger than array length, we use modulo to keep it within bounds
    k1 = k1 % len(arr)
    return arr[-k1:] + arr[:-k1]

# Example for Method 1
arr = [10, 2, 8, 7, 5, 1, 12]
k1 = 3
rotated = rotate_array(arr, k1)
print("Rotated Array using slicing:", rotated)


# Method 2: Using Reversal Algorithm

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_in_place(arr, k2):
    n = len(arr)
    k2 = k2 % n  # Ensure k2 is within array bounds
    
    # Step 1: Reverse the entire array
    reverse(arr, 0, n-1)
    
    # Step 2: Reverse the first k2 elements
    reverse(arr, 0, k2-1)
    
    # Step 3: Reverse the remaining n-k2 elements
    reverse(arr, k2, n-1)

# Example for Method 2
arr = [1, 2, 3, 4, 5]
k2 = 2
rotate_array_in_place(arr, k2)
print("Rotated Array (in-place):", arr)
