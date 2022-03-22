from flask import (render_template ,Blueprint, request)
import requests
import json

bp = Blueprint('main', __name__)

@bp.route("/")
def dashboard():
    # print("Fetching temperature ...")
    # req_temp = requests.get("https://api.thingspeak.com/channels/1569087/fields/1.json?results=1")
    # curr_temp_ob = json.loads(req_temp.text)
    # feeds = curr_temp_ob['feeds']
    # temp = feeds[0]['field1']
    # print(temp)
    
    # print("Fetching humidity...")
    # req_hum = requests.get("https://api.thingspeak.com/channels/1569087/fields/2.json?results=1")
    # curr_hum_ob = json.loads(req_hum.text)
    # feeds_hum = curr_hum_ob['feeds']
    # hum = feeds_hum[0]['field2']
    # print(hum)
    
    print("Fetching current humidity and temperature...")
    req= requests.get("https://api.thingspeak.com/channels/1569087/feeds.json?results=1")
    ob = json.loads(req.text)
    feeds = ob['feeds']
    temp = feeds[0]['field1']
    hum =  feeds[0]['field2']
    print(temp)
    print(hum)
    
    print("Fetching last 5 temperature data ....")
    req_temp = requests.get("https://api.thingspeak.com/channels/1569087/fields/1.json?results=5")
    ob_temps = json.loads(req_temp.text)
    feeds = ob_temps['feeds']
    temp_data = []
    for i in range(0 , len(feeds)) :
        temp_data.append([feeds[i]['created_at'] , feeds[i]['field1'] ])
    print(temp_data)
    
    print("Fetching last 5 humidity data ....")
    req_hum = requests.get("https://api.thingspeak.com/channels/1569087/fields/2.json?results=5")
    ob_hum = json.loads(req_hum.text)
    feeds_hum = ob_hum['feeds']
    hum_data = []
    for i in range(0 , len(feeds_hum)) :
        hum_data.append([feeds_hum[i]['created_at'] , feeds_hum[i]['field2'][0:5] ])
    print(hum_data)
    
    return render_template('dashboard.html' , temp = temp , hum = hum , temp_data  = temp_data , hum_data = hum_data)


