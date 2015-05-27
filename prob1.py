# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:11:52 2015
# solution to ACM-ICPC 2015 world finals Problem A
# for complete problem text visit http://icpc.baylor.edu/worldfinals/problems/icpc2015.pdf
# for bugs contact: xshukla@acm.org

@author: xitij
"""
import math as m
import matplotlib.pyplot as plt
import numpy as np

# =========== Base Variables ===========
x=[]
tmpDict={}
finalDict={}
# =========== Two Functions we use ===========
def getDiff(x): # this is used later, to identify the difference
    for i in x:
        tmp=i
        for j in x:
            if(x.index(j)>x.index(tmp)):
                diff=tmp-j
                if (diff>0):
                    #print(tmp,"-",j,"=",diff)
                    tmpDict[diff]=(tmp,j)
                else:
                    tmpDict[diff]=(tmp,j)
            else:
                pass

def price(p,a,b,c,d,n): # this is used first, to populate list with modelled prices
    global x
    for k in range(1,n+1):
        pr=p*(m.sin((a*k+b))+m.cos(c*k+d)+2) # modelled function
        x.append(pr)
    plot(x,n)

def plot(x,n):
    nx = np.arange(1,n+1)
    plt.plot(nx,x,"bo")
    plt.show()
price(42,1,23,4,8,10) # this is how price funtion is invoked
getDiff(x)

finalDict = sorted(tmpDict,reverse=True)
i = iter(finalDict)
j=next(i)
if(j>0):
    print(j)   # this is the output 
else:
    j=0.00    
    print(j) # this is also the output in a case there's no decline!


