# Độ phức tạp thời gian (Time Complexity): O(log n)
# Độ phức tạp không gian (Space Complexity): O(1) cho phiên bản lặp, O(log n) cho phiên bản đệ quy

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(binary_search(arr, target))  # Output: 4