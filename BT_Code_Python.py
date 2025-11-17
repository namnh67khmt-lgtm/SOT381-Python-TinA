# ======================================
# BÀI 1: Tính tổng và tích hai số
# ======================================
a = int(input("Bài 1 - Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
print("Tổng =", a + b)
print("Tích =", a * b)

# ======================================
# BÀI 2: Chu vi và diện tích hình chữ nhật
# ======================================
dai = float(input("\nBài 2 - Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
print("Chu vi =", 2 * (dai + rong))
print("Diện tích =", dai * rong)

# ======================================
# BÀI 3: Chuyển Celsius → Fahrenheit
# ======================================
c = float(input("\nBài 3 - Nhập độ C: "))
print("Độ F =", (c * 9/5) + 32)

# ======================================
# BÀI 4: Tính BMI
# ======================================
can_nang = float(input("\nBài 4 - Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
print("BMI =", can_nang / (chieu_cao ** 2))

# ======================================
# BÀI 5: Tính tiền điện
# ======================================
kwh = float(input("\nBài 5 - Nhập số kWh: "))
print("Tiền điện =", kwh * 2000, "VND")

# ======================================
# BÀI 6: Tính biểu thức A = x² + 3x – 5
# ======================================
x = float(input("\nBài 6 - Nhập x: "))
print("A =", x**2 + 3*x - 5)

# ======================================
# BÀI 7: Hoán đổi hai biến không dùng biến tạm
# ======================================
a = int(input("\nBài 7 - Nhập a: "))
b = int(input("Nhập b: "))
a, b = b, a
print("Sau khi hoán đổi: a =", a, ", b =", b)

# ======================================
# BÀI 8: Tính tuổi
# ======================================
nam_sinh = int(input("\nBài 8 - Nhập năm sinh: "))
print("Tuổi =", 2024 - nam_sinh)

# ======================================
# BÀI 9: Đổi giờ/phút/giây → tổng số giây
# ======================================
gio = int(input("\nBài 9 - Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
print("Tổng số giây =", gio*3600 + phut*60 + giay)

# ======================================
# BÀI 10: Lãi suất đơn
# ======================================
tien = float(input("\nBài 10 - Nhập số tiền gửi: "))
lai = float(input("Nhập lãi suất (%/năm): "))
thang = int(input("Nhập số tháng gửi: "))
print("Tiền lãi =", (tien * lai * thang) / 1200)

# ======================================
# BÀI 11: Giới thiệu bản thân
# ======================================
ho_ten = input("\nBài 11 - Nhập họ tên: ")
tuoi = input("Nhập tuổi: ")
que = input("Nhập quê quán: ")
print(f"Xin chào, tôi là {ho_ten}, {tuoi} tuổi, đến từ {que}.")

# ======================================
# BÀI 12: Tính phần trăm của một số
# ======================================
so = float(input("\nBài 12 - Nhập số: "))
pt = float(input("Nhập phần trăm cần tính: "))
print("Kết quả =", so * pt / 100)

# ======================================
# BÀI 13: Chia lấy phần nguyên và phần dư
# ======================================
a = int(input("\nBài 13 - Nhập a: "))
b = int(input("Nhập b: "))
print("Phần nguyên =", a // b)
print("Phần dư =", a % b)

# ======================================
# BÀI 14: Tính vận tốc
# ======================================
quang_duong = float(input("\nBài 14 - Nhập quãng đường (km): "))
thoi_gian = float(input("Nhập thời gian (giờ): "))
print("Vận tốc =", quang_duong / thoi_gian, "km/h")

# ======================================
# BÀI 15: Tính điểm trung bình 3 môn
# ======================================
toan = float(input("\nBài 15 - Nhập điểm Toán: "))
ly = float(input("Nhập điểm Lý: "))
hoa = float(input("Nhập điểm Hóa: "))
print("Điểm trung bình =", (toan + ly + hoa) / 3)

# ======================================
# BÀI 16: Diện tích và chu vi hình tròn
# ======================================
PI = 3.14159
r = float(input("\nBài 16 - Nhập bán kính: "))
print("Chu vi =", 2 * PI * r)
print("Diện tích =", PI * r * r)

# ======================================
# BÀI 17: Tính tiền sau giảm giá 15%
# ======================================
tien = float(input("\nBài 17 - Nhập giá trị đơn hàng: "))
print("Tiền sau giảm =", tien * 0.85)

# ======================================
# BÀI 18: Tổng số giờ làm việc
# ======================================
gio_ngay = float(input("\nBài 18 - Nhập số giờ làm mỗi ngày: "))
so_ngay = int(input("Nhập số ngày làm trong tháng: "))
print("Tổng giờ làm =", gio_ngay * so_ngay)

# ======================================
# BÀI 19: Đổi mét → cm, mm
# ======================================
m = float(input("\nBài 19 - Nhập mét: "))
print("Centimet =", m * 100)
print("Milimet =", m * 1000)

# ======================================
# BÀI 20: Nhiều phép toán
# ======================================
a = float(input("\nBài 20 - Nhập a: "))
b = float(input("Nhập b: "))
print("Tổng =", a + b)
print("Hiệu =", a - b)
print("Tích =", a * b)
print("Thương =", a / b)
print("Lũy thừa a^b =", a ** b)
print("Chia phần nguyên =", a // b)
print("Chia phần dư =", a % b)

