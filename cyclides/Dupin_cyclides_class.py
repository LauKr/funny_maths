# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:38:23 2020

@author: Laurenz Kruty
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from timeit import default_timer as timer
# from scipy.spatial import ConvexHull


class Zyklide:
    def __init__(self, r_off=1.5, N=100, a=10, b=5):
        self.N = N
        self.a = a
        self.b = b
        r = np.cos(np.linspace(0, 2*np.pi, N))
        self.r = r + r_off

    def ellipse(self, a, b, N):
        phi = np.linspace(0, 2*np.pi, N)
        x = (a * np.cos(phi))
        y = (b * np.sin(phi))
        coords = np.array([x, y])
        return coords

    def sphere(self, x, y, r):
        u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
        x = r*np.cos(u)*np.sin(v)-x
        y = r*np.sin(u)*np.sin(v)-y
        z = r*np.cos(v)
        return np.array([x, y, z])

    def calculate(self):
        start = timer()
        self.ellips_coords = self.ellipse(self.a, self.b, self.N)
        self.sphere_points = []
        for i in range(self.ellips_coords.shape[1]):
            self.sphere_points.append(
                self.sphere(
                    self.ellips_coords[0, i],
                    self.ellips_coords[1, i],
                    self.r[i]
                )
            )
        # self.c = ConvexHull(self.sphere_points[0][0,:,:])
        end = timer()
        print(f'Time for calculation: {end - start} s.')  # Time in seconds
        return 0

    def plot(self, theta=30, phi=45):
        start = timer()
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.set_axis_off()
        for i in range(self.ellips_coords.shape[1]):
            xi = self.sphere_points[i][0, :, :]
            yi = self.sphere_points[i][1, :, :]
            zi = self.sphere_points[i][2, :, :]
            ax.plot_surface(xi, yi, zi, color='b')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_zlim(-10, 10)
        ax.view_init(theta, phi)
        plt.savefig('cyclide.png', dpi=800)
        # plt.show()
        end = timer()
        print(f'Time for plotting: {end - start} s.')  # Time in seconds


# class Cyclide:
#     def __init__(self, a=1, b=0.98, d=0.3, N=10):
#         c = np.sqrt(a**2+b**2)
#         u = np.linspace(0, 2*np.pi, N)
#         v = np.linspace(0, 2*np.pi, N)
#         # u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
#         x = np.empty((len(u), len(v)))
#         y = np.empty((len(u), len(v)))
#         z = np.empty((len(u), len(v)))
#         for i in range(len(u)):
#             for j in range(len(v)):
#                 x[i, j] = (d*(c-a*np.cos(u[i])*np.cos(v[j]))+b*b*np.cos(u[i])
#                            / (a-c*np.cos(u[i])*np.cos(v[j])))
#                 y[i, j] = (b*np.sin(u[i])*(a-d*np.cos(v[j]))
#                            / (a-c*np.cos(u[i])*np.cos(v[j])))
#                 z[i, j] = (b*np.sin(v[j])*(c*np.cos(u[i])-d)
#                            / (a-c*np.cos(u[i])*np.cos(v[j])))
#         fig = plt.figure()
#         ax = Axes3D(fig)
#         ax.plot_surface(x, y, z)
#         ax.plot_surface(u, v, z)
#         # ax.set_xlim(-10, 10)
#         # ax.set_ylim(-10, 10)
#         # ax.set_zlim(-10, 10)
#         # ax.view_init(theta, phi)
#         plt.savefig('zyklide_test.png', dpi=600)
#         # plt.show()


if __name__ == '__main__':
    # Zy = Cyclide(N=10)
    ring_zyklide = Zyklide(a=8, b=8, N=1000)
    ring_zyklide.calculate()
    ring_zyklide.plot()
    # ring_zyklide.plot(theta=90, phi=0)
