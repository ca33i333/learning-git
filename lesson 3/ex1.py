# Hàm đảo ngược
def daoNguoc(xuoi):
    nguoc = 0

    while xuoi > 0:
        x = xuoi % 10
        xuoi = xuoi // 10
        nguoc = nguoc * 10 + x
    return nguoc

# Check số đối xứng
n = int(input())
m = daoNguoc(n)
if n == m:
    print("So doi xung")
else:
    print("Khong phai so doi xung")

# In ra các số đối xứng từ 10 đến 1000
for i in range(10, 1000):
    m = daoNguoc(i)
    if i == m:
        print(i)