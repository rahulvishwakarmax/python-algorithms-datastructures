def search_in_rotated_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # If the target is found at the mid index
        if arr[mid] == target:
            return mid

        # Check which side is sorted
        if arr[left] <= arr[mid]:
            # Left part is sorted
            if arr[left] <= target < arr[mid]:
                # Target lies in the left sorted part
                right = mid - 1
            else:
                # Target lies in the right unsorted part
                left = mid + 1
        else:
            # Right part is sorted
            if arr[mid] < target <= arr[right]:
                # Target lies in the right sorted part
                left = mid + 1
            else:
                # Target lies in the left unsorted part
                right = mid - 1

    # If the target is not found
    return -1

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = search_in_rotated_array(arr, target)
    if result != -1:
        print(f"Element {target} is found at index {result}.")
    else:
        print(f"Element {target} is not found in the array.")
