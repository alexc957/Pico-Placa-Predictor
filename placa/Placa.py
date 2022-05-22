import re


placa_regex = r"^(A|B|U|C|H|X|O|E|W|G|I|L|R|M|V|N|Q|S|P|Y|J|K|T|Z)[A-Z]{2}-\d{2,3}"
international_placa_regex = r"^(CC|CD|OI|AT|IT)-\d{4}"

class Placa():

    def __init__(self, identifier):
        
        if not self.__valitate_placa_identifier(identifier):
            raise AttributeError("Invalid placa identifier provided")
        self._identifier = identifier
        self._type = self.__get_placa_type()
        print('type ', self._type)
        self._color = self.__get_placa_color()
        

    @property
    def identifier(self):
        return self._identifier

    

    @property
    def color(self):
        return self._color

    @property 
    def type(self):
        return self._type

    def __valitate_placa_identifier(self, identifier):
        """validate if the given placa identifier it is valid or not
         - args: 
            - identifier: the placa number: ie AEB-456
        """
        
        general_placa_match = re.search(placa_regex,identifier)
        international_placa_match = re.search(international_placa_regex, identifier)
        return general_placa_match is not None or international_placa_match is not None
        
    def __get_placa_type(self):
        second_letter = self.identifier[1]
        if second_letter in ['A','U','Z']:
            return "COMERCIAL"
        if second_letter == 'E':
            return 'GUBERNAMENTAL'
        if second_letter =='X':
            return 'USO OFICIAL'
        if second_letter == 'M':
            return 'GAD'
        if re.search(international_placa_regex, self.identifier):
            return 'INTERNACIONAL'
        return 'PARTICULAR'

    def __get_placa_color(self):
        if self.type == 'COMERCIAL':
            return 'orange'
        if self.type in ['GUBERNAMENTAL','USO OFICIAL']:
            return 'gold'

        if self.type == 'GAD':
            return 'green'
        if self.type == 'PARTICULAR':
            return 'white'
        
        if self.identifier.startswith('IT'):
            return 'red'
        return 'blue'
