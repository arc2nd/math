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


def createMatrix(rowCount, colCount, dataList):
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)

    return mat















