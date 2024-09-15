import numpy as np

dataFile = input("Input the name of the file that contains your data: ")
degree = 0

while degree > 6 or degree < 1 :
    print("Degree must be > 0 and < 7")
    degree = int(input("What degree is your polynomial?"))

# read data from excel sheet
xData = [1, 2, 3, 4, 5]
yData = [6, 7, 8, 9, 10]

print("Reading file...")

if len(xData) != len(yData):
    print("number of x-coordinates must be equal to number of y-coordinates") # makes sure data is complete

orderedPairs = []

for i in range(len(xData)):
    orderedPairs.append([xData[i], yData[i]])

orderedPairs = np.array(orderedPairs)

parameters = degree + 1

for i in range(len(xData)):
    j = i + 1
    while j <= len(xData):
        k = j + 1
        while k <= len(xData):





