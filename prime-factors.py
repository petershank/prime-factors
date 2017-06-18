# your quality code here
import math

allFactors = []
factors = []
factored = False
paired = []
lowestSum = 0

while True:  # Sets up the number to factor
    try:
        number = int(input("Input an integer: "))
        break
    except ValueError:
        print("Invalid input \n")

for i in range(2, math.floor((number / 2) + 1)):  # finds the factors of that number
    if number % i == 0:
        factors.append(i)

if (len(factors) == 0):
    print("Number is already prime.")

else:
    lowestSum = (factors[0] + factors[-1])

    while factored == False:   # finds the prime factors of the number
        
        allFactors.append(factors)
        factors = []
        
        for i in range(len(allFactors)):  # runs the length of 'allFactors'
            for x in range(math.floor(len(allFactors[i]) / 2) + 1): # runs half the length of a specific list in 'allFactors'
                
                if ((allFactors[i][x] + allFactors[i][-x - 1]) < lowestSum):   #   tests for the lowest sum of two factors
                    
                    lowestSum = (allFactors[i][x] + allFactors[i][-x - 1])
                    paired = [allFactors[i][x], allFactors[i][-x - 1]]

        break   # Temporary line to end loop early
                          
print(allFactors)
print(paired)
