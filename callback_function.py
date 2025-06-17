
def pie():
    return 3.14

def area(callback):
    radius = float(input("Enter the radius of the circle: "))
    area = callback() * radius * radius
    print("The area of the circle is: ", area)

area(pie)