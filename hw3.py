import get_fixed_price as fix

percent=int(input('할인율은?'))
fix.set_per(percent)

A=int(input('A 상품의 할인된 가격은?'))
B=int(input('B 상품의 할인된 가격은?'))

print('A 상품의 정가는',fix.get_fixed_price(A),'원')
print('B 상품의 정가는',fix.get_fixed_price(B),'원')
