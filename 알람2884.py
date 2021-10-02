h, m = map(int, input().split())

if h < 24 and m < 60:
    if m > 44:
        print(h, m - 45)
    elif h > 0 and m < 45:
        print(h - 1, m + 15)
    elif h == 0:
        print(h + 23, m + 15)
