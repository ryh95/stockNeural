# MLP for Pima Indians Dataset with 10-fold cross validation
import csv

import pandas
from keras.models import Sequential
from keras.layers import Dense
from sklearn.cross_validation import StratifiedKFold
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
dataframe = pandas.read_excel("input.xlsx")
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,1:310].astype(float)
X_norm = (X-X.mean())/(X.max()-X.min())
Y = dataset[:,310]
# define 10-fold cross validation test harness
kfold = StratifiedKFold(y=Y, n_folds=10, shuffle=True, random_state=seed)
cvscores = []
for i, (train, test) in enumerate(kfold):
    # create model
    model = Sequential()
    model.add(Dense(300, input_dim=309, init='normal', activation='relu'))
    model.add(Dense(150, init='normal', activation='relu'))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X_norm[train], Y[train], nb_epoch=10, batch_size=5)
    # save weights
    model.save_weights(str(i)+'.model')
    # predict result
    predict_result = model.predict_classes(X[test])
    predict_result = predict_result.reshape(len(predict_result))
    # write results into files
    csvfile = file('resultPredict'+str(i)+'.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(predict_result)
    csvfile.close()
    # evaluate the model
    scores = model.evaluate(X[test], Y[test])
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)

print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))
