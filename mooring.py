__author__ = 'ENG-5 USER'

import numpy as np
from numpy import *
from numpy.linalg import *
from math import *


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


theta = 10.0 / 90.0 * pi / 2
P = 6000.
print("Known Values:")
print('theta: %2.3f rad' % theta)
print('P: %6.1f lbs' % P)

p1 = np.array([0, 0])
p2 = np.array([119, 0])
p3 = np.array([119, 162])
p4 = np.array([0, 162])

#print unit_vector(p3)
a = p1 - p4
b = p1 - p2
c = p1 - p3

cost = norm(b) / norm(c)
sint = norm(a) / norm(c)
tau = acos(cost)
print('tau: %2.1f' %tau)

print("vectors a, b, c", a, b, c)
def no_cross():
    print("No Cross")
    A = zeros((2, 2), dtype=float64)
    A[0] = [1, 0]
    A[1] = [0, 1]
    B = zeros((2, 1), dtype=float64)
    B[0] = [P*sint]
    B[1] = [P*cost]
    x = linalg.solve(A, B)
    print("Solving for X")
    print(x)



def only_cross():
    print("Only Cross")

    A = zeros((2, 2), dtype=float64)
    B = zeros((2, 1), dtype=float64)

    A[0] = [1, sint]
    A[1] = [0, cost]

    B[0] = P * cos(theta)
    B[1] = P * sin(theta)

    x = linalg.solve(A,B)
    print("Solving for X")
    print(x)

def with_cross():
    print("With Cross")

    A = zeros((3, 3), dtype=float64)
    B = zeros((3, 1), dtype=float64)

    A[0] = [1, 0, cost]
    A[1] = [0, 1, sint]
    A[2] = [-norm(b), norm(a), 0]

    B[0] = P * sin(theta)
    B[1] = P * cos(theta)
    B[2] = P * cos(theta + tau) / norm(c)

    x = linalg.solve(A, B)
    print("Solving for X")
    print(x)

no_cross()
only_cross()
with_cross()

