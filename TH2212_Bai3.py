def tim_max(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

def tim_min(a, b, c):
    min_value = a
    if b < min_value:
        min_value = b
    if c > min_value:
        min_value = c
    return min_value

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

result_max = tim_max(a, b, c)
result_min = tim_min(a, b, c)
print(f"Số lớn nhất là: {result_max}")
print(f"Số nhỏ nhất là: {result_min}")