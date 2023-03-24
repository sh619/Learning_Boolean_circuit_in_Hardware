import numpy as np
import tensorflow as tf
import glob
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


#####################################Final train set##################################################
average_pixel_value_final = np.mean(x_train)
final_train_x= np.where(x_train > average_pixel_value_final, 1, 0)


# convert labels to one-hot encoded vectors
num_classes = 10
y_train_onehot = np.zeros((len(y_train), num_classes))
for i, label in enumerate(y_train):
   y_train_onehot[i][num_classes - label - 1] = 1

final_train_flattened = np.zeros((final_train_x.shape[0], 794), dtype=np.int)
for i in range(final_train_x.shape[0]):
    final_train_flattened[i] = np.insert(final_train_x[i].flatten(),784,values=y_train_onehot[i])

# Add the label to training data and test data
train_data = final_train_flattened

np.savetxt('final_train.txt', train_data, fmt="%s",delimiter=",")
file = open("final_train.txt","r")
lines = file.readlines()
with open("final_train.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])



#####################################Final test set############################################################

average_pixel_value_final = np.mean(x_test)
final_test_x= np.where(x_test > average_pixel_value_final, 1, 0)

y_test_onehot = np.zeros((len(y_train), num_classes))
for i, label in enumerate(y_test):
   y_test_onehot[i][num_classes - label - 1] = 1


final_test_flattened=np.zeros((final_test_x.shape[0], 784), dtype=np.int)
for i in range(final_test_x.shape[0]):
    final_test_flattened[i] = final_test_x[i].flatten()


np.savetxt('final_test.txt', final_test_flattened, fmt="%s",delimiter=",")
np.savetxt('final_test_label.txt', y_test_onehot, fmt="%s",delimiter=",")


file = open("final_test.txt","r")
lines = file.readlines()
with open("final_test.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])