
# class represents matrix of any size and functions which enables basic matrix operations
class Matrix:
    def __init__(self, matrix, rows=0, cols=0, value=0, dict=None):
        if matrix is not None:    # when list of lists given
            if len(matrix) > 0 and len(matrix[0]) > 0:
                self.__rows = len(matrix)
                self.__cols = len(matrix[0])
                self.__array = matrix
                self.__diagonal = self.__is_diagonal()
            else:
                raise ValueError("Given empty matrix.")
        else:     # when params where given
            if rows > 0 and cols > 0:
                self.__rows = rows
                self.__cols = cols
                self.__array = [[value] * self.__cols for _ in range(self.__rows)]
                self.__diagonal = self.__is_diagonal()

                if dict is not None:                                 # dict stores info about diagonals which are to be filled with
                    for key, value in dict.items():                  # same values
                        if self.__cols > key > self.__rows * (-1):   #
                            if key >= 0:                             # for example  element 1: 9 in dict indicates that
                                for i in range(self.__rows - key):   # diagonal with index 1 (1 upper to diagonal) is to be filled                # with 9s
                                    self.__array[i][i+key] = value
                            else:
                                for i in range(self.__rows + key):
                                    self.__array[i - key][i] = value

                        else:
                            raise ValueError("Diagonal index out of range.")
                    self.__diagonal = self.__is_diagonal()

            else:
                raise ValueError("Wrong size of matrix given.")


    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def get_array(self):
        return self.__array

    def get_diagonal(self):
        return self.__diagonal

    def tril(self, k=-1):  # returns lower diagonal matrix
        L = []
        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                if i >= j - k:
                    row.append(self.__array[i][j])
                else:
                    row.append(0)
            L.append(row)
        return Matrix(L)

    def triu(self, k=1):   # returns upper diagonal matrix
        U = []
        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                if i <= j - k:
                    row.append(self.__array[i][j])
                else:
                    row.append(0)
            U.append(row)
        return Matrix(U)

    def diag(self):   # returns diagonal matrix
        if self.__rows != self.__cols:
            raise ValueError("Matrix must be square.")

        D = [[0 for j in range(self.__cols)] for i in range(self.__rows)]

        for i in range(self.__rows):
            if self.__array[i][i] != 0:
                D[i][i] = self.__array[i][i]

        return Matrix(D)

    def mull_by(self, number):    # mulltiplicates all elements of matrix by number
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__array[i][j] *= number

    def is_lower_triangular(self):
        for i in range(self.__rows):
            for j in range(i + 1, self.__cols):
                if self.__array[i][j] != 0:
                    return False

        return True

    def is_upper_triangular(self):
        for i in range(self.__rows):
            for j in range(i):
                if self.__array[i][j] != 0:
                    return False

        return True

    def __is_diagonal(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                if i != j and self.__array[i][j] != 0:
                    return False
        return True

    def inv_diagonal(self):
        if self.__diagonal:
            for i in range(self.__rows):
                self.__array[i][i] = 1 / self.__array[i][i]
        else:
            ValueError("Cant inverse non-diagonal matrix. It is not efficient.")

    def __add__(self, other):   # sum of 2 matrices
        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise ValueError("Matrices must be same size")

        A = []
        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                row.append(self.__array[i][j] + other.__array[i][j])
            A.append(row)
        return Matrix(A)

    def __sub__(self, other):   # sum of 2 matrices
        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise ValueError("Matrices must be same size")

        S = []
        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                row.append(self.__array[i][j] - other.__array[i][j])
            S.append(row)
        return Matrix(S)

    def __mul__(self, other):    # product of 2 matrices
        if self.__cols != other.__rows:
            raise ValueError("Matrices cannot be multiplied. Number of columns of first matrix must equal number of rows of second matrix.")

        M = [[0 for _ in range(other.__cols)] for _ in range(self.__rows)]

        if self.__diagonal and self.__rows == self.__cols:      # first matrix is diagonal
            for i in range(self.__rows):
                for j in range(other.__cols):
                    M[i][j] = other.__array[i][j] * self.__array[i][i]

        elif self.__diagonal and other.__cols == other.__rows:    # second matrix is diagonal
            for i in range(self.__cols):
                for j in range(other.__rows):
                    M[i][j] = other.__array[i][j] * self.__array[i][i]
        else:
            for i in range(self.__rows):
                for j in range(other.__cols):
                    for k in range(other.__rows):
                        M[i][j] += self.__array[i][k] * other.__array[k][j]

        return Matrix(M)

    def __repr__(self):
        text = f"Matrix: {self.__rows}x{self.__cols}\n"

        max_length = len(str(max(self.__array)))
        min_length = len(str(min(self.__array)))
        max_digits = len(str(max(max_length, min_length)))

        # Print the matrix with the elements aligned
        for row in self.__array:
            for element in row:
                text += str(element).rjust(max_digits + 1)
            text += "\n"

        return text
