from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt

housing = pd.read_csv("datasets/housing/housing.csv")
print(housing.head)
print(housing.info())
print(housing["ocean_proximity"].value_counts())
print(housing.describe())



housing.hist(bins=50, figsize=(12, 8))
plt.show()

import numpy as np

def shuffle_and_split_data(data, test_ratio):
	shuffled_indices = np.random.permutation(len(data))
	test_set_size = int(len(data) * test_ratio)
	test_indices = shuffled_indices[:test_set_size]
	train_indices = shuffled_indices[test_set_size:]
	return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = shuffle_and_split_data(housing, 0.2)
print(len(train_set))
print(len(test_set))
