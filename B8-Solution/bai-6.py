# Viết chương trình kiểm tra xem một số nguyên có phải là số thuận nghịch hay không (Palindrome).

def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Kiểm tra
n = int(input("Nhập một số nguyên: "))
if is_palindrome(n):
    print(f"{n} là số thuận nghịch")
else:
    print(f"{n} không phải là số thuận nghịch")
