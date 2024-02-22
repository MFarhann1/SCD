class shape:
    def __init__(self,name):

    self.name=name
    def area(self):
        pass

        def perimeter(self):
            pass
            
class Shape:
    def __init__(self, color):
        self.color = color
        def get_color(self):
            return self.color


             def area(self):
                pass

class Rectangle(Shape):
     def __init__(self, color, width, height):
          super().__init__(color)
           self.width = width
            self.height = height

 def area(self):
    return self.width * self.height

   class Circle(Shape):
       def __init__(self, color, radius):
         super().__init__(color)
           self.radius = radius

def area(self):
   import math
    return math.pi * self.radius ** 2
                        