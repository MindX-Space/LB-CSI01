# Viết chương trình tính số Fibonacci thứ n bằng phương pháp đệ quy.

def fibonacci(n):
    if n <= 0:
        return "Số không hợp lệ"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Kiểm tra
n = int(input("Nhập n: "))
print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")
