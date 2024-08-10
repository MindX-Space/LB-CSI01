'''
    Bài 3: Tìm kiếm phần tử lớn nhất trong mảng
        Bài toán: Cho một mảng, tìm phần tử lớn nhất trong mảng.
        Giải pháp: Sử dụng Linear Search để tìm phần tử lớn nhất.
        VD: arr = [1, 3, 7, 8, 5, 6, 2]
'''

def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

arr = [1, 3, 7, 8, 5, 6, 2]
print(find_max(arr))  # Output: 8
