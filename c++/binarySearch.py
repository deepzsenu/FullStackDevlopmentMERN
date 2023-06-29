import time

# Binary search using iteration
def binary_search_iterative(arr, key):
    start_time = time.perf_counter()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            end_time = time.perf_counter()
            return mid, end_time - start_time
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    end_time = time.perf_counter()
    return -1, end_time - start_time

# Binary search using recursion
def binary_search_recursive(arr, key, low, high):
    if low > high:
        return -1, 0
    
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid, 0
    elif arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, high)
    else:
        return binary_search_recursive(arr, key, low, mid - 1)

# Get user input
print("\nBinary Search (Iterative approach)")
print("Enter 5 elements:")
arr = []
for i in range(5):
    element = int(input())
    arr.append(element)

arr.sort()  # Optional: Sorting the array

key = int(input("Enter the key element to search: "))

# Perform binary search using iteration
start_time = time.perf_counter()
index, time_taken = binary_search_iterative(arr, key)
end_time = time.perf_counter()
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
print("Total time taken by CPU (End Time - Start Time) / clock per_sec:", time_taken)

print("\nBinary Search (Recursive approach)")
# Get user input
print("Enter 5 elements:")
arr = []
for i in range(5):
    element = int(input())
    arr.append(element)

arr.sort()  # Optional: Sorting the array

key = int(input("Enter the key element to search: "))

# Perform binary search using recursion
start_time = time.perf_counter()
index, _ = binary_search_recursive(arr, key, 0, len(arr) - 1)
end_time = time.perf_counter()
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
print("Total time taken by CPU (End Time - Start Time) / clock per_sec:", end_time - start_time)
