import argparse
import temp
import discomfort
import window
from loadData import results_dic 


def main():
    parser = argparse.ArgumentParser(
        description="Un programme qui exécute plusieurs fonctions avec des paramètres."
    )
    
    subparsers = parser.add_subparsers(dest="fonction", help="Choisissez une fonction à exécuter")
    
    parser_dis = subparsers.add_parser("discomfort", help="Dit si une salle est en situation d'inconfort")
    
    parser_window = subparsers.add_parser("window", help="Dit si la fenêtre d'une salle est ouverte (salle par défaut : salle de pause tétras)")
    parser_window.add_argument("--sensors", type=dict, help='''Dictionnaire sous la forme {"co2" : <capteur de co2 de la salle>,"voc" : <capteur de voc de la salle>,"temp" : <capteur de température de la salle>}''', default={
    "co2": results_dic['9_in_1_multi_sensor_carbon_dioxide_co2_level'],
    "voc" : results_dic['9_in_1_multi_sensor_volatile_organic_compound_level'],
    "temp" : results_dic['9_in_1_multi_sensor_air_temperature']})
    
    parser_temp_regress = subparsers.add_parser("regress", help="Regression linéaire de la température")
    parser_temp_regress.add_argument("--time", type=int, default=20, help="Temps en minutes de la prédiction (20 par défaut)")
    parser_temp_regress.add_argument("--sensor", type=str, default="9_in_1_multi_sensor_air_temperature", help="Capteur de température à récupérer pour la regression (salle de pause de tétras par défaut)")
    
    parser_temp_pred = subparsers.add_parser("predict", help="Prédiction de la température future sur un temps donné")
    parser_temp_pred.add_argument("--time", type=int, default=20, help="Temps en minutes de la prédiction (20 par défaut)")
    parser_temp_pred.add_argument("--sensor", type=str, default="9_in_1_multi_sensor_air_temperature", help="Capteur de température à récupérer pour la regression (salle de pause de tétras par défaut)")
    
    
    args = parser.parse_args()
    
    if args.fonction == "discomfort":
        print(discomfort.discomfort())
    elif args.fonction == "window":
        print(window.clustering_window())
    elif args.fonction == "regress":
        print(temp.regression_temp(args.time, sensor_id=args.sensor))
    elif args.fonction == "predict":
        print(temp.prediction_temp(args.time, sensor_id=args.sensor))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()