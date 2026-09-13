import math

#def speedCalculator():
#    km = float(input())
#    hrs = int(input())
#    speedCalc = km / hrs
#    print(int(speedCalc))
#speedCalculator()

#def circumferenceOfCircle():
#    radius = float(input())
#    circumference = 2 * math.pi * radius
#    print(circumference)
#circumferenceOfCircle()

#def areaOfCircle():
#    radius = float(input())
#    circleArea = math.pi * radius ** 2
#    print(circleArea)
#areaOfCircle()

#def costOfPizza():
#    diameter = float(input())
#    radius = diameter / 2
#    pizzaArea = math.pi * radius ** 2
#    pizzaCost = pizzaArea * 0.035
#    print("£",pizzaCost)
# costOfPizza()

#def slopeOfLine():
#    x1 = int(input())
#    y1 = int(input())
#    x2 = int(input())
#    y2 = int(input())
#    xDiff = x2 - x1
#    yDiff = y2 -y1
#    gradient = yDiff / xDiff
#    print(gradient)
#slopeOfLine()

#def distanceBetweenPoints():
#    x1 = int(input())
#    y1 = int(input())
#    x2 = int(input())
#    y2 = int(input())
#    xDiff = x2 - x1
#    yDiff = y2 -y1
#    gradient = yDiff / xDiff
#    distance = math.sqrt (xDiff ** 2 + yDiff ** 2)
#    print(distance)
#distanceBetweenPoints()

#def travelStatistics():
#    avgSpeed = float(input())
#    hrs = int(input())
#    distance = avgSpeed / hrs
#    fuelUsed = distance * 5
#    print(fuelUsed)
#travelStatistics()

#def sumOfSquares():
#    max = int(input())
#    list = []
#    while max > 0:
#        maxCopy = max
#        maxCopy = maxCopy ** 2
#        max = max - 1
#        list.append(maxCopy)
#    print(sum(list))
#sumOfSquares()

def averageOfNumbers():
    numAmount = int(input())
    numAmountCopy = numAmount
    list = []
    while numAmount > 0:
        numInput = int(input())
        list.append(numInput)
        numAmount = numAmount - 1
    average = sum(list) / numAmountCopy
    print(int(average))
averageOfNumbers()
        

        
    
    
