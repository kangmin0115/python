a = input()
b = input()
if a == '가위':
    if b == '가위':
        print('비겼습니다')
    elif b == '바위':
        print('B가 이겼습니다')
    elif b == '보':
        print('A가 이겼습니다')
elif a == '바위':
    if b == '가위':
        print('A가 이겼습니다')
    elif b == '바위':
        print('비겼습니다')
    elif b == '보':
        print('B가 이겼습니다')

elif a == '보':
    if b == '가위':
        print('B가 이겼습니다')
    elif b == '바위':
        print('A가 이겼습니다')
    elif b == '보':
        print('비겼습니다')
else:
    pass
