'''
Thời gian: O(n), vì mỗi phần tử của danh sách được xử lý tối đa hai lần (một lần khi mở rộng và một lần khi rút ngắn).
Không gian: O(1), vì chỉ sử dụng các biến số cố định.
'''

def has_subarray_with_sum(k, nums):
    start = 0
    current_sum = 0
    
    for end in range(len(nums)):
        current_sum += nums[end]
        
        # Rút ngắn dãy con từ bên trái nếu tổng vượt quá k
        while current_sum > k and start <= end:
            current_sum -= nums[start]
            start += 1
        
        # Kiểm tra nếu tổng của dãy con hiện tại bằng k
        if current_sum == k:
            return True
    
    return False

# Ví dụ:
k1 = 8
nums1 = [1, 5, 3, 2, 5]
print(has_subarray_with_sum(k1, nums1))  # Output: True

k2 = 5
nums2 = [1, 5, 3, 2, 5]
print(has_subarray_with_sum(k2, nums2))  # Output: True
