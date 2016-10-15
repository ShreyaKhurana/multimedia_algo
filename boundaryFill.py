# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:49:30 2016

@author: Shreya Khurana

Boundary fill recursive algo
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

coord = [[1,1],[1,6],[6,6],[6,1],[1,1]]
#coord = [[1,1], [3,4], [5, 4], [6, 1], [1,1]]
x_coord = [point[0] for point in coord]
y_coord = [point[1] for point in coord]

s = [20*4**3]

colors = iter(cm.rainbow(np.linspace(0,1, 20)))
plt.scatter(x_coord, y_coord, s=s, color='k')

plt.plot(x_coord, y_coord,'r--')

def findY(pt1, pt2, x):
    y = ((x - pt1[0])*(pt2[1] - pt1[1]) / (pt2[0] - pt1[0])) + pt1[1]
    return y

def findBoundary(pt1, pt2):
    minx = min(pt1[0], pt2[0])
    maxx = max(pt1[0], pt2[0])
    x = range(minx, maxx+1)
    y = [findY(pt1, pt2, x1) for x1 in x]
    points = [[x[i], y[i]] for i in range(len(x))]
    return points

#boundary = []
boundary = [[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[6,2],[6,3],[6,4],[6,5],[6,5],[6,6],[5,6],[4,6],[3,6],[2,6],[1,6],[1,5],[1,4],[1,3],[1,2],[1,1]]
coloured = [[2,2],[2,3],[3,3],[3,2],[2,2]]
#for point in range(len(coord) - 1):
#    boundary.extend(findBoundary(coord[point], coord[point + 1]))
    
#print boundary

x_coord = [point[0] for point in boundary]
y_coord = [point[1] for point in boundary]

plt.scatter(x_coord, y_coord, s=s, color='k')


def boundaryFill(x,y,boundary, coloured):
    if ([x,y] not in coloured) and ([x,y] not in boundary):
        plt.scatter(x,y,s=s,color=next(colors))
        coloured.append([x,y])
        boundaryFill(x+1,y,boundary, coloured)
        boundaryFill(x-1,y,boundary, coloured) 
        boundaryFill(x,y+1,boundary, coloured)
        boundaryFill(x,y-1,boundary, coloured)
        boundaryFill(x+1,y+1,boundary, coloured)
        boundaryFill(x+1,y-1,boundary, coloured)
        boundaryFill(x-1,y+1,boundary, coloured) 
        boundaryFill(x-1,y-1,boundary, coloured)
    
boundaryFill(4,4,boundary,coloured)    