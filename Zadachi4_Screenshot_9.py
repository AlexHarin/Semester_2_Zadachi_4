class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices should have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices should have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix should be equal to the number of rows in the second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Matrix should be square to find determinant")
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        for j in range(self.cols):
            det += ((-1) ** j) * self.data[0][j] * self.minor(0, j).determinant()
        return det

    def minor(self, i, j):
        return Matrix([row[:j] + row[j+1:] for row in (self.data[:i] + self.data[i+1:])])

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

A = Matrix(2, 2)
A.data = [[1, 2], [3, 4]]
B = Matrix(2, 2)
B.data = [[5, 6], [7, 8]]

print("A + B:")
print(A + B)

print("A - B:")
print(A - B)

print("A * B:")
print(A * B)

print("Transpose of A:")
print(A.transpose())

print("Determinant of A:")
print(A.determinant())
