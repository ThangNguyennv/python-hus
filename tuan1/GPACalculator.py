# Viết chương trình tính GPA và xếp loại tương ứng khi biết điểm tổng kết học phần và số tín chỉ của từng môn học
n = int(input())
sumDiem = 0
sumTC = 0
for i in range(n):
    tinChi, diem = input().split()
    tinChi = int(tinChi)
    diem = float(diem)
    sumTC += tinChi
    if 9.0 <= diem <= 10.0:
        sumDiem += tinChi * 4.0
    elif 8.5 <= diem <= 8.9:
        sumDiem += tinChi * 3.7
    elif 8.0 <= diem <= 8.4:
        sumDiem += tinChi * 3.5
    elif 7.0 <= diem <= 7.9:
        sumDiem += tinChi * 3.0
    elif 6.5 <= diem <= 6.9:
        sumDiem += tinChi * 2.5
    elif 5.5 <= diem <= 6.4:
        sumDiem += tinChi * 2.0
    elif 5.0 <= diem <= 5.4:
        sumDiem += tinChi * 1.5
    elif 4.0 <= diem <= 4.9:
        sumDiem += tinChi * 1.0
    elif 0.0 <= diem <= 3.9:
        sumDiem += tinChi * 0.0

gpa = float(sumDiem / sumTC)
gpa = round(gpa, 2)
if 3.6 <= gpa <= 4.0:
    print(f"{gpa}:", "Excellent")
elif 3.2 <= gpa <= 3.59:
    print(f"{gpa}:", "Very good")
elif 2.5 <= gpa <= 3.19:
    print(f"{gpa}:", "Good")
elif 2.0 <= gpa <= 2.49:
    print(f"{gpa}:", "Average")
elif gpa <= 2.0:
    print(f"{gpa}:", "At risk")
