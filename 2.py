def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(r):
    area=r*r*3.14
    return area

result = get_radius('넓이를 구하고자하는 원의 반지름은?')
print('반지름',result,'인 원의 넓이 = 3.14 x',result,'x',result,'=')
result = get_circle_area(r)
