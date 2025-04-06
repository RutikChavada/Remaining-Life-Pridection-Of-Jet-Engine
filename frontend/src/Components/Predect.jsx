import { useState, useEffect } from "react";
import "./predict.css";
import { startGeneration, stopGeneration, fetchSensorData } from "../Api/api";
import back from "../assets/gradient.png";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from "recharts";
import Navbar from "./navbar/navbar";

export default function RULPredictor() {
    const [sensorRecords, setSensorRecords] = useState([]);
    const [graphData, setGraphData] = useState([]);
    const [latestPrediction, setLatestPrediction] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await fetchSensorData();
                console.log("Fetched sensor data:", data);
                if (!data.error && data.length > 0) {
                    const reversedData = data.reverse();
                    setSensorRecords(reversedData);

                    const predictedValue = parseFloat(reversedData[0]?.predicted_rul) || 0;
                    setLatestPrediction(predictedValue);

                    setGraphData(prevData => [
                        ...prevData.slice(-20),
                        { time: new Date().toLocaleTimeString(), predicted: predictedValue }
                    ]);
                }
            } catch (error) {
                console.error("Error fetching sensor data:", error);
            }
        };

        const interval = setInterval(fetchData, 1000);
        return () => clearInterval(interval);
    }, []);

    const handleStart = async () => {
        const response = await startGeneration();
        alert(response.message);
    };

    const handleStop = async () => {
        const response = await stopGeneration();
        alert(response.message);
    };

    return (
        <div className="main">
            {/* <Navbar/> */}
            <img className="image-gradient" src={back} alt="background" />
            <div className="layer-blur"></div>

            <div className="middle">
                <div className="left">
                    <h2>Jet Engine RUL Prediction</h2>
                    <div>
                        <button id="b1" onClick={handleStart}>Start &gt;</button>
                        <button onClick={handleStop}>Stop</button>
                    </div>
                    <h3>Latest Predicted RUL<br /><span>{latestPrediction !== null ? latestPrediction.toFixed(2) : 'Loading...'}</span></h3>
                </div>
                <div className="right">
                    <h3>Prediction Over Time</h3>
                    <ResponsiveContainer width="100%" height={300}>
                        <LineChart data={graphData}>
                            <CartesianGrid strokeDasharray="3 3" />
                            <XAxis dataKey="time" />
                            <YAxis />
                            <Tooltip />
                            <Line type="monotone" dataKey="predicted" stroke="#8884d8" strokeWidth={2} />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </div>

            <h3 id="thead">Live Sensor Data</h3>
            <div className="table-container">
                <table>
                    <thead>
                        <tr>
                            {Object.keys(sensorRecords[0] || {}).map((col) => (
                                <th key={col}>{col}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {/* {sensorRecords.map((record, index) => (
                            <tr key={index}>
                                {Object.keys(record).map((col) => (
                                    <td key={col}>{record[col]}</td>
                                ))}
                            </tr>
                        ))} */}
                        {sensorRecords[0] && (
                            <tr>
                                {Object.keys(sensorRecords[0]).map((col) => (
                                    <td key={col}>{sensorRecords[0][col]}</td>
                                ))}
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
}
