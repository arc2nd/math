import numpy as np
import math

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


