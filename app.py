from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

cls = pickle.load(open('model.pkl', 'rb')) 

@app.route('/')
def index():
    return 'Welcome to our test api'

@app.route('/predict', methods=['POST'])
def prediction():
    res = request.get_data(as_text=True)
    data = pd.read_json(res, orient='index').transpose()
    pred = cls.predict(data)
    return f'for this entries:\n{res}\nthe prediction is {pred}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)