# Method 1 - Using Sets

def intersection(arr1, arr2):
    # convert both lists to sets
    set1 = set(arr1)
    set2 = set(arr2)

    # find intersection
    result = list(set1 & set2)
    return result

array1 = [1, 2, 2, 3, 4, 5]
array2 = [2, 2, 4, 6, 7]
print(f"Intersection: {intersection(array1, array2)}")

# Method 2 - Using Hashmap

def intersection_with_duplicates(arr1, arr2):
    # dictionary to store the frequency of elements in both arrays
    freq1 = {}
    freq2 = {}

    # count frequency of elements in arr1
    for num in arr1:
        if num in freq1:
            freq1[num] += 1
        else:
            freq1[num] = 1

    # count frequency of elements in arr2
    for num in arr2:
        if num in freq2:
            freq2[num] += 1
        else:
            freq2[num] = 1
    result = []
    for num in freq1:
        if num in freq2:
            min_count = min(freq1[num], freq2[num])
            result.extend([num] * min_count)
    for num in freq1:
        if num in freq2:
            min_count = min(freq1[num], freq2[num])
            result.extend([num] * min_count)

    return result

# Example usage:
array1 = [1, 2, 2, 3, 4, 5]
array2 = [2, 2, 4, 6, 7]

print(f"Intersection with duplicates: {intersection_with_duplicates(array1, array2)}")
