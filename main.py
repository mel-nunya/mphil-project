# NECESSARY LIBRARIES
from tensorflow import keras
from tensorflow.keras.models import Sequential, Input, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers.normalization import BatchNormalization
from tensorflow.keras.layers.advanced_activations import LeakyReLU

# CONSTANTS TO BE DEFINED HERE
batch_size = 64
epochs = 20
num_classes = 10
