n = int(input("Nhập vào số n: "))
giai_thua = 1
if 0 < n < 10:
    for i in range(1, n + 1):
        giai_thua *= i
    print(n,"! = ",giai_thua)
else:
    print("n phải thỏa mãn điều kiện 0 < n < 10")