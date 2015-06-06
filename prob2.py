# -*- coding: utf-8 -*-
"""

# solution to ACM-ICPC 2015 world finals Problem B v2
# for complete problem text visit http://icpc.baylor.edu/worldfinals/problems/icpc2015.pdf
# for bugs contact: xshukla@acm.org

@author: xitij
"""
import math as m
import matplotlib.pyplot as plt
#import numpy as np

tmpPoly1 = [6,3,2,2,4,3,6,6,6,7,4,6,2,2,2]
tmpPoly2 = [4,18,5,22,9,26,5,22,1,-2,1]
#tmpPoly1 = [4,0,0,0,2,2,2,2,0,-1,1]
#tmpPoly2 = [4,10,0,10,2,12,2,12,0,1,1]
tmp=[]

class Poly:
    cordX=[]
    cordY=[]
    cordX.clear()   
    cordY.clear()
    noVertex=-1
    vx=0
    vy=0
    perim=-1
    distance=-1
    area=-1
    apothem=0
    centroid = ()
    Xmin=-1
    Xmax=-1
    Ymin=-1
    Ymax=-1
        
    def calcArea(self):
        self.distance = m.sqrt(((self.cordX[1]-self.cordX[0])**2)+((self.cordY[1]-self.cordY[0])**2)) #side of regular polygon
        self.perim=self.noVertex*self.distance #perimiter of the polygon
        self.apothem=self.distance/(2*m.tan(m.pi/self.noVertex)) #apothem
        self.area = 0.5*self.perim*self.apothem #area of the polygon
        self.tmpX = self.cordX[0]
        self.tmpY = self.cordY[0]
        
        tx = sum(self.cordX)/self.noVertex
        ty = sum(self.cordY)/self.noVertex
        self.centroid = (tx,ty) #centroid of the regular polygon
        
        xmax = max(self.cordX)
        xmin = min(self.cordX)

        tmaxind = self.cordX.index(xmax)
        tminind = self.cordX.index(xmin)
        ymax = self.cordY[tmaxind]
        ymin = self.cordY[tminind]        
        
        self.Xmax = xmax
        self.Xmin = xmin
        self.Ymax = ymax
        self.Ymin = ymin
        
    def __init__(self,tmp):
        self.cordX=[]        
        self.cordY=[]
        self.noVertex = tmp[0]
        for i in range(1,(len(tmp)-2),2):
            self.cordX.append(tmp[i])
            
        for i in range(2,(len(tmp)-2),2):
            self.cordY.append(tmp[i])
        
        self.vx = tmp[len(tmp)-2]
        self.vy = tmp[len(tmp)-1]
        self.calcArea()


dummyPol = Poly(tmpPoly1)           
dummyPol2 = Poly(tmpPoly1)             


def propagate(dummyPol,i): #propagate the polygon over time
    
    dx=dummyPol.vx*i
    dy=dummyPol.vy*i
    
    for j,k in enumerate(dummyPol.cordX):
        dummyPol.cordX[j]=k+dx
    
    for j,k in enumerate(dummyPol.cordY):
        dummyPol.cordY[j]=k+dy
        
    dummyPol.calcArea()

def chkCollision(dummyPol,dummyPol2):

    if(dummyPol.Xmin<=dummyPol2.Xmax and dummyPol.Ymin<=dummyPol2.Ymax):
        return(True)
    else:
        return(False)

P1 = Poly(tmpPoly1)        
P2 = Poly(tmpPoly2)

i=0
inc = 0.001
tmpDist = 0
centDist = 99
while(i<10):    
    tmpDist = centDist    
    i=i+inc    
    propagate(P1,inc)
    propagate(P2,inc)
    centDist = m.sqrt(((P1.centroid[0]-P2.centroid[0])**2)+((P1.centroid[1]-P2.centroid[1])**2))        
    
    if(centDist-tmpDist>0):
        print(centDist-tmpDist,i)
        plt.plot(P1.cordX,P1.cordY,"o")
        plt.plot(P2.cordX,P2.cordY,"^")
        break
    
plt.show()
