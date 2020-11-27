import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__,template_folder='plantillas')
import pandas as pd

@app.route('/',methods=["GET"])
def getCoord():
    aCoord=[]
    aCoordMax=[]; aPm=[]
    data= pd.read_csv('uma_02.csv')
    df = pd.DataFrame(data)
    aLon= df["lon"].astype('float')
    aLat= df["lat"].astype('float')
    aMp10=df["mp10"].astype('int')
    for i in range(0,len(aLon)):
        aCoord.append([aLat[i],aLon[i]])
        if aMp10[i]>15:
            aCoordMax.append([aLat[i],aLon[i]])
            aPm.append(aMp10[i])
    
    print(aPm)
    return render_template("index.html",aCoord=aCoord,aCoordMax=aCoordMax,aPm=aPm)


if __name__ == "__main__":
    app.run()