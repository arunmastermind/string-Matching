import numpy as np
import tensorflow as tf
import tensorflow.keras

x = np.random.random((100,2))
# print(x)
y = tensorflow.keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)
print(y[2])

a = [1,2,3,4,5]
y1 = tensorflow.keras.utils.to_categorical(a, num_classes=10)
print(y1[2])

# print(np.random.randint(10, size=(1000, 1)))