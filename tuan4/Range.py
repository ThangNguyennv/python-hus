#Viết chương trình tìm tất cả các số chia hết cho 11 nhưng không phải bội số của 3, nằm trong đoạn a và b (tính cả a và b).
#Với a, b là các số nguyên được nhập từ bàn phím.
#Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu chấm phẩy và dấu cách “; ”.
def solve():
    a = int(input())
    b = int(input())
    k = []
    for i in range(a, b+1):
        if i % 11 == 0 and i % 3 != 0:
            k.append(str(i))
    for i in range(0, len(k) - 1):
        print(k[i] + '; ' , end='')
    print(k[len(k)-1])
solve()