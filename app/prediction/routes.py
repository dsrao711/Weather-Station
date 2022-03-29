from flask import (render_template ,Blueprint)
import requests
from app.utils.logger import console_logger



bp = Blueprint('prediction', __name__)

@bp.route("/predict", methods=['GET', 'POST'])
def predict():
    res= requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/mumbai?unitGroup=metric&key=W7FP6XLXWSHYCN7M6NVY6YJJ2&contentType=json")
    if res.status_code != 200:
        console_logger.debug(res.status_code)
        console_logger.debug("Something went wrong")
    data = res.json()
    temp = data['days'][-1]['temp']
    hum = data['days'][-1]['humidity']
    message = data['description']
    loc = data['resolvedAddress']
    print(message)
    
    return render_template('prediction.html' , temp = temp , hum = hum , message = message , loc = loc)


