"""
Thuật toán: Merge Sort theo phương pháp không đệ quy (iterative).
            Phương pháp này chia dần dần danh sách thành các nhóm nhỏ hơn và sau đó hợp nhất chúng theo từng cấp độ.
"""

import matplotlib.pyplot as plt

def show_list(arr, title=''):
    fig, ax = plt.subplots(figsize=(20, 4))
    ax.bar(range(len(arr)), arr)
    ax.set_title(title)
    ax.set_xlabel('index')
    ax.set_xticks(range(len(arr)))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()

sample_number_list = [5, 9, 1, 12, 30, 35, 75, 10, 15, 20, 4, 0, 20, 0, 20, 3, 6, 14]
show_list(sample_number_list, title='sample_number_list')

def merge(arr, left, right, mid):
    # Tạo hai mảng con cho phần cần hợp nhất
    arr1 = arr[left:mid]
    arr2 = arr[mid:right]
    
    n1 = len(arr1)
    n2 = len(arr2)
    i = j = 0
    k = left
 
    # Duyệt qua hai mảng con và hợp nhất
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
     
    # Thêm các phần tử còn lại từ mảng con đầu tiên
    arr[k:k+n1-i] = arr1[i:n1]
    # Thêm các phần tử còn lại từ mảng con thứ hai
    arr[k:k+n2-j] = arr2[j:n2]

def merge_sort_iter(arr):
    n = len(arr)
    current_size = 1  # Kích thước mảng con ban đầu là 1
    
    while current_size < n:
        # Duyệt qua các cặp mảng con ở mỗi cấp độ
        for left in range(0, n-1, current_size*2):
            mid = left + current_size
            if mid < n:  # Nếu còn ít nhất một cặp mảng con
                right = min(left + current_size*2, n)
                merge(arr, left, right, mid)
        
        current_size *= 2  # Tăng kích thước mảng con lên gấp đôi

# Driver code
number_list_2 = sample_number_list[:]

merge_sort_iter(number_list_2)

print("Before sorting: {}".format(sample_number_list))
print("After sorting:  {}".format(number_list_2))
show_list(number_list_2, title='number_list_2')
