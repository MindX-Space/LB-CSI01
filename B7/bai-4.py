"""
Ta đã biết cách cài đặt của thuật toán Merge Sort qua phương pháp đệ quy. Phương pháp này được sử dụng phổ biến do dễ cài đặt, tuy nhiên ta lại tốn O(log(n)) độ phức tạp bộ nhớ stack cho việc gọi đệ quy.

Ta cũng biết rằng mọi thuật toán đệ quy đều có thể được viết dưới dạng không đệ quy.

Bài toán: Hãy tìm cách cài đặt thuật toán Merge Sort mà không sử dụng đệ quy.

Gợi ý: truy cập file before và after merging trong thư mục image để xem hình minh hoạ
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