class Shape2D:
    def area(self):
        raise NotImplementedError()

class Shape3D:
    def volume(self):
        raise NotImplementedError()

class Square(Shape2D, Shape3D):
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width**2
    def volume(self, width):
        return self.width**3