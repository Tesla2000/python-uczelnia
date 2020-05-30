import numpy as np
import matplotlib.pyplot as plt
import math
import time
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
    lambda x: (1. / np.cosh(x))**2
)


class NeuralNetwork:
    def __init__(self, x, y, act1, act2, eta=0.1, layer_size=4):
        self.eta = eta
        self.input = x
        self.expected_output = y
        self.current_output = np.zeros(y.shape)

        self.weights1 = np.random.rand(layer_size, x.shape[1])
        self.weights2 = np.random.rand(1, layer_size)

        self.act1, self.act1_prim = act1
        self.act2, self.act2_prim = act2

    def feedforward(self):
        self.layer1 = self.act1(np.dot(self.input, self.weights1.T))
        self.current_output = self.act2(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.expected_output - self.current_output) * \
            self.act2_prim(self.current_output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.act1_prim(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, iterations):
        for _ in range(iterations):
            self.feedforward()
            self.backprop()


# x = np.linspace(0, 2, 21) # sinus
# y = np.sin(x * (3*np.pi/2))

x = np.linspace(-50, 50, 26)  # parabola
x = x / max(x)
y = x**2

x_reshaped = np.reshape(x, (len(x), 1))
y_reshaped = np.reshape(y, (len(y), 1))


# big_x = np.linspace(0, 2, 161) # sinus
big_x = np.linspace(-50, 50, 101)  # parabola
big_x = big_x / max(big_x)

big_x_reshaped = np.reshape(big_x, (len(big_x), 1))

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.set_title('Oryginał')
ax1.scatter(x, y)

ax2 = fig.add_subplot(2, 1, 2)
ax2.set_title('Aproksymowane')

# network = NeuralNetwork(x_reshaped, y_reshaped, sig, tanh, 0.1, 10) # sinus
network = NeuralNetwork(x_reshaped, y_reshaped, tanh,
                        tanh, 0.1, 10)  # parabola
for i in range(5000):
    network.train(100)
    network.input = big_x_reshaped
    network.feedforward()
    ax2.clear()
    ax2.set_xlabel(f"{i*100} iteracji")
    ax2.scatter(big_x_reshaped, network.current_output.flatten())
    network.input = x_reshaped
    plt.pause(0.016)
plt.show()
