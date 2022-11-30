# Q3_graded
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib as mpl

# Q3_graded
from google.colab import drive
drive.mount('/content/drive')

# Q3_graded
path = "/content/drive/My Drive/CI/"

cities = pd.read_csv(path + "Cities.csv",sep=' ', names=['city_index', 'x', 'y'], header=None)

# Q3_graded
cities.head()

# Q3_graded
def plot_path(cities, dots, epoch):
    fig = plt.figure(figsize=(5, 5))
    axis = fig.add_axes([0,0,1,1])
    axis.scatter(cities['x'], cities['y'], color='red')
    axis.plot(dots[:,0], dots[:,1], color='blue', linewidth=1)
    plt.title(f"founded path until epoch {epoch}")
    plt.show()
    plt.close()

# Q3_graded
learning_rate = 1
epochs = 50000
n = cities.shape[0] * 10
weights = np.random.rand(n, 2)

# Q3_graded
for epoch in range(1, epochs+1):
    city_index = random.randint(0, cities.shape[0]-1)  
    city_value = cities.iloc[city_index][['x', 'y']].values
    closest = np.argmin(np.linalg.norm(weights - city_value, axis=1))

    radix = np.max([n//10, 1])
    deltas = np.abs(closest - np.arange(weights.shape[0]))
    distances = np.minimum(deltas, weights.shape[0] - deltas)

    gaussian = np.exp(-(1/2)*(distances**2) / radix**2)
    weights -= gaussian[:,np.newaxis] * learning_rate * (weights - city_value)

    if epoch % 100 == 0:
          learning_rate = learning_rate * 0.999
          n = n * 0.99
    if epoch % 10000 == 0:
          plot_path(cities, weights, epoch)

# Q3_graded
best_cities = []
for i in range(cities.shape[0]):
    city_axis = list(cities.iloc[i][['x', 'y']])
    val = np.argmin(np.linalg.norm(weights - city_axis, axis=1))
    best_cities.append((i, val))

best_cities.sort(key=lambda x: x[1])
path = [index for index,val in best_cities]
path = cities.reindex(path)[['x','y']]
best_distance = np.sum(np.linalg.norm(path - np.roll(path, 1, axis=0), axis=1))
print(best_distance)

