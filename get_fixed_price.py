per=0

def set_per(percent):
    global per
    per = percent

def get_per():
    return per

def get_fixed_price(price):
    return price/(1-per/100)


def main():
    print('상품 가격 계산 모듈 테스트')

    percent=int(input('할인율은?'))
    set_per(percent)
    
    A=int(input('A 상품의 할인된 가격은?'))
    B=int(input('B 상품의 할인된 가격은?'))
    print('A 상품의 정가는',get_fixed_price(A),'원')
    print('B 상품의 정가는',get_fixed_price(B),'원')

if __name__=='__main__':
    main()
