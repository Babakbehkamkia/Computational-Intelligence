# Q2_graded
# Do not change the above line.

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
np.random.seed(0)
# Dataset
X,Y = datasets.make_circles(n_samples=576, shuffle=True, noise=0.25, random_state=None, factor=0.4)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='plasma')
plt.grid()
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.title('Data')
plt.show()

# Q2_graded

def sigmoid(Z):
    return 1/(1+np.exp(-Z))

def relu(Z):
    return np.maximum(0,Z)

def sigmoid_backward(dA, Z):
    sig = sigmoid(Z)
    return dA * sig * (1 - sig)

def relu_backward(dA, Z):
    dZ = np.array(dA, copy = True)
    dZ[Z <= 0] = 0
    return dZ

# Q2_graded

def create_model(layers):
  params = {}
  for i in range(len(layers)):
    if i == len(layers)-1:
      params[f"W{i+1}"] = np.random.randn(1, layers[i]) * 0.01
      params[f"b{i+1}"] = np.random.randn(1, 1) * 0.01
    else:
      params[f"W{i+1}"] = np.random.randn(layers[i+1], layers[i]) * 0.01
      params[f"b{i+1}"] = np.random.randn(layers[i+1], 1) * 0.01

  return params

# Q2_graded

def forward(X, params, layers, training=True):
    memory = {}
    A_curr = X
    for i in range(len(layers)):
        A_prev = A_curr
        # print(A_prev.shape)
        Z_curr = np.dot(params[f"W{i+1}"], A_prev) + params[f"b{i+1}"]
        if i == len(layers)-1:
            A_curr = sigmoid(Z_curr)
            # print('sigmoid')
        else:
            A_curr = relu(Z_curr)
            # print('relu')
        if training:
            memory[f"A{i}"] = A_prev
            memory[f"Z{i+1}"] = Z_curr
       
    return A_curr, memory

# Q2_graded

def backward(Y_pred, Y, memory, params, layers):
    grads_values = {}
    Y = Y.reshape(Y_pred.shape)
   
    dA_prev = - (np.divide(Y, Y_pred) - np.divide(1 - Y, 1 - Y_pred));    

    for i in range(len(layers)-1,-1,-1):
        dA_curr = dA_prev

        n = memory[f"A{i}"].shape[1]

        if i == len(layers)-1:
            dZ_curr = sigmoid_backward(dA_curr, memory[f"Z{i+1}"])
        else:
            dZ_curr = relu_backward(dA_curr, memory[f"Z{i+1}"])
        dW_curr = np.dot(dZ_curr, memory[f"A{i}"].T) / n
        db_curr = np.sum(dZ_curr, axis=1, keepdims=True) / n
        dA_prev = np.dot(params[f"W{i+1}"].T, dZ_curr)

        grads_values[f"dW{i+1}"] = dW_curr
        grads_values[f"db{i+1}"] = db_curr
    
    return grads_values

# Q2_graded

def update(params, grads_values, layers, learning_rate):
    for i in range(len(layers)):
        params[f"W{i+1}"] -= learning_rate * grads_values[f"dW{i+1}"]        
        params[f"b{i+1}"] -= learning_rate * grads_values[f"db{i+1}"]

    return params

# Q2_graded

def convert_prob_into_class(Y_pred):
    result = []
    Y_pred_ = Y_pred.reshape(-1)
    # print(Y_pred)
    return Y_pred >= 0.5

# Q2_graded

def loss_function(Y_pred, Y):
    m = Y_pred.shape[1]
    cost = -1 / m * (np.dot(Y, np.log(Y_pred).T) + np.dot(1 - Y, np.log(1 - Y_pred).T))
    return np.squeeze(cost)

def get_accuracy(Y_pred, Y):
    predicted_classes = convert_prob_into_class(Y_pred)
    Y_pred_ = Y_pred.reshape(-1)
    # return (Y_pred_ == Y).all(axis=0).mean()
    result = (predicted_classes == Y)
    return result.sum() / len(Y)

# Q2_graded

def decision_boundary(sample_X, weights, layers):

    x1_min, x1_max = sample_X[0, :].min() - 1, sample_X[0, :].max() + 1
    x2_min, x2_max = sample_X[1, :].min() - 1, sample_X[1, :].max() + 1
    h = 0.01

    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, h), np.arange(x2_min, x2_max, h))

    Z, _ = forward(np.c_[xx1.ravel(), xx2.ravel()].T, weights, layers, training=False)
    Z = Z.reshape(-1)
    Z[Z > 0.5] = 1
    Z[Z < 0.5] = 0
    Z = Z.reshape(xx1.shape)

    plt.figure()
    plt.contourf(xx1, xx2, Z, cmap=plt.cm.Spectral)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.scatter(sample_X[0, :], sample_X[1, :], c=Y, cmap=plt.cm.Spectral)
    plt.title("Decision Boundary")
    plt.show()

# Q2_graded

def train(X, Y, layers, epochs, learning_rate):
    params = create_model(layers)
    cost_history = []
    accuracy_history = []
    
    for i in range(epochs):
        Y_pred, cashe = forward(X, params, layers)
        cost = loss_function(Y_pred, Y)
        cost_history.append(cost)
        accuracy = get_accuracy(Y_pred, Y)
        accuracy_history.append(accuracy)
        
        grads_values = backward(Y_pred, Y, cashe, params, layers)
        params = update(params, grads_values, layers, learning_rate)

    fig, ax = plt.subplots()
    ax.plot(accuracy_history, label='acc')
    ax.plot(cost_history,label='loss')
    leg = ax.legend()

    decision_boundary(X, params, layers)
        
    # return params, cost_history, accuracy_history

# Q2_graded
# Do not change the above line.

# layers  (input layer, hidden layers)
for i in range(1, 4):  
    for j in range(1,4):
        layers = [2]
        for k in range(i):
            layers.append(256*j)

        print(f"model with {i} hidden layers and {j*256} nouron each")
        # calling the train function for training the model
        train(X.T, Y, layers, 1000, 0.5)  # (train_dataset, train_labels, layers, epochs, learning rate)
        print("=====================================================")
# Type your code here

