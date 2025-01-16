from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score
import dfparse as dfp
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from loadData import results_temp
import numpy as np

df = results_temp

def predict_temp(time,df=df,sensor_id="9_in_1_multi_sensor_air_temperature"):
    df = df[df["entity_id"] == sensor_id]  
    dfsw = dfp.DfTimeSeriesSlidingWindow(df,300, time, "value")

    X, y = dfsw.to_matrices()

    X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=1)

    regr = MLPRegressor(random_state=1,max_iter=50000, activation="relu", hidden_layer_sizes=(2048, 1024,)).fit(X_train, y_train)

    y_pred = regr.predict(X_test[:3])[0]

    print(y_pred)
    plt.plot(y_test, c="red")
    plt.plot(y_pred, c="blue", label="température prédite")
    plt.show()
    
    

predict_temp(20)