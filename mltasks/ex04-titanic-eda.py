import pandas as pd
from urllib.request import urlopen
from io import StringIO
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, r2_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np
titanic_csv = ""

with urlopen("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv") as a:
	titanic_csv = a.fp.read().decode("utf-8")

df = pd.read_csv(StringIO(titanic_csv))
df = df.drop("Name", axis=1)
df = df.drop("Ticket", axis=1)
df = df.drop("Cabin",axis=1)
df = pd.get_dummies(df, columns=["Sex"], drop_first=True)
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

# EDA
class_dist = df[df["Survived"] == 1].groupby("Pclass").size()
print(class_dist)

sex_dist = df[df["Survived"] == 1].groupby("Sex").size()
print(sex_dist)

print(df.describe())
print("missing", df.isnull().mean() * 100)


from sklearn.model_selection import train_test_split

#for i in df.iterrows():
#	print(i)
X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



pipe = Pipeline(steps = [ 
	("imputer", SimpleImputer()),
	("scaler", StandardScaler() ),
	("model", LogisticRegression() )
])

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

acs = accuracy_score(y_test, y_pred)

cnf = confusion_matrix(y_test, y_pred)
prcs = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(acs, cnf, prcs, recall, f1)
