import pickle
import random

import numpy as np
from flask import Flask, jsonify, render_template, request
from pathlib import Path

HERE = Path(__file__).parent
app = Flask(__name__)
model=pickle.load(open(HERE / "engine_model.sav","rb"))

@app.route('/')
def predict():
    return render_template('Manual_predict.html')
@app.route('/y_predict',methods=['POST','GET'])
def y_predict():
    x_test = [[int (x) for x in request.form.values()]]
    print(x_test)
    a=model.predict(x_test)
    pred = a[0]
    if(pred == 0):
        pred ="No failure expected within 30 days. "
    else:
        pred = "Maintenance Required!! Expected a failure within 30 days. "
    return render_template('Manual_predict.html', prediction_text=pred)

if (__name__=='__main__'):
    app.run(debug=True)