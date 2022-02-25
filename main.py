# -*- coding: utf-8 -*-
"""
ML model for predicting NZ COVID cases
"""

import matplotlib.pyplot as plt
import pandas as pd
# import tensorflow as tf
# from tensorflow import keras
import numpy as np


def main():
    """
    Main function
    """
    df = pd.read_csv('covid.csv', usecols=[1])
    dataset = df.values
    dataset = df.astype('float32')
    plt.plot(dataset)
    plt.show()

    train_size = int(len(dataset) * 0.67)
    test_size = len(dataset) - train_size
    train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
    print(len(train), len(test))


if __name__ == '__main__':
    main()
