import mysql.connector
import pandas as pd

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


# ===== MySQL Database Setup =====
# Update these connection parameters to match your MySQL server settings.
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',    
    password='Root@123', 
    database='ml'
)
cursor = db_connection.cursor()

# Create the sensor_data table if it doesn't exist.
create_table_query = f"""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    {', '.join([f"{col} FLOAT" for col in feature_columns])},
    predicted_rul FLOAT
)
"""
cursor.execute(create_table_query)
db_connection.commit()

print("successful make table")



# ===== Functions =====
def insert_sensor_data(data_dict):
    """Insert sensor readings and predicted RUL into the database."""
    query = f"INSERT INTO sensor_data ({', '.join(feature_columns)}, predicted_rul) VALUES ({', '.join(['%s']*(len(feature_columns)+1))})"
    values = tuple(data_dict[col] for col in feature_columns) + (data_dict["predicted_rul"],)
    cursor.execute(query, values)
    db_connection.commit()
    print("Inserted into the database")

def fetch_last_10():
    """Fetch the last 10 rows of sensor data including predicted RUL (most recent first, then reverse order)."""
    query = f"SELECT id, timestamp, {', '.join(feature_columns)}, predicted_rul FROM sensor_data ORDER BY id DESC LIMIT 10"
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = ['id', 'timestamp'] + feature_columns + ['predicted_rul']
    df = pd.DataFrame(rows, columns=columns)
    return df.iloc[::-1]  # Reverse to have the earliest row first


def pad_data(df, target_rows=10):
    """If there are fewer than 10 rows, repeat the last available row to pad the data."""
    if len(df) < target_rows and not df.empty:
        last_row = df.iloc[-1:]
        pad_count = target_rows - len(df)
        df = pd.concat([df, pd.concat([last_row]*pad_count, ignore_index=True)], ignore_index=True)
    return df