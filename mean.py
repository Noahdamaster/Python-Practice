#Noah Sulek
#CSCI 220
#means.py



#Create a function that can create seperate kinds of means
#Define the input and output
#Create loop
#Figure out the calculations for the seperate means
#Find formula for rms
#Find formula for harmonic mean
#Find formula for geometric mean
import math
def mean():
    print("This function will allow the user to specify the number of values to be entered")
    print("to output the RMS (root-mean-square) Average, the Harmonic Mean and the")
    print("Geometric Mean.")
    print()
    #Create loop
    total = 0
    setOfnum = int(input("Enter total amount of numbers to average: "))
    print()
    for i in range(setOfnum):
        numbers = float(input("Enter a number for num-" + str(i+1) + ": "))
        total = total + numbers**2
        num = setOfnum
        denom = ((1 / total) * (total))   
    #Find formula for rms
    rms_average = math.sqrt(total / setOfnum)
    
    #Find formula for harmonic mean
    #num = setOfnum
    #denom = ((1 / total) * (total))
        
    harmonic_mean = num / denom

    #Find formula for geometric mean

    geometric_mean = (total * setOfnum)**(1 / numbers)

    
    print()
    print("The output is: ")
    print()
    print("The RSM sum is", num)
    print("The RSM average is", round(rms_average, 3))
    print()
    print("The harmonic sum is", num)
    print("The harmonic mean is", round(harmonic_mean, 3))
    print()
    print("The geometric product is", num)
    print("The geometric mean is", round(geometric_mean, 3))

mean()
    

    
