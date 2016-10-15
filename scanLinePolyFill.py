# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:57:49 2016

@author: Shreya Khurana

Scan Line polygon filling algo

"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
import numpy as np

coord = [[0.5,4],[4,5], [6,2], [0,0], [0.5, 4]]
#coord = [[1,1], [3,4], [5,1], [1,1]]
x_coord = [point[0] for point in coord]
y_coord = [point[1] for point in coord]

plt.scatter(x_coord, y_coord)
plt.plot(x_coord, y_coord)

oddNumbers = range(1,2*max(y_coord)+2,2)
scanLines = [i*0.5 for i in oddNumbers]

for j in range(len(scanLines)):
    plt. plot([0, 6], [scanLines[j], scanLines[j]], 'r')
    
def findEq(pt1, pt2, y):
    x = ((y - pt1[1]) * (pt2[0] - pt1[0])/(pt2[1] - pt1[1]) ) + pt1[0]
    return x

def linesInBetween(miny, maxy, scanLines):
    scanEdge = []
    for line in scanLines:
        if (line >= miny) and (line <= maxy):
            scanEdge.append(line)
    return scanEdge

intersectionPoints = []

for edge in range(len(coord) - 1):
    pt1 = coord[edge]
    pt2 = coord[edge + 1]
    if pt2[1] != pt1[1]:
        miny = min(pt1[1], pt2[1])
        maxy = max(pt1[1], pt2[1])
        scanEdge = linesInBetween(miny, maxy, scanLines)
        x_val = [findEq(pt1, pt2, y) for y in scanEdge]
        points = [[x_val[i], scanEdge[i]] for i in range(len(scanEdge))]
        intersectionPoints.extend(points)
        
intersectionPoints = list(sorted(intersectionPoints,
                                 key=lambda intersectionPoints: (-intersectionPoints[1], intersectionPoints[0])))

s = [20*4**3]
colors = iter(cm.rainbow(np.linspace(0,1, 20)))

#print intersectionPoints
activeX = []
activeY = []
for point in range(0,len(intersectionPoints),2):

    p1 = intersectionPoints[point]
    p2 = intersectionPoints[point + 1]
    
    if p1[1] == p2[1]:
        pixelX = range(int(math.ceil(p1[0])), int(math.ceil(p2[0])))
        pixelY = [p1[1]]*len(pixelX)
        plt.scatter(pixelX,pixelY,s=s,color=next(colors))
        activeX.extend(pixelX)
        activeY.extend(pixelY)
