import numpy as np


sig = (
    lambda x: 1./(1 + np.exp(-x)),
    lambda x: x * (1. - x)
)

relu = (
    lambda x: np.maximum(0, x),
    lambda x: 1. * (x > 0)
)


# x - layer_size - 1 network
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


X = np.array(
    [[0, 0, 1],
     [0, 1, 1],
     [1, 0, 1],
     [1, 1, 1]
     ])

fns = [
    ('XOR', np.array([[0.], [1.], [1.], [0.]])),
    ('AND', np.array([[0.], [0.], [0.], [1.]])),
    ('OR', np.array([[1.], [1.], [1.], [1.]]))
]

np.set_printoptions(precision=3, floatmode='fixed')
for act1_name, act1 in [('sig', sig), ('relu', relu)]:
    print(f'{act1_name}')
    for act2_name, act2 in [('sig', sig), ('relu', relu)]:
        print(f'\t{act2_name}')
        for fn_name, fn_result in fns:
            network = NeuralNetwork(X, fn_result, act1, act2, eta=0.01)
            network.train(5000)
            print(f'\t\t{fn_name} -> \t{network.current_output.flatten()}')
            print(f'\t\t\t{fn_result.flatten()}')


# Wnioski dla nie-ustawionego seedu random:
# eta = ~0.5 - dobre dla sig-sig
# eta = ~0.3 - dobre dla relu-sig
# eta = ~0.1 - dobre dla sig-relu
# eta = ~0.01 - dobre dla relu-relu