import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    int_features[3]=np.log(int_features[3])
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction==1 : 
            output="YES"
    else:
            output="NO"

    return render_template('index.html', prediction_text="Blood Donation Expectancy : " + output)


if __name__ == "__main__":
    app.run(debug=True)
