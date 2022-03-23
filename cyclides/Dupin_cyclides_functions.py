# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:57:35 2020

@author: Laurenz Kruty
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def ellipse(a, b, N):
    phi = np.linspace(0, 2*np.pi, N)
    x = (a * np.cos(phi))
    y = (b * np.sin(phi))
    coords = np.array([x, y])
    return coords


def sphere(x, y, radius):
    u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:10j]
    x = radius*np.cos(u)*np.sin(v)-x
    y = radius*np.sin(u)*np.sin(v)-y
    z = radius*np.cos(v)
    return np.array([x, y, z])


def plot(N, a, b, r):
    fig = plt.figure()
    ax = Axes3D(fig)
    ellips_coords = ellipse(a, b, N)
    ax.plot(ellips_coords[0, :], ellips_coords[1, :])
    sphere_points = []
    for i in range(ellips_coords.shape[1]):
        sphere_points.append(sphere(ellips_coords[0, i], ellips_coords[1, i], r[i]))
        xi = sphere_points[i][0, :, :]
        yi = sphere_points[i][1, :, :]
        zi = sphere_points[i][2, :, :]
        ax.plot_surface(xi, yi, zi)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    ax.view_init(30, 45)
    # rotate the axes and update
    # for angle in range(0, 360):
    #     ax.view_init(30, angle)
    #     plt.draw()
    #     plt.pause(.001)
    plt.savefig('cyclide_with_grid.png', dpi=600)
    #plt.show()


if __name__ == '__main__':
    N = 200  # number of spheres
    r = np.cos(np.linspace(0, 2 * np.pi, N))  # positions of the spheres
    r += 1.5
    a = 10
    b = 5
    plot(N, a, b, r)
