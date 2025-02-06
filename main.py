from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

stations = pd.read_csv("data_small/stations.txt", skiprows=17)[['STAID', 'STANAME                                 ']]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>")
def station(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])[['    DATE', '   TG']]
    result = df.to_dict()

    return result

@app.route("/api/v1/<station>/<date>")
def about(station, date):

    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])

    temperature = df.loc[df['    DATE']  == date]['   TG'].squeeze() / 10
    return {"Temperature" : temperature, "Date ": date, "Station ": station}


app.run(debug=True)
