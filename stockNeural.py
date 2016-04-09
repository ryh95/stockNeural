#-*- coding: utf-8 -*-
#建立、训练多层神经网络，并完成模型的检验
from __future__ import print_function
import pandas as pd

inputfile1='train_neural.xls' #训练数据
inputfile2='test_neural.xls' #测试数据
testoutputfile = 'test_output_data.xls' #测试数据模型输出文件
data_train = pd.read_excel(inputfile1) #读入训练数据(由日志标记事件是否为洗浴)
data_test = pd.read_excel(inputfile2) #读入测试数据(由日志标记事件是否为洗浴)
y_train = data_train.iloc[:,29].as_matrix() #训练样本标签列
x_train = data_train.iloc[:,1:29].as_matrix() #训练样本特征
y_test = data_test.iloc[:,29].as_matrix() #测试样本标签列
x_test = data_test.iloc[:,1:29].as_matrix() #测试样本特征
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation

model = Sequential() #建立模型
model.add(Dense(30, input_dim=28,activation='relu')) #添加输入层、隐藏层的连接
model.add(Dropout(0.5))
model.add(Dense(40, activation='sigmoid')) #添加隐藏层、隐藏层的连接
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
#编译模型，损失函数为binary_crossentropy，用adam法求解
model.compile(loss='binary_crossentropy',optimizer='adam')

model.fit(x_train, y_train, nb_epoch = 1000, batch_size = 1) #训练模型2000次
model.save_weights('net.model') #保存模型参数

r = pd.DataFrame(model.predict_classes(x_test), columns = [u'预测结果'])
pd.concat([data_test.iloc[:,:30], r], axis = 1).to_excel(testoutputfile)
# model.predict(x_test)
