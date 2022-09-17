class Rectangale:
    def __init__(self , length , width) -> None:
        self.length = length
        self.width  = width
       

class Square(Rectangale):
    def __init__(self , length , width):
        super().__init__(length , width)  # parent class 
    def area(self):
        return self.length * self.width

class Cube(Rectangale):
    def __init__(self , length , width , height) -> None:
        super().__init__(length , width)
        self.height = height
    def volume(self):
        return self.length * self.width * self.height

sq = Square(3 , 3)
cu  = Cube(3 ,3 , 3)

print(f'Area of square  is : {sq.area()}')
print(f'volume of cube  is : {cu.volume()}')




