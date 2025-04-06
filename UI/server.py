from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import threading
import time
import random
import database
import random_num  # Import the modified random.py

app = Flask(__name__)
CORS(app)

# Load the trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

feature_columns = [
    'set1', 'set2', 'sensor2', 'sensor3', 'sensor4', 'sensor6', 'sensor7', 'sensor8', 'sensor9',
    'sensor11', 'sensor12', 'sensor13', 'sensor14', 'sensor15', 'sensor17', 'sensor20', 'sensor21'
]

running = threading.Event()  # Flag to control the background process

def generate_and_predict():
    """ Function to continuously generate sensor data and predict RUL every second """
    global running
    while running:
        sensor_values = random_num.generate_sensor_data()
        
        # Normalize and reshape for prediction
        input_data = np.array([sensor_values[col] for col in feature_columns]).reshape(1, -1)
        input_data = scaler.transform(input_data)
        input_data = input_data.reshape(1, 1, len(feature_columns))

        prediction = model.predict(input_data)
        rul_value = float(prediction[0][0])

        # Store generated data and prediction
        sensor_values["predicted_rul"] = rul_value
        database.insert_sensor_data(sensor_values)
        print(prediction)

        print(f"Generated Data: {sensor_values}")  # Debugging purpose
        time.sleep(1)

@app.route("/start", methods=["POST"])
def start_generation():
    """ Start the sensor data generation and prediction """
    global running
    if not running:
        running = True
        threading.Thread(target=generate_and_predict, daemon=True).start()
        return jsonify({"message": "Sensor data generation started."})
    return jsonify({"message": "Already running."})

@app.route("/stop", methods=["POST"])
def stop_generation():
    """ Stop the sensor data generation and prediction """
    global running
    running = False
    return jsonify({"message": "Sensor data generation stopped."})

@app.route("/fetch", methods=["GET"])
def fetch_sensor_data():
    try:
        df = database.fetch_last_10()
        data_json = df.to_dict(orient="records")    
        print("Fetched from DB:", data_json)  # Debugging line
        return jsonify(data_json)
    except Exception as e:
        return jsonify({"error": str(e)})




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)