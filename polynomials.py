import numpy as np
from itertools import combinations

# initializes the degree of the polynomial
degree = 0
while degree > 6 or degree < 1 :
    print('Degree must be > 0 and < 7')
    degree = int(input('What degree is your polynomial?'))

# enter your data here
xData = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
yData = [0, 0.64, 1.07, 1.39, 1.63, 1.82, 1.96, 2.05, 2.09]

# ensures data is complete
if len(xData) != len(yData):
    print('number of x-coordinates must be equal to number of y-coordinates') # makes sure data is complete
    exit()

orderedPairs = list(zip(xData, yData))

# initializes the number of parameters
parameters = degree + 1

# generates all possible coordinate combinations
coordinateCombos = list(combinations(orderedPairs, parameters))

# array that compiles the error for each model
combinationError = np.zeros((len(coordinateCombos), 1))
combinationNo =  0 # used to index the error array

for coordinateCombo in coordinateCombos:
    system = np.zeros((parameters, parameters)) # creates an array for the system of linear equations
    yValues = np.zeros((parameters, 1))         # creates a the y-values array
    # iterates over each coordinate in the combination
    for i in range(parameters):
        # assigns the value for the y-cordinate
        yValues[i] = coordinateCombo[i][1]

        # iterates and computes the coefficient for each term
        exponent = degree
        for j in range(parameters):
            # defines the term
            system[i ,j] = coordinateCombo[i][0]**exponent
            exponent = exponent - 1
    
    # solves the system of linear equations
    solution = np.linalg.solve(system, yValues)

    # computes the residuals (error)
    error = 0
    # computes the y-value of the model
    for coordinate in orderedPairs:
        exponent = degree
        # iterates over the coefficients
        modelYValue = 0
        for coefficient in solution:
            modelYValue = modelYValue + coefficient*coordinate[0]**exponent
            exponent = exponent - 1
        
        # computes the difference between the y-values
        coordinateError = abs(modelYValue - coordinate[1])

        # compunds the error
        error = error + coordinateError

    # adds the error for this polynomial to the array 
    combinationError[combinationNo] = error
    combinationNo = combinationNo + 1

# finds the index of the minimum error
minIndex = np.argmin(combinationError)

print(f'The minimum error is: {np.min(combinationError)}')
print(f'The coordinates for the minimum error are: ')
print(coordinateCombos[minIndex])

coordinateCombo = coordinateCombos[minIndex]
# computes the coefficients for minimum error
system = np.zeros((parameters, parameters)) # creates an array for the system of linear equations
yValues = np.zeros((parameters, 1))         # creates a the y-values array
# iterates over each coordinate in the combination
for i in range(parameters):
    # assigns the value for the y-cordinate
    yValues[i] = coordinateCombo[i][1]
    # iterates and computes the coefficient for each term
    exponent = degree
    for j in range(parameters):
        # defines the term
        system[i ,j] = coordinateCombo[i][0]**exponent
        exponent = exponent - 1

# solves the system of linear equations
solution = np.linalg.solve(system, yValues)

# formats and prints the resulting polynomial
exponent = degree
print('Your polynomial is: ')
print('f(x) = ', end = '')
for coefficient in solution:
    if(exponent != degree):
        print('+', end = '')
    
    if(exponent != 0):
        print(f'{coefficient}x^{exponent}', end = '')
        exponent = exponent - 1
    else:
        print(f'{coefficient}')
