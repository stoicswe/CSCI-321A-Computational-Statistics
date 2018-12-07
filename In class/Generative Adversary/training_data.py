import numpy as np
import math


def get_y(x, scale):
    return math.sin(x)*scale #10 + x*x


def sample_data_sine(n=10000, scale=100):
    data = []

    #x = scale*(np.random.random_sample((n,))-0.5)
    x = np.linspace(0, 2*math.pi, num=n)#
    #x = [scale*math.sin(xi) for xi in x]

    for i in range(len(x)):
        yi = get_y(x[i], scale)
        data.append([x[i], yi])

    return np.array(data)