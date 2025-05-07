count = {}

while True :
    item =input('상품명? ')
    if item == '':
        break
    else :
        mount=int(input('수량은? '))
        count[item]=mount
        print(f'장바구니에 {item} {mount}개가 담겼습니다.')
        print()
        

print()
print(f'>>> 장바구니 보기 : {count}')

print()
print('[검색]')
find=input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{find}은(는) {count[find]}개 담겨 있습니다.')
