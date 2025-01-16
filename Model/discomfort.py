import pandas as pd
from loadData import results_dic
import numpy as np


def discomfort(THRESHOLD=2, TEMP_MAX=29, TEMP_MIN = 18, HUMIDITY_MAX = 60, HUMIDITY_MIN = 40, CO2_PPM_MAX = 1000, VOC_PPM_MAX = 0.6, results_dic=results_dic, sensor_id="9_in_1_multi_sensor_air_temperature"):

    coeff = 0

    if results_dic[sensor_id][-1][1] > TEMP_MAX:
        coeff += 1
    elif results_dic[sensor_id][-1][1] < TEMP_MIN:
        coeff += 1

    if results_dic[sensor_id][-1][1] > HUMIDITY_MAX:
        coeff += 1
    elif results_dic[sensor_id][-1][1] < HUMIDITY_MIN:
        coeff += 1

    if results_dic[sensor_id][-1][1] > CO2_PPM_MAX:
        coeff += 1

    if results_dic[sensor_id][-1][1] > VOC_PPM_MAX:
        coeff += 1
    
    return coeff >= THRESHOLD

