'''
    Bài 1: Tìm kiếm một phần tử trong mảng
        Bài toán: Cho một mảng đã sắp xếp, tìm kiếm một phần tử trong mảng đó.
        Giải pháp: Sử dụng thuật toán Binary Search để tìm kiếm nhanh chóng.
        VD: arr = [1, 3, 5, 7, 9, 11, 13]
            target = 5
'''

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

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(binary_search(arr, target))  # Output: 3