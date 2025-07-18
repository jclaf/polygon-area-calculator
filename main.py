class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"{type(self).__name__}(width={self.width}, height={self.height})"

    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        draw = ''
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        for x in range(self.height):
            for y in range(self.width):
                draw += f'*'
            draw +='\n'
        return draw
    
    def get_amount_inside(self,shape):
        if type(shape).__name__ == "Square":
            return (self.width//shape.side)*(self.height//shape.side) 
        if type(shape).__name__ == "Rectangle":
            return (self.width//shape.width)*(self.height//shape.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.side = side

    def __str__(self):
        return f"{type(self).__name__}(side={self.side})"

    def set_side(self,side):
        self.side =side
        self.width = side
        self.height = side
    
    def set_width(self,side):
        self.side =side
        self.width = side
        self.height = side
    
    def set_height(self,side):
        self.side =side
        self.width = side
        self.height = side

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
