class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1>x2:
            rb_x=x1
            lt_x=x2
        else :
            rb_x=x2
            lt_x=x1

        if y1>y2:
            rb_y=y1
            lt_y=y2
        else :
            rb_y=y2
            lt_y=y1

        self.lt = Point(lt_x, lt_y)
        self.rb = Point(rb_x, rb_y)

    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.lt.x},{self.lt.y})이고 우측하단 꼭지점이 ({self.rb.x},{self.rb.y})인 사각형입니다.')
    def getHeight(self):
        return self.lt.y-self.rb.y
    def getWidth(self):
        return self.lt.x-self.rb.x
    def getArea(self):
        return self.getHeight()*self.getWidth()
    def getPerimeter(self):
        return 2*(self.getHeight()+self.getWidth())


r1=Rectangle(5,5,20,10)
a=r1.getArea()
p=r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
        


