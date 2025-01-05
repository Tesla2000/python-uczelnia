from collections.abc import Mapping
from collections.abc import Sequence
from typing import SupportsIndex

import numpy as np


class NetworkLayer:
    def __init__(self, activation_fn, shape: Sequence):
        self.fn, self.fn_prim = activation_fn
        self.weights = np.random.standard_normal(shape)
        self.values = np.zeros((shape[1]))


class NeuralNetwork:
    def __init__(self, layers: Sequence[Mapping], eta, output_shape: Sequence=(1, 1)):
        self.output_layer = np.zeros(output_shape)
        self.layers = []
        self.eta = eta

        for layer, next_layer in zip(layers[0:-1], layers[1:]):
            self.layers.append(
                NetworkLayer(layer['fn'], (next_layer['size'], layer['size']))
            )

        self.layers.append(
            NetworkLayer(layers[-1]['fn'],
                         (output_shape[0], layers[-1]['size']))
        )

    def feedforward(self, x):
        self.layers[0].values = x

        for layer, next_layer in zip(self.layers[0:-1], self.layers[1:]):
            next_layer.values = layer.fn(np.dot(layer.values, layer.weights.T))

        self.output_layer = self.layers[-1].fn(
            np.dot(self.layers[-1].values, self.layers[-1].weights.T)
        )

    def backprop(self, y):
        deltas = []

        delta = (y - self.output_layer) * \
            self.layers[-1].fn_prim(self.output_layer)
        deltas.append(self.eta * np.dot(delta.T, self.layers[-1].values))

        for layer, previous_layer in zip(reversed(self.layers[0:-1]), reversed(self.layers[1:])):
            delta = layer.fn_prim(previous_layer.values) * \
                np.dot(delta, previous_layer.weights)
            deltas.append(
                self.eta * np.dot(delta.T, layer.values)
            )

        for layer, weight in zip(self.layers, reversed(deltas)):
            layer.weights += weight

    def train(self, input, expected_output, iterations: SupportsIndex):
        for _ in range(iterations):
            self.feedforward(input)
            self.backprop(expected_output)
