# Viết chương trình đếm số lần xuất hiện của mỗi phần tử trong một danh sách.

def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Kiểm tra
lst = [1, 2, 2, 3, 4, 4, 4, 5]
print(count_occurrences(lst))
