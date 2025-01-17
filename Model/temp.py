from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score
import dfparse as dfp
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from loadData import results_temp
import numpy as np
from prophet import Prophet 
import datetime as dt

df = results_temp

def remove_tz(x):
    return pd.to_datetime(x)
     
def round_temp(x):
    return round(x,3)


def regression_temp(time,df=df,sensor_id="9_in_1_multi_sensor_air_temperature"):
    df = df[df["entity_id"] == sensor_id]  
    dfsw = dfp.DfTimeSeriesSlidingWindow(df,100, time, "value")

    X, y = dfsw.to_matrices()

    X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=1)

    regr = MLPRegressor(random_state=1,max_iter=50000, activation="relu", hidden_layer_sizes=(2048, 1024,)).fit(X_train, y_train)

    y_pred = regr.predict(X_test[:3])[0]
    
    plt.plot(y_test[0], c="red", label="température réelle")
    plt.plot(y_pred, c="blue", label="température prédite")
    plt.legend()
    plt.title("Prédiction de température")
    plt.ylabel("Température (en °C)")
    plt.xlabel("Temps (en minutes)")
    plt.show()
    
# regression_temp(20)

def prediction_temp(time, df=df, sensor_id="9_in_1_multi_sensor_air_temperature"):
    df = df[df["entity_id"] == sensor_id]  
    df = df[["_time", "value"]]
    df = df.rename(columns={"_time" : "ds", "value" : "y"})
    
    ds = df["ds"].apply(remove_tz)
    
    df["ds"] = ds.dt.tz_localize(None)
    
    model = Prophet()
    model.fit(df)
    
    future = model.make_future_dataframe(periods=365, freq='1min')
    
    pred = model.predict(future)
    pred = pred[["ds","yhat"]]
    
    current_time = dt.datetime.now(tz=None)
    future_time = current_time + dt.timedelta(minutes=time)
    
    pred = pred[pred["ds"] >= current_time]
    pred = pred[pred["ds"] <= future_time]
    
    pred["yhat"] = pred["yhat"].apply(round_temp)
    
    plt.plot(pred["ds"], pred["yhat"], c="red", label="température prédite")
    plt.title("Prédiction de température")
    plt.ylabel("Température (en °C)")
    plt.xlabel("Jour avec heures et minutess (DD HH:MM)")
    plt.show()

# prediction_temp(40)