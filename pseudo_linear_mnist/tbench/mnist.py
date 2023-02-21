import numpy as np
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


# Filter the training set to only include images with label 1 or 0
x_train = x_train[(y_train == 1) | (y_train == 0)]
y_train = y_train[(y_train == 1) | (y_train == 0)]

# Filter the test set to only include images with label 1 or 0
x_test = x_test[(y_test == 1) | (y_test == 0)]
y_test = y_test[(y_test == 1) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test)

# Convert the training set
x_train = np.where(x_train > average_pixel_value_train, 1, 0)
print(y_train.shape)
# Convert the test set
x_test = np.where(x_test > average_pixel_value_test, 1, 0)

# Flatten the image
train_image_flattened=np.zeros((x_train.shape[0], 784), dtype=np.int)
test_image_flattened=np.zeros((x_test.shape[0], 784), dtype=np.int)
for i in range(x_train.shape[0]):
    train_image_flattened[i] = x_train[i].flatten()
for i in range(x_test.shape[0]):
    test_image_flattened[i] = x_test[i].flatten()

# Save the result to a txt file
# np.savetxt('train.txt', train_image_flattened, fmt="%s",delimiter=",")
# np.savetxt('test.txt', test_image_flattened, fmt='%s',delimiter=",")

# file = open("train.txt","r")
# lines = file.readlines()
# with open("train.txt" , "w") as f:
#     for line in lines :
#         s= line.split(",")
#         for i in range(len(s)):
#             f.write(s[i])

# file = open("test.txt","r")
# lines = file.readlines()
# with open("test.txt" , "w") as f:
#     for line in lines :
#         s= line.split(",")
#         for i in range(len(s)):
#             f.write(s[i])

# Add the label to training data and test data
print(train_image_flattened.shape)
train_data = np.insert(train_image_flattened,784,values=y_train,axis=1)
test_data = np.insert(test_image_flattened,784,values=y_test,axis=1)


# Save the result to a txt file
np.savetxt('mnist_train.txt', train_data, fmt="%s",delimiter=",")
np.savetxt('mnist_test.txt', test_data, fmt='%s',delimiter=",")

file = open("mnist_train.txt","r")
lines = file.readlines()
with open("mnist_train.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("mnist_test.txt","r")
lines = file.readlines()
with open("mnist_test.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])




