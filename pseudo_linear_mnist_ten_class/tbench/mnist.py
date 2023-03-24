import numpy as np
import tensorflow as tf
import glob
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


#####################################Final test set############################################################

average_pixel_value_final = np.mean(x_test)
final_test_x= np.where(x_test > average_pixel_value_final, 1, 0)
# Define the mapping from numbers to encoding strings
mapping = {0: "000000000", 1: "000000001", 2: "000000010", 3: "000000100", 4: "000001000", 5: "000010000",6: "000100000",7: "001000000",8: "010000000", 9: "100000000"}

# Encode the input list using the mapping
encoded_numbers = [mapping[number] for number in y_test]

final_test_flattened=np.zeros((final_test_x.shape[0], 784), dtype=np.int)
for i in range(final_test_x.shape[0]):
    final_test_flattened[i] = final_test_x[i].flatten()


np.savetxt('final_test.txt', final_test_flattened, fmt="%s",delimiter=",")
np.savetxt('final_test_label.txt', encoded_numbers, fmt="%s",delimiter=",")


file = open("final_test.txt","r")
lines = file.readlines()
with open("final_test.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])




####################################Filter 0 and 1#####################################################
# Filter the training set to only include images with label 1 or 0
x_train_1 = x_train[(y_train == 1) | (y_train == 0)]
y_train_1 = y_train[(y_train == 1) | (y_train == 0)]

# Filter the test set to only include images with label 1 or 0
x_test_1 = x_test[(y_test == 1) | (y_test == 0)]
y_test_1 = y_test[(y_test == 1) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train_1)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test_1)

# Convert the training set
x_train_1 = np.where(x_train_1 > average_pixel_value_train, 1, 0)
print(y_train.shape)
# Convert the test set
x_test_1 = np.where(x_test_1 > average_pixel_value_test, 1, 0)

# Flatten the image
train_image_1_flattened=np.zeros((x_train_1.shape[0], 784), dtype=np.int)
test_image_1_flattened=np.zeros((x_test_1.shape[0], 784), dtype=np.int)
for i in range(x_train_1.shape[0]):
    train_image_1_flattened[i] = x_train_1[i].flatten()
for i in range(x_test_1.shape[0]):
    test_image_1_flattened[i] = x_test_1[i].flatten()

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
train_data_1 = np.insert(train_image_1_flattened,784,values=y_train_1,axis=1)
test_data_1 = np.insert(test_image_1_flattened,784,values=y_test_1,axis=1)


# Save the result to a txt file
np.savetxt('train_1.txt', train_data_1, fmt="%s",delimiter=",")
np.savetxt('test_1.txt', test_data_1, fmt='%s',delimiter=",")

file = open("train_1.txt","r")
lines = file.readlines()
with open("train_1.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("test_1.txt","r")
lines = file.readlines()
with open("test_1.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

############################################Filter 2 and 0##############################################


# Filter the training set to only include images with label 3 or 0
x_train_2 = x_train[(y_train == 2) | (y_train == 0)]
y_train_2 = y_train[(y_train == 2) | (y_train == 0)]

# Filter the test set to only include images with label 3 or 0
x_test_2 = x_test[(y_test == 2) | (y_test == 0)]
y_test_2 = y_test[(y_test == 2) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train_2)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test_2)

# Convert the training set
x_train_2 = np.where(x_train_2 > average_pixel_value_train, 1, 0)
y_train_2 = np.where(y_train_2 > 0, 1, 0)
# Convert the test set
x_test_2 = np.where(x_test_2 > average_pixel_value_test, 1, 0)
y_test_2 = np.where(y_test_2 > 0 , 1 , 0)
# Flatten the image
train_image_2_flattened=np.zeros((x_train_2.shape[0], 784), dtype=np.int)
test_image_2_flattened=np.zeros((x_test_2.shape[0], 784), dtype=np.int)
for i in range(x_train_2.shape[0]):
    train_image_2_flattened[i] = x_train_1[i].flatten()
for i in range(x_test_2.shape[0]):
    test_image_2_flattened[i] = x_test_2[i].flatten()

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
train_data_2 = np.insert(train_image_2_flattened,784,values=y_train_2,axis=1)
test_data_2 = np.insert(test_image_2_flattened,784,values=y_test_2,axis=1)


# Save the result to a txt file
np.savetxt('train_2.txt', train_data_2, fmt="%s",delimiter=",")
np.savetxt('test_2.txt', test_data_2, fmt='%s',delimiter=",")

file = open("train_2.txt","r")
lines = file.readlines()
with open("train_2.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("test_2.txt","r")
lines = file.readlines()
with open("test_2.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])
            

##################################################Filter 3 and 0###################################################

# Filter the training set to only include images with label 3 or 0
x_train_3 = x_train[(y_train == 3) | (y_train == 0)]
y_train_3 = y_train[(y_train == 3) | (y_train == 0)]

# Filter the test set to only include images with label 3 or 0
x_test_3 = x_test[(y_test == 3) | (y_test == 0)]
y_test_3 = y_test[(y_test == 3) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train_3)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test_3)

# Convert the training set
x_train_3 = np.where(x_train_3 > average_pixel_value_train, 1, 0)
y_train_3 = np.where(y_train_3 > 0 , 1 , 0)
# Convert the test set
x_test_3 = np.where(x_test_3 > average_pixel_value_test, 1, 0)
y_test_3 = np.where(y_test_3 > 0 , 1 , 0)

# Flatten the image
train_image_3_flattened=np.zeros((x_train_3.shape[0], 784), dtype=np.int)
test_image_3_flattened=np.zeros((x_test_3.shape[0], 784), dtype=np.int)
for i in range(x_train_3.shape[0]):
    train_image_3_flattened[i] = x_train_3[i].flatten()
for i in range(x_test_3.shape[0]):
    test_image_3_flattened[i] = x_test_3[i].flatten()

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
train_data_3 = np.insert(train_image_3_flattened,784,values=y_train_3,axis=1)
test_data_3 = np.insert(test_image_3_flattened,784,values=y_test_3,axis=1)


# Save the result to a txt file
np.savetxt('train_3.txt', train_data_3, fmt="%s",delimiter=",")
np.savetxt('test_3.txt', test_data_3, fmt='%s',delimiter=",")

file = open("train_3.txt","r")
lines = file.readlines()
with open("train_3.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("test_3.txt","r")
lines = file.readlines()
with open("test_3.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])
            
            
######################################################Filter 4 and 0##########################################
# Filter the training set to only include images with label 4 or 0
x_train_4 = x_train[(y_train == 4) | (y_train == 0)]
y_train_4 = y_train[(y_train == 4) | (y_train == 0)]

# Filter the test set to only include images with label 1 or 0
x_test_4 = x_test[(y_test == 4) | (y_test == 0)]
y_test_4 = y_test[(y_test == 4) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train_4)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test_4)

# Convert the training set
x_train_4 = np.where(x_train_4 > average_pixel_value_train, 1, 0)
y_train_4 = np.where(y_train_4 > 0 , 1 , 0)
# Convert the test set
x_test_4 = np.where(x_test_4 > average_pixel_value_test, 1, 0)
y_test_4 = np.where(y_test_4 > 0 , 1 , 0)

# Flatten the image
train_image_4_flattened=np.zeros((x_train_4.shape[0], 784), dtype=np.int)
test_image_4_flattened=np.zeros((x_test_4.shape[0], 784), dtype=np.int)
for i in range(x_train_4.shape[0]):
    train_image_4_flattened[i] = x_train_4[i].flatten()
for i in range(x_test_4.shape[0]):
    test_image_4_flattened[i] = x_test_4[i].flatten()

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
train_data_4 = np.insert(train_image_4_flattened,784,values=y_train_4,axis=1)
test_data_4 = np.insert(test_image_4_flattened,784,values=y_test_4,axis=1)


# Save the result to a txt file
np.savetxt('train_4.txt', train_data_4, fmt="%s",delimiter=",")
np.savetxt('test_4.txt', test_data_4, fmt='%s',delimiter=",")

file = open("train_4.txt","r")
lines = file.readlines()
with open("train_4.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("test_4.txt","r")
lines = file.readlines()
with open("test_4.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])
            
#####################################Filter 5 and 0#################################################
# Filter the training set to only include images with label 1 or 0
x_train_5 = x_train[(y_train == 5) | (y_train == 0)]
y_train_5 = y_train[(y_train == 5) | (y_train == 0)]

# Filter the test set to only include images with label 1 or 0
x_test_5 = x_test[(y_test == 5) | (y_test == 0)]
y_test_5 = y_test[(y_test == 5) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train_5)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test_5)

# Convert the training set
x_train_5 = np.where(x_train_5 > average_pixel_value_train, 1, 0)
y_train_5 = np.where(y_train_5 > 0 , 1 , 0)
# Convert the test set
x_test_5 = np.where(x_test_5 > average_pixel_value_test, 1, 0)
y_test_5 = np.where(y_test_5 > 0 , 1 , 0)

# Flatten the image
train_image_5_flattened=np.zeros((x_train_5.shape[0], 784), dtype=np.int)
test_image_5_flattened=np.zeros((x_test_5.shape[0], 784), dtype=np.int)
for i in range(x_train_5.shape[0]):
    train_image_5_flattened[i] = x_train_5[i].flatten()
for i in range(x_test_5.shape[0]):
    test_image_5_flattened[i] = x_test_5[i].flatten()

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
train_data_5 = np.insert(train_image_5_flattened,784,values=y_train_5,axis=1)
test_data_5 = np.insert(test_image_5_flattened,784,values=y_test_5,axis=1)


# Save the result to a txt file
np.savetxt('train_5.txt', train_data_5, fmt="%s",delimiter=",")
np.savetxt('test_5.txt', test_data_5, fmt='%s',delimiter=",")

file = open("train_5.txt","r")
lines = file.readlines()
with open("train_5.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("test_5.txt","r")
lines = file.readlines()
with open("test_5.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])
            
#########################################Filter 6 and 0##################################################
# Filter the training set to only include images with label 1 or 0
x_train_6 = x_train[(y_train == 6) | (y_train == 0)]
y_train_6 = y_train[(y_train == 6) | (y_train == 0)]

# Filter the test set to only include images with label 1 or 0
x_test_6 = x_test[(y_test == 6) | (y_test == 0)]
y_test_6 = y_test[(y_test == 6) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train_6)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test_6)

# Convert the training set
x_train_6 = np.where(x_train_6 > average_pixel_value_train, 1, 0)
y_train_6 = np.where(y_train_6 > 0 , 1 , 0)
# Convert the test set
x_test_6 = np.where(x_test_6 > average_pixel_value_test, 1, 0)
y_test_6 = np.where(y_test_6 > 0 , 1 , 0)

# Flatten the image
train_image_6_flattened=np.zeros((x_train_6.shape[0], 784), dtype=np.int)
test_image_6_flattened=np.zeros((x_test_6.shape[0], 784), dtype=np.int)
for i in range(x_train_6.shape[0]):
    train_image_6_flattened[i] = x_train_6[i].flatten()
for i in range(x_test_6.shape[0]):
    test_image_6_flattened[i] = x_test_6[i].flatten()

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
train_data_6 = np.insert(train_image_6_flattened,784,values=y_train_6,axis=1)
test_data_6 = np.insert(test_image_6_flattened,784,values=y_test_6,axis=1)


# Save the result to a txt file
np.savetxt('train_6.txt', train_data_6, fmt="%s",delimiter=",")
np.savetxt('test_6.txt', test_data_6, fmt='%s',delimiter=",")

file = open("train_6.txt","r")
lines = file.readlines()
with open("train_6.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("test_6.txt","r")
lines = file.readlines()
with open("test_6.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])
######################################################Filter 7 and 0##############################################
# Filter the training set to only include images with label 1 or 0
x_train_7 = x_train[(y_train == 7) | (y_train == 0)]
y_train_7 = y_train[(y_train == 7) | (y_train == 0)]

# Filter the test set to only include images with label 1 or 0
x_test_7 = x_test[(y_test == 7) | (y_test == 0)]
y_test_7 = y_test[(y_test == 7) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train_7)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test_7)

# Convert the training set
x_train_7 = np.where(x_train_7 > average_pixel_value_train, 1, 0)
y_train_7 = np.where(y_train_7 > 0 , 1 , 0)
# Convert the test set
x_test_7 = np.where(x_test_7 > average_pixel_value_test, 1, 0)
y_test_7 = np.where(y_test_7 > 0 , 1 , 0)

# Flatten the image
train_image_7_flattened=np.zeros((x_train_7.shape[0], 784), dtype=np.int)
test_image_7_flattened=np.zeros((x_test_7.shape[0], 784), dtype=np.int)
for i in range(x_train_7.shape[0]):
    train_image_7_flattened[i] = x_train_7[i].flatten()
for i in range(x_test_7.shape[0]):
    test_image_7_flattened[i] = x_test_7[i].flatten()

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
train_data_7 = np.insert(train_image_7_flattened,784,values=y_train_7,axis=1)
test_data_7 = np.insert(test_image_7_flattened,784,values=y_test_7,axis=1)


# Save the result to a txt file
np.savetxt('train_7.txt', train_data_7, fmt="%s",delimiter=",")
np.savetxt('test_7.txt', test_data_7, fmt='%s',delimiter=",")

file = open("train_7.txt","r")
lines = file.readlines()
with open("train_7.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("test_7.txt","r")
lines = file.readlines()
with open("test_7.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])
            
###########################################Filter 8 and 0##############################
# Filter the training set to only include images with label 1 or 0
x_train_8 = x_train[(y_train == 8) | (y_train == 0)]
y_train_8 = y_train[(y_train == 8) | (y_train == 0)]

# Filter the test set to only include images with label 1 or 0
x_test_8 = x_test[(y_test == 8) | (y_test == 0)]
y_test_8 = y_test[(y_test == 8) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train_8)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test_8)

# Convert the training set
x_train_8 = np.where(x_train_8 > average_pixel_value_train, 1, 0)
y_train_8 = np.where(y_train_8 > 0 , 1 , 0)
# Convert the test set
x_test_8 = np.where(x_test_8 > average_pixel_value_test, 1, 0)
y_test_8 = np.where(y_test_8 > 0 , 1 , 0)

# Flatten the image
train_image_8_flattened=np.zeros((x_train_8.shape[0], 784), dtype=np.int)
test_image_8_flattened=np.zeros((x_test_8.shape[0], 784), dtype=np.int)
for i in range(x_train_8.shape[0]):
    train_image_8_flattened[i] = x_train_8[i].flatten()
for i in range(x_test_8.shape[0]):
    test_image_8_flattened[i] = x_test_8[i].flatten()

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
train_data_8 = np.insert(train_image_8_flattened,784,values=y_train_8,axis=1)
test_data_8 = np.insert(test_image_8_flattened,784,values=y_test_8,axis=1)


# Save the result to a txt file
np.savetxt('train_8.txt', train_data_8, fmt="%s",delimiter=",")
np.savetxt('test_8.txt', test_data_8, fmt='%s',delimiter=",")

file = open("train_8.txt","r")
lines = file.readlines()
with open("train_8.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("test_8.txt","r")
lines = file.readlines()
with open("test_8.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

##############################################Filter 9 and 0########################################
# Filter the training set to only include images with label 1 or 0
x_train_9 = x_train[(y_train == 9) | (y_train == 0)]
y_train_9 = y_train[(y_train == 9) | (y_train == 0)]

# Filter the test set to only include images with label 1 or 0
x_test_9 = x_test[(y_test == 9) | (y_test == 0)]
y_test_9 = y_test[(y_test == 9) | (y_test == 0)]

# Calculate the average pixel value of the training set
average_pixel_value_train = np.mean(x_train_9)

# Calculate the average pixel value of the test set
average_pixel_value_test = np.mean(x_test_9)

# Convert the training set
x_train_9 = np.where(x_train_9 > average_pixel_value_train, 1, 0)
y_train_9 = np.where(y_train_9 > 0 , 1 , 0)
# Convert the test set
x_test_9 = np.where(x_test_9 > average_pixel_value_test, 1, 0)
y_test_9 = np.where(y_test_9 > 0 , 1 , 0)

# Flatten the image
train_image_9_flattened=np.zeros((x_train_9.shape[0], 784), dtype=np.int)
test_image_9_flattened=np.zeros((x_test_9.shape[0], 784), dtype=np.int)
for i in range(x_train_9.shape[0]):
    train_image_9_flattened[i] = x_train_9[i].flatten()
for i in range(x_test_9.shape[0]):
    test_image_9_flattened[i] = x_test_9[i].flatten()

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
train_data_9 = np.insert(train_image_9_flattened,784,values=y_train_9,axis=1)
test_data_9 = np.insert(test_image_9_flattened,784,values=y_test_9,axis=1)


# Save the result to a txt file
np.savetxt('train_9.txt', train_data_9, fmt="%s",delimiter=",")
np.savetxt('test_9.txt', test_data_9, fmt='%s',delimiter=",")

file = open("train_9.txt","r")
lines = file.readlines()
with open("train_9.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])

file = open("test_9.txt","r")
lines = file.readlines()
with open("test_9.txt" , "w") as f:
    for line in lines :
        s= line.split(",")
        for i in range(len(s)):
            f.write(s[i])
            
            
file_list = sorted(glob.glob("train_*.txt"))

with open("mnist_train.txt", "w") as outfile:
    for filename in file_list:
        with open(filename, "r") as infile:
            outfile.write(infile.read())
            
            
            
            
# Preparing test MNIST data