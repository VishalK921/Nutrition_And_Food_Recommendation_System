from flask import Flask,render_template, request
import pandas as pd
from model import Transform_data,model
from food_picker import food_selection
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def upload():
    if request.method == 'POST':
        w= {
            "Gender": request.form['Gender'],
            "Age": request.form['Age'],
            "family_history_with_overweight": request.form['family_history_with_overweight'],
            "FAVC": request.form['FAVC'],
            "FCVC": request.form['FCVC'],
            "NCP": request.form['NCP'],
            "CAEC": request.form['CAEC'],
            "SMOKE": request.form['SMOKE'],
            "CH2O": request.form['CH2O'],
            "SCC": request.form['SCC'],
            "FAF": request.form['FAF'],
            "TUE": request.form['TUE'],
            "CALC": request.form['CALC'],
            "MTRANS": request.form['MTRANS'],
        }
        data_df = pd.DataFrame([w])
        data=Transform_data(data_df)
        prediction=food_selection(model.predict(data))
        return render_template('output.html',pred=prediction)
