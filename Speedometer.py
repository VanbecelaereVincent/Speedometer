from flask import Flask
from flask import render_template
import os

#from DbClass import DbClass

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/speedometer')
def speedometer():
    return render_template('speedometer.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':

    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0',port=8080, debug=True)







