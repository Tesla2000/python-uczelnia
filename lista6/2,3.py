from collections.abc import Mapping
from collections.abc import Sequence

import matplotlib.pyplot as plt
import NeuralNetwork as nn
import numpy as np
# UWAGA! W TYM PLIKU ZANJDUJE SIĘ TAKŻE ZADANIE TRZECIE!

sig = (
    lambda x: 1./(1 + np.exp(-x)),
    lambda x: x * (1. - x)
)

relu = (
    lambda x: np.maximum(0, x),
    lambda x: 1. * (x > 0)
)

tanh = (
    lambda x: np.tanh(x),
    lambda x: 1-x**2
)


def mse(expected, actual: Sequence):
    sum = 0
    for index, result in enumerate(expected):
        sum += (result - actual[index])**2
    return sum/len(expected)


def visualize(test: Mapping):
    network = nn.NeuralNetwork(test['layers'], test['eta'])
    domain = test['x']/max(test['x'])
    image = test['fn'](domain)

    X = np.reshape(domain, (len(domain), 1))
    y = np.reshape(image, (len(image), 1))

    big = test['big']/max(test['big'])
    big_image = test['fn'](big)
    test_X = np.reshape(big, (len(big), 1))

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_title(test['name'])
    ax1.scatter(domain, y)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_title('Aproksymowane')

    for i in range(50):
        network.train(X, y, 100)
        network.feedforward(test_X)
        ax2.clear()
        ax2.set_xlabel(
            f"{i*100} iteracji\nMSE: {mse(big_image, network.output_layer.flatten())}")
        ax2.scatter(big, network.output_layer.flatten())
        plt.pause(0.016)
    plt.show()


tests = [
    {
        'name': 'Parabola, dwie warstwy',
        'layers': [
            {'fn': sig, 'size': 1},
            {'fn': tanh, 'size': 10},
        ],
        'x': np.linspace(-50, 50, 26),
        'big': np.linspace(-50, 50, 101),
        'fn': lambda x: x**2,
        'eta': 0.2
    },
    {
        'name': 'Sinus, dwie warstwy',
        'layers': [
            {'fn': tanh, 'size': 1},
            {'fn': tanh, 'size': 10}
        ],
        'x': np.linspace(0, 2, 21),
        'big': np.linspace(0, 2, 161),
        'fn': lambda x: np.sin((3*np.pi/2) * x),
        'eta': 0.01
    },
    {
        'name': 'Parabola, trzy warstwy',
        'layers': [
            {'fn': sig, 'size': 1},
            {'fn': sig, 'size': 10},
            {'fn': sig, 'size': 10},
        ],
        'x': np.linspace(-50, 50, 26),
        'big': np.linspace(-50, 50, 101),
        'fn': lambda x: x**2,
        'eta': 0.1
    },
    {
        'name': 'Sinus, trzy warstwy',
        'layers': [
            {'fn': tanh, 'size': 1},
            {'fn': tanh, 'size': 10},
            {'fn': tanh, 'size': 10}
        ],
        'x': np.linspace(0, 2, 21),
        'big': np.linspace(0, 2, 161),
        'fn': lambda x: np.sin((3*np.pi/2) * x),
        'eta': 0.01
    }
]

for test in tests:
    visualize(test)
