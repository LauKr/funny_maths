#!/usr/bin/python
""" Calculation of Pi via Monte-Carlo """

import random
import numpy as np
from time import process_time
MAX_STEPS = 1000000
REPEATS = 100


def method_1() -> float:
    """
    Generate two random numbers between 0 and 1 (as x and y coordinates).
    If x*x + y*y < 1, that is (x, y) inside the unit circle (segment).
    Pi is calculated by the fraction of points in the circle vs total number.
    """
    for i in range(REPEATS):
        step = 0
        sum = 0
        while step < MAX_STEPS:
            x = random.random()
            y = random.random()
            if x*x + y*y < 1.0:
                sum += 1
            step += 1
        estimate = 4.0 * sum / MAX_STEPS
    return estimate


def method_2() -> float:
    """
    Generates one random number [0, 1) as x and calculates the corresponding
    y value to put (x, y) on the unit circle.
    """
    for i in range(REPEATS):
        step = 0
        sum = 0.0
        while step < MAX_STEPS:
            x = random.random()
            y = (1.0 - x*x) ** 0.5
            sum = sum + y
            step += 1
        estimate = 4.0 * sum / MAX_STEPS
    return estimate


def method_3() -> float:
    """
    Generates a periodic x-grid and generates the corresponding y values to form a unit circle.
    """
    step = 1.0 / MAX_STEPS
    for i in range(REPEATS):
        sum = 0.0
        x = 0.0
        while x <= 1.0:
            y = (1.0 - x*x) ** 0.5
            sum = sum + y
            x += step
        estimate = 4.0 * sum / MAX_STEPS
    return estimate


def method_4() -> float:
    """
    Basically the same as method3, but utiliting the numpy module.
    """
    x_dom = np.linspace(0, 1, MAX_STEPS)
    for i in range(REPEATS):
        y     = np.sqrt(1-np.power(x_dom, 2))
        estimate    = 4.0 * y.sum() / MAX_STEPS
    return estimate


if __name__ == '__main__':
    lst_methods = [
        method_1,
        method_2,
        method_3,
        method_4,
        ]
    for method in lst_methods:
        t1 = process_time()
        pi = method()
        t2 = process_time()
        print("Pi was approximated to {} using {} steps and {} repeats in {} seconds.".format(pi, MAX_STEPS, REPEATS, round(t2-t1, 5)))
