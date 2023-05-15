# This is a sample Python script.
from flask import Flask, render_template, request
import pickle

import helper

# import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
# v = pickle.load(open('v.pkl', 'rb'))
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
app = Flask(__name__)


# @app.route('/', methods='POST')
# def home():
#     # user_input_1 = request.form.get('user_input_1')
#     # user_input_2 = request.form.get('user_input_2')
#     # query = helper.query_point_creator(user_input_1, user_input_2)
#     # output = model.predict(query)
#     # print('output')
#
#     return render_template('index.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        print("post")
        user_input_1 = request.form.get('user_input_1')
        user_input_2 = request.form.get('user_input_2')
        query = helper.query_point_creator(user_input_1, user_input_2)
        print(user_input_1)
        output = model.predict(query)
        if output:
            return render_template('index.html', prediction_text="true")
        else:
            return render_template('index.html', prediction_textt="false")
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()






