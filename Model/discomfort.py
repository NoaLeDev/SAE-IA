import pandas as pd
from loadData import results_dic
import numpy as np

def discomfort(THRESHOLD=2, TEMP_MAX=29, TEMP_MIN = 18, HUMIDITY_MAX = 60, HUMIDITY_MIN = 40, CO2_PPM_MAX = 1000, VOC_PPM_MAX = 0.6, results_dic=results_dic):

    coeff = 0

    if results_dic["9_in_1_multi_sensor_air_temperature"][-1][1] > TEMP_MAX:
        coeff += 1
    elif results_dic["9_in_1_multi_sensor_air_temperature"][-1][1] < TEMP_MIN:
        coeff += 1

    if results_dic["9_in_1_multi_sensor_humidity"][-1][1] > HUMIDITY_MAX:
        coeff += 1
    elif results_dic["9_in_1_multi_sensor_humidity"][-1][1] < HUMIDITY_MIN:
        coeff += 1

    if results_dic["9_in_1_multi_sensor_carbon_dioxide_co2_level"][-1][1] > CO2_PPM_MAX:
        coeff += 1

    if results_dic['9_in_1_multi_sensor_volatile_organic_compound_level'][-1][1] > VOC_PPM_MAX:
        coeff += 1
    
    res = coeff >= THRESHOLD
    if res:
        return "Vous êtes en situation d'inconfort."
    else :
        return "Vous êtes dans une situation confortable."

