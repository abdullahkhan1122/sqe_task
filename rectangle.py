# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Function to calculate the perimeter of a rectangle
def calculate_perimeter(length, width):
    return 2 * (length + width)

# Main block of the program
if __name__ == "__main__":
    # Input from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculating area and perimeter
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    # Displaying the results
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

