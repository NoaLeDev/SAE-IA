from influxdb_client import InfluxDBClient, Point
import pandas as pd

# InfluxDB Configuration
# INFLUXDB_URL = "http://10.103.101.127:8086/"
INFLUXDB_URL = "http://51.83.36.122:8086/"
#INFLUXDB_URL = "http://10.103.1.44:5003/ "
# INFLUXDB_TOKEN = "khzRozF_2KQaxcE7b0dU0SuR17Did9cclTTvcFv6ZCLhb_IFhddl8igzCs3YGQgUQj1FNLHcwNqvAGsEvn7W_g=="
INFLUXDB_TOKEN = "V5_uV4fxRIfcTbkek-HqftjwxxYsbh76t8p_j9_9b6bL0DYTv4rqoxOfj7Ng3gfnmkuYIk3in1pAbDUjomvzAw=="
#INFLUXDB_TOKEN = "IHZveuksmZNqpWjiUPELnbZFkjrkdOWLbTRgv4nS6zl43KRPUQvfVR_vw_yMV-vUL6O4Ckz2o1PI5mCcSaNE3A=="
# ORG = "SAE de Zinzin"
ORG = "IUT-INFO"
#ORG = "DomoCorp"
# BUCKET = "SAEdeZinzin"
BUCKET = "groupe4"
#BUCKET = "HA_Bucket"

client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=ORG, timeout=120_000)

query_api = client.query_api()

def loadTemp(query_api = query_api, ORG=ORG, BUCKET=BUCKET, time='''-10d'''):
    query_temp = f'''from(bucket: "{BUCKET}")
    |> range (start: {time})
    |> filter(fn:  (r) => r._measurement == "°C")
    |> filter(fn:  (r) => r._field == "value")
    |> truncateTimeColumn(unit: 1m)
    |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")'''
    
    return query_api.query_data_frame(query_temp, ORG)


def loadDis(query_api = query_api, ORG=ORG, BUCKET=BUCKET, time='''-10d'''):
    query_discomfort = f'''from(bucket: "{BUCKET}")
    |> range (start: {time})
    |> truncateTimeColumn(unit: 1m)
    |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")'''

    results_list = query_api.query(query_discomfort).to_values(columns=['entity_id', '_time', 'value'])

    results_dic = {}

    for _id, time, value in results_list:
        if _id not in results_dic:
            results_dic[_id] = []
        
        results_dic[_id].append((time, value))

    return results_dic
