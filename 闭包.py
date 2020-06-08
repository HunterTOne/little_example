# 闭包
class Line(object):
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k * x + self.b)


line1 = Line(1, 2)
line1(0)
line1(1)
line1(2)