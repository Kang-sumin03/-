def buy(count):

    print('[구입]')               #주프로그램부에 while True 반복문 => 선택문으로 변경
    item =input('상품명? ')

    if item == '':
        print()
        return False            #주프로그램부 while True가 무한루프 안되려면 F/T로 반환

    else :
        mount=int(input('수량은? '))
        count[item]=mount
        print(f'장바구니에 {item} {mount}개가 담겼습니다.')
        print()
            
        return True


def show(item_list):
    print(f'>>> 장바구니 보기 :{item_list}')
    print()


def find(shopping_list):
    print('[검색]')
    wish_item=input('장바구니에서 확인하고자 하는 상품은? ')
    if wish_item in shopping_list:
        print(f'{wish_item}은(는) {shopping_list[wish_item]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {wish_item}은(는) 없습니다.')

shopping_bag={}

while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)
