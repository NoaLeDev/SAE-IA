from loadData import results_dic
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import dfparse 


result = {
    "co2": results_dic['9_in_1_multi_sensor_carbon_dioxide_co2_level'],
    "voc" : results_dic['9_in_1_multi_sensor_volatile_organic_compound_level'],
    "temp" : results_dic['9_in_1_multi_sensor_air_temperature']
}

def clustering_window(sensors=result):
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
        return False
    else :
        return True 

print(clustering_window())