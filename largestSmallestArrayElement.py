# Find the largest/smallest element in array

arr = [3, 1, 4, 1, 5, 9, 2, 6]
largest = arr[0]
smallest = arr[0]

for num in arr:
    if num>largest:
        largest = num
    if num<smallest:
        smallest = num
print("Largest:" , largest, "Smallest:", smallest)

# using built in function

small = min(arr)
large = max(arr)
print("large:",large,"small:", small)

# using sorting

sorted_arr = sorted(arr)  # Sorts the array in ascending order

smallest = sorted_arr[0]
largest = sorted_arr[-1]
print("Smallest:", smallest, "Largest:", largest)
