import numpy as np

if len(test_m[row-1]) < col:
   for i in range(len(test_m[row-1]), col):
       test_m[row-1].append(None)if len(test_m[row-1]) < col:
   for i in range(len(test_m[row-1]), col):
       test_m[row-1].append(None)

import math

VERBOSITY = 1

def _log(priority, msg):
    if VERBOSITY >= priority:
        print(msg)

matrix_list = []
for i in range(9):
    matrix_list.append(np.random.randint(10, size=10))
rand_matrix = np.matrix(matrix_list)

img_matrix = np.arange(100).reshape(10,10)

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


with np.printoptions(precision=3, suppress=True):
    print(img_matrix)

img_list = img_matrix.tolist()

# assumes numpy matrices
# first pass
def apply_transform(in_matrix, transf_matrix):
    rows, cols = in_matrix.shape
    print('rows:{}\ncols:{}'.format(rows, cols))
    out_matrix = np.matrix(np.zeros([rows, cols]))
    for i in range(0, rows-1):
        for j in range(0, cols-1):
            print('i:{}\nj:{}'.format(i, j))
            val = in_matrix[i, j]
            print('val:{}'.format(val))
            new_row, new_col = simple_transf(np.array([i, j]), transf_matrix).tolist()[0]
            int_row = int(new_row)
            int_col = int(new_col)
            print('new_row:{}\nnew_col:{}'.format(new_row, new_col))
            if int_row >= rows:
                int_row = int_row % rows
            if int_col >= cols:
                int_col = int_col % cols
            out_matrix[int(int_row), int(int_col)] = val
    return out_matrix

shear_out = apply_transform(img_matrix, y_shear_matrix)
stretch_out = apply_transform(img_magrix, y_stretch_matrix)



def apply_transform2(in_matrix, transf_matrix):
    rows, cols = in_matrix.shape
    _log(2, 'rows:{}\ncols:{}'.format(rows, cols))
    out_matrix = []
    # for every row
    for i in range(0, rows-1):
        # for every column
        for j in range(0, cols-1):
            _log(1, 'i:{}\nj:{}'.format(i, j)) 
            val = in_matrix[i, j]
            _log(2, 'val:{}'.format(val))
            new_row, new_col = simple_transf(np.array([i, j]), transf_matrix).tolist()[0]
            int_row = int(new_row)
            int_col = int(new_col)
            _log(2, 'new_row:{}\nnew_col:{}'.format(new_row, new_col))
            # if new transformed position is outside the existing out_matrix
            # then add a new row or col
            add_to_matrix2d(in_matrix, [int_row, int_col], val)
    return out_matrix


# in_matrix = np.array([[]])  # an empty matrix
# in_matrix = np.array([[1.0, 2.0], [3.0, 4.0]])  # an very basic matrix already populated
# add_to_matrix2d(in_matrix, [8,8], 4)  # returns an 8x8 matrix

#TODO: make sure I copy the in_matrix over successfully even if I don't have to expand it
# take in a matrix, a vector, and a valut
# if that vector does not exist in that matrix, expand the matrix until it does
# then place that value at that vector
def add_to_matrix2d(in_matrix, vector, value=0.0):
    out_matrix = []
    max_row = vector[0]
    max_col = vector[1]
    rows, cols = in_matrix.shape
    _log(1, 'max_row: {}\nmax_col: {}\nrows: {}\ncols: {}\n'.format(max_row, max_col, rows, cols))
    # add new rows
    if max_row >= rows-1:
        for i in range(0, max_row+1):
            _log(1, i)
            out_matrix.append([])
    # add new columns to each and every row
    for row in range(0, max_row+1):
        if max_col >= cols-1:
            for j in range(0, max_col+1):
                # _log(1, j)
                out_matrix[row].append(None)
    # copy in_matrix values to out_matrix spots
    for i in range(0, rows-1):
        for j in range(0, cols-1):
            init = in_matrix[i,j]
            _log(1, '{},{}: {}'.format(i,j,init))
            out_matrix[i][j] = init
    # place this value in the vector spot
    out_matrix[vector[0]][vector[1]] = value
    return np.array(out_matrix)
            







