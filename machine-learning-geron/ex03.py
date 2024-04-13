import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

url = "https://github.com/ageron/data/raw/main/lifesat/lifesat.csv"
lifesat = pd.read_csv(url)
lifesat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.show()

X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

model = KNeighborsRegressor(n_neighbors=3)

model.fit(X,y)
X_new = [[37_655.2]] 
print(model.predict(X_new)) 
