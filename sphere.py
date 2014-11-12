import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from pylab import *
import time
from matplotlib import animation
import math

def go():
    startTime = time.clock()
    for i in range(0,200):
        print("rendering frame :", str(i))
        filename = "C:\\Users\\Peter\\Documents\\GitHub\\UGS-303\\sphere\\sphere" + str(i) + ".png"
        filename2= "C:\\Users\\Peter\\Documents\\GitHub\\UGS-303\\sphere\\circle" + str(i) + ".png"
        plotPlane(i).savefig(filename)
        close()
        plotCircle(i).savefig(filename2)
        close()
    print("Elapsed time: ", str(time.clock()-startTime))

def circle():
    fig = plt.figure()

def plotPlane(n):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")

    u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:10j]
    x=np.cos(u)*np.sin(v)
    y=np.sin(u)*np.sin(v)
    z=np.cos(v)
    ax.plot_wireframe(x, y, z, color="r")

    point = np.array([-10,-10, 1-n/100.0])
    normal = np.array([0,0,1])
    d = -point.dot(normal)

    xx,yy = np.meshgrid(range(-1,2), range(-1,2))
    zz = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]
    plane = ax.plot_wireframe(xx,yy,zz)
    return fig

def plotCircle(n):
    d = 2.0-n/100.0
    fig = plt.figure()
    ax = fig.gca()
    circle = plt.Circle((0,0), sqrt(1-(1-d)*(1-d)), fill=False)
    ax.add_artist(circle)
    ax.set_xlim([-1.5,1.5])
    ax.set_ylim([-1.5,1.5])
    return fig
    
