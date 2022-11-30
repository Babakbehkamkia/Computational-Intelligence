# Q2_graded
from tensorflow import keras
import tensorflow as tf

(X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
X_train = X_train / 255

# Q2_graded
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

# Q2_graded
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets

# Q2_graded
class Hopfield:
    def __init__(self, train_data):
        train_data = np.array(train_data)
        dims = train_data.shape
        self.weights = np.zeros((dims[1], dims[1]))
        sum = 0
        count = 0
        for i in range(len(train_data)):
            for j in range(len(train_data[i])):
                sum += train_data[i][j]
                count += 1
        mean = sum / count
        for item in train_data:
            self.weights += np.outer(item - mean, item - mean)
        for i in range(dims[1]):
            self.weights[i, i] = 0
        self.weights /= len(train_data)

    def update(self, x):
        delta = self.weights.dot(x)
        result = []
        for i in delta:
            if i >= 0:
                result.append(1)
            else:
                result.append(-1)
        return np.array(result)

def Add_Noise(data, noise):   
    data = data.reshape((10,-1))
    for i in range(data.shape[0]):
        s = np.random.binomial(1, noise, data.shape[1])
        for j in range(data.shape[1]):
            if s[j] == 1:
                data[i][j] *= -1
    return data

def compute_accuracy(true_image, removed_noise_image):
    return 1 - np.sum(true_image != removed_noise_image) / 784

# Q2_graded
noises = [0.1, 0.3, 0.6]
Hopfield_sizes = [2, 200, 20000]
final_acc = {}

# Q2_graded
for i in range(3):
    indexes = np.random.randint(0, len(X_train), size=Hopfield_sizes[i])
    items = X_train[indexes]

    train = []
    for item in items:
        train.append(np.sign(item.reshape(-1) * 2 - 1))

    for j in range(3):
        indexes = []
        for k in range(10):
            indexes += random.sample(mnist_dict[k], 1)

        data_copy = X_train[indexes]
        sign_data = np.array([np.sign(t.reshape(-1) * 2 - 1) for t in data_copy])
        data_noise = Add_Noise(sign_data, noise=noises[j])

        fig = plt.figure(figsize=(30, 10), constrained_layout=True)
        spec = fig.add_gridspec(2, 10)
        axs = {}
        count_x = 0
        count_y = 0
        for noisy in data_noise:
            axs[f"ax{count_x * 10 + count_y}"] = fig.add_subplot(spec[count_x, count_y])
            axs[f"ax{count_x * 10 + count_y}"].imshow(noisy.reshape(28, 28))
            count_y += 1

        hf = Hopfield(train)

        count_x += 1
        count_y = 0
        accuracies = []
        
        for index in range(len(data_noise)):
            pred = hf.update(data_noise[index])
            axs[f"ax{count_x * 10 + count_y}"] = fig.add_subplot(spec[count_x, count_y])
            axs[f"ax{count_x * 10 + count_y}"].imshow(pred.reshape(28, 28))
            accuracies.append(compute_accuracy(sign_data[index], pred))
            count_y += 1
        
        final_acc[(Hopfield_sizes[i], noises[j])] =np.max(accuracies)
        
        fig.suptitle(f"images with noise rate of {noises[j]} and hopfield size of {Hopfield_sizes[i]}",fontsize = 50)

# Q2_graded
!pip install tabulate
from tabulate import tabulate
keys = list(final_acc.keys())
data = [[f"{keys[0][1] * 100}%", f'{final_acc[keys[0]]}',f'{final_acc[keys[3]]}',f'{final_acc[keys[6]]}'],
        [f"{keys[1][1] * 100}%", f'{final_acc[keys[1]]}',f'{final_acc[keys[4]]}',f'{final_acc[keys[7]]}'],
        [f"{keys[2][1] * 100}%", f'{final_acc[keys[2]]}',f'{final_acc[keys[5]]}',f'{final_acc[keys[8]]}'],]
col_names = ["Noise \ Network Size",f'n1={keys[0][0]}',f'n2={keys[3][0]}',f'n3={keys[6][0]}']
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))

