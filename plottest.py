import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from pylab import *
import time

def go():
    startTime = time.clock()
    for i in range(0,200):
        print("rendering frame ", str(i))
        filename = "C:\\Users\\Peter\\Desktop\\temp\\" + str(i) + "(3).png"
        scatter(i).savefig(filename)        

    print("Elapsed time: ", str(time.clock()-startTime))

def scatter(n):
    z2 = -2 + (n/50.0)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_zlim(-2,2)
    xRange = []
    yRange = []
    zRange = []
    x = -2
    while x<2:
        y = -2
        while y<2:
            z = -2
            while z<2:
                if mandelbrot(x,z,y,z2):
                    xRange.append(x)
                    yRange.append(y)
                    zRange.append(z)
                z = z+0.04
            y = y+0.04
        x = x+0.04
    ax.scatter(xRange, yRange, zRange, marker=".")
    return fig

def main():
    x1Range = np.arange(-2,1, 0.01)
    y1Range = x2Range = y2Range = x1Range.copy()
    
    x1Range, y1Range = np.meshgrid(x1Range, y1Range)
    x2Range, y2Range = np.meshgrid(x2Range, y2Range)
    zs = np.array([mandelbrot(x1,y1,x2,y2) for x1,y1,x2,y2 in zip(
        np.ravel(x1Range),
        np.ravel(y1Range),
        np.ravel(x2Range),
        np.ravel(y2Range))])
    z = zs.reshape(x1Range.shape)

    
    print("x: ", size(x1Range))
    print("z: ", size(z))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    print("plotting...")
    ax.plot_surface(xRange, yRange, z, rstride=1, cstride=1)
    fig.show()


    
"""
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    fig.show()
"""
    
def mandelbrot(a, b):
    maxIteration = 100
    maxModulus = 2
    x = 0.0
    y = 0.0
    i = 0
    
    while i < maxIteration:
        if x*x + y*y > maxModulus:
            return 0
        xtemp = x*x - y*y + a
        y = 2*x*y + b
        x = xtemp
        i=i+1

    return 1

def mandelbrot(x1, y1, x2, y2):
    a = x1*x2
    b = y1*y2
    maxIteration = 200
    maxModulus = 2
    x = 0.0
    y = 0.0
    i = 0
    
    while i < maxIteration:
        if x*x + y*y > maxModulus:
            return False
        if i%2:
            xtemp = x*x - y*y + x1
            y = 2*x*y + y1
            x = xtemp
        else:
            xtemp = x*x - y*y + x2
            y = 2*x*y + y2
            x = xtemp
        i=i+1

    return True
    
