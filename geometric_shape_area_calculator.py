#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    # TODO: In terminal, print a unique welcome message to your user
    # TODO: In terminal, print a message to the user that "Circle = 1"
    # TODO: In terminal, print a message to the user that "Rectangle = 2"
    # TODO: In terminal, print a message to the user that "Triangle = 3"

    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    # TODO: Convert the variable 'choice' to an integer data type.
    

    circle_pi = math.pi # DO NOT MODIFY, assigning the variable circle_pi to equal Pi ~3.14
  
    

    if : # ADD THE LOGIC TO THE IF STATEMENT, IF CHOICE IS A CIRLCE -- DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle
        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        # TODO: Convert 'radius' to float.
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  


    elif : #ADD THE LOGIC TO THE ELIF STATEMENT, IF CHOICE IS A RECTANGLE -- DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        # TODO: Convert both 'length' and 'width' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        # HINT: The formula to find the area of a rectangle: length times width

    elif : #ADD THE LOGIC TO THE ELIF STATEMENT, IF CHOICE IS A TRIANGLE -- DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        # TODO: Convert both 'base' and 'height' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        # HINT: The formula to find the area of a Triangle: half times base times height


    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print this statement "Invalid choice. Please select a valid option (1/2/3)."
        

    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
