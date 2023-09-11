import math

def main():
    print("Welcome to the Geometric Shape Area Calculator!")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = int(input("Please select a shape (1/2/3): "))

    if choice == 1:
        # Calculate the area of a circle
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius**2
        print(f"The area of the circle is: {area:.2f} square units.")
    elif choice == 2:
        # Calculate the area of a rectangle
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area:.2f} square units.")
    elif choice == 3:
        # Calculate the area of a triangle
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area:.2f} square units.")
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()