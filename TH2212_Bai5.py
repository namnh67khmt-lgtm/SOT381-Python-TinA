def tinh_ketqua(n):
    tu_so = 0
    for i in range(1, n + 1):
        tu_so += i

    mau_so = 0
    for i in range(2, n + 2, 2):
        mau_so += i

    ket_qua = tu_so / mau_so
    return ket_qua

n = int(input("Nhập số n: "))
result = tinh_ketqua(n)
print(f"Kết quả phép tính là: {result}")