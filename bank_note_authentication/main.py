from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == "POST":
        try:
            var = float(request.form['variance'])
            skew = float(request.form['skewness'])
            curt = float(request.form['curtosis'])
            entro = float(request.form['entropy'])

            filename = "bank_note.sav"
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict([[var,skew,curt,entro]])
            print('The predicted value is ',prediction[0])
            ans = prediction[0]
            if ans==0:
                say = "Not Authenticate"
            else:
                say = "Authenticate"

            return render_template('results.html', pre=say)
        except Exception as e:
            print('The Exception Message is ', e)
            return "Something is Wrong !!!"
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

