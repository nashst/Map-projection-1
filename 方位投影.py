from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time,matplotlib
from numpy import pi as pi
from math import radians as radians
from math import cos as cos
from math import sin as sin
from random import choice as choice
import random

if __name__ == '__main__':
    values=["plasma"]

    count=0

    filepath=r'C:\Users\esa72\PycharmProjects\sgx\Date\201902\CoordTransfer\visualization\image'

    a=6378137
    b=6356752.314

    height=b*0.96

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

        xs_1 = [x0]
        ys_1 = [y0]
        zs_1 = [height]

        while i<50:
            m=random.randint(0,99)
            n=random.randint(0,99)

            if z[m][n]>0 and x[m][n]>0 and y[m][n]>0:
                x_new=x[m][n]
                y_new=y[m][n]
                z_new=z[m][n]

                xs.append(x_new*1.03)
                ys.append(y_new*1.03)
                zs.append(z_new*1.03)

                xs_1.append(x_new)
                ys_1.append(y_new)
                zs_1.append(height)

                plt.plot([x_new, x_new], [y_new, y_new], [z_new, height], color='black', linestyle='--',alpha=0.7,zorder=1000)

                i+=1

        ax.text(8500000,30000,30000,'X',fontsize=12)
        ax.text(30000,8500000,30000,'Y',fontsize=12)
        ax.text(30000,30000,8500000,'Z',fontsize=12)
        ax.text(x0,0,0,'X0',zorder=3,style='italic')
        ax.text(0,y0,0,'Y0',zorder=3,style='italic')
        ax.text(0,0,z0,'Z0',zorder=3,style='italic')

        ax.scatter(xs,ys,zs,color='red',s=10,zorder=1000)
        ax.scatter(xs_1,ys_1,zs_1,color='yellow',s=10,zorder=1000)

        ax.plot_surface(x,y,z,cmap="winter",alpha=0.7)
        # ax.contourf(x,y,z,zdir='z',offset=height,cmap="winter")
        print(x[...,np.newaxis].shape)
        print((b*np.ones(np.size(x[...,np.newaxis]))).shape)
        ax.plot_wireframe(x,y,b*np.ones(np.shape(x)))

        plt.plot([-11000000, a], [0, 0], [0, 0], color='indigo')
        plt.plot([0, 0], [-11000000, a], [0, 0], color='indigo')
        plt.plot([0, 0], [0, 0], [-11000000, a], color='indigo')

        ax.quiver(0,0,a,0,0,2500000,length=1,color='indigo')
        ax.quiver(0,a,0,0,2500000,0,length=1,color='indigo')
        ax.quiver(a,0,0,2500000,0,0,length=1,color='indigo')

        ax.set_xlim(-7000000,7000000)
        ax.set_ylim(-7000000,7000000)
        ax.set_zlim(-7000000,7000000)

        ax.view_init(20,-40)

        plt.show()

        plt.close()

