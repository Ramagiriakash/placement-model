from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    iq = int(request.form['iq'])
    cgpa = float(request.form['cgpa'])

    result = model.predict([[iq, cgpa]])

    return render_template(
        'index.html',
        prediction="PLACED" if result[0] == 1 else "NOT PLACED"
    )

if __name__ == "__main__":
    app.run(debug=True)
