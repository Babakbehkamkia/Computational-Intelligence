# Q1_graded
from tensorflow import keras
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Q1_graded
x_train = x_train/255

# Q1_graded
unique, counts = np.unique(y_train, return_counts=True)

result = np.column_stack((unique, counts)) 
print (result)

# Q1_graded
import random

mnist_dict = {
              0:[],
              1:[],
              2:[],
              3:[],
              4:[],
              5:[],
              6:[],
              7:[],
              8:[],
              9:[]
             }

for i in range(len(y_train)):
    mnist_dict[y_train[i]].append(i)

indexes = []

for i in range(10):
    indexes += random.sample(mnist_dict[i], 500)
    
print(len(indexes))

# Q1_graded
inputs = x_train[indexes].reshape(5000,-1)

inputs.shape

# Q1_graded
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)


# Hyper Parameters:
n = 5000
neurons = 400
image_shape = (28,28)
flatten_image_shape = image_shape[0] * image_shape[1]
grid_shape = (int(np.sqrt(neurons)),int(np.sqrt(neurons)))
learning_rate = 0.1
radius = 1
epochs = 600


def calculate_distance(a, index):
    i,j = np.indices(a, sparse=True)
    return (i-index[0])**2 + (j-index[1])**2

def convert_1D_2D(a):
    a0 = (int) (a/grid_shape[0])
    a1 = a % grid_shape[1]
    return a0, a1


def make_grid(weights, epoch):
    grid = np.zeros((grid_shape[0] * image_shape[0], grid_shape[1] * image_shape[1]))
    for i in range(grid_shape[0]):
        for j in range(grid_shape[1]):
            each_weight = weights[i * grid_shape[0] + j]
            convert_to_image = each_weight.reshape(image_shape[0], image_shape[1])
            grid[i * image_shape[0]: (i + 1) * image_shape[0], j * image_shape[1]: (j + 1) * image_shape[1]] = convert_to_image

    plt.imshow(grid, cmap="gray")
    plt.title(f"epoch {epoch}")
    plt.show()

# Q1_graded
def training(learning_rate, radius, learning_rate_decay=False, radius_decay=False):
    weights = np.random.rand(neurons, flatten_image_shape) 

    for epoch in range(1,epochs+1):
        batch = inputs[np.random.choice(len(inputs), size=128)]
        if epoch % 100 == 0:
            make_grid(weights, epoch)
            if learning_rate_decay:
                learning_rate *= 0.95
            if radius_decay:
                radius *= 0.95
        for sample in batch:
            best_neuron = np.argmin(np.sum((weights - sample) ** 2, axis=1))
            distances = calculate_distance(grid_shape, convert_1D_2D(best_neuron))
            distances = (-1 / (2 * radius ** 2)) * distances.reshape(-1, 1)
            weights = weights - learning_rate * (np.exp(distances) * (weights - sample))

# Q1_graded
training(learning_rate, radius)

# Q1_graded
training(learning_rate, radius, True)

# Q1_graded
training(learning_rate, radius, False, True)

# Q1_graded
training(learning_rate, radius, True, True)

