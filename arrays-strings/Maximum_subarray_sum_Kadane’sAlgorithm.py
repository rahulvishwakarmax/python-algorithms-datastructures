# Kadane's Algorithm: Maximum Subarray Sum
# Kadane's Algorithm is used to find the maximum sum of a contiguous subarray in an array of integers. 
# The algorithm works by keeping track of the current sum of the subarray and updating the maximum sum encountered so far.

def max_subarray_sum(arr):

    max_sum= float('-inf')  # -inf (negative infinity) is used to represent the smallest possible value in mathematics and programming.
    current_sum = 0         

    for num in arr:
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0
    
    return max_sum

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum subarray sum: {max_subarray_sum(array)}")