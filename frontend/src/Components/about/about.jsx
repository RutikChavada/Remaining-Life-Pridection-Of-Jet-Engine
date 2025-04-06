import React, { useEffect, useState } from "react";
import "./about.css";
import back from "../../assets/gradient.png";
import rutvik from "../../assets/rutvik.jpg";
import harshil from "../../assets/harshil.jpg";

function About() {
    const [isVisible, setIsVisible] = useState(false);

    useEffect(() => {
        // Trigger animations when component mounts
        setIsVisible(true);
    }, []);

    return (
        <div className={`main ${isVisible ? 'visible' : ''}`}>
            <img className="image-gradient" src={back} alt="background" />
            <div className="layer-blur"></div>

            <div className="project">
                <p>
                    The Jet Engine Remaining Useful Life (RUL) Prediction System is a
                    real-time full-stack application that estimates how long a jet
                    engine can operate safely based on live temperature sensor data.
                    Built with a Python Flask backend and a React frontend, the system
                    uses a machine learning model to predict RUL every second. The React
                    dashboard displays current temperature, predicted life, and a live
                    graph, with controls to start or stop predictions. Data flows
                    between frontend and backend via REST APIs. This project
                    demonstrates predictive maintenance using AI and real-time
                    monitoring, helping improve engine safety and reduce unexpected
                    failures in aviation.
                </p>
            </div>

            <div className="aboutus">
                <div className="leftside">
                    <div className="top">
                    <img src={rutvik} alt="Rutvik Chavada" />
                    <h3>Rutvik Chavada</h3>
                    </div>
                    <p>
                        I am Rutvik Chavada developed the complete full-stack structure of the
                        project, including the Flask server and the React frontend. I am
                        responsible for building the REST APIs, integrating real-time data
                        flow, and designing the user interface to display sensor readings
                        and predictions in a smooth, responsive, and interactive
                        dashboard.
                    </p>
                </div>

                <div className="rightside">
                    <div className="up"><img src={harshil} alt="Harshil Kothiya" />
                    <h3>Harshil Kothiya</h3></div>
                    <p>
                        I am Harshil Kothiya handled the machine learning and SQL components of
                        the project. I trained the model using historical jet engine data
                        to predict the Remaining Useful Life (RUL) and managed data
                        storage and retrieval using SQL. My work ensured accurate
                        predictions and efficient data handling for real-time monitoring
                        and analysis.
                    </p>
                </div>
            </div>
        </div>
    );
}

export default About;
