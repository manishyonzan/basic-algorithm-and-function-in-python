# Neural Network from Scratch
# Building a neural network from scratch is an excellent way to understand its inner workings. Below is a step-by-step guide to implementing a basic neural network using Python and NumPy.

# 1. Initialize Parameters

# Define the weights and biases for each layer. These are initialized randomly for weights and as zeros for biases.

import numpy as np

def initialize_parameters(layer_dims):
    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)
    for l in range(1, L):
        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1]) * 0.01
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
    return parameters


# 2. Forward Propagation
# Compute the activations for each layer using the sigmoid activation function.

def sigmoid(Z):
   return 1 / (1 + np.exp(-Z))


def forward_propagation(X, parameters):
    caches = []
    A = X
    L = len(parameters) // 2
    for l in range(1, L + 1):
       A_prev = A
       Z = np.dot(parameters['W' + str(l)], A_prev) + parameters['b' + str(l)]
       A = sigmoid(Z)
       caches.append((A_prev, Z))
    return A, caches


# 3. Compute Cost
# Calculate the cost using binary cross-entropy.

def compute_cost(A, Y):
    m = Y.shape[1]
    cost = (-1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))
    return cost


# 4. Backward Propagation
# Update the gradients of weights and biases using backpropagation.
def backward_propagation(A, Y, caches, parameters):
    grads = {}
    L = len(caches)
    m = Y.shape[1]
    dA = -(np.divide(Y, A) - np.divide(1 - Y, 1 - A))
    for l in reversed(range(L)):
        A_prev, Z = caches[l]
        dZ = dA * sigmoid(Z) * (1 - sigmoid(Z))
        grads["dW" + str(l+1)] = (1/m) * np.dot(dZ, A_prev.T)
        grads["db" + str(l+1)] = (1/m) * np.sum(dZ, axis=1, keepdims=True)
        dA = np.dot(parameters["W" + str(l+1)].T, dZ)
    return grads


# 5. Update Parameters
# Adjust weights and biases using gradient descent.

def update_parameters(parameters, grads, learning_rate):
    L = len(parameters) // 2
    for l in range(1, L + 1):
        parameters["W" + str(l)] -= learning_rate * grads["dW" + str(l)]
        parameters["b" + str(l)] -= learning_rate * grads["db" + str(l)]
    return parameters


# 6. Train the Model
# Combine all steps into a training loop.

def train(X, Y, layer_dims, learning_rate=0.01, epochs=1000):
    parameters = initialize_parameters(layer_dims)
    for i in range(epochs):
        A, caches = forward_propagation(X, parameters)
        cost = compute_cost(A, Y)
        grads = backward_propagation(A, Y, caches, parameters)
        parameters = update_parameters(parameters, grads, learning_rate)
        if i % 100 == 0:
            print(f"Cost after epoch {i}: {cost}")
    return parameters

# Example Usage
# Train a neural network with 3 layers: input (2 nodes), hidden (4 nodes), and output (1 node).

X_train = np.random.rand(2, 100) # Example input data
Y_train = (np.sum(X_train, axis=0) > 1).reshape(1, 100) # Example labels
layer_dims = [2, 4, 1]
parameters = train(X_train, Y_train, layer_dims)