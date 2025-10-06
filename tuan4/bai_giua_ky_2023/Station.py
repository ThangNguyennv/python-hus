import math

class Station:
    '''
    Lớp mô tả trạm đo lượng mưa gồm các thông tin:
    name: tên trạm
    sid: mã trạm
    lat: vĩ độ
    lon: kinh độ
    rain: từ điển về lượng mưa có khóa là ngày là 1 chuỗi dạng (năm-tháng-ngày),
                  ví dụ 1980-6-22, và giá trị là lượng mưa đo được trong ngày đó

    '''

    # Hàm dựng, sinh viên không cần làm gì với hàm này
    def __init__(self, name, sid, lat, lon):
        self.name = name
        self.sid = sid
        self.lat = lat
        self.lon = lon
        self.rain = dict()

    # Hàm tính gán giá trị cho thuộc tính rain, sinh viên không cần làm gì với hàm này
    def set_rain_infor(self, rain_dict):
        self.rain = rain_dict

    # Hàm tạo ra chuỗi đại diện cho đối tượng, sinh viên không cần làm gì với hàm này
    def __str__(self):
        return '{name:%s, id:%s, lat:%.3f, lon:%.3f}' % (self.name, self.sid, self.lat, self.lon)

    # Hàm tính khoảng cách Euclid từ trạm hiện tại đến trạm stattion
    def get_distance(self, station):
        '''
        Sinh viên cần hoàn thiện hàm này
        Khoảng cách Euclid được tính bằng căn bậc 2 của tổng bình phương của hiệu các tọa độ
        '''

        return math.sqrt((self.lat - station.lat) ** 2 + (self.lon - station.lon) ** 2)

    # Hàm lấy ra giá trị mưa theo ngày
    def get_rain_value(self, date):
        '''
        Sinh viên cần hoàn thiện hàm này,
        nếu date có trong từ điển mưa thì trả lại giá trị là lượng mưa của ngày đó,
        nếu ngược lại thì trả lại giá trị là 0
        '''
        if date in self.rain:
            return self.rain[date]
        else:
            return 0

















