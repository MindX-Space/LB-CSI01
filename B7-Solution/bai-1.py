"""
Thuật toán: Binary Search, mục đích là để tìm một giá trị trong danh sách đã sắp xếp giảm dần theo giá. 
            Sau khi tìm thấy một giá trị khớp, thuật toán tiếp tục tìm kiếm sang trái và phải của vị trí tìm thấy để tìm tất cả các mặt hàng có cùng giá.
Độ phức tạp: O(log n)
"""

ample_input_list = [
    {"id": 613, "name": "Television", "price": 12000000},
    {"id": 982, "name": "Headphone", "price": 1000000},
    {"id":  24, "name": "Backpack", "price": 250000},
    {"id": 389, "name": "Vinamilk Icecream", "price": 35000},
    {"id": 432, "name": "Big Cola", "price": 20000},
    {"id": 678, "name": "Chocopie", "price": 20000},
    {"id": 354, "name": "Mint", "price": 15000}
]

def binary_search_comp(data_list, value, compare_func):
    left = 0
    right = len(data_list) - 1
 
    while left <= right:
        mid = (left + right) // 2
        mid_item = data_list[mid]
        
        compare_result = compare_func(mid_item, value)  # do comparison
        if compare_result == 1:  # larger
            left = mid + 1
        elif compare_result == -1:  # smaller
            right = mid - 1
        else:  # equal
            return mid

    return -1

def compare(item, num):
    if item['price'] < num:
        return -1  # smaller
    elif item['price'] > num:
        return 1   # larger
    return 0  # equal

def find_items(item_list, price):
    # Check for empty list
    if not item_list:
        return "List is empty"
    
    # Binary search for one index
    index = binary_search_comp(item_list, price, compare)
    
    if index == -1:
        return "Not found"
    else:
        # If found, search left and right for same-price items
        length = len(item_list)
        left = index
        right = index
        
        # Find items on the left with the same price
        while left > 0 and item_list[left - 1]['price'] == price:
            left -= 1
        
        # Find items on the right with the same price
        while right < length - 1 and item_list[right + 1]['price'] == price:
            right += 1
        
        # Return the items found
        return item_list[left:right + 1]

# Gọi hàm với giá tiền cần tìm
price = 20000
result = find_items(sample_input_list, price)

# In kết quả
if result == "Not found":
    print(f"Item with price {price} not found")
else:
    print(f"Found item(s) with price {price}:")
    for item in result:
        print(item)
