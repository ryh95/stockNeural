#-*- coding: utf-8 -*-
import csv
import os

import pandas as pd

from tools.cm_plot import * #导入自行编写的混淆矩阵可视化函数


def predict(filename,type,indicator,input_dim):
    neuralInputPath = 'data/neuralInput/' + filename + '/' + type + '/'
    neuralModelsPath = 'data/neuralModels/' + filename + '/' + type + '/'
    neuralOutputPath = 'data/neuralOutput/' + filename + '/' + type + '/'

    data = pd.read_excel(neuralInputPath + 'input' + indicator + '.xlsx')
    data = data.values
    # shuffle(data)

    p = 0.8  # 设置训练数据比例
    train = data[:int(len(data) * p), 1:]
    train_X = train[:,:input_dim].astype(float)
    train_X = (train_X-train_X.mean())/(train_X.max()-train_X.min())
    train_Y = train[:,input_dim]
    # train = (train-train.mean())/(train.max()-train.min())
    test = data[int(len(data) * p):, 1:]
    test_X = test[:, :input_dim].astype(float)
    test_X = (test_X - test_X.mean()) / (test_X.max() - test_X.min())
    test_Y = test[:, input_dim]
    # test = (test-test.mean())/(test.max()-test.min())

    from keras.models import Sequential  # 导入神经网络初始化函数
    from keras.layers.core import Dense, Activation, Dropout  # 导入神经网络层函数、激活函数

    if not os.path.exists(neuralModelsPath):
        os.mkdir(neuralModelsPath)
    netfile = neuralModelsPath+indicator+'.model'  # 构建的神经网络模型存储路径

    net = Sequential()
    net.add(Dense(300, input_dim=input_dim, init='normal', activation='relu'))
    net.add(Dense(150, init='normal', activation='relu'))
    net.add(Dense(1, init='normal', activation='sigmoid'))
    # Compile model
    net.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    net.fit(train_X,train_Y, nb_epoch=150, batch_size=5)

    scores = net.evaluate(test_X, test_Y)
    print("%s: %.2f%%" % (net.metrics_names[1], scores[1] * 100))

    # if os.path.exists(neuralModelsPath+indicator+'.model'):
    #     net.load_weights(netfile)
    # else:
    #     net.fit(train_X, train_Y, nb_epoch=100, batch_size=5)  # 训练模型，循环100次
    #     net.save_weights(netfile)  # 保存模型

    if type == 'binary':
        predict_result = net.predict_classes(test_X).reshape(len(test_X))  # 预测结果变形
        '''这里要提醒的是，keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n x 1维数组，而不是通常的 1 x n'''

        cm_plot(test_Y.tolist(), predict_result.tolist()).show() #显示混淆矩阵可视化结果

        from sklearn.metrics import roc_curve #导入ROC曲线函数
        import matplotlib.pyplot as plt

        predict_result2 = net.predict(test_X).reshape(len(test))
        fpr, tpr, thresholds = roc_curve(test_Y, predict_result2, pos_label=1)
        plt.plot(fpr, tpr, linewidth=2, label = 'ROC of LM') #作出ROC曲线
        plt.xlabel('False Positive Rate') #坐标轴标签
        plt.ylabel('True Positive Rate') #坐标轴标签
        plt.ylim(0,1.05) #边界范围
        plt.xlim(0,1.05) #边界范围
        plt.legend(loc=4) #图例
        plt.show() #显示作图结果
    elif type == 'real':
        predict_result = net.predict(test[:, 1:input_dim+1]).reshape(len(test))  # 预测结果变形

    if not os.path.exists(neuralOutputPath):
        os.mkdir(neuralOutputPath)
    csvfile = file(neuralOutputPath + 'resultPredict' + indicator + '.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(predict_result)
    csvfile.close()