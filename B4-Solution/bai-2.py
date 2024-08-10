'''
    Bài 2: Tìm kiếm tất cả các lần xuất hiện của một phần tử trong mảng
        Bài toán: Cho một mảng, tìm tất cả các vị trí xuất hiện của một phần tử trong mảng.
        Giải pháp: Sử dụng Linear Search để duyệt qua toàn bộ mảng và ghi nhận các vị trí xuất hiện.
        VD: arr = [1, 3, 7, 8, 7, 5, 6, 7, 2]
            target = 5
'''

def linear_search_all(arr, target):
    positions = []
    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)
    return positions

arr = [1, 3, 7, 8, 7, 5, 6, 7, 2]
target = 7
print(linear_search_all(arr, target))  # Output: [2, 4, 7]