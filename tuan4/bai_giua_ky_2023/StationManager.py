from Station import Station
import csv

# Hàm đọc dữ liệu về các trạm
def read_sation_fromfile(station_file):
    '''
    Hàm thực hiện đọc dữ liệu từ file station_file, đây là 1 file định dạng csv,
    mỗi dữ liệu được phân cách nhau bởi dấu phẩy , (xem file dữ liệu mẫu station.csv để rõ hơn)
    dòng đầu tiên là tên các thuộc tính của trạm

    các dòng tiếp theo, mỗi dòng gồm 4 thông tin tương ứng với các thuộc tính của trạm


    Hướng dẫn:
        Đọc dòng đầu tiên để biết được thứ tự các thuộc tính (có thể bỏ qua dòng này nếu đã biết được thứ tự đó)
        Với mỗi dòng tiếp theo, đọc dòng đó, phân tách theo dấu phẩy, lưu các giá trị vào các biến với kiểu dữ liệu tương ứng,
        Tạo đối tượng Station với các thuộc tính đã đọc được ở trên, sau đó đưa đối tượng vào danh sách kết quả.

    '''

    station_list = []
    with open(station_file, encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Bỏ qua dòng tiêu đề

        for row in reader:
            name = row[0]
            sid = row[1]
            lon = float(row[2])
            lat = float(row[3])

            station = Station(name, sid, lat, lon)
            station_list.append(station)
    return station_list

# Hàm đọc dữ liệu về lượng mưa
def read_rain_fromfile(rain_file, station_list):
    '''
    Hàm thực hiện đọc dữ liệu từ file rain_file, đây là 1 file định dạng csv,
    mỗi dữ liệu được phân cách nhau bởi dấu phẩy , (xem file dữ liệu mẫu rain.csv để rõ hơn)

    MỤC TIÊU CỦA HÀM LÀ ĐỌC DỮ LIỆU MƯA CỦA MỖI TRẠM, để bổ sung thông tin rain cho các trạm trong station_list

    dòng đầu tiên là nhãn time và tên của các trạm (có 146 trạm),
    - Mỗi dòng tiếp theo gồm 147 giá trị, giá trị đầu tiên 1 chuỗi (str) chỉ là thời gian định dạng năm-tháng-ngày,
        và 146 giá trị tiếp theo là lượng mưa của từng trạm

    Hướng dẫn:
        Đọc dòng đầu tiên để biết được thứ tự của các trạm dựa vào tên trạm
        - Có thể lưu các tên trạm vào 1 danh sách, hoặc 1 cách biểu diễn nào đó để biết được thứ tự của trạm theo tên trạm
        - Tạo 1 danh sách, trong đó mỗi phần tử là 1 từ điển, thứ tự của các phần tử nên trùng với thứ tự của tên trạm

        Với mỗi dòng tiếp theo, đọc dòng đó, phân tách các giá trị theo dấu phẩy,
            - giá trị đầu tiên là chuỗi thời gian sẽ là khóa
            - 146 giá trị tiếp theo sẽ là các giá trị tương ứng với khóa trên
            - Thêm lần lượt các cặp khóa-giá trị vào các từ điển trong danh sách theo thứ tự

        Sau khi đọc hết tệp,
        Cập nhật thông tin của các trạm trong station_list bằng cách gọi đến hàm set_rain_infor của mỗi trạm, với các từ điển tương ứng đã được
        tạo ở bước trước

    '''
    with open(rain_file, encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # lấy dòng tiêu đề, sau đó reader sẽ không đọc dòng tiêu đề nữa

        # Danh sách tên trạm (bỏ cột đầu tiên là "time")
        station_names = header[1:]

        # Tạo 1 từ điển để tra nhanh: tên trạm → đối tượng Station
        name_to_station = {}
        for s in station_list:
            name_to_station[s.name] = s

        # Khởi tạo dict mưa rỗng cho từng trạm
        rain_dicts = {}
        for name in station_names:
            rain_dicts[name] = {}

        # Đọc từng dòng(hàng) dữ liệu mưa
        for row in reader:
            date = row[0]  # giá trị đầu tiên là thời gian(ngày)
            rain_values = row[1:]  # còn lại là tất cả các giá trị mưa

            # enumerate: hàm duyệt có chỉ số(index)
            for i, name in enumerate(station_names):
                try:
                    rain_value = float(rain_values[i])
                except ValueError:
                    rain_value = 0.0  # nếu dữ liệu lỗi, gán 0
                rain_dicts[name][date] = rain_value
        for station in station_list:
            if station.name in rain_dicts:
                station.set_rain_infor(rain_dicts[station.name])


def count_rainy_day(s):
    '''
    imput: s là 1 Station

    Hàm thực hiệm tìm và trả về số ngày mưa (lượng mưa > 0) của trạm s

    '''
    count = 0
    for k, v in s.rain.items():
        if v > 0:
            count += 1
    return count


def get_stations_rain_frequent(station_list):
    '''
    imput:station_list là một danh sách các Station

    Hàm thực hiệm tìm và trả về 1 danh sách k tên trạm trong station_list có số ngày mưa nhiều nhất
    (có thể có 1 trạm hoặc nhiều hơn 1 trạm có cùng số ngày mưa)
    Danh sách kết quả được sắp xếp tăng dần theo tên trạm

    '''
    for station in station_list:
        station.rain_count = count_rainy_day(station)

    max_rain_days = max(s.rain_count for s in station_list)

    top_stations = [s for s in station_list if s.rain_count == max_rain_days]

    top_stations.sort(key=lambda s: s.name)

    result = [s.name for s in top_stations]
    return result


def find_k_neighbor(s, station_list, k=5):
    '''
    imput: s là 1 Station, station_list là một danh sách các Station

    Hàm thực hiệm tìm và trả về 1 danh sách k tên trạm trong station_list,
    có khoảng cách gần nhất với trạm s,
    Danh sách kết quả được sắp xếp tăng dần theo khoảng cách tới trạm s

    '''
    other_stations = [station for station in station_list if station.sid != s.sid]
    for station in other_stations:
        station.distanceToS = station.get_distance(s)
    other_stations.sort(key=lambda st: st.distanceToS)
    min_stations = other_stations[:k]
    result = [st.name for st in min_stations]
    return result


def find_stations_rain_under_avg(station_list):
    '''
    imput:station_list là một danh sách các Station

    Hàm thực hiệm tìm và trả về 1 danh sách k tên trạm trong station_list có tổng lượng mưa thấp
    hơn tổng lượng mưa trung bình của tất cả các trạm trong station_lít

    Danh sách kết quả được sắp xếp tăng dần theo tên trạm

    '''
    total_rain = 0
    for station in station_list:
        # Tính tổng giá trị mưa trong từ điển rain
        total_rain += sum(station.rain.values())
    averageRain = total_rain / len(station_list)
    newStationList = [station for station in station_list if sum(station.rain.values()) < averageRain]
    newStationList.sort(key=lambda s: s.name)
    result = [s.name for s in newStationList]
    return result


def find_highest_rain_station(station_list):
    '''
        imput: station_list là một danh sách các Station

        Hàm thực hiện trả về danh sách các tên trạm có tổng lượng mưa lớn nhất
        (có thể có nhiều hơn 1 trạm có lượng mưa bằng lượng mưa lớn nhất)
        danh sách kết quả được sắp tăng dần theo tên trạm

    '''
    max_total_rain = max(sum(s.rain.values()) for s in station_list)
    max_total_rain_list = [s for s in station_list if sum(s.rain.values()) == max_total_rain]
    max_total_rain_list.sort(key=lambda s: s.name)
    result = [s.name for s in max_total_rain_list]
    return result


































