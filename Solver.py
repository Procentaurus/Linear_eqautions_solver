from Matrix import Matrix
from ErrorManager import ErrorManager
import time


# class represents solver of sytem of linear equations
class Solver:

    def __init__(self, matrix, vector):
        if matrix.get_cols() > 0 and matrix.get_rows() > 0:
            self.__matrix = matrix
        else:
            raise ValueError("Given empty matrix.")

        if vector.get_cols() == 1:
            self.__vector = vector
        else:
            raise ValueError("Parameter given is not a vertical vector.")

    def set_vector(self, vector):
        if vector.get_cols() == 1:
            self.__vector = vector
        else:
            raise ValueError("Parameter given is not a vertical vector.")

    def jacobi_method(self, res_norm_given):
        D = self.__matrix.diag()
        L = self.__matrix.tril()
        U = self.__matrix.triu()

        L.mull_by(-1)
        U.mull_by(-1)

        sum = L + U
        elem1 = self.__matrix_system_of_equations(D, sum)
        D.inv_diagonal()
        elem2 = D * self.__vector

        iterations = 0
        outcome = Matrix(None, self.__vector.get_rows(), self.__vector.get_cols(), 1)
        last_res_norm = 1
        res_norm_vector = []

        start = time.time()

        while res_norm_given < last_res_norm:
            outcome = elem1 * outcome + elem2

            last_res = ErrorManager.count_residuum(self.__matrix, outcome, self.__vector)
            last_res_norm = ErrorManager.count_norm2(last_res)
            res_norm_vector.append(last_res_norm)

            iterations += 1
            print(iterations)
            if iterations == 50:
                break

        end = time.time()
        time_elapsed = end - start

        return outcome, iterations, time_elapsed, res_norm_vector

    def gauss_seidl_method(self, res_norm_given):
        D = self.__matrix.diag()
        L = self.__matrix.tril()
        U = self.__matrix.triu()

        L.mull_by(-1)
        U.mull_by(-1)

        elem1 = D - L
        elem2 = self.__forward_substitution(elem1, self.__vector)

        iterations = 0
        outcome = Matrix(None, self.__vector.get_rows(), self.__vector.get_cols(), 1)
        last_res_norm = 1
        res_norm_vector = []

        start = time.time()

        while res_norm_given < last_res_norm:
            outcome = self.__forward_substitution(elem1, U * outcome) + elem2

            last_res = ErrorManager.count_residuum(self.__matrix, outcome, self.__vector)
            last_res_norm = ErrorManager.count_norm2(last_res)
            res_norm_vector.append(last_res_norm)
            iterations += 1
            print(iterations)
            if iterations == 50:
                break

        end = time.time()
        time_elapsed = end - start

        return outcome, iterations, time_elapsed, res_norm_vector

    def lu_method(self, k):

        start = time.time()
        L, U = self.__lu_decomposition(k)

        y = self.__forward_substitution(L, self.__vector)
        x = self.__backward_substitution(U, y)

        res = ErrorManager.count_residuum(self.__matrix, x, self.__vector)
        res_norm = ErrorManager.count_norm2(res)

        end = time.time()
        time_elapsed = end - start

        return x, time_elapsed, res_norm

    def __lu_decomposition(self, k):
        # Initialize L and U matrices
        n = self.__matrix.get_cols()
        m = self.__matrix.get_rows()

        L = [[int(i == j) for j in range(n)] for i in range(m)]
        U = [[self.__matrix.get_array()[i][j] for j in range(n)] for i in range(m)]

        # Perform banded Gaussian elimination to compute LU factors
        for j in range(n):
            # Compute the band range for this column
            u = min(m - 1, j + k)

            # Compute the multipliers and update the matrix
            for i in range(j+1, min(m, j + k)):
                multiplier = U[i][j] / U[j][j]
                for d in range(j, min(n, u+1)):
                    U[i][d] -= multiplier * U[j][d]

                L[i][j] = multiplier

        return Matrix(L), Matrix(U)

    def __forward_substitution(self, matrix, vector):   # solves system of linear equations
                                                        # for lower-traingular matrix
        R = [[0] for _ in range(vector.get_rows())]

        for i in range(vector.get_rows()):
            R[i][0] = vector.get_array()[i][0]
            for j in range(i):
                R[i][0] -= matrix.get_array()[i][j] * R[j][0]
            R[i][0] /= matrix.get_array()[i][i]

        return Matrix(R)

    def __backward_substitution(self, matrix, vector):
        # solves system of linear equations for upper-triangular matrix
        R = [[0] for _ in range(vector.get_rows())]
        n = vector.get_rows()

        for i in range(n - 1, -1, -1):
            R[i][0] = vector.get_array()[i][0]
            for j in range(i + 1, n):
                R[i][0] -= matrix.get_array()[i][j] * R[j][0]
            R[i][0] /= matrix.get_array()[i][i]

        return Matrix(R)

    def __matrix_system_of_equations(self, matrix1, matrix2):
        if matrix1.get_diagonal:
            n = matrix1.get_rows()
            m = matrix2.get_cols()
            X = [[0.0] * m for i in range(n)]

            for j in range(m):
                for i in range(n):
                    X[i][j] = matrix2.get_array()[i][j] / matrix1.get_array()[i][i]

            return Matrix(X)
        else:
            raise ValueError("First matrix should be diagonal for good time complexity")



