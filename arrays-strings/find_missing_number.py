def find_missing_numbers(nums):
# calculate the expected sum for numbers from 0 to n
    n = len(nums)
    expected_sum = n * (n+1) // 2

    # calculating the actual sum of all elements in the array
    actual_sum = sum(nums)

    # The missing number is the difference between the expected and actual sum
    return expected_sum - actual_sum

if __name__  ==  "__main__":
    array = [0,1,3]
    missing_num = find_missing_numbers(array)
    print("The missing number is: " , missing_num)