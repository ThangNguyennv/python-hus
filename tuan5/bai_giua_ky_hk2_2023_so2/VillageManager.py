from Village import Village
import csv


def read_village_from_file(fileName):
    """
    Hàm đọc tệp dữ liệu về phường. Hàm này thực hiện đọc dữ liệu từ các phường
    từ tệp fileName sau đó tạo ra các đối tượng Village tương ứng và lưu vào 1 danh
    sách, sau khi kết thúc việc đọc dữ liệu, hàm này trả lại danh sách các phường
    đã tạo được.

    dữ liệu trong tệp fileName được lưu dưới dạng csv,
    dòng đầu tiên là tên các thuộc tính của phường: vid,name,town
    các dòng tiếp theo, mỗi dòng chứa thông tin của 1 phường, mỗi thông tin cách nhau bởi 1 dấu phẩy ,
    Ví dụ:
    vid,name,town
    D-00001,Phúc Xá,Ba Đình
    B-00004,Trúc Bạch,Ba Đình
    D-00006,Vĩnh Phúc,Ba Đình
    """
    village_list = []
    with open(fileName, encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            vid = row[0]
            name = row[1]
            town = row[2]

            village = Village(name, vid, town)
            village_list.append(village)
    return village_list


def read_village_student_from_file(fileName, village_list):
    """
    Hàm thực hiện việc đọc file số lượng thí sinh thi vào cấp 3 của mỗi phường để bổ sung thêm thông tin
    vào thuộc tính student của mỗi Village trong village_list,
    Nhiệm vụ của hàm này là đọc dữ liệu số lượng thí sinh thi vào cấp 3 theo năm và ghi vào thuộc tính student
    của phường đó. Chú ý là việc thêm thông tin cần theo đúng mã phường (vid) của phường đó.

    fileName chứa thông tin về số lượng thí sinh thi vào cấp 3 theo từng năm
    được lưu dưới dạng csv.
    Dòng đầu tiên là tên các thuộc tính của dữ liệu: vid,2018,2019,2020,2021,2022,2023 (mã phường và các năm khảo sát)
    dữ liệu của mỗi phường được lưu trên 1 dòng bao gồm mã phường và số lượng thí sinh tương ứng với năm đó.

    Ví dụ về file:

    vid,2018,2019,2020,2021,2022,2023
    D-00001,7408,7554,7674,7775,7875,7969
    B-00004,6758,6883,6986,7074,7148,7277
    D-00006,7000,7114,7197,7331,7470,7566
    D-00007,7377,7492,7592,7710,7843,7942
    """
    with open(fileName, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)

        year_list = header[1:]
        student_dicts = {}

        for row in reader:
            vid = (row[0])  # cột đầu tiên là các giá trị vid
            student_quantities = row[1:]  # từ cột 1 trở đi là số lượng thí sinh của từng năm theo mỗi phường
            quantities = {}
            for i, year in enumerate(year_list):
                try:
                    student_quantity = (student_quantities[i])
                except ValueError:
                    student_quantity = 0
                quantities[int(year)] = int(student_quantity)

            student_dicts[vid] = quantities

        for village in village_list:
            if village.vid in student_dicts:
                village.student = student_dicts[village.vid]


def get_Hanoi_student_change(village_list):
    """
    Hàm thực hiện trả về danh sách các năm (int)được sắp xếp tăng dần theo
    số lượng thí sinh thi vào cấp 3 TĂNG THÊM mỗi năm trên toàn thành phố Hà Nội.
    output: [2019, 2020, 2021, 2022, 2023]
    """
    year_list = {}
    for x in village_list:
        for year, quantity in x.student.items():
            year_list[year] = year_list.get(year, 0) + quantity
    result = {}
    for k, v in year_list.items():
        if k != next(iter(year_list)):
            result[k] = v - year_list[next(iter(year_list))]

    sorted_result = dict(sorted(result.items(), key=lambda item: item[1]))
    m = []
    for k in sorted_result.keys():
        m.append(k)
    return m


def get_top_village_by_year(village_list, rank, year):
    """
    Hàm trả về 1 danh sách tên phường với xếp hạng ( = rank)
    và có số lượng thí sinh trong năm (year)
    lớn hơn giá trị trung bình của tất cả số thí sinh của thành phố Hà Nội trong năm đó
    Danh sách được sắp sếp theo số lượng thí sinh.

    Ví dụ: rank = 2, year = 2018
    Tìm tất cả tên phường trong đó phường là phường loại 2 có số thí sinh thi vào cấp 3
    năm 2018 lớn hơn trung bình số thí sinh thi vào cấp 3 năm 2018 trên toàn thành phố Hà Nội.
    output: ['Cống Vị',...,'Yên Hòa']
    """
    village_rank_list = []
    for x in village_list:
        if x.get_rank() == rank:
            village_rank_list.append(x)
    sum_quantity_student_year = sum(x.student[year] for x in village_list)
    average_student_year = sum_quantity_student_year / len(village_list)
    result = []
    for x in village_rank_list:
        for k, v in x.student.items():
            if k == year:
                if v > average_student_year:
                    result.append(x)
    result.sort(key=lambda x: x.student[year])
    m = [x.name for x in result]
    return m


def sorted_town_by_avg_student(village_list):
    """
    Hàm trả về một danh sách các quận (town) được xắp sếp tăng dần
    theo số lượng thí sinh thi cấp 3 trung bình của các phường trong quận đó.
    Giá trị trung bình được tính trên tất cả các năm cho tất cả các phường thuộc quận đó

    output: ['Ba Đình','Cầu Giấy','Hoàn Kiếm','Long Biên','Tây Hồ']
    """
    town_all_list = []
    for x in village_list:
        town_all_list.append(x.town)
    unique_town_list = set(town_all_list)
    result = {}
    for y in unique_town_list:
        sum_student_quantities = 0
        count = 0
        for x in village_list:
            if x.town == y:
                for v in x.student.values():
                    sum_student_quantities += v
                count += 1
        result[y] = int(sum_student_quantities / count)
    sorted_result = dict(sorted(result.items(), key=lambda item: item[1]))
    m = []
    for k in sorted_result.keys():
        m.append(k)
    return m
