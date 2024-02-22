class shape:
    def __init__(self,name):

    self.name=name
    def area(self):
        pass

        def perimeter(self):
            pass
 class Shape:
    def __init__(self):
        pass  # You may have common attributes or methods for all shapes here

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def calculate_area(self):
        import math
        return math.pi * self.__radius**2

    def calculate_perimeter(self):
        import math
        return 2 * math.pi * self.__radius

class DataProcessor:
    @staticmethod
    def demonstrate_operations():
        # Example operations on Python data structures
        # Lists
        my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        my_list.sort()
        my_list.append(7)
        my_list.remove(2)
        print("Sorted List:", my_list)

        # Tuples
        my_tuple = (1, 2, 3, 4, 5)
        print("Tuple:", my_tuple)

        # Dictionaries
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        my_dict['d'] = 4
        del my_dict['b']
        print("Dictionary:", my_dict)

        # Sets
        my_set = {1, 2, 3, 4, 5}
        my_set.add(6)
        my_set.remove(3)
        print("Set:", my_set)


# Testing
if __name__ == "__main__":
    # Testing shapes
    rectangle = Rectangle(4, 5)
    print("Rectangle Area:", rectangle.calculate_area())
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())

    circle = Circle(3)
    print("Circle Area:", circle.calculate_area())
    print("Circle Perimeter:", circle.calculate_perimeter())

    # Testing data structure methods
    DataProcessor.demonstrate_operations()
git add shapes.py data_structures.py
git commit -m "Added Rectangle, Circle classes, and DataProcessor class"
git push origin master  # or your branch name
