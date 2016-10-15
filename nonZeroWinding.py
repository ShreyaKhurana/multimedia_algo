# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:26:14 2016

@author: Shreya Khurana

Non-zero winding rule to detect whether a point is inside or outside

"""

import matplotlib.pyplot as plt

#coord = [[1,2], [3,4], [5,2], [1,2]]
#coord = [[0.5,3],[1,1], [2,2], [1.5, 4], [0.5, 3]]
coord = [[1,1], [1,3], [2,4], [3,3], [4,4], [5,3], [5,1],[1,1]]

x_coord = [point[0] for point in coord]
y_coord = [point[1] for point in coord]

point = [4,3.5]

plt.scatter(x_coord, y_coord)
plt.plot(x_coord, y_coord)

plt.scatter(point[0], point[1])
plt.plot([-5,point[0]], [point[1], point[1]])

intersections = 0
brk = 0
def findX(pt1, pt2, y):
    x = ((y - pt1[1]) * (pt2[0] - pt1[0])/(pt2[1] - pt1[1]) ) + pt1[0]
    return x

for i in range(len(coord) - 1):
    pt1 = coord[i]
    pt2 = coord[i + 1]
    if (pt1[1] >= point[1] and pt2[1] < point[1]) or (pt1[1] < point[1] and pt2[1] >= point[1]):
        if point[0] >= pt1[0] or point[0] >= pt2[0]:
            if findX(pt1, pt2, point[1]) < point[0]:
                if pt2[1] > pt1[1]:
                    intersections += 1
                elif pt2[1] < pt1[1]:
                    intersections -= 1
            elif findX(pt1, pt2, point[1]) == point[0]:
                brk = 1
                print 'Point on the edge'
                break
            
if brk == 0:
    print intersections
    if intersections == 0:
        print 'Outside'
    else:
        print 'inside'