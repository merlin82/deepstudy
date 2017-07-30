# -*- coding: UTF-8 -*-
from Network2 import Network
from datetime import datetime

def loadData(file):
    data = []
    label = []
    fin = open(file,'r')
    while 1:
        line = fin.readline()
        if not line:
            break
        tokens = line.strip().split()
        fea = []
        try:
            lab = float(tokens[-1])
            for i in range(0,len(tokens)-1,1):
                value = float(tokens[i])
                fea.append(value)
        except:
            continue

        if lab == 1:
            label.append([0,1])
        else:
            label.append([1, 0])
        data.append(fea)
    return data,label

def get_training_data_set():
    return loadData('train_data')

def get_test_data_set():
    return loadData('test_data')

def get_result(vec):
    max_value_index = 0
    max_value = 0
    for i in range(len(vec)):
        if vec[i] > max_value:
            max_value = vec[i]
            max_value_index = i
    return max_value_index

def evaluate(network, test_data_set, test_labels):
    error = 0
    total = len(test_data_set)
    for i in range(total):
        label = get_result(test_labels[i])
        predict = get_result(network.predict(test_data_set[i]))

        if label != predict:
            error += 1
    return float(error) / float(total)

def train_and_evaluate():
    last_error_ratio = 1.0
    epoch = 0
    train_data_set, train_labels = get_training_data_set()
    test_data_set, test_labels = get_test_data_set()
    network = Network([2, 2, 2])
    while True:
        epoch += 1
        network.train(train_labels, train_data_set, 0.1, 1)
        print '%s epoch %d finished' % (datetime.now(), epoch)
        if epoch % 10 == 0:
            error_ratio = evaluate(network, test_data_set, test_labels)
            print '%s after epoch %d, error ratio is %f' % (datetime.now(), epoch, error_ratio)
            if error_ratio >= last_error_ratio:
                break
            else:
                last_error_ratio = error_ratio

if __name__ == '__main__':
    train_and_evaluate()
