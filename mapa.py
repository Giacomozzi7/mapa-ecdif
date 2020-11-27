import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd

def index():  #Se define la ruta del Web Server
    return render_template("index.html")

import pandas as pd

def getCoord():
    aCoord=[]
    data= pd.read_csv('uma_02.csv')
    df = pd.DataFrame(data)
    aLon= df["lon"].astype('float')
    aLat= df["lat"].astype('float')
    for i in range(0,len(aLon)):
        aCoord.append([aLat[i],aLon[i]])
    
    return aCoord

df = getCoord()


if __name__ == "__main__":
    app.run()