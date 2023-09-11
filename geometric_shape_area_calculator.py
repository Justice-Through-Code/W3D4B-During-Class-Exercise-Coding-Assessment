import math # DO NOT MODIFY

def main():
    print("Welcome to the Geometric Shape Area Calculator!") # DO NOT MODIFY
    print("Circle = 1") # DO NOT MODIFY
    print("Rectangle = 2") # DO NOT MODIFY
    print("Triangle = 3")# DO NOT MODIFY

    circle_pi = math.pi # DO NOT MODIFY
  
    # TODO: Assign a new variable named 'choice'.
    # TODO: Ask the user to: "Please select a shape by entering 1 for Circle, 2 for Rectangle, or 3 for Triangle." and assign the input to the 'choice' variable.
    # TODO: Convert the variable 'choice' to an integer data type.

    if choice == 1: # DO NOT MODIFY
        # Calculate the area of a circle
        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        # TODO: Convert 'radius' to float.
        # HINT: The area of a circle: 'circle_pi' times radius squared


    elif choice == 2: # DO NOT MODIFY
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        # TODO: Convert both 'length' and 'width' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        # HINT: The formula for the area of a rectangle: length times width

    elif choice == 3: # DO NOT MODIFY
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        # TODO: Convert both 'base' and 'height' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        # HINT: The area of a Triangle: half times base times height


    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print this statement "Invalid choice. Please select a valid option (1/2/3)."
        print("Invalid choice. Please select a valid option (1/2/3).")

    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
