#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
names = (
    "Class",
    "Alcohol",
    "Malic acid",
    "Ash",
    "Alcalinity of ash",
    "Magnesium",
    "Total phenols",
    "Flavanoids",
    "Nonflavanoid phenols",
    "Proanthocyanins",
    "Color intensity",
    "Hue",
    "OD280/OD315 of diluted wines",
    "Proline"
    )
dataset = pd.read_csv(url, names=names, delimiter=',')
dataset.info()

#%%
x = dataset.drop(["Class"], axis=1) # axis=1 berarti kolom, axis-0 berarti row
y = dataset["Class"]

print(dataset.shape)
print(x.shape)
print(y.shape)

#%%
y = pd.get_dummies(y)
print(y.sample(10))
print(y.shape)

#%%
from sklearn.preprocessing import MinMaxScaler
x = MinMaxScaler().fit_transform(x)
print(x)

#%%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

print(f"x_train : {x_train.shape}")
print(f"x_test : {x_test.shape}")
print(f"y_train : {y_train.shape}")
print(f"y_test : {y_test.shape}")
#%%
corr = pd.concat([pd.DataFrame(x), pd.DataFrame(y)], axis=1, sort=False)
corr.corr(method='pearson')
#%%
from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(13**2+13, (13**2+13)/2),
                      activation="relu", max_iter=5000, alpha=0.01, verbose=False, solver="sgd")
h = model.fit(x_train, y_train)

#%%
y_test = np.array(y_test)
y_pred = model.predict(x_test)

#%%
from sklearn.metrics import mean_squared_error, classification_report, confusion_matrix, accuracy_score

print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1)))
print(f"Accuracy is : {accuracy_score(y_pred,y_test)}")
plt.plot(h.loss_curve_)
