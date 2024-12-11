class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

# Sử dụng
rect = Rectangle(5, 10)
areaNumber = rect.area

print(areaNumber)
