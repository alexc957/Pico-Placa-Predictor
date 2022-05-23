# Pico y Placa predictor
This program can predict whether or not a car can be on the road based on the past pico y placa [restrictions](httphttps://ecuador.seguros123.com/todo-lo-que-debes-saber-del-famoso-pico-y-placa/:// "restrictions").

according to the pico y placa we have the following rules:
- schedule:
      - morning: 7:00 - 9:30.
      - evening: 16:00 - 19:30.

- based on the schedule, cars with the following last digit on the placa cannot be on the road:
      - Monday: 1 and 2.
      - Tuesday: 3 and 4
      - Wednesday: 5 and 6.
      - Thursday: 7 and 8.
      - Friday: 9 and 0.

### requirements
  - python 3.7+.
  - pytest
  - pip.

### Project structure
* placa/: has the following clases:
	* Placa: represents instances of placas and validates them according to the ecuadorian law. 
	PicoPlacaPredictor: the class that helps us to predict whether or not the vehicle can be on the road based on the pico y placa rules.
	
* tests/: has the tests suites for both the Placa class and the PicoPlacaPredictor.
* requirements.txt: a list of python modules required by the program.
* README.md: self explanatory. 


### Installation and usage 

1. clone the repository.
2. create a virtual enviroment (optional).
3. run `pip install -r requirements.py` 
4. run `python main.py -h` for more detal instructions as shown below.
5. basic usage: `python main.py placa date time` where:
	* placa: is the string representing the placa number (MUP-8581).
	* date: a string that represents the date. 
	* time: an integer that represents the hour when the driver wants to be outside.
6. To run the tests just run: `pytest`. 

```bash
usage: python main.py placa date time

Predict wether or not a vehicle has pico y placa restrictions given the placa,
a date string and integer representing the hour

positional arguments:
  p           the placa identifier: example AUB-5651
  d           A date string in the format dd/mm/YYYY
  t           An Intenger representing the hour when the vehicle is on the
              road, it has to be betwee 0 and 23

optional arguments:
  -h, --help  show this help message and exit

```

### Example 
#### vehicle can be on the road
```cmd
D:\Projects\pythonProjects\picoPlacaPredictor>python main.py AUB-5981 23/06/2022 8
Your vehicle can be on the road

```

#### vehicle can't be on the road
```cmd
D:\Projects\pythonProjects\picoPlacaPredictor>python main.py LUO-8544 17/05/2022 8  
Your vehicle must not be on the road
```

Note: do not use python2.