from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

target_names = iris.target_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

pipeline = Pipeline(
    steps=[("scaler", StandardScaler()), ("classifier", DecisionTreeClassifier())]
)

pipeline.fit(X=X_train, y=y_train)
y_pred = pipeline.predict(X=X_test)

from sklearn.metrics import r2_score, accuracy_score

acc = accuracy_score(y_pred=y_pred, y_true=y_test)
print(acc)
