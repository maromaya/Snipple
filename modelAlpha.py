import numpy as np
import pandas as pd
import lightgbm as lgb
from lightgbm import LGBMClassifier

def lightGBM(X, y):
    # Splitting Dataset in two parts
    data_train = X[1:800]
    data_test = X[800:1000]
    y_train = y[1:800]
    y_test = y[800:1000]

    # Creating an object for model and fitting it on training data set
    model = LGBMClassifier()
    model.fit(data_train, y_train)
    pred = model.predict(data_test)
    accuracy = model.score(data_test, y_test)
    print(accuracy)
    return model

    # Predicting the Target variable
    # pred = model.predict(data_test)
    # print(pred)
    # accuracy = model.score(data_test, y_test)
    # print(accuracy)

def getPrediction(x):
    data = pd.read_csv("MOCK_DATA (18).csv")
    y_alpha = pd.read_csv("alpha_label.csv")
    y_alpha = np.ravel(y_alpha)
    model=lightGBM(data, y_alpha)
    x=np.array(x)
    x=x.reshape(1,-1)
    return model.predict(x)

