import numpy as np
import scipy as sp
import pandas as pd
from flask import Flask,request,jsonify,render_template
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask (__name__)
model = pickle.load (open ('model.pkl','rb'))

@app.route ('/')
def home():
    return render_template ('index.html') 


@app.route ('/predict',methods=['POST','GET'])
def predict():
    
    float_features = [float(X) for X in request.form.values()]
    
    features =  [np.array(float_features)]
    
    prediction = model.predict (features)
     
    if prediction == 1:
        return render_template ('index.html',prediction_text='Employee Might Leave The Job')
    if prediction == 0:
        return render_template ('index.html',prediction_text='Employee Might Not Leave The Job')

if __name__ == "__main__":
    app.run (debug=True)