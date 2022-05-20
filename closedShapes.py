## closedShapes.py
## CSCI 220
## Noah Sulek



# purpose: Program function that executes both prism() and cylinder()
# input: specify number of prisms and the number of cylinders - by user
# output: run the appropriate function the appropriate number of times
import math
def main():
    
    # find the number of each object
   
    cylinders = eval(input("Enter number of cylinders: "))
    prisms = eval(input("Enter number of prisms: "))
    
    #set up each as variables for the other programs

    cylinders = cylinders
    prisms = prisms

    print("This program will calculate the volume and surface area of the cylinder and prism: ")

#begin cylinder and prism programs
        
# purpose: Program to calculate and output the volume and surface area of a cylinder
# input: value of r and h - by user
# output: volume and surface area of a cylinder - to monitor
def cylinder():
    #pi = math.pi
    #use loop for variables in main function
    #Get value of r (radius) and l (height)
    
    r = int(input("Enter value of radius: "))
    l = int(input("Enter value of height: "))

    #Calculate volume
    volumeC = math.pi * ((r)**2) * l
    print("volume of the cylinder is:",volumeC)
        
    #Calculate surface area
    surfaceA = (2 * math.pi * (r**2)) + (2 * math.pi * r * l)
    print("surface area of the cylinder is:", surfaceA)                                       

    #end cylinder function
    cylinder()

# purpose: Program to calculate and output the volume and surface area of a rectangular
# prism assuming a square base
# input: value of x and h - by user
# output: volume and surface area of a rectangular prism - to monitor
# begin program with loop
def prism():
    for i in range(prisms):
    x = eval(input("Enter value of width: "))
    h = eval(input("Enter value of length: "))
    
    #Calculate volume
    volumeP = (x**2) * (h)
    print("volume of the prism:",volumeP)
    
    #Calculate surface area
    surfaceArea = (4 * x * h) + (2 * (x**2))             
    print("sureface area of the prism:",surfaceArea)

    #end prism program
    prism()

    #end main program
    
    main()



      


    



    
      
