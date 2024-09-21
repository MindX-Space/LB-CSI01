"""
Thuật toán: Bubble Sort
            Dùng để sắp xếp các từ dựa trên số ký tự của chúng, và nếu hai từ có cùng số ký tự, bạn so sánh dựa trên thứ tự bảng chữ cái.
"""

most_common_100 = "the of to and a in is it you that he was for on are with as I his they be at one have this from or had by hot but some what there we can out other were all your when up use word how said an each she which do their time if will way about many then them would write like so these her long make thing see him two has look more day could go come did my sound no most number who over know water than call first people may down side been now find"

def sort_word_list(most_common_100):
    # Tách danh sách các từ
    word_list = most_common_100.split(' ')
    
    # Sắp xếp theo chiều dài từ và sau đó theo thứ tự bảng chữ cái
    sorted_words = sorted(word_list, key=lambda word: (len(word), word))
    
    # Ghép lại thành một chuỗi
    return ' '.join(sorted_words)

# Gọi hàm
sorted_words_string = sort_word_list(most_common_100)
print(sorted_words_string)
