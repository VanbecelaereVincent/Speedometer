from flask import Flask, request, redirect, url_for
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

    nieuwe_datums = []


    index = 0

    datums = get_sessies_datums()

    print(datums)

    for datum in datums:
        lijst = []
        nieuwe_datum = datum[0].strftime('%Y-%m-%d')
        lijst.append(nieuwe_datum)
        lijst.append(index)
        lijst.append(0)
        print(lijst)
        nieuwe_datums.append(lijst)
        index += 1


    print(nieuwe_datums)

    comment = ""

    if request.method == 'POST':

        comment = "Het formulier werd reeds verzonden"

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



    return render_template('speedometer.html', comment = comment, nieuwe_datums = nieuwe_datums, datums = datums)


@app.route('/speedometerchart', methods= ['POST', 'GET'])

def speedometerchart():


    if request.method == 'POST':

        try:
            result = request.form
            datum = result['selected']
            print(result)
        except:
            return redirect(url_for('speedometer'))

        db = dbconn.DbConnection()


        sql1 = ('select DS.Eindtijd , DS.Afstand, cast(S.Einde as date) from Deelsessie as DS LEFT join Sessie as S on DS.SessieID = S.ID')



        try:
            resultaten = db.query(sql1)
            print(resultaten)

            print(resultaten[0][0])
            print(resultaten[0][2])


            datas = []
            datas_grafiek = []
            totale_afstand = 0


            for resultaat in resultaten:
                einde = str(resultaat[2])
                print(einde)
                if(einde == datum):
                    data = [str(resultaat[0]), resultaat[1]]
                    datas.append(data)

            print(datas)

            for lijst in datas:
                totale_afstand += lijst[1]

            datas_grafiek.append(totale_afstand)
            datas_grafiek.append(datas[0][0])
            datas_grafiek.append(datas[-1][0])

            print(datas_grafiek)

        except:
            datas_grafiek=[0,'','']

        return render_template('speedometerchart.html', data = datas_grafiek)





@app.route('/contact',methods= ['POST', 'GET'])
def contact():



    return render_template('contact.html')





def get_sessies_datums():

    nieuwe_datums = []

    db = dbconn.DbConnection()

    sql1 = ('SELECT DISTINCT cast(Begin as DATE) from Sessie ORDER BY Begin ASC')

    datums = db.query(sql1)

    # for datum in datums:
    #
    #     nieuwe_datum = "{0}-{1}-{2}".format(datum[0], datum[1], datum[2])
    #     nieuwe_datums.append(nieuwe_datum)




    return datums



if __name__ == '__main__':

    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0',port=8080, debug=True)







