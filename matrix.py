class Matrix(object):
    def __init__(self, source_obj=None):
        import types
        if source_obj:
            if isinstance(source_obj, types.StringType):
                self.build_from_maya(source_obj)
            elif isinstance(source_obj, types.ListType):
                self.build_from_list(source_obj)

    def build_from_maya(self, maya_obj):
        import maya.cmds as cmds
        lSpace = cmds.getAttr('{}.matrix'.format(maya_obj))
        self.matrix = [lSpace[0:4], lSpace[4:8], lSpace[8:12], lSpace[12:]]
        pSpace = cmds.getAttr('{}.parentMatrix'.format(maya_obj))
        self.parent = [pSpace[0:4], pSpace[4:8], pSpace[8:12], pSpace[12:]]
        wSpace = cmds.getAttr('{}.worldMatrix'.format(maya_obj))
        self.world = [wSpace[0:4], wSpace[4:8], wSpace[8:12], wSpace[12:]]
        iSpace = cmds.getAttr('{}.inverseMatrix'.format(maya_obj))
        self.inverse = [iSpace[0:4], iSpace[4:8], iSpace[8:12], iSpace[12:]]

        self.xBasis = self.parent[0]
        self.yBasis = self.parent[1]
        self.zBasis = self.parent[2]

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



def getPositions(object):
    thisType = cmds.ls(object, st=True)[1]
    if thisType != "joint":
        thisPos = cmds.objectCenter(cmds.listRelatives(object, fullPath=1, s=True)[0], gl=True)
    else:
        #thisPos = cmds.objectCenter(object, gl=True)
        thisPos = cmds.xform(object, q=True, t=True, a=True, ws=True)
    return thisPos

def setPositions(object, thisPos):
    cmds.xform(object, t=thisPos, a=True, ws=True)

def distance(start, end):
    deltaX = start[0] - end[0]
    deltaY = start[1] - end[1]
    deltaZ = start[2] - end[2]

    powX = math.pow(deltaX, 2)
    powY = math.pow(deltaY, 2)
    powZ = math.pow(deltaZ, 2)
    powers = powX + powY + powZ
    distanceBetween = math.sqrt(powers)

    return distanceBetween

def get_scale(in_obj):
    m = Matrix(in_obj)
    xScale = distance([0.0, 0.0, 0.0], m.world[0][0:3])
    yScale = distance([0.0, 0.0, 0.0], m.world[1][0:3])
    zScale = distance([0.0, 0.0, 0.0], m.world[2][0:3])
    return (xScale, yScale, zScale)


# Cross Product Trick:
#	start with a single vector (init_vec)
#	take it's cross with a random vector (second_vec = cross(init_vec, rand_vec))
#	take a cross of those two (third_vec = cross(init_vec, second_vec))
#	This will yield you three vectors, each of which is at 90deg from each other
#	Normalize them and you have a local space
def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c
    
# Ok, officially dot product doesn't usually include the cosine, but that's a 
# convenient way to express it and is pretty standard in Maya
def dot(a, b):
    import math
    return math.cos(sum([i*j for (i, j) in zip(a, b)]))

def normalize(in_vec):
    import math
    factor = 1.0
    length = (in_vec[0] * in_vec[0]) + (in_vec[1] * in_vec[1]) + (in_vec[2] * in_vec[2])
    tmpX=tmpY=tmpZ = 0
    normV = in_vec

    if len == 0.0:
        return -1
    else:
        factor = 1.0/math.sqrt(length)

    if factor != 1.0:
        tmpX = in_vec[0]
        tmpY = in_vec[1]
        tmpZ = in_vec[2]

        tmpX *= factor
        tmpY *= factor
        tmpZ *= factor

        normV = [tmpX, tmpY, tmpZ]

    return normV

# how to express a vector from one space in another space.
# same magnitude, same direction (parallel in world space
# to original vector), different origin, different basis vectors
def re_space_vector(in_vector, new_basis_obj):
    v = in_vector
    m = Matrix(new_basis_obj) # get the matrix of the new basis object
    # multiply each component of the vector by each component of the new axis bases, and then add those
    # components together to get our new (x,y,z) coordinate
    accumulator = []
    for row in m.matrix[:3]:
        accuI = 0.0
        for i in range(len(v)):
            accuI += v[i] * row[i]
        accumulator.append(accuI)
    return accumulator

    scale = get_scale(new_basis_obj)
    result = []
    for i in range(len(v)):
        result.append(scale[i] / accumulator[i])
    return result

