print("WELCOME TO AREA CALCULATOR")
op = input("Enter 1 for Triangle \nEnter 2 for square \nEnter 3 for Rectangle \nEnter 4 for Circle ")
if op == "1":
    base = float(input("Enter base of Triangle " ))
    height = float(input("Enter height of Triangle " ))
    print("your Triangle area is:-" , 0.5 * base * height )
elif op == "2":
    side = float(input("Enter side of a Square "))  
    print("your Square area is:- " , side * side)  
elif op == "3":
    length = float(input("Enter length of Rectangle " ))
    breadth = float(input("Enter breadth of Rectangle " ))
    print("your Rectangle area is:- " , length * breadth)
elif op == "4":
    radius = float(input("Enter radius of Circle " ))
    print("your Circle area is:- " , 3.14 * radius * radius)
