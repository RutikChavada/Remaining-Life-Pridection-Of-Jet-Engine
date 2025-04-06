import React, { useEffect } from "react";
import "./home.css"; 
import back from "../../assets/gradient.png";
import Navbar from "../navbar/navbar";

function Home() {
    useEffect(() => {
        const script = document.createElement("script");
        script.type = "module";
        script.src = "https://unpkg.com/@splinetool/viewer@1.9.82/build/spline-viewer.js";
        document.body.appendChild(script);

        return () => {
            document.body.removeChild(script);
        };
    }, []);

    return (
        <>
            <div className="main">
                {/* <Navbar className="nav" /> */}
                <img className="image-gradient" src={back} alt="background" />
                <div className="layer-blur"></div>

                <div className="outer">
                    <div className="content">
                        <div className="box"><div className="tag">Prediction</div></div>
                        <h1>Make a Jet Plane<br />Life Prediction</h1>
                        <p className="discription">
                            Welcome! Here you can analyze the lifespan of your Jet Plane.
                            Check if your aircraft is safe or in danger!
                        </p>
                        <div className="buttons">
                            <a href="/about" className="about">About Us &gt;</a>
                            <a href="/pridect" className="getstart">Get Started &gt;</a>
                        </div>
                    </div>

                    {/* 3D Model */}
                    <div className="spline-container">
                        <spline-viewer url="https://prod.spline.design/lWme2NdiopkzrVrG/scene.splinecode"></spline-viewer>
                    </div>
                </div>
            </div>
        </>
    );
}

export default Home;
