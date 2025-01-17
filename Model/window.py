import loadData
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import dfparse 


def clustering_window(sensor_co2 = "9_in_1_multi_sensor_carbon_dioxide_co2_level", sensor_voc = "9_in_1_multi_sensor_volatile_organic_compound_level", sensor_temp="9_in_1_multi_sensor_air_temperature"):
    results_dic = loadData.loadDis()

    result = {
        "co2": results_dic[sensor_co2],
        "voc" : results_dic[sensor_voc],
        "temp" : results_dic[sensor_temp]
    }

    df_list = []

    for key, value in result.items():
        df = pd.DataFrame(value, columns = ["time", key])
        df_list.append(df)



    first_merge = pd.merge(left=df_list[0], right=df_list[1], left_on="time", right_on="time")
    final_merge = pd.merge(left=first_merge, right=df_list[2], left_on="time", right_on="time")

    X = final_merge.drop(columns=["time"])

    kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)

    print(kmeans.labels_)
    print(kmeans.cluster_centers_)

    current_value = X.tail(1)

    y = kmeans.predict(current_value)

    if y[0] :
        return "La fenêtre est fermée."
    else :
        return "La fenêtre est ouverte."
