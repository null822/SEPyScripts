﻿from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, c):
        self.color = c
        
    def get_color(self):
        return self.color
    
    @abstractmethod
    def get_area(self):
        pass
    
class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side
    
    def get_area(self):
        return self.side * self.side


s = Square("red", 5.0)
print(f"{s.get_color()} {s.get_area()}")