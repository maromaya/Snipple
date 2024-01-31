import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
import lightgbm as lgb

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
    return model

    # Predicting the Target variable
    # pred = model.predict(data_test)
    # print(pred)
    # accuracy = model.score(data_test, y_test)
    # print(accuracy)


data = pd.read_csv("MOCK_DATA (18).csv")
y_alpha = pd.read_csv("alpha_label.csv")
y_alpha = np.ravel(y_alpha)
y_H = pd.read_csv("H_label.csv")
y_H = np.ravel(y_H)
modelAlpha =lightGBM(data, y_alpha)
modelH =lightGBM(data, y_H)

modelAlpha.booster_.save_model("modelAlpha.txt")
modelH.booster_.save_model("modelH.txt")


