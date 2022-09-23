import math
from scipy import integrate


def laplace_function(x):
    return math.exp(-x * x / 2) * 2 / math.sqrt(2 * math.pi)


M_rectangle_trapezoid_method = 2 / math.exp(3 / 2)
M_simpsons_method = 2 / (math.exp(math.sqrt(3 + math.sqrt(6))))


def rectangle_method(x_a, x_b, h):
    n = int((x_b - x_a) / h)
    sum = 0
    cur_x = x_a
    for i in range(0, n):
        sum += h * abs(laplace_function((cur_x + cur_x + h) / 2))
        cur_x += h

    return sum, h ** 2 * M_rectangle_trapezoid_method * (x_b - x_a) / 24


def trapezoid_method(x_a, x_b, h):
    n = int((x_b - x_a) / h)
    sum = 0
    cur_x = x_a
    for i in range(0, n):
        sum += 0.5 * h * (abs(laplace_function(cur_x)) + abs(laplace_function(cur_x + h)))
        cur_x += h

    return sum, h ** 2 * M_rectangle_trapezoid_method * (x_b - x_a) / 12


def simpsons_method(x_a, x_b, h):
    n = int((x_b - x_a) / h)
    x = []
    cur = x_a
    sum = 0
    for i in range(0, n + 1):
        x.append(cur)
        cur += h
    for i in range(0, n):
        sum += abs(
            (h / 3) * (laplace_function(x[i]) + laplace_function(x[i + 1]) + laplace_function((x[i + 1] + x[i]) / 2)))

    return sum, h ** 4 * M_simpsons_method * (x_b - x_a) / 180


output_rectangle_method = rectangle_method(0, 6.5, 0.00001)
output_trapezoid_method = trapezoid_method(0, 6.5, 0.00001)
output_simpsons_method = simpsons_method(0, 6.5, 0.001)
print("quad")
print(integrate.quad(laplace_function, 0, 6.5), "\n")
print("h = 0.00001")
print('rectangle_method')
print(output_rectangle_method[0], output_rectangle_method[1])
print('trapezoid_method')
print(output_trapezoid_method[0], output_trapezoid_method[1])
print('simpsons_method')
print(output_simpsons_method[0], output_simpsons_method[1])
print("\n")
