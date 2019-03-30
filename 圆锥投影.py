from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time,matplotlib
from numpy import pi as pi
from math import radians as radians
from math import sqrt as sqrt
from math import cos as cos
from math import sin as sin
from math import tan as tan
from math import atan as atan
import math
from random import choice as choice
import random

if __name__ == '__main__':
    values=["plasma"]

    count=0

    filepath=r'C:\Users\esa72\PycharmProjects\sgx\Date\201902\CoordTransfer\visualization\image'

    a=6378137
    b=6356752.314

    u=np.linspace(0,2*pi,100)
    # u=np.linspace(-radians(3),radians(3),100)
    v=np.linspace(0,pi,100)

    x=a*np.outer(np.cos(u),np.sin(v))
    y=a*np.outer(np.sin(u),np.sin(v))
    z=b*np.outer(np.ones(np.size(u)),np.cos(v))

    for value in values:
        u0=pi/3
        v0=pi/3

        x0=a*cos(u0)*sin(v0)
        y0=a*sin(u0)*sin(v0)
        z0=b*cos(v0)

        print(x.shape)
        print(y.shape)
        print(z.shape)

        fig=plt.figure()
        ax=fig.gca(projection='3d')

        plt.axis('off')

        i=0

        xs=[x0]
        ys=[y0]
        zs=[z0]

        for i in np.linspace(0,2*pi,200):
            angle=55
            sidelength=13000000

            x_yuanzhui=sidelength*cos(radians(angle))*sin(i)
            y_yuanzhui=sidelength*cos(radians(angle))*cos(i)
            z_yuanzhui=10000000-sidelength*sin(radians(angle))

            # plt.plot([0, x_yuanzhui], [0, y_yuanzhui], [10000000, z_yuanzhui], color='black', linestyle='--')
            plt.plot([0, x_yuanzhui], [0, y_yuanzhui], [10000000, z_yuanzhui], color='black',alpha=0.3)

        # ax.text(8500000,30000,30000,'X',fontsize=12)
        # ax.text(30000,8500000,30000,'Y',fontsize=12)
        # ax.text(30000,30000,8500000,'Z',fontsize=12)
        # ax.text(x0,0,0,'X0',zorder=3,style='italic')
        # ax.text(0,y0,0,'Y0',zorder=3,style='italic')
        # ax.text(0,0,z0,'Z0',zorder=3,style='italic')

        ax.scatter(xs,ys,zs,color='gray',s=20)

        ax.plot_surface(x,y,z,cmap="winter",alpha=0.7)
        # ax.contourf(x,y,z,zdir='x',offset=12000000,cmap="winter",alpha=0.7)

        # plt.plot([-11000000, a], [0, 0], [0, 0], color='indigo')
        # plt.plot([0, 0], [-11000000, a], [0, 0], color='indigo')
        # plt.plot([0, 0], [0, 0], [-11000000, a], color='indigo')

        # ax.quiver(0,0,a,0,0,2500000,length=1,color='indigo')
        # ax.quiver(0,a,0,0,2500000,0,length=1,color='indigo')
        # ax.quiver(a,0,0,2500000,0,0,length=1,color='indigo')

        ax.set_xlim(-5500000,5500000)
        ax.set_ylim(-5500000,5500000)
        ax.set_zlim(-5500000,5500000)

        # ax.view_init(270,0)

        # plt.title(value)
        plt.show()

        plt.close()

