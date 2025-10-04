def loan(A, r, n):
    print("Vay:", "{:,.2f}".format(A), "Đồng")
    print("Lãi suất:", "{:,.2f}".format(r * 100) + "%/tháng")
    print("Trong:", "{:,.2f}".format(n), "tháng")
    X = ((A * (1 + r) ** n) * r) / (((1 + r) ** n) - 1)
    print("Mỗi tháng cần trả: " + " {:,.3f}".format(X), "Đồng")