import numpy as np
from flask import Flask, jsonify, request, render_template
import math
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    #return 'Hello World!'
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():

    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    pred = model.predict(final_features)
    x = pred[0]
    return render_template("index.html", prediction_text="Provável valor de vendas globais em milhões: " + str(format(x, '.2f')))


@app.route("/api", methods=["POST"])
def results():
    data = request.get_json(force=True)
    pred = model.predict([np.array(list(data.values()))])

    output = str(pred[0])
    return jsonify(output)