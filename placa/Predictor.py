"""
    the rules are based on: https://ecuador.seguros123.com/todo-lo-que-debes-saber-del-famoso-pico-y-placa/
    
"""

from datetime import datetime, time
import calendar


morning_start_time = time(7,0)
morning_end_time = time(9,30)

evening_start_time = time(16,0)
evening_end_time = time(19,30)
can_drive_msg = "Your vehicle can be on the road"
cant_drive_msg = "Your vehicle must not be on the road"

restricted_digits_perday = {
    "Monday": ["1","2"],
    "Tuesday": ["3","4"],
    "Wednesday": ["5","6"],
    "Thursday": ["7","8"],
    "Friday": ["9","0"]
}



        



class PicoPlacaPredictor:
    """
        Singleton of PicoPlacaPredictor to use just one instance of the predictor. 
    """
    __instance = None 

    @staticmethod
    def get_instance():
        if PicoPlacaPredictor.__instance == None:
            return PicoPlacaPredictor()
        return PicoPlacaPredictor.__instance

    def __init__(self):
        if PicoPlacaPredictor.__instance != None:
            raise Exception("This class is a singleton")
        else:
            PicoPlacaPredictor.__instance = self 

    def __is_outside_of_time_restriction(self, time) -> bool:
        return (time<morning_start_time) or (time>morning_end_time and time<evening_start_time) or (time>evening_end_time)
    
    def predict(self,placa, date, time) -> str:
        driving_datetime = datetime.strptime(f"{date} {time}:00", "%d/%m/%Y %H:%M")
       # cls.strategy = MondayStrategy()
      
        
        day_name = calendar.day_name[driving_datetime.weekday()] 
        time_obj = driving_datetime.time()
      
        if self.__is_outside_of_time_restriction(time_obj):            
            return can_drive_msg  

        last_digit = placa.get_last_digit()
        
        today_restricted_digits = restricted_digits_perday[day_name]
       
        if last_digit in today_restricted_digits:
            return cant_drive_msg
        return can_drive_msg
     






        #raise NotImplementedError('Not implemented yet')




# %%

