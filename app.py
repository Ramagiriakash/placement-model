from flask import Flask, request
import pickle

app = Flask(__name__)

# load your already created model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    iq = int(request.form['iq'])
    cgpa = float(request.form['cgpa'])

    result = model.predict([[iq, cgpa]])

    return "PLACED" if result[0] == 1 else "NOT PLACED"

app.run()