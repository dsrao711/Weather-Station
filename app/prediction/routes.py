from flask import (render_template ,Blueprint)

bp = Blueprint('prediction', __name__)

@bp.route("/predict", methods=['GET', 'POST'])
def predict():
    return render_template('prediction.html', title ='Prediction')


