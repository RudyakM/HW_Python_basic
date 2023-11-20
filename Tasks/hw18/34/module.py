class Checker:
    msg_ok = 'Треугольник построить можно!'
    msg_err = 'Из этих чисел треугольник собрать не получится...'
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def  is_triangle(self):
        if (self.x + self.y > self.z) and (self.x + self.z > self.y) and (self.y + self.z > self.x):
            return Checker.msg_ok
        else:
            return Checker.msg_err