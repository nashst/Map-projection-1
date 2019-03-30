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

        while i<20:
            m=random.randint(0,99)
            n=random.randint(0,99)

            if x[m][n]>0 and -a*sin(radians(10))<y[m][n]<a*sin(radians(10)):
                x_new=x[m][n]
                y_new=y[m][n]
                z_new=z[m][n]

                xs.append(x_new)
                ys.append(y_new)
                zs.append(z_new)

                e = sqrt(a ** 2 - b ** 2) / a
                ep = sqrt(a ** 2 - b ** 2) / b

                e2p = (a ** 2 - b ** 2) / (b ** 2)
                e2 = (a ** 2 - b ** 2) / (a ** 2)

                theta = atan(a * z_new / (b * sqrt(x_new ** 2 + y_new ** 2)))
                B = atan((z_new + e2p * b * sin(theta) ** 3) / (sqrt(x_new ** 2 + y_new ** 2) - e2 * a * cos(theta) ** 3))

                diff = 1
                while diff > 0.1 ** 10:
                    diff = atan(z_new / sqrt(x_new ** 2 + y_new ** 2) * (1 + a * e2 * sin(B) / (z_new * sqrt(1 - e2 * sin(B) ** 2)))) - B
                    B = atan(z_new / sqrt(x_new ** 2 + y_new ** 2) * (1 + a * e2 * sin(B) / (z_new * sqrt(1 - e2 * sin(B) ** 2))))

                L = math.atan(y_new / x_new)

                print('B,l',B,L)

                lat=B
                lon=L

                k0 = 0.9996

                t = tan(lat)
                eta = ep * cos(lat)
                N = a / sqrt(1 - e ** 2 * (sin(lat) ** 2))

                m0 = a * (1 - e ** 2)
                m2 = 3 / 2 * e ** 2 * m0
                m4 = 5 / 4 * e ** 2 * m2
                m6 = 7 / 6 * e ** 2 * m4
                m8 = 9 / 8 * e ** 2 * m6

                a0 = m0 + m2 / 2 + 3 * m4 / 8 + 5 * m6 / 16 + 35 * m8 / 128
                a2 = m2 / 2 + m4 / 2 + 15 * m6 / 32 + 7 * m8 / 16
                a4 = m4 / 8 + 3 * m6 / 16 + 7 * m8 / 32
                a6 = m6 / 32 + m8 / 16
                a8 = m8 / 128

                X = a0 * lat - a2 / 2 * sin(2 * lat) + a4 / 4 * sin(4 * lat) - a6 / 6 * sin(6 * lat) + a8 / 8 * sin(8 * lat)

                x_final = k0 * (X + 1 / 2 * N * t * (cos(lat) ** 2) * lon ** 2 + 1 / 24 * N * t * (5 - t ** 2 + 9 * eta ** 2 + 4 * eta ** 4) * cos(lat) ** 4 * lon ** 4 + 1 / 720 * N * t * (61 - 58 * t ** 2 + t ** 4 + 270 * eta ** 2 - 330 * eta ** 2 * t ** 2) * cos(lat) ** 6 * lon ** 6)

                y_final = k0 * (N * cos(lat) * lon + 1 / 6 * N * (1 - t ** 2 + eta ** 2) * cos(lat) ** 3 * lon ** 3 + 1 / 120 * N * (5 - 18 * t ** 2 + t ** 4 + 14 * eta ** 2 - 58 * eta ** 2 * t ** 2) * cos(lat) ** 5 * lon ** 5)

                xs.append(12000000)
                ys.append(y_final)
                zs.append(x_final)

                print(x_final,y_final)

                plt.plot([x_new, 12000000], [y_new, y_final], [z_new, x_final], color='black', linestyle='--')

                i+=1

        ax.text(8500000,30000,30000,'X',fontsize=12)
        ax.text(30000,8500000,30000,'Y',fontsize=12)
        ax.text(30000,30000,8500000,'Z',fontsize=12)
        ax.text(x0,0,0,'X0',zorder=3,style='italic')
        ax.text(0,y0,0,'Y0',zorder=3,style='italic')
        ax.text(0,0,z0,'Z0',zorder=3,style='italic')

        ax.scatter(xs,ys,zs,color='gray',s=20)

        ax.plot_surface(x,y,z,cmap="winter",alpha=0.7)
        ax.contourf(x,y,z,zdir='x',offset=12000000,cmap="winter",alpha=0.7)

        plt.plot([-11000000, a], [0, 0], [0, 0], color='indigo')
        plt.plot([0, 0], [-11000000, a], [0, 0], color='indigo')
        plt.plot([0, 0], [0, 0], [-11000000, a], color='indigo')

        ax.quiver(0,0,a,0,0,2500000,length=1,color='indigo')
        ax.quiver(0,a,0,0,2500000,0,length=1,color='indigo')
        ax.quiver(a,0,0,2500000,0,0,length=1,color='indigo')

        ax.set_xlim(-7000000,7000000)
        ax.set_ylim(-7000000,7000000)
        ax.set_zlim(-9000000,9000000)

        ax.view_init(20,-40)

        # plt.title(value)
        plt.show()

        plt.close()

