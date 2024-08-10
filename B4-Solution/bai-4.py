'''
    Bài 4: Tìm kiếm phần tử nhỏ nhất trong mảng
        Bài toán: Cho một mảng, tìm phần tử nhỏ nhất trong mảng.
        Giải pháp: Sử dụng Linear Search để tìm phần tử nhỏ nhất.
        VD: arr = [1, 3, 7, 8, 5, 6, 2]
'''

def find_min(arr):
    if not arr:
        return None
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

arr = [1, 3, 7, 8, 5, 6, 2]
print(find_min(arr))  # Output: 1