import button
import LCD
import datetime
import time
#import threading
import dbconn

tijden_sessie = []

deel_sessie = []
deel_sessies = []

parameter1 = 0
parameter2 = 0


start_sessie = 0
einde_sessie = 0

huidige_afstand = 0
total_distance = 0
stop = 0

def opslaan_deelsessies():

    import HallSensor

    global start, stop, huidige_afstand, total_distance

    #threading.Timer(60.0, opslaan_deelsessies).start()

    stop = datetime.datetime.now()
    total_distance = HallSensor.totale_afstand
    afgelegde_afstand = total_distance - huidige_afstand

    start = datetime.datetime.now() - datetime.timedelta(seconds=60)

    start = start.strftime('%H:%M:%S')
    stop = stop.strftime('%H:%M:%S')


    deel_sessies.append([start, stop, afgelegde_afstand])

    huidige_afstand = total_distance




def write_deelsessies():


    deel_sessies.remove(deel_sessies[0])

    db = dbconn.DbConnection()

    sql1 = ('SELECT ID from Sessie ORDER BY ID DESC LIMIT 1')

    SessieID = db.query(sql1)

    for deelsessie in deel_sessies:

        sql2 = (
            'INSERT INTO Deelsessie (Begintijd, Eindtijd, Afstand, SessieID) '
            'VALUES ( %(new_begin)s, %(new_einde)s, %(new_afstand)s ,%(new_SessieID)s );'
        )



        params2 = {
            'new_begin': deelsessie[0],
            'new_einde': deelsessie[1],
            'new_afstand': deelsessie[2],
            'new_SessieID': SessieID[0][0]
        }

        db.execute(sql2, params2)

    for deelsessie in deel_sessies:
        deel_sessies.remove(deelsessie)


def write_sessie():
    db = dbconn.DbConnection()

    sql1 = ('SELECT ID from SnelheidsmeterGebruiker ORDER BY ID DESC LIMIT 1')

    snelheidsmeterGebruikerID = db.query(sql1)

    print(snelheidsmeterGebruikerID)

    sql2 = (
        'INSERT INTO Sessie (Begin, Einde, SnelheidsmeterGebruikerID) '
        'VALUES ( %(new_begin)s, %(new_einde)s, %(new_SnelheidsmeterGebruikerID)s );'
    )

    params2 = {
        'new_begin': tijden_sessie[0],
        'new_einde': tijden_sessie[1],
        'new_SnelheidsmeterGebruikerID': snelheidsmeterGebruikerID[0][0]
    }

    db.execute(sql2, params2)

    tijden_sessie.remove(tijden_sessie[0])
    tijden_sessie.remove(tijden_sessie[0])


while True:


    wissel = button.wissel

    if wissel == 0:
        LCD.write('Begin een sessie', '', '', '')

    if wissel == 1:

        if(parameter1 == 0):
                start_sessie = int(str(datetime.datetime.now())[17:19])
                start_sessie_voor_lijst = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                tijden_sessie.append(start_sessie_voor_lijst)

        parameter1 += 0.000000000000000000000001

        nu = int(str(datetime.datetime.now())[17:19]) #14:16 voor minutes

        if(nu == start_sessie+ 2 ):
              print('test')
              #opslaan_deelsessies()

        start_sessie = nu




        import HallSensor

        snelheid = '{0} km/u'.format(HallSensor.snelheid)

        totale_afstand = '{0} km'.format(HallSensor.totale_afstand)

        LCD.write('----SPEEDOMETER-----', snelheid, totale_afstand, time.ctime(int(time.time())))
        time.sleep(1)

    if wissel == 2:
        einde_sessie = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tijden_sessie.append(einde_sessie)

        LCD.write('Einde sessie', '', '', '')

        write_sessie()
        #print(tijden_sessie)
        #write_deelsessies()
        parameter1 = 0
        time.sleep(3)


