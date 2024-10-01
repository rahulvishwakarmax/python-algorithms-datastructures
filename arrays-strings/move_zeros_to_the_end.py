def move_zeros_to_end(arr):
    # pointer for the position of the next non-zero element
    j = 0

    # traverse throught he array
    for i in range(len(arr)):
        # if the current element is not zero , swap it with the element at position j
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

array = [0,1,0,3,12]
print(f"Array after moving zeros to the end: {move_zeros_to_end(array)}")