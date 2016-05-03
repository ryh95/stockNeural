#-*- coding: utf-8 -*-
import pandas as pd
inputfile = 'input.xls' #灰色预测后保存的路径
outputfile = 'output.xls' #神经网络预测后保存的结果
modelfile = '1-net.model' #模型保存路径
data = pd.read_excel(inputfile) #读取数据
feature = ['3ma-5ma', '3ma-10ma','3ma-15ma', '3ma-30ma', '3ma-90ma', '3ma-200ma','3ma-400ma','5ma-10ma','5ma-15ma','5ma-30ma','5ma-90ma','5ma-200ma','5ma-400ma','10ma-15ma','10ma-30ma'
           ,'10ma-90ma','10ma-200ma','10ma-400ma','15ma-30ma','15ma-90ma','15ma-200ma','15ma-400ma','30ma-90ma','30ma-200ma','30ma-400ma','90ma-200ma','90ma-400ma','200ma-400ma'] #特征所在列
print (len(feature))
data_train = data.loc[range(20071219,20140721)].copy() #取2014年前的数据建模
data_mean = data_train.mean()
data_std = data_train.std()
data_train = (data_train - data_mean)/data_std #数据标准化
x_train = data_train[feature].as_matrix() #特征数据
y_train = data_train['results'].as_matrix() #标签数据

from keras.models import Sequential
from keras.layers.core import Dense, Activation

model = Sequential() #建立模型
model.add(Dense(60,input_dim=28))
model.add(Activation('relu')) #用relu函数作为激活函数，能够大幅提供准确度
model.add(Dense(1,input_dim=60))
model.compile(loss='mean_squared_error', optimizer='adam') #编译模型
model.fit(x_train, y_train, nb_epoch = 20, batch_size = 16) #训练模型，学习一万次
model.save_weights(modelfile) #保存模型参数

#预测，并还原结果。
x = ((data[feature] - data_mean[feature])/data_std[feature]).as_matrix()
# data[u'y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']
data[u'y_pred'] = model.predict(x)
data.to_excel(outputfile)

import matplotlib.pyplot as plt #画出预测结果图
p = data[['y','y_pred']].plot(subplots = True, style=['b-o','r-*'])
plt.show()