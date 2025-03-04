from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
import joblib

app = Flask(__name__)

model = tf.keras.models.load_model("model/ddos_logistic_regression.h5")
scaler = joblib.load("model/scaler.pkl")
encoder = joblib.load("model/encoder.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        source_port = int(data["source_port"])
        dest_port = int(data["dest_port"])
        packet_length = float(data["packet_length"])
        packets_time = float(data["packets_time"])
        highest_layer = data["highest_layer"]
        transport_layer = data["transport_layer"]

        new_data = pd.DataFrame([{
            "Source Port": source_port,
            "Dest Port": dest_port,
            "Packet Length": packet_length,
            "Packets/Time": packets_time,
            "Highest Layer": highest_layer,
            "Transport Layer": transport_layer
        }])

        encoded_new_data = encoder.transform(new_data[["Highest Layer", "Transport Layer"]])
        encoded_new_df = pd.DataFrame(encoded_new_data, columns=encoder.get_feature_names_out())

        numericals = ["Source Port", "Dest Port", "Packet Length", "Packets/Time"]
        new_data[numericals] = scaler.transform(new_data[numericals])

        new_data["Packet Rate"] = new_data["Packets/Time"] / new_data["Packet Length"]

        final_input = pd.concat([new_data.drop(columns=["Highest Layer", "Transport Layer"]), encoded_new_df], axis=1)

        prediction = model.predict(final_input)
        result = int(prediction[0][0] > 0.5)

        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
