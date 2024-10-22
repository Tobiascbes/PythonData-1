#!/usr/bin/env python3

import math
def triangle():
    base = input("Give the base of the triangle: ")
    height = input("Give the height of the triangle: ")
    area = int(height) * int(base) / 2
    print(f"The area is {area}")

def square():
    a = input("Give the length: ")
    b = input("Give the height: ")
    area = int(a) * int(b)
    print(f"The area is {area}")

def circle():
    r = input("Give the radius of the circle: ")
    area = math.pi * int(r)**2
    print(f"The area is {area}")

def main():
    isRunning = True
    while isRunning:
        choice = input("Choose a shape!: \nTriangle\nrectangle\ncircle\n").lower()
        if choice == "":
            isRunning = False
        elif choice == "triangle":
            triangle()
        elif choice == "rectangle":
            square()
        elif choice == "circle":
            circle()
        else:
            print("Unknown shape!")
            
   
        

if __name__ == "__main__":
    main()