def read_single_digit(n):
    if n=='0':
        print('영',end='')
    if n=='1':
        print('일',end='')
    if n=='2':
        print('이',end='')
    if n=='3':
        print('삼',end='')
    if n=='4':
        print('사',end='')
    if n=='5' :
        print('오',end='')
    if n=='6' :
        print('육',end='')
    if n=='7' :
        print('칠',end='')
    if n=='8':
        print('팔',end='')
    if n=='9':
        print('구',end='')


def read_number(num):
    A=read_single_digit(num[0])
    B=read_single_digit(num[1])
    C=read_single_digit(num[2])


number=input('세 자리 정수 입력: ')
read_number(number)
