# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:47:23 2016

@author: Shreya Khurana

Cohen Sutherland Line clipping algo
"""
import matplotlib as plt

P2 = [2.0, 4.0]
P1 = [7.0, 5.0]
#
slope = (P2[1] - P1[1]) / (P2[0] - P1[0])
#
plt.pyplot.plot([P1[0],P2[0]], [P1[1], P2[1]], 'r')
plt.pylab.xlim([0, 9])
plt.pylab.ylim([0, 9])
xmin = 3
xmax = 6
ymin = 3
ymax = 6
#
plt.pyplot.plot([0,9],[ymin, ymin])
plt.pyplot.plot([0,9],[ymax, ymax])
plt.pyplot.plot([xmin, xmin], [0,9])
plt.pyplot.plot([xmax, xmax], [0,9])

def findX(pt1, pt2, y):
    x = ((y - pt1[1]) * (pt2[0] - pt1[0])/(pt2[1] - pt1[1]) ) + pt1[0]
    return x

def findY(pt1, pt2, x):
    y = ((x - pt1[0])*(pt2[1] - pt1[1]) / (pt2[0] - pt1[0])) + pt1[1]
    return y

def codeAssign(point):
    if point[0] < xmin:
        if point[1] < ymin:
            code = '0101'
        elif point[1] > ymax:
            code = '1001'
        else :
            code = '0001'
    elif point[0] > xmax:
        if point[1] < ymin:
            code = '0110'
        elif point[1] > ymax:
            code = '1010'
        else :
            code = '0010'
    else:
        if point[1] < ymin:
            code = '0100'
        elif point[1] > ymax:
            code = '1000'
        else :
            code = '0000'
    return code
    
code1 = codeAssign(P1)
code2 = codeAssign(P2)
#print code1
#print code2
#print code1
if code1 == '0000' and code2 == '0000':
    print 'line inside the window'
elif True in [code1[i] == '1' and code2[i] == '1' for i in range(4)]:
    print 'Line trivially rejected'
else:
#    print 'line to be clipped'
    bottom_intersection = findX(P1, P2, ymin)
    top_intersection = findX(P1, P2, ymax)
    left_intersection = findY(P1, P2, xmin)
    right_intersection = findY(P1, P2, xmax)
    
    # For bottom_intersection, cutting the outside part
    if P1[1] < ymin:
        plt.pyplot.plot([bottom_intersection, P1[0]], [ymin, P1[1]], 'w')
    elif P2[1] < ymin:
        plt.pyplot.plot([bottom_intersection, P2[0]], [ymin, P2[1]], 'w')
    
    # For top_intersection
    if P1[1] > ymax:
        plt.pyplot.plot([top_intersection, P1[0]], [ymax, P1[1]], 'w')
    elif P2[1] > ymax:
        plt.pyplot.plot([top_intersection, P2[0]], [ymax, P2[1]], 'w')
        
    #For right intersection
    if P1[0] > xmax:
        plt.pyplot.plot([xmax, P1[0]], [right_intersection, P1[1]], 'w')
    elif P2[0] > xmax:
        plt.pyplot.plot([xmax, P2[0]], [right_intersection, P2[1]], 'w')
        
    # For left intersection
    if P1[0] < xmin:
        plt.pyplot.plot([xmin, P1[0]], [left_intersection, P1[1]], 'w')
    elif P2[0] < xmin:
        plt.pyplot.plot([xmin, P2[0]], [left_intersection, P2[1]], 'w')
    
#    print bottom_intersection
#    print right_intersection
#    print top_intersection
#    print left_intersection
