#occu.py 9/22
from flask import Flask, render_template
from utils.occupations import L, randomVal, site

app = Flask(__name__)

@app.route("/")
def firstPg():
    return "this is the home page" 

@app.route("/occupations")
def secondPg():
    return render_template('occu.html', t="Occupations", l = L, random = randomVal, s = site)

if __name__ == "__main__":
    app.debug = True
    app.run()
