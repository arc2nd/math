class Matrix4(object):
    def __init__(self, source_obj=None):
        import types
        if isinstance(source_obj, types.ListType):
            self.build_from_list(source_obj)

    def build_from_list(self, mlist):
        self.matrix = [mlist[0:4], mlist[4:8], mlist[8:12], mlist[12:]]

    def mprint(self, matrix):
        print(matrix[0])
        print(matrix[1])
        print(matrix[2])
        print(matrix[3])

    def assembleMatrix(self, x, y, z):
        outM = []
        outM.extend(x)
        outM.extend(y)
        outM.extend(z)
        outM.extend([0.0, 0.0, 0.0, 0.0])
        return outM

    def lprint(self, list):
        print(list[0:4])
        print(list[4:8])
        print(list[8:12])
        print(list[12:])

class Matrix3(object):
    def __init__(self, source_obj=None):
        import types
        if isinstance(source_obj, types.ListType):
            self.build_from_list(source_obj)

    def build_from_list(self, mlist):
        self.matrix = [mlist[0:3], mlist[3:6], mlist[6:9]]

    def mprint(self, matrix):
        print(matrix[0])
        print(matrix[1])
        print(matrix[2])

    def assembleMatrix(self, x, y, z):
        outM = []
        outM.extend(x)
        outM.extend(y)
        outM.extend(z)
        return outM

    def lprint(self, list):
        print(list[0:3])
        print(list[3:6])
        print(list[6:9])

class Matrix2(object):
    def __init__(self, source_obj=None):
        import types
        if isinstance(source_obj, types.ListType):
            self.build_from_list(source_obj)

    def build_from_list(self, mlist):
        self.matrix = [mlist[0:2], mlist[2:4]]

    def mprint(self, matrix):
        print(matrix[0])
        print(matrix[1])

    def assembleMatrix(self, x, y):
        outM = []
        outM.extend(x)
        outM.extend(y)
        return outM

    def lprint(self, list):
        print(list[0:2])
        print(list[2:4])


import numpy as np
import math

matrix_list = []
for i in range(9):
    matrix_list.append(np.random.randint(10, size=10))
img_matrix = np.matrix(matrix_list)

# 2d transformation matrices
k = 2.0
theta = 45.0  # degrees rotation
x_stretch_matrix = np.matrix([[k, 0.0], [0, 1.0]])
y_stretch_matrix = np.matrix([1.0, 0.0], [0.0, k])
squeeze_matrix = np.matrix([[k, 0.0], [0.0, 1.0/k]])
clockwise_matrix = np.matrix([math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)])
counter_clock_matrix = np.matrix([math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)])

x_axis_shear = np.matrix([1.0, k], [0.0, 1.0])
y_axis_shear = np.matrix([1.0, 0.0], [k, 1.0])

def simple_transf(vector, matrix):
    return matrix.dot(vector)

# 3d transformation matrices
v = [0.0, 1.0, 0.0] # axis to rotate around (unit vector l,m,n)
l = v[0]
m = v[1]
n = v[2]
rot_matrix_row_0 = np.array((l * l * (1-math.cos(theta)) + math.cos(theta)),
                            (m * l * (1-math.cos(theta)) - (n * math.sin(theta))),
                            (n * l * (1-math.cos(theta)) + (m * math.sin(theta))))

rot_matrix_row_1 = np.array((l * m * (1-math.cos(theta)) + (n * math.sin(theta))),
                            (m * m * (1-math.cos(theta) + (math.cos(theta)))),
                            (n * m * (1-math.cos(theta) - (l * math.sin(theta)))))

rot_matrix_row_2 = np.array((l * n * (1-math.cos(theta)) - (m * math.sin(theta))),
                            (m * n * (1-math.cos(theta)) + (l * math.sin(theta))),
                            (n * n * (1-math.cos(theta)) - (math.cos(theta))))

rotation_matrix = np.matrix([rot_matrix_row_0, rot_matrix_row_1, rot_matrix_row_2])






