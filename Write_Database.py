import logging

import Speedometer
import LCD
import time
# import HallSensor
#import Application
from dbconn import DbConnection
#logging.basicConfig(level=logging.DEBUG)

#sessie_tijden = Application.tijden_sessie

#einde_sessie = Application.einde_sessie

def schrijf_sessie():

        db = DbConnection('speedometerdb')

        # sql = (
        #      'INSERT INTO Sessie ("Begin", "Einde") '
        #      'VALUES ( %(new_begin)s, %(new_einde)s, %(new_SnelheidsmeterGebruikerID)s );'
        #  )
        # params = {
        #      'new_begin': sessie_tijden[0],
        #      'new_einde': sessie_tijden[1],
        #      'new_SnelheidsmeterGebruikerID': 1
        #  }

        sql = (
            'INSERT INTO Sessie (ID, Begin, Einde, SnelheidsmeterGebruikerID) '
            'VALUES ( %(new_id)s ,%(new_begin)s, %(new_einde)s, %(new_SnelheidsmeterGebruikerID)s );'
         )

        params = {
             'new_id': 2,
             'new_begin': "",
             'new_einde':  "",
             'new_SnelheidsmeterGebruikerID': 1
         }

        db.execute(sql, params)


schrijf_sessie()





