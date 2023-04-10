from Matrix import Matrix
import math


# implements basic error counting by creating residuum or counting norm
class ErrorManager:

    @staticmethod
    def count_residuum(matrix, outcome, impulse_vector):
        r = matrix * outcome
        r -= impulse_vector
        return r

    @staticmethod
    def count_norm2(vector):

        e2 = 0
        for i in range(vector.get_rows()):
            e2 += vector.get_array()[i][0] ** 2

        return math.sqrt(e2)
