from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score, f1_score, confusion_matrix
wine = load_wine()

y = wine.target

X = wine.data


for kval in range(3,10):
   pipeline = Pipeline(steps = [
	("scaler", StandardScaler() ),
	("model", KNeighborsClassifier(n_neighbors = 3) )
])

   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

   pipeline.fit(X_train, y_train)
   y_pred = pipeline.predict(X_test)
   print("k =",kval)
   print("accuracy_score", accuracy_score(y_test, y_pred))
   print("r2_score", r2_score(y_test, y_pred))
   print("f1_score", f1_score(y_test, y_pred, average='weighted'))
   print("confusion_matrix", confusion_matrix(y_test, y_pred))
   print("===")
