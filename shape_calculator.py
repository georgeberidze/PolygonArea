class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.height + 2 * self.width)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            'Too long or too wide'
            return "Too big for picture."
        else:
            result = ""
            for height in range(self.height):
                result += f"{'*'*self.width}\n"
            return result

    def get_amount_inside(self, other):
        'Calculates how many times one shape fits into another one'
        return (self.height // other.height) * (self.width // other.width)

    def __str__(self):
        return f"{__class__.__name__}(width={self.width}, height={self.height})" 
    
class Square(Rectangle):
    'Inherits from Rectangle class'
    def __init__(self, side):
        'Since this is a square, all sides are the same'
        super().__init__(side, side)

    def set_side(self, side):
        self.height = side
        self.width = side
        pass

    def __str__(self):
        return f"{__class__.__name__}(side={self.width})"

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_width(self, new_height):
        self.set_side(new_height)

"""
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
"""


