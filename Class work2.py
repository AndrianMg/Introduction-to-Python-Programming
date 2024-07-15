# create a function that calculate the area of a rectangle using two positional arguments (lenght and width). We are going to call the function with different values and observe the result.
 
def calculate_rectangle_area(length, width):
    area = length * width
    return area
 
# Calling the function with different values
length1, width1 = 10, 5
area1 = calculate_rectangle_area(length1, width1)
print(f"The area of a rectangle with length {length1} and width {width1} is {area1}.")
 
length2, width2 = 12, 8
area2 = calculate_rectangle_area(length2, width2)
print(f"The area of a rectangle with length {length2} and width {width2} is {area2}.")