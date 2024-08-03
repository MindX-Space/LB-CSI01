# Độ phức tạp thời gian (Time Complexity): O(n)
# Độ phức tạp không gian (Space Complexity): O(1)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 3, 5, 7, 9]
target = 7
print(linear_search(arr, target)) # Output: 3