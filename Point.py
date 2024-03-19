class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

a = Point(3, 7)
print("a : abscisse =", a.x)
print("a : ordonnee =", a.y)
a.x = 6
a.y = 10
print("a : abscisse =", a.x)
print("a : ordonnee =", a.y)