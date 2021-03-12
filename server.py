import pandas as pd
import pickle

from flask import (Flask, jsonify, request)
from manager import load_pipeline

server = Flask(__name__)


pipeline = load_pipeline('./trained_model/forest.pickle')


# Сервер будет обрабатывать GET запросы на 0.0.0.0:5000/predict

@server.route("/predict", methods=["GET"])
def predict():
    required = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'DT_1', 'DT_2']

    try:
        for argument in required:
            if argument not in request.args:
                raise KeyError(f'"{argument}" is required')

        data = {k: request.args[k] for k in request.args if k in required}
        df = pd.DataFrame([data.values()], columns=data.keys())

        result = {
            'predicted': pipeline.predict(df)[0],
            'real': request.args['MEDV'] if 'MEDV' in request.args else None
        }
        return jsonify(result), 200
    except KeyError as e:
        return jsonify({'error': str(e)}), 500
