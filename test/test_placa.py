from sys import platform
if "win" in platform:
    from ..placa.Placa import Placa
else:
    from placa.Placa import Placa

import pytest

class TestPlaca:

    def setup(self):
        self.placa = Placa("POM-561")

    def test_new_placa(self):
        assert self.placa.identifier ==  "POM-561"
        assert self.placa.color == 'white'
        assert self.placa.type == 'PARTICULAR' 
        #raise NotImplementedError('Not implemented yet') 

    
    def test_invalid_placa(self):
        with pytest.raises(AttributeError):
            new_placa = Placa("ASDFSDF-855")

        #raise NotImplementedError('Not implemented yet') 
    def test_GAD_placa(self):
        gad_placa = Placa('AMC-0123')
        assert gad_placa.type == 'GAD'
        assert gad_placa.color == 'green'

    def test_international_placa(self):
        international_plca = Placa("CD-0123")
        assert international_plca.type == 'INTERNACIONAL'
        assert international_plca.color == 'blue'
        #raise NotImplementedError('Not implemented yet') 
    
    def test_temporary_international(self):
        international_plca = Placa("IT-0123")
        assert international_plca.type == 'INTERNACIONAL'
        assert international_plca.color == 'red'

    def test_invalid_international_placa(self):
        with pytest.raises(AttributeError):
            new_placa = Placa("AZ-987S")
        


