from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import urllib.request
import os

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":


        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        date_dep = pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M")
        Journey_day = int(date_dep.day)
        Journey_month = int(date_dep.month)

        # Departure
        Dep_hour = int(date_dep.hour)
        Dep_min = int(date_dep.minute)
        

        # Arrival
        date_arr = request.form["Arrival_Time"]
        date_arr = pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M")
        Arrival_hour = int(date_arr.hour)
        Arrival_min = int(date_arr.minute)

        # Duration
        duration = abs(date_arr - date_dep)                         
        duration_in_s = duration.total_seconds()
        hours = round(duration_in_s / 3600,2)
        

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['airline']
        air_arr = [0,0,0,0,0,0,0,0,0,0,0]
        
        if(airline=='Jet Airways'):
            air_arr[0] = 1

        elif (airline=='IndiGo'):
            air_arr[1] = 1
            
        elif (airline=='Air India'):
            air_arr[2] = 1
            
        elif (airline=='Multiple carriers'):
            air_arr[3] = 1 
            
        elif (airline=='SpiceJet'):
            air_arr[4] = 1 
            
        elif (airline=='Vistara'):
            air_arr[5] = 1

        elif (airline=='GoAir'):
            air_arr[6] = 1

        elif (airline=='Multiple carriers Premium economy'):
            air_arr[7] = 1

        elif (airline=='Jet Airways Business'):
            air_arr[8] = 1

        elif (airline=='Vistara Premium economy'):
            air_arr[9] = 1
            
        elif (airline=='Trujet'):
            air_arr[10] = 1

        
        # Source
        # Banglore = 0 (not in column)

        Source = request.form["Source"]
        source_arr = [0,0,0,0]
        if (Source == 'Delhi'):
            source_arr[0] = 1

        elif (Source == 'Kolkata'):
            source_arr[1] = 1

        elif (Source == 'Mumbai'):
            source_arr[2] = 1

        elif (Source == 'Chennai'):
            source_arr[3] = 1


        # Destination
        # Banglore = 0 (not in column)
        dest = request.form["Destination"]
        dest_arr = [0,0,0,0,0]

        if (dest == 'Cochin'):
            dest_arr[0] = 1
        
        elif (dest == 'Delhi'):
            dest_arr[1] = 1

        elif (dest == 'New_Delhi'):
            dest_arr[2] = 1

        elif (dest == 'Hyderabad'):
            dest_arr[3] = 1

        elif (dest == 'Kolkata'):
            dest_arr[4] = 1        

        
        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            hours,
            air_arr[2],
            air_arr[6],
            air_arr[1],
            air_arr[0],
            air_arr[8],
            air_arr[3],
            air_arr[7],
            air_arr[4],
            air_arr[10],
            air_arr[5],
            air_arr[9],
            source_arr[3],
            source_arr[0],
            source_arr[1],
            source_arr[2],
            dest_arr[0],
            dest_arr[1],
            dest_arr[3],
            dest_arr[4],
            dest_arr[2]
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price could be Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
