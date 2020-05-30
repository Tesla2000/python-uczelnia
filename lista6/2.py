import numpy as np
import matplotlib.pyplot as plt

sig = (
    lambda x: 1./(1 + np.exp(-x)),
    lambda x: x * (1. - x)
)

relu = (
    lambda x: np.maximum(0, x),
    lambda x: 1. * (x > 0)
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


x = np.linspace(0, 2, 21)
y = np.sin(x * (3*np.pi/2))

x_reshaped = np.reshape(x, (21, 1))
y_reshaped = np.reshape(y, (21, 1))

print(y)
network = NeuralNetwork(x_reshaped, y_reshaped, sig, sig, 0.1, 5)
network.train(30000)
print(network.current_output)
network.input = np.reshape(np.linspace(0, 2, 161), (161, 1))
network.feedforward()
# jeszcze nie działa