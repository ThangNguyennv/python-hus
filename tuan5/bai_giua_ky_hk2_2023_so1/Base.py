import math


def find_minimum_sum(nums):
    """
    Tìm đỉnh núi có tổng nhỏ nhất.
    Cho một danh sách số nguyên dương nums
    Bộ 3 chỉ số i, j, k được gọi là đỉnh núi nếu thỏa mãn:
    i < j < k và nums[i] < nums[j] và nums[j] > nums[k]
    Ví dụ 1: input [8,6,1,5,3]
    với i = 2, j = 3 k = 4 tương ứng tạo thành một đỉnh núi với tổng bằng 9 (1 + 5 + 3)
    output: 9
    Ví dụ 2: input [5,4,8,7,10,2]
    i = 0, j = 2, k = 5 tạo thành một đỉnh núi với tổng bằng 15.
    i = 1, j = 4, k = 5 tạo thành một đỉnh núi với tổng bằng 16.
    i = 1, j = 2, k = 5 tạo thành một đỉnh núi với tổng bằng 13
    output : 13
    Nếu không tồn tại đỉnh núi nào trong danh sách
    output : -1
    """
    minResult = 9999999999
    check = 0;
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] < nums[j] and nums[j] > nums[k]:
                    minResult = min(minResult, nums[i] + nums[j] + nums[k])
                    check = 1
    if check == 1:
        return minResult
    else:
        return -1


def cosin_distance(v1, v2):
    """
    Tính khoảng cách cosin của 2 vector,
    input: v1, v2 là danh sách có cùng kích thước
    Cosin distance được tính theo công thức:
    cho trong đề bài.
    """
    dot = sum(a * b for a, b in zip(v1, v2))
    norm_u = math.sqrt(sum(c ** 2 for c in v1))
    norm_v = math.sqrt(sum(c ** 2 for c in v2))
    if norm_u == 0 or norm_v == 0:  # tránh chia cho 0
        return 0
    return dot / (norm_u * norm_v)


def get_hightest_gdp(country_list):
    """
    country_list là một danh sách trong đó mỗi phần tử là một tuple có cấu trúc như sau:
    (country_id, region, gdp, area)
    country_id: mã quốc gia
    region: khu vực (Asia, EU, USA...)
    gdp: tổng thu nhập quốc dân
    area: diện tích tương ứng với quốc gia đó
    tìm ra và trả về một danh sách 3 mã quốc gia
    có chỉ số gdp cao nhất được sắp xếp giảm dần theo chỉ số gdp.
    """
    result = []
    max_gdp = max(country[2] for country in country_list)
    count = 0
    for country in country_list:
        if country[2] <= max_gdp:
            count += 1
            if count <= 3:
                result.append(country)
            else:
                break
    result.sort(key=lambda x: x[2], reverse=True)
    k = []
    for i in range(0, 3):
        k.append(result[i][0])
    return k