a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a + b > c and a + c > b and b + c > a:
    print("Có thể là ba cạnh của tam giác.")
else:
    print("Không thể là ba cạnh của tam giác.")