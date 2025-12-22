h = float(input("Nhập độ dài cạnh h: "))
w = float(input("Nhập độ dài cạnh w: "))
chu_vi = (w + h) * 2
dien_tich = w * h
while True:
    if 0.0 <= w and h <= 100.0:
        break
    else:
       print("Dữ liệu sai phải thỏa điều kiện")
print("Chu vi hình chữ nhật là: ", chu_vi)
print("Diện tích hình chữ nhật là: ", dien_tich)

