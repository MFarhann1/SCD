from shape import rectangle and circle
from shapes import Rectangle, Circle

def print_details(shape):
    print(f"Area: {shape.calculate_area()}")
    print(f"Perimeter: {shape.calculate_perimeter()}")

if __name__ == "__main__":
    # Instantiate objects of Rectangle and Circle
    rectangle = Rectangle(4, 5)
    circle = Circle(3)

    # Demonstrate polymorphism
    print("Rectangle Details:")
    print_details(rectangle)

    print("\nCircle Details:")
    print_details(circle)
git add main.py
git commit -m "Added main.py script demonstrating polymorphism"
git push origin master  # or your branch name