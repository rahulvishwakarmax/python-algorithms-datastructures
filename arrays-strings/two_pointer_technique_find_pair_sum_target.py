# Implement the two-pointer technique for finding a pair that sums to a target


def find_pair_sum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left<right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return(arr[left], arr[right])
        elif current_sum<target:
            left += 1
        else: right -= 1

    return None

# Example

arr = [10, 2, 8, 7, 5, 1, 12]
target = 20

pair = find_pair_sum(arr, target)

if pair:
    print("Pair found:", pair)
else:
    print("No pair found bitch")
