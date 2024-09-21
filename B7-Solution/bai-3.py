"""
Thuật toán: Counting Sort, là một thuật toán có độ phức tạp O(n+k) với n là số lượng phần tử và k là miền giá trị. 
            Nên sử dụng các bài toán có số lượng giá trị không lớn và có tính nguyên vẹn.
            Tuy nhiên cần đảm bảo miền giá trị được xử lý chính xác và các bước tính toán giá trị index cần phải hợp lý.
"""

flower_prices = [
    {'name': 'Red Rose', 'price': 10000},
    {'name': 'Lily', 'price': 12000},
    {'name': 'Orchid', 'price': 100000},
    {'name': 'Blue Rose', 'price': 20000},
    {'name': 'Daisy', 'price': 12000},
    {'name': 'Tulip', 'price': 20000},
    {'name': 'Chrysanthemum', 'price': 10000},
    {'name': 'Sunflower', 'price': 20000}
]

def counting_sort_flower(arr):
    # trivial cases
    if len(arr) <= 1:
        return arr
    
    # get the range of counting indices
    min_val = 10  # representing 10,000
    max_val = 100  # representing 100,000
    val_range = max_val - min_val + 1
    
    # count occurrences of each value
    count = [0] * val_range
    for flower in arr:
        count_index = flower['price'] // 1000 - min_val
        count[count_index] += 1
        
    # build `next_indices` by creating a cumulative count
    next_indices = [0] * val_range
    total_count = 0
    for i in range(val_range):
        next_indices[i] = total_count
        total_count += count[i]
    
    # traverse `arr` to place the values into `sorted_arr`
    sorted_arr = [None] * len(arr)
    for flower in arr:
        count_index = flower['price'] // 1000 - min_val
        sorted_arr[next_indices[count_index]] = flower
        next_indices[count_index] += 1
        
    return sorted_arr

flower_prices_2 = flower_prices[:]

flower_prices_2 = counting_sort_flower(flower_prices_2)

print("Before sorting:")
for flower in flower_prices:
    print(flower)
print("After sorting:")
for flower in flower_prices_2:
    print(flower)