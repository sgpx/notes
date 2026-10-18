from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score, accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import GridSearchCV, KFold, cross_val_score

kernels = ('linear', 'poly', 'rbf', 'sigmoid')
ds = load_breast_cancer()
X = ds.data
y = ds.target

p_grid = {"C": [1, 10, 100], "gamma": [0.01, 0.1]}


for kernel in kernels:
	svc1 = SVC(kernel=kernel)
	kf = KFold(n_splits=4, shuffle=True)
	gscv = GridSearchCV(estimator = svc1, param_grid = p_grid, cv = kf)
	pipeline = Pipeline(steps = [("impute", SimpleImputer()), ("scaler", StandardScaler()),   ("classifier", gscv )])
	X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.8)
	pipeline.fit(X=X_train, y=y_train)
	y_pred = pipeline.predict(X_test)       

	acc = accuracy_score(y_pred, y_test)
	f1s = f1_score(y_pred, y_test)
	cnf = confusion_matrix(y_test, y_pred)
	print(kernel, acc, f1s, cnf)
