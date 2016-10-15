# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 13:22:51 2016

@author: Shreya Khurana

NLN Line clipping algo
"""

import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import twoDFigure as two

P2 = [9.0, 4.0]
P1 = [4.0, 4.0]

plt.plot([P1[0],P2[0]], [P1[1], P2[1]], 'k')
plb.xlim([0, 9])
plb.ylim([0, 9])

xmin = 3
xmax = 6
ymin = 3
ymax = 6

plt.plot([0,9],[ymin, ymin])
plt.plot([0,9],[ymax, ymax])
plt.plot([xmin, xmin], [0,9])
plt.plot([xmax, xmax], [0,9])

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


def bringToPos(P1, P2):
    code1 = codeAssign(P1)

    if code1 == '0101':
        P1 = two.reflectionAboutLine(P1[0],P1[1],0,3,3,3)
        P1 = [P1[0][0], P1[0][1]]
        P2 = two.reflectionAboutLine(P2[0],P2[1],0,3,3,3)
        P2 = [P2[0][0], P2[0][1]]
    elif code1 == '0100':
        P1 = two.reflectionAboutLine(P1[0],P1[1],3,3,6,3)
        P1 = [P1[0][0], P1[0][1]]
        P2 = two.reflectionAboutLine(P2[0],P2[1],3,3,6,3)
        P2 = [P2[0][0], P2[0][1]]
    elif code1 == '0010':
        P1 = two.reflectionAboutLine(P1[0],P1[1],6,3,6,6)
        P1 = [P1[0][0], P1[0][1]]
        P2 = two.reflectionAboutLine(P2[0],P2[1],6,3,6,6)
        P2 = [P2[0][0], P2[0][1]]
    elif code1 == '1000':
        P1 = two.reflectionAboutLine(P1[0],P1[1],3,6,6,6)
        P1 = [P1[0][0], P1[0][1]]
        P2 = two.reflectionAboutLine(P2[0],P2[1],3,6,6,6)
        P2 = [P2[0][0], P2[0][1]]  
    elif code1 == '1010':
        P1 = two.reflectionAboutLine(P1[0],P1[1],4.5,0,4.5,9)
        P1 = [P1[0][0], P1[0][1]]
        P2 = two.reflectionAboutLine(P2[0],P2[1],4.5,0,4.5,9)
        P2 = [P2[0][0], P2[0][1]]
    elif code1 == '0110':
        P1 = two.reflectionAboutLine(P1[0],P1[1],0,0,9,9)
        P1 = [P1[0][0], P1[0][1]]
        P2 = two.reflectionAboutLine(P2[0],P2[1],0,0,9,9)
        P2 = [P2[0][0], P2[0][1]]
        
    return [P1,P2]

[P1,P2] = bringToPos(P1, P2)

plt.plot([P1[0],P2[0]], [P1[1], P2[1]], 'k--')

code1 = codeAssign(P1)
code2 = codeAssign(P2)

winLeftDown = [3,3]
winLeftUp = [3,6]
winRightDown = [6,3]
winRightUp = [6,6]

plt.plot([P1[0],winLeftDown[0]], [P1[1], winLeftDown[1]], 'y--')
plt.plot([P1[0],winRightDown[0]], [P1[1], winRightDown[1]], 'y--')
plt.plot([P1[0],winRightUp[0]], [P1[1], winRightUp[1]], 'y--')
plt.plot([P1[0],winLeftUp[0]], [P1[1], winLeftUp[1]], 'y--')

def findSlope(P1, P2):
    try: 
        slope = (P2[1] - P1[1])/(P2[0] - P1[0])
    except ZeroDivisionError :
        slope = 99999999
    return slope

slopeLeftUp = findSlope(P1, winLeftUp)
slopeLeftDown = findSlope(P1, winLeftDown)
slopeRightUp = findSlope(P1, winRightUp)
slopeRightDown = findSlope(P1, winRightDown)
slopeLine = findSlope(P1, P2)

print slopeLeftDown
print slopeLeftUp
print slopeRightUp
print slopeRightDown
print slopeLine

if code1 == '0000':
    case = 1
elif code1 == '0001':
    case = 2
elif code1 == '1001':
    case = 3
else:
    case = 'Not defined'
  
if code1 == code2:
    case = 4
 
region = 'Invisible'
   
if case == 1:
    if slopeLine > slopeLeftUp and slopeLine < slopeLeftDown and P1[0] > P2[0]:
        region = 'L'
    elif ((slopeLine > -10**10 and slopeLine < slopeLeftUp) or (slopeLine < 10**10 and slopeLine >= slopeRightUp)) and P2[1] > P1[1]:
        region = 'T'
    elif slopeLine > slopeRightDown and slopeLine < slopeRightUp and P1[0] < P2[0]:
        region = 'R'
    elif ((slopeLine < 10**10 and slopeLine > slopeLeftDown) or (slopeLine > -10**10 and slopeLine < slopeRightDown)) and P2[1] < P1[1]:
        region = 'B'
   
elif case == 2:
    if slopeLine >= slopeRightUp and slopeLine < slopeLeftUp:
        if P2[1] < ymax:
            region = 'L'
        else: 
            region = 'LT'
    elif slopeLine >= slopeRightDown and slopeLine < slopeRightUp:
        if P2[0]< xmax:
            region = 'L'
        else:
            region = 'LR'
    elif slopeLine >= slopeLeftDown and slopeLine < slopeRightDown:
        if P2[1] > ymin:
            region = 'L'
        else:
            region = 'LB'
            
elif case == 3:
    if abs(slopeLeftUp) >= 1:
        print 'Here'
        if slopeLine >= slopeRightDown and slopeLine < slopeRightUp:
            if P2[0] < xmax:
                region = 'T'
            else: 
                region = 'TR'
        elif slopeLine >= slopeLeftUp and slopeLine < slopeRightDown:
            if P2[1] > ymin:
                region = 'T'
            else:
                region = 'TB'
        elif slopeLine >= slopeLeftDown and slopeLine < slopeLeftUp:
            if P2[1] > ymin:
                region = 'L'
            else:
                region = 'LB'
                
    else:
        if slopeLine >= slopeLeftUp and slopeLine < slopeRightUp:
            if P2[0] < xmax:
                region = 'T'
            else: 
                region = 'TR'
        elif slopeLine >= slopeRightDown and slopeLine < slopeLeftUp:
            if P2[0] < xmax:
                region = 'L'
            else:
                region = 'LR'
        elif slopeLine >= slopeLeftDown and slopeLine < slopeRightDown:
            if P2[1] > ymin:
                region = 'L'
            else:
                region = 'LB'
                
print region