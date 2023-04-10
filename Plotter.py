import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


def plot_linear_chart(x_data, y_data, name):
    fig, ax = plt.subplots()

    max_y = max(y_data)
    i = -1
    while max_y != 0:
        max_y = max_y//10
        i += 1

    ax.yaxis.set_major_formatter(lambda x, pos: str(x))

    # Plot the data
    ax.plot(x_data, y_data)
    ax.set_title(f'Value of residuum norm for method {name}')

    # Show the plot
    plt.show()


def plot_linear_chart_multi(x_data, y1_data, y2_data, y3_data):

    plt.plot(x_data, y1_data, label='Jacobi')
    plt.plot(x_data, y2_data, label='Gauss-Seidel')
    plt.plot(x_data, y3_data, label='LU factorization')
    plt.title('Comparison of time used by algorithms while working with various data sizes')
    plt.legend()
    plt.xlim([0, 1000])
    plt.show()