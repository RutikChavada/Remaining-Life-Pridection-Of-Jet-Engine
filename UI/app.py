import streamlit as st
import pandas as pd
import numpy as np
import random
import time
import plotly.express as px
import joblib
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)
# import files
import database
import random_num


model = None
scaler = None
feature_columns = [
    'set1',
    'set2',
    'sensor2',
    'sensor3',
    'sensor4',
    'sensor6',
    'sensor7',
    'sensor8',
    'sensor9',
    'sensor11',
    'sensor12',
    'sensor13',
    'sensor14',
    'sensor15',
    'sensor17',
    'sensor20',
    'sensor21'
]



# functiosn

def load_models():
    
    with open('model.pkl', 'rb') as f:
        global model
        model = joblib.load(f) 

    with open('scaler.pkl', 'rb') as f:
        global scaler
        scaler = joblib.load(f)

    print("successfully load the models")



def predict_rul(data):
    #1 scale the data
    data = scaler.transform(data)

    # reshap
    # print(feature_columns)
    data = data.reshape(1, 10, len(feature_columns))

    predict = model.predict(data);

    print("successfully predict the value", predict[0][0])
    
    return predict[0][0]



def main():
    st.title("Real-time Sensor Data Prediction UI")

    # Control for starting/stopping the prediction loop.
    if 'run' not in st.session_state:
        st.session_state.run = False
    if 'time_points' not in st.session_state:
        st.session_state.time_points = []
    if 'predicted_rul_list' not in st.session_state:
        st.session_state.predicted_rul_list = []
    if 'iteration' not in st.session_state:
        st.session_state.iteration = 1

    col1, col2 = st.columns(2)
    if col1.button("Predict"):
        st.session_state.run = True
    if col2.button("Stop"):
        st.session_state.run = False

    # Placeholders for charts and prediction text.
    rul_text_placeholder = st.empty()            # For displaying the predicted RUL
    time_vs_rul_chart_placeholder = st.empty()   # For time vs. predicted RUL (line chart)

    # =======================
    # Main Loop (runs while "Predict" is active)
    # =======================
    while st.session_state.run:
        # 1. Generate sensor readings and insert into DB.
        sensor_data = random_num.generate_sensor_data()
        database.insert_sensor_data(sensor_data)
        
        # 2. Fetch the last 10 rows and pad if needed.
        df_data = database.fetch_last_10()
        df_data = database.pad_data(df_data, 10)
        
        # 3. Compute a dummy prediction.
        prediction = predict_rul(df_data[feature_columns])
        
        # 6. Update the time vs. predicted RUL chart.
        # Use the iteration count as the time axis.
        st.session_state.time_points.append(st.session_state.iteration)
        st.session_state.predicted_rul_list.append(prediction)
        st.session_state.iteration += 1
        # Create a DataFrame for the line chart.
        df_time_vs_rul = pd.DataFrame({
            "Time": st.session_state.time_points,
            "Predicted RUL": st.session_state.predicted_rul_list
        })

        # Use st.line_chart to update the chart.
        time_vs_rul_chart_placeholder.line_chart(df_time_vs_rul.set_index("Time"))
        
        # 5. Display the predicted RUL.
        rul_text_placeholder.text(f"Predicted RUL: {prediction:.2f}")

        
        time.sleep(1)
    else:
        st.write("Press the Predict button to start real-time predictions.")


if __name__ == '__main__':
    load_models()
    main()