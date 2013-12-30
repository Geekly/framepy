__author__ = 'ENG-5 USER'
from elem_props import *
import numpy as np
from numpy import ndarray
from math import sqrt

def pf_stiffness():
    ''''

        Calculate the stiffness matrix for a 2D frame element

    '''''

    pass

def pf_stiff(elem):
    A = elem.A
    I = elem.I
    E = elem.E
    L = sqrt((elem.x2-elem.x1)**2 + (elem.y2 - elem.y1)**2)
    k = E/L * np.array([A,  0., 0., -A, 0., 0.,
                        0., 12.*I/L**2, 6.*I/L, 0., -12.*I/L**2, 6.*I/L,
                        0., 6.*I/L, 4.*I, 0., -6.*I/L, 2.*I,
                        -A, 0., 0., A, 0., 0.,
                        0., -12.*I/L**2, -6.*I/L, 0., 12.*I/L**2, -6.*I/L,
                        0., 6.*I/L, 2.*I, 0., -6.*I/L, 4.*I], dtype=np.float64)
