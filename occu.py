#occu.py 9/22
from flask import Flask, render_template
from occupations import L, randomVal

app = Flask(__name__)

@app.route("/")
def firstPg():
    return "this is the home page" 

@app.route("/occupations")
def secondPg():
    return render_template('occu.html', t="Occupations", l=L)
    #return str(L) + randomVal

@app.route("/thirdpg")
def thirdPg():
    return "this is the third page" 

if __name__ == "__main__":
    app.debug = True
    app.run()
