# Function to calculate the area of a square
def square_area(side):
  return side**2

# Function to calculate the area of a triangle
def triangle_area(base, height):
  return (base * height) / 2

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
  return length * width

# Function to calculate the surface area of a cube
def cube_surface_area(side):
  return 6 * side**2

# Function to calculate the surface area of a cuboid
def cuboid_surface_area(length, width, height):
  return 2*(length*width + width*height + height*length)

# Function to calculate the volume of a cube
def cube_volume(side):
  return side**3

# Function to calculate the volume of a cuboid
def cuboid_volume(length, width, height):
  return length*width*height

# Main function
def main():
  shape = input('''
------------ Calculate area of ---------------
[ square, triangle, rectangle, cube, cuboid ]
----------------------------------------------
Enter the shape name : ''')

  if shape == "square":
    side = float(input("Enter the side length of the square: "))
    area = square_area(side)
    print(f"The area of the square is {area}")
  elif shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangle_area(base, height)
    print(f"The area of the triangle is {area}")
  elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is {area}")
  elif shape == "cube":
    side = float(input("Enter the side length of the cube: "))
    surface_area = cube_surface_area(side)
    volume = cube_volume(side)
    print(f"The surface area of the cube is {surface_area}")
    print(f"The volume of the cube is {volume}")
  elif shape == "cuboid":
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))
    surface_area = cuboid_surface_area(length, width, height)
    volume = cuboid_volume(length, width, height)
    print(f"The surface area of the cuboid is {surface_area}")
    print(f"The volume of the cuboid is {volume}")
  else:
    print("Invalid shape")
