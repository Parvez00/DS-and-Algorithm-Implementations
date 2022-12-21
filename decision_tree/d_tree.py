from __future__ import print_function

import numpy as np
import pandas as pd


header = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality']

data = pd.read_csv("dataset.csv",header=None, names=header)

mylist = data['fixed acidity'].tolist()

print(mylist)


def unique_vals(rows, col):
    """Find the unique values for a column in a dataset."""
    return set([row[col] for row in rows])