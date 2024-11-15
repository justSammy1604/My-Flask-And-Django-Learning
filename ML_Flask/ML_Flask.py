from flask import Flask,render_template,url_for,request,jsonify
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb')) 

@app.route('/')
def home():
    return render_template('model.html')

@app.route('/predict',methods=['POST'])
def predict():
    init_features = [float(x) for x in request.form.values()]
    final_features = [np.array(init_features)]

    prediction = model.predict(final_features)




    return render_template('model.html',prediction_text='Prediction Class: {} '.format(prediction))


if __name__ == '__main__':
    app.run(debug=True,port=4444)
