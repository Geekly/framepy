__author__ = 'khooks'
from math import sqrt
import numpy as np
from numpy import ndarray
from elem_props import *

a = 1. #in^2
e = 10e6 #lb/in^2
i = 1000. #in^4
props = Properties()
props.A = a
props.E = e
props.I = i

print(props)
#element geometry
xydt = np.dtype([('node', np.int32), ('values', np.float64, 2)])
bcdt = np.dtype([('bc', np.int32), ('node', np.int32), ('values', np.float64, (3))])
conndt = np.dtype([('nodes', np.int32, (2)), ('propertyID', np.int32)])

xy = np.zeros((3, 2), dtype=np.float64)
xy[0] = [100, 75]
xy[1] = [0, 75]
xy[2] = [200, 0]
print(xy)

bc = np.zeros((2,4),dtype=np.int16)
bc[0] = [ 2 ,1,1,1]
bc[1] = [ 3, 1,1,1]
print(bc)

conn = np.zeros((2, 3), dtype=np.int16)
conn[0] = [2, 1, 1]
conn[1] = [1, 3, 1]
print(conn)

mprop = np.zeros((1, 3), dtype=np.float64)
mprop[0] = [1e4, 10., 1e3]
print(mprop)

jtloads = np.zeros((1), dtype='int16, float64, float64, float64')
#jtloads[0] = [1, 0., -10., -1000.]
print(jtloads)
#print(xy[xy['index']])
#xy = np.array([(1, (100., 75.)), (2, (0., 75.)), (3, (200., 0.))], dtype=xydt)
memloads = np.zeros((2,), dtype='int32, float64, float64, float64, float64, float64, float64')
memloads[0] = (1, 0, 12., 200., 0, 12., -200.)
memloads[1] = (2, -6., 8, 250., -6., 8., -250.)
print(memloads)

print( pf_stiff( [mprop[0][0], mprop[0][1], mprop[0][2]]))


