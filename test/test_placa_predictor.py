import pytest
from ..placa.Placa import Placa

from ..placa.Predictor import PicoPlacaPredictor 


class TestPlacaPredictor():

    def setup(self):
        self.predictor = PicoPlacaPredictor.get_instance()

    def test_monday_pico_placa(self):
        """
        Test wether or not a vehicle should be on the road on monday at 8 o'clock
        11 am, and 17 pm.
        """
        placa1 = Placa("AUB-5981") 
        prediction1 = self.predictor.predict(placa1,"23/05/2022",8)
        
        placa2 = Placa("GTU-9871")
        prediction2 = self.predictor.predict(placa2,"16/05/2022",11)

        placa3 = Placa("LUO-8542")
        prediction3 = self.predictor.predict(placa3,'16/05/2022',17,)

        placa4 = Placa("MYN-5876")
        prediction4 = self.predictor.predict(placa4,"23/05/2022",8)

        assert prediction1 == 'Your vehicle must not be on the road'
        assert prediction2 == 'Your vehicle can be on the road'
        assert prediction3 == 'Your vehicle must not be on the road'   
        assert prediction4 == 'Your vehicle can be on the road'


    def test_tuesday_pico_placa(self):
        """
        Test wether or not a vehicle should be on the road on tuesday at 8 o'clock
        11 am, and 17 pm.
        """
        placa1 = Placa("AUB-593") 
        prediction1 = self.predictor.predict(placa1,"24/05/2022",8)
        
        placa2 = Placa("GTU-9873")
        prediction2 = self.predictor.predict(placa2,"17/05/2022",11)

        placa3 = Placa("LUO-8544")
        prediction3 = self.predictor.predict(placa3,'17/05/2022',17)

        placa4 = Placa("MYN-5876")
        prediction4 = self.predictor.predict(placa4, "24/05/2022",8)

        assert prediction1 == 'Your vehicle must not be on the road'
        assert prediction2 == 'Your vehicle can be on the road'
        assert prediction3 == 'Your vehicle must not be on the road'   
        assert prediction4 == 'Your vehicle can be on the road'


    def test_wednesday_pico_placa(self):
        """
        Test wether or not a vehicle should be on the road on wednesday at 8 o'clock
        11 am, and 17 pm.
        """
        placa1 = Placa("AUB-595") 
        prediction1 = self.predictor.predict(placa1,"25/05/2022",8)
        
        placa2 = Placa("GTU-9875")
        prediction2 = self.predictor.predict(placa2,"18/05/2022",11)

        placa3 = Placa("LUO-8546")
        prediction3 = self.predictor.predict(placa3,'18/05/2022',17)

        placa4 = Placa("MYN-5879")
        prediction4 = self.predictor.predict(placa4, "25/05/2022",8)

        assert prediction1 == 'Your vehicle must not be on the road'
        assert prediction2 == 'Your vehicle can be on the road'
        assert prediction3 == 'Your vehicle must not be on the road'   
        assert prediction4 == 'Your vehicle can be on the road'

    def test_thursday_pico_placa(self):
        """
        Test wether or not a vehicle should be on the road on thursday at 8 o'clock
        11 am, and 17 pm.
        """
        placa1 = Placa("AUB-597") 
        prediction1 = self.predictor.predict(placa1,"26/05/2022",8)
        
        placa2 = Placa("GTU-9878")
        prediction2 = self.predictor.predict(placa2,"19/05/2022",11)

        placa3 = Placa("LUO-8547")
        prediction3 = self.predictor.predict(placa3,'19/05/2022',17)

        placa4 = Placa("MYN-5871")
        prediction4 = self.predictor.predict(placa4, "26/05/2022",8)

        assert prediction1 == 'Your vehicle must not be on the road'
        assert prediction2 == 'Your vehicle can be on the road'
        assert prediction3 == 'Your vehicle must not be on the road'   
        assert prediction4 == 'Your vehicle can be on the road'



    def test_friday_pico_placa(self):
        """
        Test wether or not a vehicle should be on the road on thursday at 8 o'clock
        11 am, and 17 pm.
        """
        placa1 = Placa("AUB-599") 
        prediction1 = self.predictor.predict(placa1,"27/05/2022",8)
        
        placa2 = Placa("GTU-9879")
        prediction2 = self.predictor.predict(placa2,"20/05/2022",11)

        placa3 = Placa("LUO-8540")
        prediction3 = self.predictor.predict(placa3,'20/05/2022',17)

        placa4 = Placa("MYN-5871")
        prediction4 = self.predictor.predict(placa4,"27/05/2022",8)

        assert prediction1 == 'Your vehicle must not be on the road'
        assert prediction2 == 'Your vehicle can be on the road'
        assert prediction3 == 'Your vehicle must not be on the road'   
        assert prediction4 == 'Your vehicle can be on the road'