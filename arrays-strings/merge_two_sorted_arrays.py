# Merge Two Sorted Arrays

def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = j = 0

    # traverse both arrays and insert the smaller element into the merged array
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # if there are  remaining elements in arr1 , append them

    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    
    # if there are  remaining elements in arr2 , append them
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    
    return merged_array

if __name__ == "__main__":
    array1 = [1, 3, 5, 7]
    array2 = [2, 4, 6, 8]

print(f"Merged Sorted Array: {merge_sorted_arrays(array1, array2)}")