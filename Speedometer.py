from flask import Flask, request
from flask import render_template
import os
import dbconn


#from DbClass import DbClass

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/speedometer', methods= ['POST', 'GET'])

def speedometer():

    comment = ""

    if request.method == 'POST':

        comment = "Het werd verzonden"

        result = request.form
        if(result['naam'] != ""):

            naam = result['naam']
        else:
            naam = "Default"

        if(result['voornaam'] != ""):
            voornaam= result['voornaam']
        else:
            voornaam = "Default"

        if(result['leeftijd'] != ""):
            leeftijd = result['leeftijd']
        else:
            leeftijd = 69

        if(result['diameter wiel'] != ""):
            diameter = result['diameter wiel']
        else:
            diameter = 100

        print(result)

        db = dbconn.DbConnection()

        sql1 = (
            'INSERT INTO Gebruiker (Naam, Voornaam, Leeftijd, DiameterWiel) '
            'VALUES ( %(new_Naam)s, %(new_Voornaam)s, %(new_Leeftijd)s, %(new_Diameter)s );'
        )

        params1 = {
            'new_Naam': naam,
            'new_Voornaam': voornaam,
            'new_Leeftijd': leeftijd,
            'new_Diameter': diameter
        }

        db.execute(sql1, params1)

        sql2 = ('SELECT ID from Gebruiker ORDER BY ID DESC LIMIT 1')

        gebruikerID = db.query(sql2)
        print(gebruikerID)

        sql3 = ('SELECT ID from Snelheidsmeter ORDER BY ID DESC LIMIT 1')

        snelheidsmeterID = db.query(sql3)
        print(snelheidsmeterID)

        sql4 = ('INSERT INTO SnelheidsmeterGebruiker (SnelheidsmeterID, GebruikerID)  '
            'VALUES ( %(new_snelheidsmeterid)s, %(new_gebruikerid)s );')

        params2 = {
            'new_snelheidsmeterid': snelheidsmeterID[0][0],
            'new_gebruikerid': gebruikerID[0][0],

        }

        db.execute(sql4,params2)



    return render_template('speedometer.html', comment = comment)

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':

    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0',port=8080, debug=True)







