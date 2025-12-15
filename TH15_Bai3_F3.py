n = int(input("Nhập số nguyên n: "))
tong = 0
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:  
        tong += i
print("Tổng các số từ 1 đến", n, "chia hết cho 2 và 3 là:", tong)