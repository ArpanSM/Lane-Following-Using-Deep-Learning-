# import the necessary packages
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Activation, Flatten, Dense
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from imutils import paths
import numpy as np
import argparse
import random
import cv2
import os
import matplotlib





#Then we define a class LeNet that can be used to build a CNN. Here
# as you can see this class has a function build which accepts arguments width, height, 
#depth, and classes.



class LeNet:
    @staticmethod
    def build(width, height, depth, classes):
        model = Sequential()
        inputShape = (height, width, depth)
# first set of CONV => RELU => POOL layers
        model.add(Conv2D(20, (5, 5), padding="same",
        input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    # second set of CONV => RELU => POOL layers
        model.add(Conv2D(50, (5, 5), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
# first (and only) set of FC => RELU layers
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))
# softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))
# return the constructed network architecture
        return model
        
    


   # initialize the model








#provide the path where your training image folders are present. You must have created 
#three folders forward, left, and right and place the corresponding images captured above 
#in respective folders.
    


dataset = './Dataset' # please change this path
# initialize the data and labels
print("[INFO] loading images...")
data = []
labels = []
 
# grab the image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images(dataset)))
random.seed(42)
random.shuffle(imagePaths)
# loop over the input images
for imagePath in imagePaths:
    # load the image, pre-process it, and store it in the data list
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (28, 28))
    image = img_to_array(image)
    data.append(image)
# extract the class label from the image path and update the
# labels list
    label = imagePath.split(os.path.sep)[-2]
    print(label)
    if label == 'forward':
        label = 0
    elif label == 'right':
        label = 1
    else:
        label =2
    labels.append(label)

    
    
    



#provide the path where your training image folders are present.
# You must have created three folders forward, left, and right and place 
#the corresponding images captured above in respective folders.
 
    

dataset = './Dataset' # please change this path
# initialize the data and labels
print("[INFO] loading images...")
data = []
labels = []
 


# grab the image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images(dataset)))
random.seed(42)
random.shuffle(imagePaths)
# loop over the input images
for imagePath in imagePaths:
    # load the image, pre-process it, and store it in the data list
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (28, 28))
    image = img_to_array(image)
    data.append(image)
# extract the class label from the image path and update the
    # labels list
    label = imagePath.split(os.path.sep)[-2]
    print(label)
    if label == 'forward':
        label = 0
    elif label == 'right':
        label = 1
    else:
        label =2
    labels.append(label)
    
    
    
#The above code then grabs the path of each image present in sub-folders, 
#stores in list imagePaths, and shuffles them.
    
    
#urther, each image is then read, resized, converted into numpy array and stored 
#in data. Now we also have to assign a label to each of the images.
# For this we extract the folder name from the image path of each image. 
#Then, we compare if folder name is ‘forward’, we assign label of 0. Similarly label of 1 and 2
# is assigned to images present in folder ‘right’, and ‘left’.
    
    
    
#that is why it was required to create sub-folders and place the similar 
#images in different folders.




# scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)
 
# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data,
    labels, test_size=0.25, random_state=42)
# convert the labels from integers to vectors
trainY = to_categorical(trainY, num_classes=3)
testY = to_categorical(testY, num_classes=3)




# initialize the number of epochs to train for, initial learning rate,
# and batch size
EPOCHS = 15
INIT_LR = 1e-3
BS = 32
# initialize the model
print("[INFO] compiling model...")
model = LeNet.build(width=28, height=28, depth=3, classes=3)
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="binary_crossentropy", optimizer=opt,
    metrics=["accuracy"])
 
# train the network
print("[INFO] training network...")
H = model.fit(trainX, trainY, batch_size=BS,
    validation_data=(testX, testY),# steps_per_epoch=len(trainX) // BS,
    epochs=EPOCHS, verbose=1)
 
# save the model to disk
print("[INFO] serializing network...")
model.save("model")
