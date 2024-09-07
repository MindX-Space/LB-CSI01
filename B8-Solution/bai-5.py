# Viết chương trình nhận vào một chuỗi và trả về chuỗi đã được đảo ngược.

def reverse_string(s):
    return s[::-1]

# Kiểm tra
s = input("Nhập chuỗi: ")
print("Chuỗi sau khi đảo ngược:", reverse_string(s))
