n = int(input("Nhập số nguyên dương n: "))
tong = 0
for i in range(1, n + 1, 2):
    tong += i ** 2
print("Tổng bình phương các số lẻ từ 1 đến",n,"là:",tong)