import json
import requests
from app.utils.logger import console_logger
from flask import Blueprint, render_template
from app import config

bp = Blueprint('main', __name__)


@bp.route('/')
def dashboard():
<<<<<<< HEAD
    # Curr temp and humidity    
    print("Fetching current humidity and temperature...")
    req= requests.get("https://api.thingspeak.com/channels/1688703/feeds.json?api_key=8EE4CMD1HH4XF2GU&results=5")
    ob = json.loads(req.text)
    feeds = ob['feeds']
    temp = feeds[0]['field1']
    hum =  feeds[0]['field2']
    rain =  feeds[0]['field3']
    print(temp)
    print(hum)
    print(rain)
    message = "Pleasant"
    rain_message = "No rain"
    if(float(temp) >= 30.00):
        message = "Hot"
    if(float(rain) <= 30.00):
        rain_message = "Expecting shower"
    
    # Graphs
    print("Fetching last 5 temperature data ....")
    req_temp = requests.get("https://api.thingspeak.com/channels/1569087/fields/1.json?results=5")
    ob_temps = json.loads(req_temp.text)
    feeds = ob_temps['feeds']
    temp_values = []
    temp_labels = []
    for i in range(0 , len(feeds)) :
        temp_values.append(feeds[i]['field1'] )
        temp_labels.append(feeds[i]['created_at'] )
    print(temp_values , temp_labels)
    # [['2022-03-22T15:34:23Z', '31.80'], ['2022-03-22T15:34:39Z', '31.70'], ['2022-03-22T15:34:54Z', '31.70'], ['2022-03-22T15:35:10Z', '31.70'], ['2022-03-22T15:35:26Z', '31.80']]
    
    print("Fetching last 5 humidity data ....")
    req_hum = requests.get("https://api.thingspeak.com/channels/1569087/fields/2.json?results=5")
    ob_hum = json.loads(req_hum.text)
    feeds_hum = ob_hum['feeds']
    hum_values = []
    hum_labels = []
    for i in range(0 , len(feeds_hum)) :
        hum_values.append(feeds_hum[i]['field2'][0:5])
        hum_labels.append(feeds_hum[i]['created_at'])
    print(hum_values , hum_labels)
    # [['2022-03-22T15:34:23Z', '38.00'], ['2022-03-22T15:34:39Z', '38.00'], ['2022-03-22T15:34:54Z', '38.00'], ['2022-03-22T15:35:10Z', '38.00'], ['2022-03-22T15:35:26Z', '38.00']]
    # graph1 = requests.get("https://api.thingspeak.com/channels/1569087/charts/1")
    # with open("temp.html", "w") as f:
    #     f.write(graph1.text)

    return render_template('dashboard.html' , temp = temp , hum = hum , rain = rain , labels = temp_labels , values = temp_values , message = message , rain_message = rain_message )
=======
    # Fetching the data of the latest 30 entries

    res = requests.get(
        "https://api.thingspeak.com/channels/1688703/feeds.json",
        params={"api_key": config.API_KEY, "results": config.RESULTS}
    )

    if res.status_code != 200:
        console_logger.debug(res.status_code)
        console_logger.debug("Something went wrong")

    data = res.json()

    # Parsing data and creating page data variables
    temp = data['feeds'][-1]['field1']
    hum = data['feeds'][-1]['field2']
    rain = data['feeds'][-1]['field3']

    temperature = []
    humidity = []
    rains = []
    logtime = []

    for feed in data['feeds']:
        logtime.append(feed['created_at'])
        temperature.append(feed['field1'])
        humidity.append(feed['field2'])
        rains.append(feed['field3'])

    graph = json.dumps({
        'logtime': logtime,
        'temperature': temperature,
        'humidity': humidity,
        'rains': rains
    })

    return render_template(
        'dashboard.html',
        temp=temp,
        hum=hum,
        rain=rain,
        graph=graph
    )

# @bp.route("/")
# def dashboard():
#     # Curr temp and humidity
#     print("Fetching current humidity and temperature...")
#     req = requests.get(
#         "https://api.thingspeak.com/channels/1688703/feeds.json?api_key=8EE4CMD1HH4XF2GU&results=5")
#     ob = json.loads(req.text)
#     feeds = ob['feeds']
#     temp = feeds[0]['field1']
#     hum = feeds[0]['field2']
#     rain = feeds[0]['field3']
#     print(temp)
#     print(hum)
#     print(rain)

#     # Graphs
#     print("Fetching last 5 temperature data ....")
#     req_temp = requests.get(
#         "https://api.thingspeak.com/channels/1569087/fields/1.json?results=5")
#     ob_temps = json.loads(req_temp.text)
#     feeds = ob_temps['feeds']
#     temp_values = []
#     temp_labels = []
#     for i in range(0, len(feeds)):
#         temp_values.append(feeds[i]['field1'])
#         temp_labels.append(feeds[i]['created_at'])
#     print(temp_values, temp_labels)
#     # [['2022-03-22T15:34:23Z', '31.80'], ['2022-03-22T15:34:39Z', '31.70'], ['2022-03-22T15:34:54Z', '31.70'], ['2022-03-22T15:35:10Z', '31.70'], ['2022-03-22T15:35:26Z', '31.80']]

#     print("Fetching last 5 humidity data ....")
#     req_hum = requests.get(
#         "https://api.thingspeak.com/channels/1569087/fields/2.json?results=5")
#     ob_hum = json.loads(req_hum.text)
#     feeds_hum = ob_hum['feeds']
#     hum_values = []
#     hum_labels = []
#     for i in range(0, len(feeds_hum)):
#         hum_values.append(feeds_hum[i]['field2'][0:5])
#         hum_labels.append(feeds_hum[i]['created_at'])
#     print(hum_values, hum_labels)
#     # [['2022-03-22T15:34:23Z', '38.00'], ['2022-03-22T15:34:39Z', '38.00'], ['2022-03-22T15:34:54Z', '38.00'], ['2022-03-22T15:35:10Z', '38.00'], ['2022-03-22T15:35:26Z', '38.00']]
#     # graph1 = requests.get("https://api.thingspeak.com/channels/1569087/charts/1")
#     # with open("temp.html", "w") as f:
#     #     f.write(graph1.text)

#     return render_template('dashboard.html', temp=temp, hum=hum, rain=rain, labels=temp_labels, values=temp_values)
>>>>>>> c5b57e1dcb31f6e43fa1f438e98ff7b738d71209


# bp.route("/graphs")


# def graphs():
#     return render_template('temp.html')
