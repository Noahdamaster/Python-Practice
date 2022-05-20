import math
def square():
    print("This program wil output the square of a number.")
    print()
    
    number = int(input("Enter number to be squared: "))
                            
    print("output =", number**2)





def cmToIn():

    cent = eval(input("Enter number of centimeters: "))
    
    inch = cent / 2.54

    print("x cm =", cent, " = ", "y in =", inch)
    
    



def avgGrades():

    total = 0
    for i in range(30):
        grade = float(input("Enter grade " + str(i+1) + ": "))
        total = total + grade

    average = total / 30

    print("average grade", "=", average, "%")


def series():

    numTerms = int(input("Enter numTerms: "))
    total = 0
    for i in range(numTerms):
        num = i * 2
        denom = 5 + (i *5)
        value = num / denom

        total = total + value

        print("Total: ", total)

def threes():

    for i in range (0,300, 3):
        print(i, end = " ")

import math
def calcVolume():

    radi = eval(input("Enter the radius: "))

    r = radi ** 3
    pi = math.pi
    vol = (4 / 3) * (pi) * r

    print("Result volume = ",round(vol,3))            

import math
def calcAnswers():

    x = eval(input("Enter x: "))
    y = eval(input("Enter y: "))

    pi = math.pi
    sqrt = math.sqrt

    answer1 = 2 * ((4+y) / (x-3))
    
    answer2 = pi * sqrt(y) / 7
    
    answer3 = (4 * x**3) + y**x / 5
    
    print(answer1, answer2, answer3)



import graphic 
def main():
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()

main()
























