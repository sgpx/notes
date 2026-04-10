# %%
!pip3 install pandas matplotlib numpy scikit-learn

# %%
import pandas as pd

# %%
import matplotlib.pyplot as plt

# %%
import numpy as np

# %%
housing = pd.read_csv("housing.csv")


# %%
housing.info()

# %%
housing["ocean_proximity"].value_counts()

# %%
housing.hist(bins=50, figsize=(12,8))

# %%
plt.show()


# %%
housing.hist(bins=50, figsize=(12,8))

# %%
np.random.permutation(len(housing))

# %%
from zlib import crc32
crc32(np.int64(1232112))

# %%
housing.reset_index()

# %%
def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio * 2**32

# %%
def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_ : is_id_in_test_set(id_, test_ratio))
    return data.loc[-in_test_set], data.loc[in_test_set]

# %%
housing_with_id = housing.reset_index()

# %%
tr , ts = split_data_with_id_hash(housing_with_id, 0.2, "index")


# %%
housing_with_id

# %%
tr

# %%
ts

# %%
from sklearn.model_selection import train_test_split

# %%
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

# %%
mxicut = pd.cut(housing["median_income"], bins=[0,1.5,3,4.5,6,np.inf], labels=[1,2,3,4,5])

# %%
housing["income_cat"] = mxicut

# %%
mxicut

# %%
mxicut.value_counts()

# %%
mxicut.value_counts().sort_index()

# %%
mxicut.value_counts().sort_index().plot.bar(rot=0, grid=True)

# %%
mxicut.value_counts().sort_index().plot.bar(rot=0, grid=False)

# %%
from sklearn.model_selection import StratifiedShuffleSplit

# %%
splitter = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42)

# %%
strat_splits = []

# %%
mysplit = splitter.split(housing, housing["income_cat"])

# %%
mysplit

# %%
for i in mysplit: print(i)

# %%
mysplit = splitter.split(housing, housing["income_cat"])
for i,j in mysplit: print(i,j)

# %%
mysplit = splitter.split(housing, housing["income_cat"])
for train_index, test_index in mysplit:
    strat_train_set_n = housing.iloc[train_index]
    strat_test_set_n = housing.iloc[test_index]
    strat_splits.append([strat_train_set_n, strat_test_set_n])
strat_train_set, strat_test_set = strat_splits[0]

# %%
strat_train_set, strat_test_set = train_test_split(housing, test_size=0.2, stratify=housing["income_cat"], random_state=42)

# %%
strat_test_set["income_cat"].value_counts() / len(strat_test_set)

# %%
for myset in (strat_train_set, strat_test_set): myset.drop("income_cat", axis=1, inplace=True)

# %%
myset

# %%
help(myset.drop)


# %%
strat_train_set.copy()

# %%
housing.plot(kind="scatter", x="longitude", y="latitude", grid=True)

# %%
from sklearn.model_selection import StratifiedShuffleSplit

housing = pd.read_csv("housing.csv")
housing["income_cat"] = pd.cut(housing["median_income"], bins=[0,1.5,3,4.5,6,np.inf], labels=[1,2,3,4,5])


splitter = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
mysplit = splitter.split(housing, housing["income_cat"])

strat_splits = []
mysplit = splitter.split(housing, housing["income_cat"])
for train_index, test_index in mysplit:
    strat_train_set_n = housing.iloc[train_index].copy()
    strat_test_set_n = housing.iloc[test_index].copy()
    strat_splits.append([strat_train_set_n, strat_test_set_n])
strat_train_set, strat_test_set = strat_splits[0]


for myset in (strat_train_set, strat_test_set):
    myset.drop("income_cat", axis=1, inplace=True)
housing.plot(kind="scatter", x="longitude", y="latitude", grid=True)
housing = housing.drop("ocean_proximity", axis=1)
corr_matrix = housing.corr()
print(corr_matrix["median_house_value"].sort_values(ascending=True))



# %%
from pandas.plotting import scatter_matrix
attributes = ["median_house_value","median_income","total_rooms","housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12,8))
plt.show()

# %%
housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1, grid=True)
plt.show()

# %%



