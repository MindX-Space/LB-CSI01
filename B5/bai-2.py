"""
Thuật toán: Hash Map

Thời gian: O(n) - vì mỗi phần tử trong danh sách được xét một lần.
Không gian: O(n) - để lưu hash map.
"""

def find_ice_cream_indices(m, prices):
    price_map = {}
    
    for i, price in enumerate(prices):
        complement = m - price
        if complement in price_map:
            return price_map[complement], i
        price_map[price] = i

m = 4
prices = [1, 4, 5, 3, 2]
result = find_ice_cream_indices(m, prices)
print(result)  # Output: (0, 3)