"""
Một siêu thị lưu danh sách các mặt hàng dưới dạng list, mỗi mặt hàng là một dictionary như sau:
   {"id": 354, "name": "Vinamilk Icecream", "price": 35000}

Cho danh sách mặt hàng đã được sắp xếp theo giá từ lớn đến nhỏ, hãy tìm tất cả mặt hàng có giá tiền p được nhập.

Input: Danh sách các mặt hàng và giá tiền p cần tìm.
Output: Danh sách các mặt hàng có giá tiền p, hoặc "Not found".
"""

sample_input_list = [
    {"id": 613, "name": "Television", "price": 12000000},
    {"id": 982, "name": "Headphone", "price": 1000000},
    {"id":  24, "name": "Backpack", "price": 250000},
    {"id": 389, "name": "Vinamilk Icecream", "price": 35000},
    {"id": 432, "name": "Big Cola", "price": 20000},
    {"id": 678, "name": "Chocopie", "price": 20000},
    {"id": 354, "name": "Mint", "price": 15000}
]

sample_output_list = [
    {"id": 432, "name": "Big Cola", "price": 20000},
    {"id": 678, "name": "Chocopie", "price": 20000}
]