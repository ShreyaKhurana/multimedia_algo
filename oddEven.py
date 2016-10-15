# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 16:02:26 2016

@author: Shreya Khurana

Odd even rule for checking if a point is inside a figure or outside

"""

def findX(pt1, pt2, y):
    x = ((y - pt1[1]) * (pt2[0] - pt1[0])/(pt2[1] - pt1[1]) ) + pt1[0]
    return x

def isInside(coord, point):
    
    intersections = 0
    brk = 0
    for i in range(len(coord) - 1):
        pt1 = coord[i]
        pt2 = coord[i + 1]
        if (pt1[1] >= point[1] and pt2[1] < point[1]) or (pt1[1] < point[1] and pt2[1] >= point[1]):
            if point[0] >= pt1[0] or point[0] >= pt2[0]:
                if findX(pt1, pt2, point[1]) < point[0]:
                    intersections += 1
                elif findX(pt1, pt2, point[1]) == point[0]:
                    brk = 1
                    print 'Point on the edge'
                    break
#    elif pt1[1] == point[1] or pt2[1] == point[1]:
#        if point[0] >= max(pt1[0], pt2[0]):
#            intersections += 1
#            print pt1
#            print pt2
    if brk == 0:
#        print intersections
        if intersections % 2 == 0:
            return False
        else:
            return True
    else:
        return 'Point on edge'