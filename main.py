import argparse
from placa.Placa import Placa
from placa.Predictor import PicoPlacaPredictor
from matplotlib.style import use




parser = argparse.ArgumentParser(
    description='Predict wether or not a vehicle has pico y placa restrictions given the placa, a date string and integer representing the hour ',
    usage="python main.py placa date time")

parser.add_argument("placa", metavar='p',type=str,help="the placa identifier: example AUB-5651",)
parser.add_argument("date", metavar='d',type=str, help="A date string in the format dd/mm/YYYY")
parser.add_argument("time", metavar='t', type=int, help="An Intenger representing the hour when the vehicle is on the road, it has to be betwee 0 and 23")

if __name__ =='__main__':
    args = parser.parse_args()
   
    placa = Placa(args.placa)
    date = args.date 
    time = args.time 
    predictor = PicoPlacaPredictor.get_instance()
    print(predictor.predict(placa,date,time)) 
    #print("arguments", args)
    