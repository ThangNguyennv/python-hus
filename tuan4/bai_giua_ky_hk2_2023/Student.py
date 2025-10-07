class Student:
    """
    Lớp mô tả 1 sinh viên bao gồm các thông tin sau:
    name :(str) tên sinh viên
    sid:(int) mã số sinh viên có định dạng 2000xxxx trong đó 2 mã số đầu
    đại diện cho năm nhập học của sinh viên.
    Sinh viên năm nhất hiện có mssv bắt đầu bằng 2200xxxx
    department:(str) khoa sinh viên đang theo học.
    grade:(dict) một từ điển chứa mã môn học và điểm số tương ứng với môn học đó.
    điểm được chấm theo thang 100.
    """

    def __init__(self, name, sid, department):
        self.name = name
        self.sid = sid
        self.department = department
        self.grade = dict()

    def __str__(self):
        """
        Hàm in thông tin student sinh viên không cần làm gì hàm này.
        """
        return '{name:%s, sid:%s, department:%s}' % (self.name, self.sid, self.department)

    def get_year(self):
        """
        Hàm trả về sinh viên đang theo học năm thứ mấy.
        sid bắt đầu bằng 2200 : sinh viên năm 1
        sid bắt đầu bằng 2100 : sinh viên năm 2
        ...
        sid bắt đầu bằng 1800: sinh viên năm 5
        """
        if str(self.sid)[:2] == '22':
            return 1
        elif str(self.sid)[:2] == '21':
            return 2
        elif str(self.sid)[:2] == '20':
            return 3
        elif str(self.sid)[:2] == '19':
            return 4
        elif str(self.sid)[:2] == '18':
            return 5
        return None
    def get_avg_grade(self):
        """
        Hàm trả về điểm trung bình của sinh viên
        """
        total = sum(self.grade.values())
        count = len(self.grade)
        return total / count