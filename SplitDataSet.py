from sklearn.datasets import fetch_openml
import numpy as np
from scipy.ndimage.interpolation import shift

# receive MNIST dataset
mnist = fetch_openml('mnist_784', version=1)

# split our data
x = mnist["data"]
y = mnist["target"]

# split our data set to train and test depend on given hyperparameter
x_train, x_test, y_train, y_test = x[:6000], x[6000:], y[:6000], y[6000:]


# shift our data in 4 main direction to have better accuracy
def shift_image(image, dx, dy):
    image = image.reshape((28, 28))
    shifted_image = shift(image, [dy, dx], cval=0, mode="constant")
    return shifted_image.reshape(-1)


'''
for more information you can search about "data augmentation"

'''

image = x_train[1000]

# Ex.

# shifting down
shifted_image_down = shift_image(image, 0, 5)
# shifted left
shifted_image_left = shift_image(image, -5, 0)


# first make our data into list
x_train_augmented = [image for image in x_train]
y_train_augmented = [label for label in y_train]

# transfer whole data train with function
for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    for image, label in zip(x_train, y_train):
        x_train_augmented.append(shift_image(image, dx, dy))
        y_train_augmented.append(label)

# and covert our list into numpy array
x_train_augmented = np.array(x_train_augmented)
y_train_augmented = np.array(y_train_augmented)

# make  shuffle train set
shuffle_idx = np.random.permutation(len(x_train_augmented))

x_train_augmented = x_train_augmented[shuffle_idx]
y_train_augmented = y_train_augmented[shuffle_idx]

