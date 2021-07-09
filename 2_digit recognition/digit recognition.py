import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf #tf contain up to 60000 training sample and it will test up to 10000 sample

mnist = tf.keras.datasets.mnist #tensorflow contain mnist data set which can be loaded using keras
(x_train,y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
 
'''y is digits from 0 to 9 and which end classification and 
this are the labels which we don't need to scall down '''

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape= (28, 28)))   #input layer 
model.add(tf.keras.layers.Dense(units= 128, activation= tf.nn.relu))    #hidden layer 1
model.add(tf.keras.layers.Dense(units= 128, activation= tf.nn.relu))    #hidden layer 2
model.add(tf.keras.layers.Dense(units= 10, activation= tf.nn.softmax))   #output layer

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs= 3) #epochs= how many time model going to see the data 
                                              # or how many times we going to repeat the process

loss, accuracy= model.evaluate(x_test, y_test)
print(accuracy)
print(loss)

model.save('digits.model')

for x in range(1, 8):
	img = cv2.imread(f'{x}.jpeg')[:,:,0]
	img = np.invert(np.array([img]))
	prediction = model.predict(img)
	print("result:",  end = " ")
	print(np.argmax(prediction))
	plt.imshow(img[0], cmap = plt.cm.binary) 
	plt.show()