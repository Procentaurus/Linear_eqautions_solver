from Solver import Solver
from Matrix import Matrix
from Plotter import *

import math

base_size = 925
# sizes = [100, 500, 1000, 2000, 3000]
# times_elapsed_j = []
# times_elapsed_gs = []
# times_elapsed_lu = []
#
# for i in range(len(sizes)):
#     matrix_1 = Matrix(None, sizes[i], sizes[i], 0, {0: 5 + 7, 1: -1, 2: -1, -1: -1, -2: -1})
#     b = Matrix([[math.sin(i * 5)] for i in range(sizes[i])])
#     solver_1 = Solver(matrix_1, b)
#     x, iterations_j, time_j, res_norm_j = solver_1.jacobi_method(10 ** (-9))
#     x2, iterations_gs, time_gs, res_norm_gs = solver_1.gauss_seidl_method(10 ** (-9))
#     x3, time_lu, res_norm_lu = solver_1.lu_method(4)
#     times_elapsed_j.append(time_j)
#     times_elapsed_gs.append(time_gs)
#     times_elapsed_lu.append(time_lu)

# plot_linear_chart_multi(sizes, times_elapsed_j, times_elapsed_gs, times_elapsed_lu)

matrix_1 = Matrix(None, base_size, base_size, 0, {0: 5+7, 1: -1, 2: -1, -1: -1, -2: -1})
matrix_2 = Matrix(None, base_size, base_size, 0, {0: 3, 1: -1, 2: -1, -1: -1, -2: -1})
b = Matrix([[math.sin(i*5)] for i in range(base_size)])

# solver_1 = Solver(matrix_1, b)
# solver_2 = Solver(matrix_2, b)


# outcome_1_j, iterations_1_j, time_elapsed_1_j, res_norm_vector_1_j = solver_1.jacobi_method(10**(-9))
# outcome_1_gs, iterations_1_gs, time_elapsed_1_gs, res_norm_vector_1_gs = solver_1.gauss_seidl_method(10**(-9))
# outcome_2_j, iterations_2_j, time_elapsed_2_j, res_norm_vector_2_j = solver_2.jacobi_method(10**(-9))
# outcome_2_gs, iterations_2_gs, time_elapsed_2_gs, res_norm_vector_2_gs = solver_2.gauss_seidl_method(10**(-9))

# print(time_elapsed_1_j)
# print(time_elapsed_1_gs)
# plot_linear_chart([i for i in range(iterations_1_j)], res_norm_vector_1_j, "Jacobi")
# plot_linear_chart([i for i in range(iterations_1_gs)], res_norm_vector_1_gs, "Gauss-Seidel")

# plot_linear_chart([i for i in range(iterations_2_j)], res_norm_vector_2_j, "Jacobi")
# plot_linear_chart([i for i in range(iterations_2_gs)], res_norm_vector_2_gs, "Gauss-Seidel")

solver_test = Solver(matrix_2, b)
outcome, time_elapsed, res_norm = solver_test.lu_method(4)
print(outcome)
print(time_elapsed)
print(res_norm)
