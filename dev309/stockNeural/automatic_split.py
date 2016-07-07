# MLP with automatic validation set
import pandas
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
dataframe = pandas.read_excel("../input.xlsx", header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[1:,1:310].astype(float)
Y = dataset[1:,310]
X_norm = (X-X.mean())/(X.max()-X.min())
# create model
model = Sequential()
model.add(Dense(300, input_dim=309, init='normal', activation='relu'))
model.add(Dense(150, init='normal', activation='relu'))
model.add(Dense(1, init='normal', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X_norm, Y, validation_split=0.33, nb_epoch=150, batch_size=10)