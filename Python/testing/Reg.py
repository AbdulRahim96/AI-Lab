import unittest
import numpy as np

def forward_mlp(input_x: np.array, weights: list, biases: list) -> np.array:
    """compute the forward pass of a multilayer perceptron.
    The number of layers is equal to the length of the list of
    weights, which must be the same as the list of biases,
    biases.
    args:
        input_x, np.array, input data
        weights, list of np.arrays, a list of np.array matrices,
             representing the weights
        biases: list of np.arrays, a list of biases for each
             layer
    returns:
          result, np.array, the output of the network
    """
    assert len(weights) == len(biases)
    for layer_index in range(len(weights) - 1):
        input_x = np.tanh(np.matmul(input_x, weights[layer_index]) + biases[layer_index])
    output = np.matmul(input_x, weights[-1]) + biases[-1]
    return output

def get_loss(input_x: np.array, weights: list, biases: list, target: np.array) -> np.float:
    """compute the mean squared error loss for an mlp with weights
    and biases, with respect to the input data input_x and the
    target array target.
    args:
        input_x, np.array, input data
        weights, list of np.arrays, a list of np.array matrices,
            representing the weights
        biases: list of np.arrays, a list of biases for each
            layer
        target: np.array, the target values
    returns:
          loss, np.float, the loss
    """
    output = forward_mlp(input_x, weights, biases)
    return np.mean((output - target)**2)

get_loss_grad = grad(get_loss, argnum=(1,2))

class TestMLP(unittest.TestCase):
    """tests for MLP, get_loss, and get_grad_loss"""
    def setUp(self):
        pass

    def test_forward_mlp(self):
        """test forward_mlp"""
        input_x = np.array([[1, 2, 3], [4, 5, 6]])
        weights = [np.array([[1, 2], [3, 4]]), 
                   np.array([[5, 6], [7, 8]]), 
                   np.array([[9, 10], [11, 12]])]
        biases = [np.array([[1, 2]]), np.array([[3, 4]]), np.array([[5, 6]])]
        output = forward_mlp(input_x, weights, biases)
        self.assertTrue(np.allclose(output, np.array([[-0.9, -0.9], [-0.9, -0.9]])))

    def test_get_loss(self):
        """test get_loss"""
        input_x = np.array([[1, 2, 3], [4, 5, 6]])
        weights = [np.array([[1, 2], [3, 4]]), 
                   np.array([[5, 6], [7, 8]]), 
                   np.array([[9, 10], [11, 12]])]
        biases = [np.array([[1, 2]]), np.array([[3, 4]]), np.array([[5, 6]])]
        target = np.array([[1, 1], [1, 1]])
        loss = get_loss(input_x, weights, biases, target)
        self.assertTrue(np.allclose(loss, 0.5))
