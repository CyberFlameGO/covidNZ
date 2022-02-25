# -*- coding: utf-8 -*-
"""
ML model for predicting NZ COVID cases
"""

import matplotlib as plt
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


if __name__ == '__main__':
    main()
