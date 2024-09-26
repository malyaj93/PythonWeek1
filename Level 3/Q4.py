class Shape:
  def area(self):
    # Returning 0 by default for the parent class
    return 0

class Square(Shape):
  def __init__(self, length):
    self.length = length

  def area(self):
    return self.length ** 2

# Example usage:
shape = Shape()
print(shape.area())

dimensions = int(input("Enter the side of square : "))
square = Square(dimensions)
print(square.area())