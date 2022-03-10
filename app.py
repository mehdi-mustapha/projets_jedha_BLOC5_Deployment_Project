from flask import Flask, request, jsonify, render_template
import joblib

appFlask = Flask(__name__)

@appFlask.route("/", methods=["GET"])
def index():

    return render_template('index.html')


@appFlask.route("/predict", methods=["POST"])
def predict():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        req = request.get_json()
        # Check mandatory key
        if "input" in req.keys():
            # Load model
            classifier = joblib.load("model.joblib")
            print("recu de request:{}".format(req["input"]))
            # Predict
            prediction = classifier.predict(req["input"])
            print("Ceci est la prediction: {}".format(prediction))
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            #prediction = str(prediction[0])


            #return jsonify({"predict": prediction}), 200
            return jsonify([str(pred) for pred in prediction]), 200

    return jsonify({"msg": "Error: not a JSON or no email key in your request"})


if __name__ == "__main__":
    #appFlask.run(debug=True) # ca sert en local seulement
    appFlask.run(host='0.0.0.0', debug=True) # pour deployer dans heroku
