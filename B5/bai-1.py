'''
Thuật toán: Frequency Counting Mode Algorithm

Thời gian: O(n), vì cần duyệt qua danh sách một lần để đếm và một lần để tìm mode.
Không gian: O(n), để lưu trữ tần suất xuất hiện của các phần tử trong dictionary.
'''


from collections import Counter

def find_largest_mode(nums):
    if not nums:
        return None

    # Đếm số lần xuất hiện của mỗi phần tử
    count = Counter(nums)
    
    # Tìm giá trị có tần suất lớn nhất
    max_frequency = max(count.values())
    mode_candidates = [num for num, freq in count.items() if freq == max_frequency]
    
    # Trả về giá trị lớn nhất trong các mode
    return max(mode_candidates)

# Ví dụ:
nums = [1, 2, 3, 2, 3]
result = find_largest_mode(nums)
print(result)  # Output: 3