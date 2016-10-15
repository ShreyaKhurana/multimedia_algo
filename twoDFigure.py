# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 06:54:20 2016

@author: Shreya Khurana

2D transformations
"""
import math 
import numpy as np
import matplotlib.pyplot as plt

#coord = [[0, 0], [0, 4], [6, 4], [6, 0], [0, 0]]
#x_coord = [point[0] for point in coord]
#y_coord = [point[1] for point in coord]
#plt.plot(x_coord, y_coord)
#plt.scatter(x_coord, y_coord)

def scalePoint(x,y,sx,sy):
    scale = np.matrix([[sx, 0], [0, sy]])
    point = np.matrix([[x],[y]])
    return (scale*point).transpose().tolist()
    
def rotatePoint(x,y,th):
    th = math.radians(th)
    point = np.matrix([[x],[y]])
    rot = np.matrix([[math.cos(th), -math.sin(th)],[math.sin(th), math.cos(th)]])
    return (rot*point).transpose().tolist()
    
def translatePoint(x,y,tx,ty):
    trans = np.matrix([[tx],[ty]])
    point = np.matrix([[x],[y]])
    return (trans + point).transpose().tolist()

def rotateAboutPoint(x,y,x1,y1,th):
    trans = translatePoint(x,y,-x1,-y1)
    rot = rotatePoint(trans[0][0],trans[0][1],th)
    return translatePoint(rot[0][0],rot[0][1],x1,y1)
    
def scaleAboutPoint(x,y,x1,y1,sx,sy):
    trans = translatePoint(x,y,-x1,-y1)
    rot = scalePoint(trans[0][0],trans[0][1],sx,sy)
    return translatePoint(rot[0][0],rot[0][1],x1,y1)
    
def refX(x,y):
    refx = np.matrix([[1, 0], [0, -1]])
    point = np.matrix([[x],[y]])
    return (refx*point).transpose().tolist()
    
def reflectionAboutLine(x,y,x1,y1,x2,y2):
    if x2 == x1:
        slope = 9999999
#        refy = np.matrix([[-1, 0], [0, 1]])
#        point = np.matrix([[x],[y]])
#        return (refy*point).tolist()
    
    else:
        slope = (y2 - y1)/(x2 - x1)
        
    th = math.degrees(math.atan(slope))
    trans = translatePoint(x,y,-x1,-y1)
    rot = rotatePoint(trans[0][0],trans[0][1],-th)
    ref = refX(rot[0][0], rot[0][1])
    rotInv = rotatePoint(ref[0][0],ref[0][1],th)
    return translatePoint(rotInv[0][0],rotInv[0][1],x1,y1)
        
        
def shearX(x,y,shx,yref):
    point = np.matrix([[x],[y],[1]])
    sh = np.matrix([[1,shx,-shx*yref],[0,1,0],[0,0,1]])
    return (sh*point).transpose().tolist()
    
#ans = reflectionAboutLine(1,2,0,3,3,3)
#plt.plot([0,3],[3,3])
#plt.scatter([0,3,1, ans[0][0]],[3,3,2, ans[0][1]])
#print ans[0][0]
#print ans[0][1]
#
#
#sx = 2
#sy = 3 
#newCoord = []
#for point in coord:
#    if [6,4] != point:
#        newCoord.extend(scaleAboutPoint(point[0], point[1], 6,4,2,2))
#    else:
#        newCoord.append([6,4])
#    
##for point in coord:
##    newCoord.extend(shearX(point[0],point[1],2,0))
##print newCoord
#x_coord = [point[0] for point in newCoord]
#y_coord = [point[1] for point in newCoord]
#plt.plot(x_coord, y_coord, 'r--')
#plt.scatter(x_coord, y_coord)