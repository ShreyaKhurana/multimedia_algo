# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 18:08:12 2016

@author: Shreya Khurana

Weiler Atherton algo
"""

import matplotlib.pyplot as plt
import matplotlib.pylab as plb
from cohenSutherland import findX, findY
from oddEven import isInside

#coord = [[1.0,4.0], [4.0,1.0], [5.0,5.0], [1.0,4.0]]
coord = [[6.0,7.0],[12.0,8.0],[12.0,6.0],[8.0,5.0],[13.0,3.0],[6.0,3.0],[6.0,7.0]]
plt.plot([point[0] for point in coord], [point[1] for point in coord], 'k')
plb.xlim([0, 30])
plb.ylim([0, 15])

xmin = 10.0
xmax = 20.0
ymin = 1.0
ymax = 10.0

winLeftDown = [xmin, ymin]
winLeftUp = [xmin, ymax]
winRightDown = [xmax, ymin]
winRightUp = [xmax, ymax]

window = [xmin, ymin, xmax, ymax]
winCoord = [winLeftDown, winLeftUp, winRightUp, winRightDown, winLeftDown]
plt.plot([point[0] for point in winCoord], [point[1] for point in winCoord], 'r')

def liesInsideX(pt1, pt2, x):
    return (pt1[0] < x < pt2[0]) or (pt2[0] < x < pt1[0])

def liesInsideY(pt1, pt2, y):
    return (pt1[1] < y < pt2[1]) or (pt2[1] < y < pt1[1])

polyAllPoints = list(coord)

counter = 0

xminIntersection = []
xmaxIntersection = []
yminIntersection = []
ymaxIntersection = []

for index,point in enumerate(coord[:len(coord) - 1]):
    if liesInsideX(point, coord[index+1], xmin) == True:
        crossPoint = [xmin, findY(point, coord[index+1],xmin)]
        polyAllPoints.insert(index+1+counter, crossPoint)
        xminIntersection.append(crossPoint)
        counter += 1
        
    if liesInsideY(point, coord[index+1], ymax) == True:
        crossPoint = [findX(point, coord[index+1],ymax), ymax]
        polyAllPoints.insert(index+1+counter, crossPoint)
        ymaxIntersection.append(crossPoint)
        counter += 1
        
    if liesInsideX(point, coord[index+1], xmax) == True:
        crossPoint = [xmax, findY(point, coord[index+1],xmax)]
        polyAllPoints.insert(index+1+counter, crossPoint)
        xmaxIntersection.append(crossPoint)
        counter += 1
        
    if liesInsideY(point, coord[index+1], ymin) == True:
        crossPoint = [findX(point, coord[index+1],ymin), ymin]
        polyAllPoints.insert(index+1+counter, crossPoint)
        yminIntersection.append(crossPoint)
        counter += 1
        
#print polyAllPoints   

xminIntersection = list(sorted(xminIntersection, key=lambda xminIntersection:(xminIntersection[1])))
ymaxIntersection = list(sorted(ymaxIntersection, key=lambda ymaxIntersection:(ymaxIntersection[0])))
xmaxIntersection = list(sorted(xmaxIntersection, key=lambda xmaxIntersection:(-xmaxIntersection[1])))
yminIntersection = list(sorted(yminIntersection, key=lambda yminIntersection:(-yminIntersection[0])))

windowAllPoints = [winLeftDown]
windowAllPoints.extend(xminIntersection)
windowAllPoints.append([winLeftUp])
windowAllPoints.extend(ymaxIntersection)
windowAllPoints.append([winRightUp])
windowAllPoints.extend(xmaxIntersection)
windowAllPoints.append([winRightDown])
windowAllPoints.extend(yminIntersection)
windowAllPoints.append([winLeftDown])

#print windowAllPoints
clipArea = []
startVertex =  currentVertex = 0
nextVertex = currentVertex + 1
traversed = [polyAllPoints[startVertex]]
traversedAll = False

while not traversedAll:
#    print polyAllPoints[currentVertex]
#    print polyAllPoints[nextVertex]
    if isInside(winCoord, polyAllPoints[currentVertex]) == False and isInside(winCoord, polyAllPoints[nextVertex]) == 'Point on edge':
        traversed.extend([polyAllPoints[nextVertex], polyAllPoints[nextVertex + 1]])
        currentVertex = nextVertex + 1
        
    elif isInside(winCoord, polyAllPoints[currentVertex]) == True and isInside(winCoord, polyAllPoints[nextVertex]) == True:
        traversed.append(polyAllPoints[nextVertex])
        currentVertex = nextVertex
    
    elif isInside(winCoord, polyAllPoints[currentVertex]) == False and isInside(winCoord, polyAllPoints[nextVertex]) == False:
        traversed.append(polyAllPoints[nextVertex])
        currentVertex = nextVertex
        
    elif isInside(winCoord, polyAllPoints[currentVertex]) == True and isInside(winCoord, polyAllPoints[nextVertex]) == 'Point on edge':
        currentVertex = polyAllPoints.index(windowAllPoints[windowAllPoints.index(polyAllPoints[nextVertex]) + 1])
        traversed.extend([polyAllPoints[nextVertex], polyAllPoints[currentVertex]])
    
    if traversed[-1] in traversed[:len(traversed) - 1] and traversed[-1] != polyAllPoints[startVertex]:
        currentVertex = nextVertex + 1
        traversed.extend([polyAllPoints[nextVertex], polyAllPoints[currentVertex]])
    nextVertex = currentVertex + 1

    if polyAllPoints[currentVertex] == polyAllPoints[startVertex]:
        traversedAll = True
        
print traversed
