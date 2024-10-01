def find_majority_element(nums):
    candidate = None
    count = 0

    # Find a candidate

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # verify the candidate

    count = sum(1 for num in nums if num ==  candidate)

    return candidate if count > len(nums) // 2 else None

if __name__ == "__main__":
    array = [3,2,3,5,3]
    majority_element = find_majority_element(array)
    if majority_element:
        print("The majority element is:", majority_element)
    else:
        print("There is no majority element.")